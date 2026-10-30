# Verification

Email-only profile update checked on October 30, 2026.

- 21 backend tests pass, including normalized email identity, configured-owner matching, profile isolation, progress/reaction/completion restoration on another device, and continuity with a previous verified owner's state.
- 6 frontend tests pass, including remembering, clearing and rejecting malformed device profile data, and topic/swipe navigation.
- Strict TypeScript checking and the production frontend build pass.
- Email link requests, Supabase Auth SDK and JWT verification dependencies have been removed.
- Legacy Render auth-mode values map to the explicitly requested email-only flow. No new dashboard variable is required for the existing service.

Earlier checks verified mobile layouts at iPhone Air dimensions, per-topic restoration, reaction replacement and persistent Finish behavior. Physical iPhone Safari testing and provider backup restore rehearsal remain separate checks.

Browser verification: the email form opened the actual reader immediately, a page reload restored the remembered profile without prompting, and Change email returned to the setup form. No sign-in emails were requested. Alembic upgraded an existing revision-001 SQLite test database to revision 002 successfully.
