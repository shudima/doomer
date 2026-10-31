import pytest
import yaml
from fastapi.testclient import TestClient
from backend.catalog import Catalog
from backend.main import create_app
from backend.settings import ROOT
from backend.tests.test_app import settings


def markdown_alpha(settings, insert=False, image='images/figure.svg'):
    folder=settings.content_dir/'alpha'
    (folder/'images/figure.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500"><rect width="800" height="500" fill="white"/></svg>')
    (folder/'diagrams').mkdir(exist_ok=True)
    (folder/'diagrams/flow.mmd').write_text('flowchart TD\n A --> B\n')
    records=[]
    for file in sorted(folder.glob('*.yaml')):
        row=yaml.safe_load(file.read_text());file.unlink()
        row.pop('text');row['schema_version']=2
        records.append(row)
    if insert:
        records.insert(1,{**records[0],'id':'alpha-004','title':'An added example'})
    for index,row in enumerate(records,1):
        row['sort_order']=index
        body=f'One **clear idea**.\n\n![A useful figure]({image})\n\n[Editable source](diagrams/flow.mmd)\n\n```mermaid\nflowchart TD\n A --> B\n```'
        (folder/f'{index:03}-idea.md').write_text('---\n'+yaml.safe_dump(row)+'---\n\n'+body+'\n')
    return folder


def test_markdown_api_and_authenticated_assets(settings):
    markdown_alpha(settings)
    configured=settings.model_copy(update={'auth_mode':'email','owner_email':'owner@example.org'})
    with TestClient(create_app(configured)) as client:
        profile=client.post('/api/profile',json={'email':'owner@example.org'}).json()
        headers={'X-Doomer-Profile':profile['profile_id']}
        topic=client.get('/api/topics/alpha',headers=headers).json()
        doom=topic['dooms'][0]
        assert doom['format']=='markdown' and doom['schema_version']==2
        assert '**clear idea**' in doom['text']
        asset=doom['assets']['images/figure.svg']
        assert (asset['width'],asset['height'])==(800,500)
        assert client.get(asset['url']).status_code==401
        response=client.get(asset['url'],headers=headers)
        assert response.status_code==200 and 'image/svg+xml' in response.headers['content-type']
        source=client.get(doom['assets']['diagrams/flow.mmd']['url'],headers=headers)
        assert source.status_code==200 and source.text.startswith('flowchart')
        assert 'text/plain' in source.headers['content-type']
        assert client.get('/api/topics/alpha/assets/original.pdf',headers=headers).status_code==404
        legacy=client.get('/api/topics/beta',headers=headers).json()['dooms'][0]
        assert legacy['format']=='text' and legacy['assets']=={}
        assert client.get('/health/ready').json()=={'status':'ok','topics':2,'dooms':6,'markdown_dooms':3}


def test_migration_keeps_progress_reactions_and_finished_topics_after_insertion(settings):
    with TestClient(create_app(settings)) as before:
        assert before.put('/api/topics/alpha/progress',json={'doom_id':'alpha-002','expected_version':0}).status_code==200
        before.put('/api/dooms/alpha-002/reaction',json={'value':'like'})
        before.post('/api/topics/beta/finish')
    markdown_alpha(settings,insert=True)
    with TestClient(create_app(settings)) as after:
        detail=after.get('/api/topics/alpha').json()
        assert detail['doom_id']=='alpha-002'
        assert detail['position']==2 and detail['version']==1
        assert detail['dooms'][2]['reaction']=='like'
        assert detail['dooms'][1]['id']=='alpha-004'
        library=after.get('/api/topics').json()
        assert library['finished_count']==1
        assert [t['id'] for t in library['finished_topics']]==['beta']


@pytest.mark.parametrize('image',['../outside.svg','/images/figure.svg','https://example.org/figure.svg','images/missing.png'])
def test_catalog_rejects_noncontained_or_missing_figures(settings,image):
    markdown_alpha(settings,image=image)
    with pytest.raises((ValueError,FileNotFoundError)):
        Catalog(settings.content_dir)


def test_catalog_rejects_active_svg_and_duplicate_ids(settings):
    folder=markdown_alpha(settings)
    figure=folder/'images/figure.svg'
    clean=figure.read_text()
    figure.write_text(clean.replace('</svg>','<script>alert(1)</script></svg>'))
    with pytest.raises(ValueError,match='Active SVG'):
        Catalog(settings.content_dir)
    figure.write_text(clean)
    second=folder/'002-idea.md'
    second.write_text(second.read_text().replace('id: alpha-002','id: alpha-001'))
    with pytest.raises(ValueError,match='Duplicate doom ID'):
        Catalog(settings.content_dir)


def test_complete_migrated_catalog():
    catalog=Catalog(ROOT/'dooms')
    assert len(catalog.topics)>=31
    assert len(catalog.dooms)>=746
    assert all(d['format']=='markdown' for t in catalog.topics.values() for d in t.dooms)
    assert sum(bool(d['asset_names']) for t in catalog.topics.values() for d in t.dooms)>=46
    # Published identities are stable even when examples change display order.
    for topic in catalog.topics.values():
        for d in topic.dooms:
            assert d['id'].startswith(topic.id+'-')
