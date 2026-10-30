FROM node:24-bookworm-slim AS frontend
WORKDIR /build/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci --no-fund --no-audit
COPY frontend/ ./
RUN npm run build

FROM python:3.14-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 UV_LINK_MODE=copy
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY backend/ backend/
COPY alembic.ini ./
COPY .agents/skills/reel-it/references/ .agents/skills/reel-it/references/
COPY dooms/ dooms/
COPY --from=frontend /build/frontend/dist frontend/dist/
COPY scripts/start.sh scripts/start.sh
RUN groupadd --gid 10001 app && useradd --uid 10001 --gid app --no-create-home app && chmod +x scripts/start.sh && chown -R app:app /app
USER app
ENV PATH="/app/.venv/bin:$PATH"
ENV DOOMER_ENVIRONMENT=production DOOMER_AUTH_MODE=email
EXPOSE 8000
CMD ["sh", "scripts/start.sh"]
