from contextlib import asynccontextmanager
from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import time
import uuid
from urllib.parse import urlparse
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
from sqlalchemy import delete, func, select, text, update
from sqlalchemy.orm import Session, sessionmaker
from starlette.middleware.trustedhost import TrustedHostMiddleware
from .auth import Identity, email_hash, get_identity, normalize_email
from .catalog import Catalog
from .db import Base, EmailProfile, Reaction, TopicState, get_db, insert_for, make_engine
from .settings import Settings, get_settings

log = logging.getLogger('doomer')
logging.basicConfig(level=logging.INFO, format='%(message)s')

class ProfileBody(BaseModel):
    model_config = ConfigDict(extra='forbid')
    email: str = Field(min_length=3, max_length=254)

class ProgressBody(BaseModel):
    model_config = ConfigDict(extra='forbid')
    doom_id: str
    expected_version: int = Field(ge=0)

class ReactionBody(BaseModel):
    model_config = ConfigDict(extra='forbid')
    value: Literal['like', 'dislike'] | None

def create_app(settings: Settings | None = None, engine=None):
    settings = settings or get_settings()
    settings.check()
    if engine is None:
        if settings.database_url.startswith('sqlite:'):
            (Path(__file__).resolve().parent.parent / 'data').mkdir(exist_ok=True)
        engine = make_engine(settings.database_url)

    @asynccontextmanager
    async def lifespan(app):
        if settings.environment == 'development':
            Base.metadata.create_all(engine)  # Production schema changes use Alembic, never create_all.
        app.state.catalog = Catalog(settings.content_dir)
        yield
        engine.dispose()

    app = FastAPI(title='Doomer', version='0.1.0', lifespan=lifespan,
                  docs_url='/api/docs' if settings.environment == 'development' else None, redoc_url=None,
                  openapi_url='/api/openapi.json' if settings.environment == 'development' else None)
    app.state.settings = settings
    app.state.engine = engine
    app.state.session_factory = sessionmaker(engine, expire_on_commit=False)
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.trusted_hosts())
    if settings.sentry_dsn:
        import sentry_sdk
        sentry_sdk.init(dsn=settings.sentry_dsn, environment=settings.environment, release=settings.release,
                        send_default_pii=False, traces_sample_rate=0.05)

    @app.middleware('http')
    async def request_log(request, call_next):
        started = time.monotonic()
        request_id = str(uuid.uuid4())
        try:
            response = await call_next(request)
        except Exception as error:
            log.error(json.dumps({'event':'request_failed', 'request_id':request_id, 'exception_type':type(error).__name__}))
            # Preserve the exception for configured error tracking without leaking it to the client.
            if settings.sentry_dsn:
                import sentry_sdk
                sentry_sdk.capture_exception()
            response = JSONResponse({'detail':'Something went wrong. Please retry.', 'request_id':request_id}, status_code=500)
        response.headers['X-Request-ID'] = request_id
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Referrer-Policy'] = 'no-referrer'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
        connects = "'self'"
        if settings.frontend_sentry_dsn:
            connects += ' https://' + (urlparse(settings.frontend_sentry_dsn).hostname or '')
        response.headers['Content-Security-Policy'] = f"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' blob: data:; font-src 'self'; connect-src {connects}; object-src 'none'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'"
        if request.url.path.startswith('/api'):
            response.headers['Cache-Control'] = 'no-store'
        route = request.scope.get('route')
        log.info(json.dumps({'event':'http_request', 'request_id':request_id, 'method':request.method,
                             'route':getattr(route, 'path', 'unmatched'), 'status':response.status_code,
                             'duration_ms':round((time.monotonic()-started)*1000, 1)}))
        return response

    @app.get('/health/live')
    def live():
        return {'status':'ok'}

    @app.get('/health/ready')
    def ready():
        try:
            with engine.connect() as conn:
                conn.execute(text('SELECT 1'))
                conn.execute(select(TopicState.user_id).limit(1))
                conn.execute(select(EmailProfile.email_hash).limit(1))
            return {'status':'ok', 'topics':len(app.state.catalog.topics)}
        except Exception:
            return JSONResponse({'status':'unavailable'}, status_code=503)

    @app.get('/api/config')
    def config():
        return {'auth_mode':settings.auth_mode, 'sentry_dsn':settings.frontend_sentry_dsn, 'release':settings.release}

    @app.post('/api/profile')
    def set_profile(body: ProfileBody, db: Session = Depends(get_db)):
        try:
            email = normalize_email(body.email)
        except ValueError as error:
            raise HTTPException(422, str(error))
        if settings.owner_email and email != settings.owner_email:
            raise HTTPException(403, 'Use the email configured for this Doomer.')
        profile_id = email_hash(email)
        profile = db.get(EmailProfile, profile_id)
        if profile is None:
            user_id = 'email:' + profile_id
            # Preserve a single existing verified owner's history on first profile creation.
            # Original progress/reaction rows are retained and never deleted or rewritten.
            if settings.owner_email:
                from uuid import UUID
                ids = set(db.scalars(select(TopicState.user_id).union(select(Reaction.user_id))))
                legacy = []
                for candidate in ids:
                    try:
                        UUID(candidate)
                        legacy.append(candidate)
                    except (ValueError, TypeError):
                        pass
                if len(legacy) == 1 and db.scalar(select(EmailProfile.email_hash).where(EmailProfile.user_id == legacy[0])) is None:
                    user_id = legacy[0]
            stmt = insert_for(db, EmailProfile, {'email_hash':profile_id, 'user_id':user_id})
            db.execute(stmt.on_conflict_do_nothing(index_elements=['email_hash']))
            db.commit()
        return {'profile_id':profile_id, 'email':email}

    def topic_or_404(topic_id):
        topic = app.state.catalog.topics.get(topic_id)
        if topic is None:
            raise HTTPException(404, 'Topic not found.')
        return topic

    def ensure_state(db, user, topic):
        stmt = insert_for(db, TopicState, {'user_id':user.id, 'topic_id':topic.id,
                                          'doom_id':topic.dooms[0]['id'], 'version':0})
        db.execute(stmt.on_conflict_do_nothing(index_elements=['user_id','topic_id']))
        db.commit()
        return db.get(TopicState, (user.id, topic.id))

    def snapshot(topic, state):
        ids = [d['id'] for d in topic.dooms]
        current = state.doom_id if state and state.doom_id in ids else ids[0]
        return {'id':topic.id, 'title':topic.title, 'count':len(ids), 'doom_id':current,
                'position':ids.index(current), 'version':state.version if state else 0,
                'finished':bool(state and state.finished_at)}

    @app.get('/api/topics')
    def topics(user: Identity = Depends(get_identity), db: Session = Depends(get_db)):
        states = {s.topic_id:s for s in db.scalars(select(TopicState).where(TopicState.user_id == user.id))}
        summaries = [snapshot(t, states.get(t.id)) for t in app.state.catalog.topics.values()]
        finished = [topic for topic in summaries if topic['finished']]
        return {'topics':[topic for topic in summaries if not topic['finished']],
                'finished_topics':finished,
                'total_topics':len(summaries), 'user_id':user.id,
                'finished_count':len(finished)}

    @app.get('/api/topics/{topic_id}')
    def detail(topic_id: str, user: Identity = Depends(get_identity), db: Session = Depends(get_db)):
        topic = topic_or_404(topic_id)
        state = ensure_state(db, user, topic)
        if state.finished_at:
            raise HTTPException(410, 'You have finished this topic.')
        reactions = {r.doom_id:r.value for r in db.scalars(select(Reaction).where(Reaction.user_id == user.id,
                                                                                 Reaction.doom_id.in_([d['id'] for d in topic.dooms])))}
        rows = [{'id':d['id'], 'title':d['title'], 'text':d['text'], 'sort_order':d['sort_order'],
                 'language':d['language'], 'source_locator':d['source_locator'],
                 'image_url':f"/api/topics/{topic.id}/images/{d['sort_order']}",
                 'reaction':reactions.get(d['id'])} for d in topic.dooms]
        return {**snapshot(topic, state), 'dooms':rows}

    @app.get('/api/topics/{topic_id}/images/{order}')
    def image(topic_id: str, order: int, user: Identity = Depends(get_identity)):
        topic = topic_or_404(topic_id)
        if not 1 <= order <= len(topic.dooms):
            raise HTTPException(404, 'Image not found.')
        file = (topic.folder / topic.dooms[order-1]['background_image']).resolve(strict=True)
        if not file.is_relative_to(topic.folder.resolve()):
            raise HTTPException(404)
        return FileResponse(file)

    @app.put('/api/topics/{topic_id}/progress')
    def progress(topic_id: str, body: ProgressBody, user: Identity = Depends(get_identity), db: Session = Depends(get_db)):
        topic = topic_or_404(topic_id)
        if body.doom_id not in {d['id'] for d in topic.dooms}:
            raise HTTPException(422, 'Doom does not belong to this topic.')
        ensure_state(db, user, topic)
        result = db.execute(update(TopicState).where(TopicState.user_id == user.id, TopicState.topic_id == topic.id,
                    TopicState.version == body.expected_version, TopicState.finished_at.is_(None))
                    .values(doom_id=body.doom_id, version=TopicState.version+1, updated_at=datetime.now(timezone.utc)))
        db.commit()
        if result.rowcount != 1:
            raise HTTPException(409, 'Progress changed on another device. Reload this topic to continue.')
        return {'version':body.expected_version+1}

    @app.put('/api/dooms/{doom_id}/reaction')
    def react(doom_id: str, body: ReactionBody, user: Identity = Depends(get_identity), db: Session = Depends(get_db)):
        if doom_id not in app.state.catalog.dooms:
            raise HTTPException(404, 'Doom not found.')
        if body.value is None:
            db.execute(delete(Reaction).where(Reaction.user_id == user.id, Reaction.doom_id == doom_id))
        else:
            stmt = insert_for(db, Reaction, {'user_id':user.id, 'doom_id':doom_id, 'value':body.value})
            db.execute(stmt.on_conflict_do_update(index_elements=['user_id','doom_id'],
                       set_={'value':body.value, 'updated_at':datetime.now(timezone.utc)}))
        db.commit()
        return {'reaction':body.value}

    @app.post('/api/topics/{topic_id}/finish')
    def finish(topic_id: str, user: Identity = Depends(get_identity), db: Session = Depends(get_db)):
        topic = topic_or_404(topic_id)
        ensure_state(db, user, topic)
        db.execute(update(TopicState).where(TopicState.user_id == user.id, TopicState.topic_id == topic.id,
                     TopicState.finished_at.is_(None)).values(finished_at=datetime.now(timezone.utc), version=TopicState.version+1))
        db.commit()
        return {'finished':True}

    @app.get('/{path:path}')
    def frontend(path: str):
        if path.startswith(('api/', 'health/')):
            raise HTTPException(404)
        dist = settings.frontend_dir.resolve()
        candidate = (dist / path).resolve()
        if candidate.is_relative_to(dist) and candidate.is_file():
            return FileResponse(candidate)
        if Path(path).suffix or path:
            raise HTTPException(404)
        if (dist / 'index.html').exists():
            return FileResponse(dist / 'index.html', headers={'Cache-Control':'no-cache'})
        return JSONResponse({'detail':'Build the frontend with npm run build in frontend/.'}, status_code=503)
    return app

app = create_app()
