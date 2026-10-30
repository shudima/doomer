from functools import lru_cache
from pathlib import Path
from pydantic import Field, field_validator
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
    sentry_dsn: str = ''
    frontend_sentry_dsn: str = ''
    release: str = 'development'
    allowed_hosts: str = 'localhost,127.0.0.1,testserver'
    render_external_hostname: str = Field(default='', validation_alias='RENDER_EXTERNAL_HOSTNAME')

    @field_validator('auth_mode', mode='before')
    @classmethod
    def replace_legacy_email_link_mode(cls, value):
        # This personal app now uses unverified email labels at the owner's request.
        # Existing Render services can keep their old environment value during rollout.
        return 'email' if value == 'supabase' else value

    def trusted_hosts(self) -> list[str]:
        # Render supplies the service's exact public hostname; no wildcard is needed.
        values = [*self.allowed_hosts.split(','), self.render_external_hostname]
        return list(dict.fromkeys(host.strip() for host in values if host.strip()))

    def check(self):
        if self.auth_mode not in {'local', 'email'}:
            raise ValueError('DOOMER_AUTH_MODE must be local or email')
        if self.environment != 'development':
            if self.auth_mode != 'email':
                raise ValueError('Production requires email profiles; local preview is development-only')
            if not self.database_url.startswith(('postgresql://', 'postgresql+psycopg://', 'postgres://')):
                raise ValueError('Production requires managed PostgreSQL')
        if self.owner_email:
            from .auth import normalize_email
            self.owner_email = normalize_email(self.owner_email)

@lru_cache
def get_settings():
    settings = Settings()
    settings.check()
    return settings
