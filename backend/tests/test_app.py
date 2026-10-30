from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
import json
import shutil
import jwt
import pytest
import yaml
from cryptography.hazmat.primitives.asymmetric import ec
from fastapi import HTTPException
from fastapi.testclient import TestClient
from backend.auth import Identity, get_identity, verify_token
from backend.catalog import Catalog
from backend.main import create_app
from backend.settings import ROOT, Settings

@pytest.fixture
def settings(tmp_path):
    for name in ['alpha', 'beta']:
        folder = tmp_path / 'content' / name
        (folder / 'images').mkdir(parents=True)
        (folder / 'images/bg.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920"/>')
        for index in range(1,4):
            data = {'schema_version':1, 'id':f'{name}-{index:03}', 'title':f'Idea {index}', 'text':'Useful test content.',
                    'sort_order':index, 'source_type':'article', 'source_url':'https://example.org/source',
                    'source_file':None, 'source_title':f'Topic {name}', 'source_locator':'Section: Example',
                    'language':'en', 'background_image':'images/bg.svg'}
            (folder / f'{index:03}-idea.yaml').write_text(yaml.safe_dump(data))
    return Settings(database_url='sqlite:///' + str(tmp_path/'test.db'), content_dir=tmp_path/'content',
                    frontend_dir=tmp_path/'dist', allowed_hosts='testserver', auth_mode='local', environment='development')

@pytest.fixture
def client(settings):
    with TestClient(create_app(settings)) as client:
        yield client

def test_progress_resumes_and_is_a_position_not_a_high_water_mark(client):
    assert client.get('/api/topics/alpha').json()['position'] == 0
    assert client.put('/api/topics/alpha/progress', json={'doom_id':'alpha-003','expected_version':0}).json()['version'] == 1
    assert client.get('/api/topics/alpha').json()['position'] == 2
    assert client.put('/api/topics/alpha/progress', json={'doom_id':'alpha-002','expected_version':1}).status_code == 200
    assert client.get('/api/topics/alpha').json()['position'] == 1
    assert client.get('/api/topics/beta').json()['position'] == 0

def test_progress_survives_application_restart(settings):
    with TestClient(create_app(settings)) as first:
        first.put('/api/topics/alpha/progress', json={'doom_id':'alpha-002','expected_version':0})
    with TestClient(create_app(settings)) as second:
        assert second.get('/api/topics/alpha').json()['doom_id'] == 'alpha-002'

def test_stale_device_cannot_overwrite_progress(client):
    client.put('/api/topics/alpha/progress', json={'doom_id':'alpha-003','expected_version':0})
    assert client.put('/api/topics/alpha/progress', json={'doom_id':'alpha-002','expected_version':0}).status_code == 409
    assert client.get('/api/topics/alpha').json()['doom_id'] == 'alpha-003'

def test_cross_topic_doom_is_rejected(client):
    assert client.put('/api/topics/alpha/progress', json={'doom_id':'beta-001','expected_version':0}).status_code == 422

def test_reactions_replace_and_can_be_removed(client):
    for value in ['like','dislike',None]:
        assert client.put('/api/dooms/alpha-001/reaction',json={'value':value}).status_code == 200
        assert client.get('/api/topics/alpha').json()['dooms'][0]['reaction'] == value
    assert client.put('/api/dooms/alpha-001/reaction',json={'value':'other'}).status_code == 422

def test_finish_is_idempotent_and_cannot_be_resurrected(client):
    client.put('/api/dooms/alpha-001/reaction',json={'value':'like'})
    assert client.post('/api/topics/alpha/finish').status_code == 200
    assert client.post('/api/topics/alpha/finish').status_code == 200
    assert [t['id'] for t in client.get('/api/topics').json()['topics']] == ['beta']
    assert client.get('/api/topics/alpha').status_code == 410
    assert client.put('/api/topics/alpha/progress',json={'doom_id':'alpha-001','expected_version':1}).status_code == 409
    client.post('/api/topics/beta/finish')
    assert client.get('/api/topics').json()['topics'] == []

def test_users_are_isolated(client):
    client.put('/api/topics/alpha/progress',json={'doom_id':'alpha-003','expected_version':0})
    client.put('/api/dooms/alpha-001/reaction',json={'value':'like'})
    client.post('/api/topics/beta/finish')
    client.app.dependency_overrides[get_identity] = lambda: Identity('different-user','different@example.org')
    assert len(client.get('/api/topics').json()['topics']) == 2
    detail = client.get('/api/topics/alpha').json()
    assert detail['position'] == 0
    assert detail['dooms'][0]['reaction'] is None

