from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
import json
import shutil
import pytest
import yaml
from fastapi import HTTPException
from fastapi.testclient import TestClient
from backend.auth import Identity, get_identity
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
    configured = settings.model_copy(update={'auth_mode':'email', 'owner_email':'owner@example.org'})
    with TestClient(create_app(configured)) as private:
        assert private.get('/api/topics').status_code == 401
        assert private.get('/api/topics/alpha/images/1').status_code == 401
        assert private.post('/api/topics/alpha/finish').status_code == 401
        assert private.get('/api/config').status_code == 200
        assert private.get('/health/live').status_code == 200

def test_production_cannot_use_preview_auth_or_ephemeral_sqlite(settings):
    with pytest.raises(ValueError,match='email profiles'):
        create_app(settings.model_copy(update={'environment':'production'}))
    with pytest.raises(ValueError,match='PostgreSQL'):
        create_app(settings.model_copy(update={'environment':'production','auth_mode':'email'}))

def test_catalog_rejects_missing_assets(settings):
    (settings.content_dir/'alpha/images/bg.svg').unlink()
    with pytest.raises(FileNotFoundError):
        Catalog(settings.content_dir)


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

def email_client(settings, owner='reader@example.com'):
    configured = settings.model_copy(update={'auth_mode':'email','owner_email':owner})
    return TestClient(create_app(configured))

def test_email_profile_needs_no_code_or_email_delivery(settings):
    with email_client(settings) as client:
        first = client.post('/api/profile', json={'email':' Reader@Example.com '})
        assert first.status_code == 200
        profile = first.json()
        assert profile['email'] == 'reader@example.com'
        headers = {'X-Doomer-Profile':profile['profile_id']}
        assert client.get('/api/topics',headers=headers).status_code == 200
        same = client.post('/api/profile',json={'email':'reader@example.com'}).json()
        assert same == profile
        assert client.get('/api/config').json()['auth_mode'] == 'email'
        assert 'supabase_publishable_key' not in client.get('/api/config').json()

def test_email_profiles_restore_progress_reactions_and_completion_on_another_device(settings):
    with email_client(settings) as first:
        profile = first.post('/api/profile',json={'email':'reader@example.com'}).json()
        headers = {'X-Doomer-Profile':profile['profile_id']}
        assert first.put('/api/topics/alpha/progress',headers=headers,json={'doom_id':'alpha-002','expected_version':0}).status_code == 200
        first.put('/api/dooms/alpha-002/reaction',headers=headers,json={'value':'like'})
        first.post('/api/topics/beta/finish',headers=headers)
    with email_client(settings) as second:
        profile2 = second.post('/api/profile',json={'email':'READER@example.com'}).json()
        assert profile2 == profile
        headers2 = {'X-Doomer-Profile':profile2['profile_id']}
        detail = second.get('/api/topics/alpha',headers=headers2).json()
        assert detail['position'] == 1
        assert detail['dooms'][1]['reaction'] == 'like'
        assert [t['id'] for t in second.get('/api/topics',headers=headers2).json()['topics']] == ['alpha']

def test_email_setup_rejects_invalid_and_unconfigured_addresses(settings):
    with email_client(settings) as client:
        assert client.post('/api/profile',json={'email':'wrong@example.com'}).status_code == 403
        assert client.post('/api/profile',json={'email':'not-an-email'}).status_code == 422
        assert client.get('/api/topics',headers={'X-Doomer-Profile':'0'*64}).status_code == 403

def test_different_emails_have_separate_progress_when_owner_is_not_restricted(settings):
    with email_client(settings,owner='') as client:
        a = client.post('/api/profile',json={'email':'one@example.com'}).json()
        b = client.post('/api/profile',json={'email':'two@example.com'}).json()
        assert a['profile_id'] != b['profile_id']
        client.post('/api/topics/alpha/finish',headers={'X-Doomer-Profile':a['profile_id']})
        assert len(client.get('/api/topics',headers={'X-Doomer-Profile':a['profile_id']}).json()['topics']) == 1
        assert len(client.get('/api/topics',headers={'X-Doomer-Profile':b['profile_id']}).json()['topics']) == 2

def test_email_setup_retains_existing_verified_owner_history(settings):
    from backend.db import Reaction, TopicState
    previous_id = '8aa9898a-5436-4339-b49c-4a38e65248ff'
    with email_client(settings) as client:
        with client.app.state.session_factory() as session:
            session.add(TopicState(user_id=previous_id,topic_id='alpha',doom_id='alpha-002',version=7))
            session.add(Reaction(user_id=previous_id,doom_id='alpha-002',value='like'))
            session.commit()
        profile = client.post('/api/profile',json={'email':'reader@example.com'}).json()
        headers = {'X-Doomer-Profile':profile['profile_id']}
        detail = client.get('/api/topics/alpha',headers=headers).json()
        assert detail['position'] == 1
        assert detail['version'] == 7
        assert detail['dooms'][1]['reaction'] == 'like'
        assert client.get('/api/topics',headers=headers).json()['user_id'] == previous_id

def test_old_render_mode_value_maps_to_the_requested_email_only_flow():
    settings = Settings(auth_mode='supabase',owner_email='reader@example.com',_env_file=None)
    assert settings.auth_mode == 'email'
    settings.check()

def test_email_profile_settings_do_not_require_auth_service_keys():
    settings = Settings(environment='production',auth_mode='email',
                        database_url='postgresql://user:password@localhost/db',owner_email='Reader@Example.com',_env_file=None)
    settings.check()
    assert settings.owner_email == 'reader@example.com'
