# Hosted setup: email profiles + PostgreSQL

Doomer now asks for an email once and opens the feed immediately. It does not send a verification email or sign-in link and does not use Supabase Auth. The email is an unverified label for saved progress. Anyone who knows the address can use that profile. This behavior was explicitly selected for this personal app.

## Existing Render deployment

Push the updated code and let the checks/deployment finish. No new environment variable or mail-provider account is needed. An existing `DOOMER_AUTH_MODE=supabase` value is accepted as a legacy alias for the new `email` mode, so the existing deployment transitions without a dashboard change. New deployments should set `DOOMER_AUTH_MODE=email`.

Keep `DOOMER_DATABASE_URL` pointing to the existing PostgreSQL database. Supabase can remain the managed database provider. The unused `DOOMER_SUPABASE_URL` and `DOOMER_SUPABASE_PUBLISHABLE_KEY` entries can be removed from Render at your convenience; the application no longer reads them.

## Environment variables

| Variable | Value |
| --- | --- |
| `DOOMER_ENVIRONMENT` | `production` |
| `DOOMER_AUTH_MODE` | `email` |
| `DOOMER_DATABASE_URL` | Managed PostgreSQL URI; for the current Supabase database use the session-pooler URI with `sslmode=require` |
| `DOOMER_OWNER_EMAIL` | Your email. When set, the profile form accepts only that address. Matching ignores case and surrounding whitespace. |
| `DOOMER_ALLOWED_HOSTS` | Optional custom domains; Render's default hostname is recognized automatically |
| `DOOMER_SENTRY_DSN` | Optional backend error reporting |
| `DOOMER_FRONTEND_SENTRY_DSN` | Optional frontend error reporting |
| `DOOMER_RELEASE` | Optional release/commit identifier |

The Docker image and `render.yaml` use email mode by default. Startup runs Alembic migrations, including the email-profile mapping table, before starting FastAPI. PostgreSQL is still required for hosted state; local SQLite files on an ephemeral host are not a substitute.

## Use the app

1. Open your Render app URL.
2. Enter the configured owner email and press **Start reading**.
3. The device remembers that profile in browser storage and opens the feed directly on future visits.
4. Enter the same email on another device to resume the same saved topics, reactions and completion state.
5. Use **Your space → Change email** to clear the remembered profile on a device. This does not delete saved data.

No Supabase Auth user, JWT signing key, SMTP provider, redirect URL, magic link or email quota is involved. If a single previously verified owner already has saved history, the first matching owner profile links to that existing identity; original progress and reaction rows remain unchanged.

## New hosting setup

Put the source and content in a private Git repository, connect it to Render as a Docker web service, and provide the variables above. Select a managed PostgreSQL provider and a backup plan appropriate to your data. Review current paid-resource terms before creating resources. `render.yaml` describes the application service; database credentials belong in Render's environment settings.

## Backups and checks

Keep managed PostgreSQL backups enabled in the database provider, and keep source YAML/images/PDFs in Git. Health checks use `/health/ready`. Test that progress resumes on another device and that finished topics remain excluded after a reload. See OPERATIONS.md for recovery and dependency-update practices.

Local preview remains available with `sh scripts/dev.sh`. To test email profiles locally, set `DOOMER_AUTH_MODE=email` before running it; the local database is separate from hosted data.