def test_unknown_and_traversal_paths_fail(client):
    assert client.get('/api/topics/missing').status_code == 404
    assert client.get('/api/topics/alpha/images/99').status_code == 404
    assert client.get('/api/unknown').status_code == 404
    assert client.get('/.env').status_code == 404
    assert client.get('/%2e%2e/AGENTS.md').status_code == 404

def test_private_endpoints_require_auth(settings):
    configured = settings.model_copy(update={'auth_mode':'supabase', 'owner_email':'owner@example.org',
                         'supabase_url':'https://project.supabase.co', 'supabase_publishable_key':'publishable-test'})
    with TestClient(create_app(configured)) as private:
        assert private.get('/api/topics').status_code == 401
        assert private.get('/api/topics/alpha/images/1').status_code == 401
        assert private.post('/api/topics/alpha/finish').status_code == 401
        assert private.get('/api/config').status_code == 200
        assert private.get('/health/live').status_code == 200

def test_production_cannot_use_preview_auth_or_ephemeral_sqlite(settings):
    with pytest.raises(ValueError,match='authentication'):
        create_app(settings.model_copy(update={'environment':'production'}))
    with pytest.raises(ValueError,match='PostgreSQL'):
        create_app(settings.model_copy(update={'environment':'production','auth_mode':'supabase'}))

def test_catalog_rejects_missing_assets(settings):
    (settings.content_dir/'alpha/images/bg.svg').unlink()
    with pytest.raises(FileNotFoundError):
        Catalog(settings.content_dir)

def test_auth_checks_signature_audience_expiry_and_owner(monkeypatch):
    key = ec.generate_private_key(ec.SECP256R1())
    other_key = ec.generate_private_key(ec.SECP256R1())
    monkeypatch.setattr('backend.auth.jwks_client',lambda url:SimpleNamespace(get_signing_key_from_jwt=lambda token:SimpleNamespace(key=key.public_key())))
    settings = Settings(auth_mode='supabase', owner_email='owner@example.org',supabase_url='https://project.supabase.co',supabase_publishable_key='test')
    now = datetime.now(timezone.utc)
    base = {'sub':'owner-id', 'email':'owner@example.org','role':'authenticated','iat':now,'exp':now+timedelta(hours=1),
            'aud':'authenticated','iss':'https://project.supabase.co/auth/v1'}
    token = lambda claims, signing_key=key:jwt.encode(claims,signing_key,algorithm='ES256',headers={'kid':'test'})
    assert verify_token(token(base),settings).id == 'owner-id'
    for changes, signing_key, status in [({'email':'stranger@example.org'},key,403),({'aud':'other'},key,401),
           ({'exp':now-timedelta(minutes=1)},key,401),({},other_key,401),({'iss':'https://attacker.example'},key,401)]:
        with pytest.raises(HTTPException) as caught:
            verify_token(token({**base,**changes},signing_key), settings)
        assert caught.value.status_code == status


def test_render_platform_hostname_is_accepted(settings, monkeypatch):
    monkeypatch.setenv('RENDER_EXTERNAL_HOSTNAME', 'doomer-b5gn.onrender.com')
    configured = Settings(**settings.model_dump(exclude={'render_external_hostname'}))
    with TestClient(create_app(configured)) as deployed:
        headers = {'host':'doomer-b5gn.onrender.com'}
        assert deployed.get('/api/config', headers=headers).status_code == 200
        assert deployed.get('/health/live', headers=headers).status_code == 200
        assert deployed.get('/health/ready', headers=headers).status_code == 200
        assert deployed.get('/api/config', headers={'host':'attacker.example'}).status_code == 400


def test_render_hostname_works_with_empty_optional_host_list(settings, monkeypatch):
    monkeypatch.setenv('RENDER_EXTERNAL_HOSTNAME', 'doomer-b5gn.onrender.com')
    configured = Settings(**{**settings.model_dump(exclude={'render_external_hostname'}), 'allowed_hosts':''})
    with TestClient(create_app(configured)) as deployed:
        assert deployed.get('/api/config', headers={'host':'doomer-b5gn.onrender.com'}).status_code == 200


def test_custom_host_stays_allowed_without_allowing_arbitrary_hosts(settings, monkeypatch):
    monkeypatch.setenv('RENDER_EXTERNAL_HOSTNAME', 'doomer-b5gn.onrender.com')
    configured = Settings(**{**settings.model_dump(exclude={'render_external_hostname'}),
                             'allowed_hosts':' testserver, read.example.com, '})
    with TestClient(create_app(configured)) as deployed:
        assert deployed.get('/api/config', headers={'host':'read.example.com'}).status_code == 200
        assert deployed.get('/api/config', headers={'host':'doomer-b5gn.onrender.com'}).status_code == 200
        assert deployed.get('/api/config', headers={'host':'anything.onrender.com'}).status_code == 400
