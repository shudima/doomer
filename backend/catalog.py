from dataclasses import dataclass
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
import yaml
import jsonschema
from .settings import ROOT

@dataclass(frozen=True)
class Topic:
    id: str
    title: str
    dooms: tuple[dict, ...]
    folder: Path

class Catalog:
    def __init__(self, directory: Path):
        self.topics = {}
        self.dooms = {}
        schema = json.loads((ROOT / '.agents/skills/reel-it/references/reel.schema.json').read_text())
        if not directory.is_dir():
            raise ValueError('Content directory does not exist')
        for folder in sorted(directory.iterdir()):
            if not folder.is_dir() or folder.name.startswith('.'):
                continue
            if folder.is_symlink() or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', folder.name):
                raise ValueError(f'Invalid collection directory: {folder.name}')
            rows = []
            for file in folder.glob('*.yaml'):
                if file.is_symlink():
                    raise ValueError('Symlinked content is not accepted')
                row = yaml.safe_load(file.read_text(encoding='utf-8'))
                jsonschema.validate(row, schema)
                if not file.name.startswith(f"{row['sort_order']:03}-"):
                    raise ValueError(f'Filename/order mismatch: {file.name}')
                image = (folder / row['background_image']).resolve(strict=True)
                if not image.is_relative_to(folder.resolve()) or not image.stat().st_size:
                    raise ValueError('Image escapes collection or is empty')
                if image.suffix == '.svg':
                    svg = ET.parse(image).getroot()
                    # Collection images are trusted local assets; reject active SVG content.
                    if any(n.tag.split('}')[-1] in {'script', 'foreignObject'} or any(k.lower().startswith('on') for k in n.attrib) for n in svg.iter()):
                        raise ValueError('Active SVG content is not accepted')
                if row['source_file']:
                    source = (folder / row['source_file']).resolve(strict=True)
                    if not source.is_relative_to(folder.resolve()) or not source.stat().st_size:
                        raise ValueError('Invalid local source')
                if row['id'] in self.dooms:
                    raise ValueError(f"Duplicate doom ID: {row['id']}")
                self.dooms[row['id']] = folder.name
                rows.append(row)
            if not rows:
                continue
            rows.sort(key=lambda x: x['sort_order'])
            if [r['sort_order'] for r in rows] != list(range(1, len(rows) + 1)):
                raise ValueError(f'Noncontiguous collection: {folder.name}')
            if len({r['source_title'] for r in rows}) != 1:
                raise ValueError('Inconsistent source title')
            self.topics[folder.name] = Topic(folder.name, rows[0]['source_title'], tuple(rows), folder)
