from dataclasses import dataclass, field
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
import yaml
import jsonschema
from markdown_it import MarkdownIt
from PIL import Image
from .settings import ROOT


@dataclass(frozen=True)
class Asset:
    path: Path
    token: str
    width: int | None = None
    height: int | None = None


@dataclass(frozen=True)
class Topic:
    id: str
    title: str
    dooms: tuple[dict, ...]
    folder: Path
    assets: dict[str, Asset] = field(default_factory=dict)


def contained_file(folder: Path, name: str):
    if not isinstance(name, str) or '\\' in name or name.startswith('/') or any(part in {'.','..'} for part in name.split('/')):
        raise ValueError('Invalid collection asset path')
    candidate = folder / name
    if candidate.is_symlink():
        raise ValueError('Symlinked assets are not accepted')
    candidate = candidate.resolve(strict=True)
    if not candidate.is_relative_to(folder.resolve()) or not candidate.is_file() or not candidate.stat().st_size:
        raise ValueError('Asset escapes collection or is empty')
    return candidate


def image_size(path: Path):
    if path.suffix.lower() == '.svg':
        svg = ET.parse(path).getroot()
        if svg.tag.split('}')[-1] != 'svg':
            raise ValueError('Invalid SVG')
        for node in svg.iter():
            if node.tag.split('}')[-1] in {'script','foreignObject'} or any(key.lower().startswith('on') for key in node.attrib):
                raise ValueError('Active SVG content is not accepted')
            if any(key.split('}')[-1] == 'href' and not value.startswith('#') for key,value in node.attrib.items()):
                raise ValueError('SVG external resources are not accepted')
        dimensions = []
        for key in ['width','height']:
            match = re.fullmatch(r'(\d+(?:\.\d+)?)(?:px)?', svg.get(key,''))
            dimensions.append(float(match[1]) if match else None)
        if None in dimensions:
            box = re.split(r'[\s,]+', svg.get('viewBox','').strip())
            if len(box) != 4:
                raise ValueError('SVG needs dimensions')
            dimensions = [float(box[2]),float(box[3])]
        return tuple(round(value) for value in dimensions)
    if path.suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.gif'}:
        raise ValueError('Unsupported image format')
    with Image.open(path) as image:
        size = image.size
        image.verify()
    return size


def parse_reel(file: Path, schemas: dict):
    content = file.read_text(encoding='utf-8-sig')
    if file.suffix == '.md':
        if not content.startswith('---\n'):
            raise ValueError('Markdown reel needs frontmatter')
        parts = content[4:].split('\n---\n',1)
        if len(parts) != 2 or not parts[1].strip():
            raise ValueError('Markdown reel needs closed frontmatter and a body')
        row = yaml.safe_load(parts[0])
        jsonschema.validate(row, schemas[2])
        return {**row,'text':parts[1].strip(),'format':'markdown'}
    row = yaml.safe_load(content)
    jsonschema.validate(row, schemas[1])
    return {**row,'format':'text'}


def references(tokens):
    for token in tokens:
        if token.type == 'image':
            yield token.attrGet('src'), True
        elif token.type == 'link_open':
            target = token.attrGet('href') or ''
            if target and not re.match(r'^(?:https?://|mailto:|#)', target):
                yield target, False
        if token.children:
            yield from references(token.children)


class Catalog:
    def __init__(self, directory: Path):
        self.topics = {}
        self.dooms = {}
        base = ROOT / '.agents/skills/reel-it/references'
        schemas = {1:json.loads((base/'reel.schema.json').read_text()),2:json.loads((base/'reel-markdown.schema.json').read_text())}
        parser = MarkdownIt('commonmark', {'html':False})
        if not directory.is_dir():
            raise ValueError('Content directory does not exist')
        for folder in sorted(directory.iterdir()):
            if not folder.is_dir() or folder.name.startswith('.'):
                continue
            if folder.is_symlink() or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',folder.name):
                raise ValueError(f'Invalid collection directory: {folder.name}')
            rows, assets, dimensions = [], {}, {}
            for file in sorted(folder.iterdir()):
                if file.suffix not in {'.yaml','.md'} or file.name == 'coverage.md':
                    continue
                if file.is_symlink():
                    raise ValueError('Symlinked content is not accepted')
                row = parse_reel(file,schemas)
                if not file.name.startswith(f"{row['sort_order']:03}-"):
                    raise ValueError(f'Filename/order mismatch: {file.name}')
                background = contained_file(folder,row['background_image'])
                if background not in dimensions:
                    dimensions[background] = image_size(background)
                if row['source_file']:
                    contained_file(folder,row['source_file'])
                names = []
                if row['format'] == 'markdown':
                    for name,is_image in references(parser.parse(row['text'])):
                        name = name.split('#',1)[0]
                        if not name.startswith(('images/','diagrams/','source/')):
                            raise ValueError(f'Markdown assets must be local: {name}')
                        path = contained_file(folder,name)
                        if is_image:
                            if not name.startswith('images/'):
                                raise ValueError('Figures must be under images/')
                            if path not in dimensions:
                                dimensions[path] = image_size(path)
                            width,height = dimensions[path]
                        else:
                            if path.suffix not in {'.mmd','.pdf','.svg','.png','.jpg','.jpeg','.webp','.gif'}:
                                raise ValueError('Unsupported linked asset')
                            if path.suffix == '.svg' and path not in dimensions:
                                dimensions[path] = image_size(path)
                            width,height = dimensions.get(path,(None,None))
                        if name not in assets:
                            token = hashlib.sha256(name.encode()).hexdigest()[:20]
                            assets[name] = Asset(path,token,width,height)
                        names.append(name)
                row['asset_names'] = list(dict.fromkeys(names))
                if row['id'] in self.dooms:
                    raise ValueError(f"Duplicate doom ID: {row['id']}")
                self.dooms[row['id']] = folder.name
                rows.append(row)
            if not rows:
                continue
            rows.sort(key=lambda row:row['sort_order'])
            if [row['sort_order'] for row in rows] != list(range(1,len(rows)+1)):
                raise ValueError(f'Noncontiguous collection: {folder.name}')
            if len({(row['source_title'],row['source_url'],row['source_type'],row['language']) for row in rows}) != 1:
                raise ValueError('Inconsistent source metadata')
            self.topics[folder.name] = Topic(folder.name,rows[0]['source_title'],tuple(rows),folder,assets)
