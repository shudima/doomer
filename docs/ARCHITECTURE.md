# Architecture

## Runtime

- React + TypeScript + Vite provide the mobile reading interface.
- FastAPI serves the built UI, profile setup, feed APIs and background assets on one origin.
- SQLAlchemy stores state in managed PostgreSQL in production and SQLite for local preview.
- Content remains in versioned Markdown/frontmatter collections under `dooms/`.
- Render runs the Docker image. JSON logs, health checks and optional Sentry cover basic operation.

## Email is a profile label

The app intentionally has no sign-in step, password or email verification. A person enters their email once. The server normalizes it and creates or looks up a persistent email-profile mapping. The browser remembers the profile identifier and sends it with subsequent requests. The same email on another device resolves to the same state.

This is not authentication. Anyone who knows an accepted email can use that profile and change its saved state. Profile identifiers are not secret credentials. `DOOMER_OWNER_EMAIL`, when configured, limits the accepted label to the owner's address; it does not prove ownership of that address.

The Supabase Auth client, JWT verification, sign-in links and mail-delivery requirements have been removed. Supabase may still host PostgreSQL. Old `DOOMER_AUTH_MODE=supabase` deployments normalize to `email` for compatibility with this explicitly requested product change.

## Data model and continuity

- `doomer.email_profile`: normalized-email SHA-256 identifier mapped to a stable state owner ID. Raw email addresses are not stored in this table.
- `doomer.topic_state`: `(user_id, topic_id)` key, current doom ID, version, completion timestamp and update timestamp.
- `doomer.reaction`: `(user_id, doom_id)` key, like/dislike and update timestamp.

On first owner-profile setup, a single existing legacy UUID identity can be linked to that profile. Existing topic and reaction rows are retained; the change does not rewrite or delete them. Fresh profiles use deterministic email-based state IDs. Re-entering an email is idempotent, including differences in case or surrounding whitespace.

Production startup applies Alembic revision 002 to add the mapping table. App requests remain scoped to the selected profile. Invalid or absent profile IDs are rejected and prompt the user to set their email. Static source PDFs/content sources are not exposed as website directories.

## Feed behavior

Opening the app selects a random unfinished topic at its saved doom. New topics start at 1. Vertical scrolling advances within a topic; a deliberate left or right swipe or the footer button selects another eligible topic. A single remaining topic stays open. All finished topics produce the completed feed state.

Progress writes use an expected version to prevent stale device state from overwriting a newer position. Finish is idempotent and cannot be cleared by progress writes. Reactions are mutually exclusive and can be removed. Returning to the app refreshes state from the server. Save failures remain visible; no offline write queue is promised.

## Content and operation

The catalog validates YAML or Markdown/frontmatter, order, source metadata and in-collection assets at startup. New collections become visible on restart/redeploy. Stable collection slugs and doom IDs preserve history. Production state lives outside the application container. The host allowlist includes Render's exact platform hostname and optional explicitly configured custom domains.

The topic explorer keeps finished topics in the searchable library, marked Finished. They remain excluded from random browsing and cannot be reopened by progress writes. `/api/topics` retains unfinished `topics` for feed compatibility and adds `finished_topics` summaries. The feed header and explorer show finished topics out of the complete catalog total.

The reader has one persistent topic/source header with the current doom counter. Original source URLs and locators are returned with doom details. Cards contain the heading and text, while the next-doom control floats in the reserved right margin; no footer limits the reading viewport. Completion totals remain available in the topic explorer.
