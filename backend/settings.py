from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT / '.env', env_prefix='DOOMER_', extra='ignore', populate_by_name=True)
    environment: str = 'development'
    auth_mode: str = 'local'
    database_url: str = 'sqlite:///' + str(ROOT / 'data/doomer.db')
    content_dir: Path = ROOT / 'dooms'
    frontend_dir: Path = ROOT / 'frontend/dist'
    owner_email: str = ''
    supabase_url: str = ''
    supabase_publishable_key: str = ''
    sentry_dsn: str = ''
    frontend_sentry_dsn: str = ''
    release: str = 'development'
    allowed_hosts: str = 'localhost,127.0.0.1,testserver'
    render_external_hostname: str = Field(default='', validation_alias='RENDER_EXTERNAL_HOSTNAME')

    def trusted_hosts(self) -> list[str]:
        # Render supplies the service's exact public hostname; no wildcard is needed.
        values = [*self.allowed_hosts.split(','), self.render_external_hostname]
        return list(dict.fromkeys(host.strip() for host in values if host.strip()))

    def check(self):
        if self.auth_mode not in {'local', 'supabase'}:
            raise ValueError('DOOMER_AUTH_MODE must be local or supabase')
        if self.environment != 'development':
            if self.auth_mode != 'supabase':
                raise ValueError('Production requires Supabase authentication')
            if not self.database_url.startswith(('postgresql://', 'postgresql+psycopg://', 'postgres://')):
                raise ValueError('Production requires managed PostgreSQL')
        if self.auth_mode == 'supabase':
            if not (self.owner_email and self.supabase_url.startswith('https://') and self.supabase_publishable_key):
                raise ValueError('Configure owner email, Supabase HTTPS URL and publishable key')

@lru_cache
def get_settings():
    settings = Settings()
    settings.check()
    return settings
