"""Install project-local build tools, leaving system packages untouched."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tarfile
import urllib.request
import zipfile

root = Path('/home/dima/projects/doomer')
tools = root / '.tools'
tools.mkdir(exist_ok=True)
if not (tools / 'node/bin/node').exists():
    releases = json.load(urllib.request.urlopen('https://nodejs.org/dist/index.json'))
    version = next(r['version'] for r in releases if r['version'].startswith('v24.') and r['lts'])
    name = f'node-{version}-linux-x64.tar.xz'
    base = f'https://nodejs.org/dist/{version}/'
    archive = tools / name
    urllib.request.urlretrieve(base + name, archive)
    checks = urllib.request.urlopen(base + 'SHASUMS256.txt').read().decode()
    expected = next(line.split()[0] for line in checks.splitlines() if line.endswith('  ' + name))
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == expected
    with tarfile.open(archive) as handle:
        handle.extractall(tools, filter='data')
    (tools / f'node-{version}-linux-x64').rename(tools / 'node')
    archive.unlink()
if not (tools / 'uv').exists():
    metadata = json.load(urllib.request.urlopen('https://pypi.org/pypi/uv/json'))
    wheel = next(x for x in metadata['urls'] if 'manylinux' in x['filename'] and 'x86_64' in x['filename'])
    archive = tools / wheel['filename']
    urllib.request.urlretrieve(wheel['url'], archive)
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == wheel['digests']['sha256']
    with zipfile.ZipFile(archive) as handle:
        member = next(n for n in handle.namelist() if n.endswith('/uv') and '/scripts/' in n)
        (tools / 'uv').write_bytes(handle.read(member))
    (tools / 'uv').chmod(0o755)
    archive.unlink()
print('Project-local Node and uv ready.')
