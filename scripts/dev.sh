#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
export PATH="$PWD/.tools/node/bin:$PATH"
if [ ! -x .tools/uv ] || [ ! -x .tools/node/bin/node ]; then
  python3 scripts/bootstrap_tools.py
fi
.tools/uv sync --frozen
(cd frontend && npm ci --no-fund --no-audit && npm run build)
mkdir -p data
exec .venv/bin/uvicorn backend.main:app --host 127.0.0.1 --port "${PORT:-8000}" --no-access-log
