from datetime import datetime
from sqlalchemy import DateTime, Integer, MetaData, String, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from fastapi import Request
from .settings import get_settings

class Base(DeclarativeBase):
    metadata = MetaData(schema='doomer')

class TopicState(Base):
    __tablename__ = 'topic_state'
    user_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    topic_id: Mapped[str] = mapped_column(String(250), primary_key=True)
    doom_id: Mapped[str] = mapped_column(String(300))
    version: Mapped[int] = mapped_column(Integer, default=0)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Reaction(Base):
    __tablename__ = 'reaction'
    user_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    doom_id: Mapped[str] = mapped_column(String(300), primary_key=True)
    value: Mapped[str] = mapped_column(String(7))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

def make_engine(url):
    if url.startswith('postgres://'):
        url = url.replace('postgres://', 'postgresql+psycopg://', 1)
    elif url.startswith('postgresql://'):
        url = url.replace('postgresql://', 'postgresql+psycopg://', 1)
    sqlite = url.startswith('sqlite:')
    engine = create_engine(url, pool_pre_ping=True, connect_args={'check_same_thread': False} if sqlite else {},
                           execution_options={'schema_translate_map': {'doomer': None}} if sqlite else {})
    return engine

def get_db(request: Request):
    with request.app.state.session_factory() as session:
        yield session

def insert_for(session, model, values):
    if session.bind.dialect.name == 'postgresql':
        from sqlalchemy.dialects.postgresql import insert
    else:
        from sqlalchemy.dialects.sqlite import insert
    return insert(model).values(**values)
