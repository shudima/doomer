# Verification

Verified locally on October 30, 2026.

## Automated checks

- 12 backend tests pass: saved-position restoration, backward progress, process restart, stale-device conflict handling, cross-topic validation, reaction replacement/removal, idempotent completion and exclusion, per-user isolation, unknown/traversal paths, protected endpoints, production-mode safeguards, missing content assets, and signed JWT validation cases.
- 3 frontend tests pass: topic eligibility, random selection coverage and deliberate directional swipe recognition.
- Strict TypeScript checking and the Vite production build pass.
- Application migrations successfully create the initial schema in an isolated SQLite database.
- Production npm dependency audit reports no known vulnerabilities at verification time.

## Browser checks

- Opened the actual built React app served by FastAPI with the real survey collection.
- Revalidated the catalog after two additional collections appeared: 3 real topics, 117 dooms. All three packages pass catalog validation.
- Inspected at 420 x 912 (iPhone Air logical layout) and 420 x 780 (shorter browser viewport).
- Measured all 44 rendered cards at both sizes: reader content does not overlap source information.
- Next-doom navigation advances the card, saves the position and restores it after reload.
- Like survives reload; dislike replaces it rather than activating both reactions.
- Switching with only one unfinished topic keeps that topic visible with an explanatory message.
- With two separate QA collections, switching to a new topic starts at doom 1 and returning restores doom 2. These fixtures live under ignored test data, not the real content library.
- Finish confirmation works in a separate preview database. The completed topic remains absent after a page reload and the all-caught-up state appears.
- Inspected the email sign-in UI with test-only configuration without sending emails. Email delivery remains a hosted setup check.

## Outstanding environment checks

Live Supabase email delivery, a real hosted PostgreSQL database, external cross-device sync, managed backups and Render deployment require the user's new service accounts and configuration. They have not been claimed as live.

The local Docker engine was unavailable at the time of verification. The Dockerfile and hosting blueprint are provided, but a full container image build and containerized PostgreSQL test have not been completed. The local app itself builds and runs without Docker.

Viewport testing used the desktop browser at mobile dimensions, not a physical iPhone running Safari. Safe-area spacing and standalone metadata are implemented; a physical-device check belongs in the hosted setup steps. No offline-write capability is claimed.
