# Verification

Email-only profile update checked on October 30, 2026.

- 21 backend tests pass, including normalized email identity, configured-owner matching, profile isolation, progress/reaction/completion restoration on another device, and continuity with a previous verified owner's state.
- 6 frontend tests pass, including remembering, clearing and rejecting malformed device profile data, and topic/swipe navigation.
- Strict TypeScript checking and the production frontend build pass.
- Email link requests, Supabase Auth SDK and JWT verification dependencies have been removed.
- Legacy Render auth-mode values map to the explicitly requested email-only flow. No new dashboard variable is required for the existing service.

Earlier checks verified mobile layouts at iPhone Air dimensions, per-topic restoration, reaction replacement and persistent Finish behavior. Physical iPhone Safari testing and provider backup restore rehearsal remain separate checks.

Browser verification: the email form opened the actual reader immediately, a page reload restored the remembered profile without prompting, and Change email returned to the setup form. No sign-in emails were requested. Alembic upgraded an existing revision-001 SQLite test database to revision 002 successfully.


## iPhone Home Screen layout — October 30, 2026

- Cards grow to contain all prose and source credits; longer dooms scroll inside the existing feed. Saved positions and next/previous controls use actual card bounds rather than assuming every card equals the viewport height.
- The app fills the usable web view, uses an opaque iOS status bar, and applies bottom safe-area padding once. Automatic text inflation is disabled while retaining readable type and normal user zoom.
- 9 frontend tests and the production TypeScript/Vite build pass. Uneven-height progress tests cover reading within a long doom, moving between cards, viewport resizing and top overscroll.
- Browser checks at 393×730, 393×600 and 420×912 verified the formerly clipped Jev doom, reaching its full text and source, next-doom offsets, per-topic resume after reload, and footer placement at the viewport bottom.
- Physical iPhone Home Screen validation remains necessary. Existing installed shortcuts may need removal and re-adding to pick up the changed status-bar metadata.


## Finished topics in the explorer — October 30, 2026

- `/api/topics` now includes separate finished-topic summaries. The existing unfinished-topic array still drives random browsing. Completion counts use only topics in the current catalog.
- Finished topics remain searchable, visibly marked Finished, and retain the original completion state. The feed header and explorer show completed topics out of the full total.
- All 21 backend tests and 9 frontend tests pass, with strict TypeScript and production build checks. API regressions cover idempotent completion, all topics finished, profile isolation and cross-device restoration of finished summaries/counts.
- An isolated browser preview at 393×730 verified finishing a topic, immediate 1/14 count updates, all 14 topics remaining listed, finding the finished topic via search, and persistence after reload. Live user completion records were not changed during these tests.


## Compact reader — October 30, 2026

- A single header shows the full topic title, original source link (or PDF label), current section/page/timestamp and one accessible doom counter. The API now returns each doom's source type and URL; local source paths remain private.
- Removed duplicate in-card topic attribution, chapter number, bottom source credit and navigation footer. The next-doom arrow floats within the existing right margin. The feed uses the full remaining height with safe-area padding; long cards retain natural scrolling. Topic completion totals remain in the explorer.
- 23 backend tests and 9 frontend tests pass, including article-link and local-PDF attribution contracts. Production TypeScript/Vite build passes.
- Browser checks at 420×912, 393×730 and 393×600 covered the exact article/doom 17 of 19 from the user's screenshot, full-text reachability on a short viewport, correct progress restoration and next-doom counter/section updates. PDF page attribution and keyboard topic switching were also checked. No live profile progress was used for these checks.


## Markdown catalog migration — 2026-10-31

- All 31 collection validators pass: 746 Markdown dooms, 73 labeled added examples, 46 original article figures, three added Mermaid diagrams with editable source and portable SVG overviews.
- A baseline audit verifies all 673 original doom IDs, all original source metadata and byte-identical original PDF attachments. Collection IDs are unchanged.
- Backend: 31 tests pass, including legacy and Markdown compatibility, asset authentication and containment, active-SVG rejection, and persistence of progress/reactions/finished topics after format conversion and insertion before a saved doom.
- Frontend: 13 tests pass, including emphasis, lists, GFM tables, literal code, unsafe HTML/link handling, local figure placeholders and lazy diagram rendering. TypeScript and the production Vite build pass. Mermaid is dynamically imported; its larger diagram-engine chunks remain outside the initial reader load.
- Browser checks at 393×730: a source figure loads; enlargement, zoom and horizontal figure scrolling work; a long card scrolls to its diagram without changing its current doom; Mermaid renders and enlarges; the cache example renders its table and resumes the seeded doom by ID. No horizontal document overflow and no console errors were observed in these checks. This is desktop viewport emulation, not a physical Safari/iPhone test.
- GitHub Actions now validates all collections as well as running the application tests and build.

See [migration details](MARKDOWN-MIGRATION.md) for counts, compatibility and source-visual limitations.
