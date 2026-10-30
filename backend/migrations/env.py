from alembic import context
from sqlalchemy import text
from backend.db import Base, make_engine
from backend.settings import get_settings

engine = make_engine(get_settings().database_url)
with engine.connect() as connection:
    postgres = connection.dialect.name == 'postgresql'
    if postgres:
        connection.execute(text('CREATE SCHEMA IF NOT EXISTS doomer'))
        connection.commit()
    context.configure(connection=connection, target_metadata=Base.metadata,
                      version_table_schema='doomer' if postgres else None, include_schemas=True)
    with context.begin_transaction():
        context.run_migrations()
