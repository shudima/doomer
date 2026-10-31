#!/usr/bin/env python3
"""Validate Markdown/frontmatter reels and legacy YAML collections (no network)."""
import argparse
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

import jsonschema
import yaml

REFERENCES = Path(__file__).resolve().parents[1] / 'references'
IMAGE = re.compile(r'!\[([^\]]*)\]\(\s*<?([^\s)>]+)>?(?:\s+[\"\'][^\n]*?[\"\'])?\s*\)')
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(\s*<?([^\s)>]+)>?(?:\s+[\"\'][^\n]*?[\"\'])?\s*\)')
FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')


def prose_without_fences(body):
    visible = []
    opened = None
    for line in body.splitlines():
        match = FENCE.match(line)
        if opened:
            if match and match[1][0] == opened[0] and len(match[1]) >= len(opened) and not match[2].strip():
                opened = None
        elif match:
            opened = match[1]
        else:
            visible.append(line)
    if opened:
        raise ValueError('Unclosed Markdown code fence')
    # Inline code can teach Markdown syntax without actually embedding a figure.
    return re.sub(r'(`+)(?!`)(.+?)(?<!`)\1(?!`)', '', '\n'.join(visible), flags=re.S)


def local_file(folder, relative):
    if not isinstance(relative, str) or '\\' in relative or Path(relative).is_absolute():
        raise ValueError(f'Use a collection-relative path with / separators: {relative!r}')
    if any(part in {'.', '..'} for part in relative.split('/')) or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', relative):
        raise ValueError(f'Asset path is not a local contained path: {relative}')
    target = folder / relative
    resolved = target.resolve(strict=True)
    if not resolved.is_relative_to(folder) or not resolved.is_file() or not resolved.stat().st_size:
        raise ValueError(f'Missing, empty or escaping asset: {relative}')
    return resolved


def image_dimensions(path):
    if path.suffix.lower() == '.svg':
        svg = ET.parse(path).getroot()
        if svg.tag.split('}')[-1] != 'svg':
            raise ValueError(f'Not an SVG: {path.name}')
        for node in svg.iter():
            if node.tag.split('}')[-1] in {'script', 'foreignObject'} or any(key.lower().startswith('on') for key in node.attrib):
                raise ValueError(f'Active SVG content: {path.name}')
            for key, value in node.attrib.items():
                if key.split('}')[-1] == 'href' and not value.startswith('#'):
                    raise ValueError(f'SVG must embed its visual content locally: {path.name}')
        dimensions = []
        for name in ('width', 'height'):
            match = re.fullmatch(r'(\d+(?:\.\d+)?)(?:px)?', svg.get(name, ''))
            dimensions.append(float(match[1]) if match else None)
        if None not in dimensions:
            return dimensions
        viewbox = re.split(r'[\s,]+', svg.get('viewBox', '').strip())
        if len(viewbox) == 4:
            return float(viewbox[2]), float(viewbox[3])
        raise ValueError(f'SVG needs dimensions or a viewBox: {path.name}')
    if path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.gif'}:
        raise ValueError(f'Unsupported image type: {path.name}')
    try:
        from PIL import Image
    except ImportError as error:
        raise ValueError('Install Pillow to decode raster assets') from error
    with Image.open(path) as image:
        dimensions = image.size
        image.verify()
    return dimensions


def parse_reel(path):
    value = path.read_text(encoding='utf-8-sig')
    if path.suffix == '.yaml':
        row = yaml.safe_load(value)
        return row, row.get('text', '') if isinstance(row, dict) else '', 'reel.schema.json'
    if not value.startswith('---\n'):
        raise ValueError('Markdown reel must start with YAML frontmatter')
    parts = value[4:].split('\n---\n', 1)
    if len(parts) != 2:
        raise ValueError('Markdown frontmatter needs a closing --- line')
    return yaml.safe_load(parts[0]), parts[1].strip(), 'reel-markdown.schema.json'


def validate_collection(directory):
    folder = Path(directory).resolve(strict=True)
    if not folder.is_dir():
        raise ValueError('Collection must be a directory')
    local_file(folder, 'coverage.md')
    files = [path for path in folder.iterdir() if path.suffix in {'.yaml', '.md'} and path.name != 'coverage.md']
    if not files:
        raise ValueError('No reels found')
    if len({path.suffix for path in files}) != 1:
        raise ValueError('Do not mix Markdown and legacy YAML reels in one collection')
    for path in files:
        if not re.match(r'^\d{3,}-.+\.(?:md|yaml)$', path.name) or path.is_symlink():
            raise ValueError(f'Invalid reel filename: {path.name}')
    files.sort(key=lambda path: int(path.name.split('-', 1)[0]))
    sources = set()
    ids = set()
    checked_images = {}
    for index, path in enumerate(files, 1):
        try:
            row, body, schema_name = parse_reel(path)
            schema = json.loads((REFERENCES / schema_name).read_text())
            jsonschema.validate(row, schema)
            if not body.strip():
                raise ValueError('Reel body is empty')
            if row['sort_order'] != index or not path.name.startswith(f'{index:03}-'):
                raise ValueError('Order must be contiguous and match filenames')
            if not re.fullmatch(re.escape(folder.name) + r'-[0-9]{3,}', row['id']) or row['id'] in ids:
                raise ValueError('ID must use the collection prefix plus a unique numeric identity')
            ids.add(row['id'])
            sources.add(tuple(row[field] for field in ('source_url', 'source_file', 'source_title', 'source_type', 'language')))
            background = local_file(folder, row['background_image'])
            if background not in checked_images:
                checked_images[background] = image_dimensions(background)
            width, height = checked_images[background]
            if width <= 0 or height <= width:
                raise ValueError('Background image must be portrait')
            if row['source_file']:
                pdf = local_file(folder, row['source_file'])
                if b'%PDF-' not in pdf.read_bytes()[:1024]:
                    raise ValueError('Preserved source is not a PDF')
            if path.suffix == '.md':
                prose = prose_without_fences(body)
                images = list(IMAGE.finditer(prose))
                if len(images) != len(re.findall(r'!\[', prose)):
                    raise ValueError('Use inline Markdown figures: ![alt text](images/file.ext)')
                for match in images:
                    if not match[1].strip():
                        raise ValueError('Figures need meaningful alt text')
                    if not match[2].startswith('images/'):
                        raise ValueError('Inline figures must be local assets under images/')
                    figure = local_file(folder, match[2])
                    if figure not in checked_images:
                        checked_images[figure] = image_dimensions(figure)
                for match in LINK.finditer(prose):
                    target = match[1]
                    if target.startswith(('https://', 'http://', '#', 'mailto:')):
                        continue
                    local_file(folder, target.split('#', 1)[0])
        except (ValueError, OSError, ET.ParseError, yaml.YAMLError, jsonschema.ValidationError) as error:
            raise ValueError(f'{path.name}: {error}') from error
    if len(sources) != 1:
        raise ValueError('Source metadata must be consistent across the collection')
    return len(files), files[0].suffix, ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('collections', nargs='+', type=Path)
    args = parser.parse_args()
    all_ids = set()
    try:
        for collection in args.collections:
            count, extension, ids = validate_collection(collection)
            if all_ids.intersection(ids):
                raise ValueError('Duplicate reel IDs across collections')
            all_ids.update(ids)
            print(f'Valid: {collection.name}: {count} {extension} reels')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Invalid: {error}\n')


if __name__ == '__main__':
    main()
