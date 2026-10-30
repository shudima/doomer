# Doomer

A phone-first feed of source-backed text reels with unverified email profiles. Built in `/home/dima/projects/doomer` with React, TypeScript and FastAPI.

## Run on this computer

```bash
cd /home/dima/projects/doomer
sh scripts/dev.sh
```

Open [http://localhost:8000](http://localhost:8000). The script installs project-local tooling if needed, installs locked dependencies, builds the UI and starts the API on loopback. Stop with Ctrl+C.

The local preview stores state in `data/doomer.db` using SQLite and shows **Saved locally**. It does not send emails or sync to another device. Do not expose preview mode to the internet. Hosted state uses PostgreSQL and an email profile selected once on each device. This is an unverified profile label, not authentication. Local-preview bypass mode remains development-only.

For UI development, run the backend command below. In a second shell export the same project-local Node path, change to `frontend/` and run `npm run dev`. Vite proxies API calls to the backend.

```bash
export PATH="$PWD/.tools/node/bin:$PATH"
.venv/bin/uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

## Behavior

- Opening the app picks a random unfinished topic. New topics start at doom 1; returning topics resume the current saved doom.
- Scroll down/up within the topic. Swipe left or right to choose another unfinished topic, excluding the current one. The footer offers an equivalent button. Keyboard: down/space for next doom, up for previous, left/right for another topic.
- Open the three-dot menu for a searchable topic explorer. Pick a topic directly to resume its saved doom. Finished topics stay excluded.
- Like and dislike are mutually exclusive reactions to a doom. Tap an active reaction again to remove it. Feedback appears selected after the database confirms the write.
- Finish applies to the whole topic. A confirmation avoids accidental permanent exclusions. After the server saves it, the topic leaves the feed. Reactions remain saved. There is intentionally no automatic finishing at the final doom.
- If only one topic remains, switching keeps it open and explains why. If all topics are finished, the feed shows a completed state and can check for new content.
- Progress saves after scrolling settles, including backward navigation. A sync indicator shows pending or failed writes. Switching topics and finishing wait for pending progress; retry recovers failed saves. Stale updates from another device produce a conflict rather than silently overwriting newer progress.

At initial verification the library contains **3 real topics and 117 dooms**: the AI-era SDLC survey (44), the agentic AI harness survey (62), and the AI-bubble collection (11). The app loads the actual collections under `dooms/`; topic choices are not hard-coded.

## Deployment and operation

Follow [the setup guide](docs/SETUP.md) to configure managed hosting, email profiles, PostgreSQL and backups. See [architecture](docs/ARCHITECTURE.md), [maintenance](docs/OPERATIONS.md) and [verification](docs/VERIFICATION.md).

## Project layout

```text
frontend/       React + TypeScript; mobile reader, email setup and touch navigation
backend/        FastAPI; profile identity, catalog, database state and health checks
backend/tests/  Persistence, authorization and data-integrity tests
dooms/          Original YAML collections, backgrounds and preserved sources
.agents/        reel-it skill and the shared content schema
docs/           Setup, architecture, operations and verification
scripts/        Local setup and deployment entrypoint
Dockerfile      Frontend build + a single non-root Python service
render.yaml     Managed-hosting blueprint; secrets supplied through dashboard
```

## Checks

```bash
.tools/uv run pytest -q
export PATH="$PWD/.tools/node/bin:$PATH"
cd frontend
npm test
npm run build
```

Both dependency sets are locked: `uv.lock` and `frontend/package-lock.json`. The GitHub Actions workflow runs tests and builds before deployment. No application secrets belong in Git.

## Email-only profiles

Enter your email once and start reading immediately. No email is sent. Each device remembers the selected profile. The same email shares saved progress across devices. Anyone who enters that address can access the profile; there is no verification step. Supabase may still supply PostgreSQL, but Supabase Auth is no longer used. See docs/SETUP.md for current environment variables.
