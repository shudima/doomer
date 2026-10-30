"""Unverified email profiles: identity labels, not authentication credentials."""
from dataclasses import dataclass
import hashlib
import re
from fastapi import HTTPException, Request
from .db import EmailProfile

@dataclass(frozen=True)
class Identity:
    id: str
    email: str = ''

def normalize_email(value: str) -> str:
    value = value.strip().casefold()
    if len(value) > 254 or not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', value):
        raise ValueError('Enter a valid email address.')
    return value

def email_hash(email: str) -> str:
    return hashlib.sha256(normalize_email(email).encode('utf-8')).hexdigest()

def get_identity(request: Request):
    settings = request.app.state.settings
    if settings.auth_mode == 'local' and settings.environment == 'development':
        return Identity('local-preview', 'Local preview')
    profile_id = request.headers.get('X-Doomer-Profile', '')
    if not re.fullmatch(r'[0-9a-f]{64}', profile_id):
        raise HTTPException(401, 'Set your email to open your saved progress.')
    if settings.owner_email and profile_id != email_hash(settings.owner_email):
        raise HTTPException(403, 'Use the email configured for this Doomer.')
    with request.app.state.session_factory() as session:
        profile = session.get(EmailProfile, profile_id)
        if profile is None:
            raise HTTPException(401, 'Set your email again to restore your profile.')
        return Identity(profile.user_id)
