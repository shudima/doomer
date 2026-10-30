from dataclasses import dataclass
from functools import lru_cache
import jwt
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .settings import Settings, get_settings

bearer = HTTPBearer(auto_error=False)

@dataclass(frozen=True)
class Identity:
    id: str
    email: str

@lru_cache(maxsize=4)
def jwks_client(url):
    return jwt.PyJWKClient(url + '/auth/v1/.well-known/jwks.json', cache_keys=False, lifespan=300, timeout=8)

def verify_token(token: str, settings: Settings) -> Identity:
    issuer = settings.supabase_url.rstrip('/') + '/auth/v1'
    try:
        key = jwks_client(settings.supabase_url.rstrip('/')).get_signing_key_from_jwt(token)
        claims = jwt.decode(token, key.key, algorithms=['ES256', 'RS256'], audience='authenticated', issuer=issuer,
                            options={'require': ['exp', 'sub', 'iat', 'iss', 'aud']}, leeway=15)
    except jwt.PyJWKClientConnectionError:
        raise HTTPException(503, 'Sign-in verification is temporarily unavailable. Please retry.')
    except jwt.PyJWTError:
        raise HTTPException(401, 'Your session has expired. Please sign in again.', headers={'WWW-Authenticate':'Bearer'})
    if claims.get('role') != 'authenticated' or not claims.get('email') or claims['email'].casefold() != settings.owner_email.casefold():
        raise HTTPException(403, 'This is a private Doomer account.')
    return Identity(claims['sub'], claims['email'])

def get_identity(request: Request, credentials: HTTPAuthorizationCredentials | None = Depends(bearer)):
    settings = request.app.state.settings
    if settings.auth_mode == 'local' and settings.environment == 'development':
        return Identity('local-preview', 'Local preview')
    if credentials is None:
        raise HTTPException(401, 'Please sign in to continue.', headers={'WWW-Authenticate':'Bearer'})
    return verify_token(credentials.credentials, settings)
