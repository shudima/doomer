# Maintenance and observability

## Normal operation

Render supervises the application process, restarts unhealthy services and retains deployment logs. Structured stdout events include a generated request ID, route template, method, status and duration. They exclude authorization headers, emails, request bodies and URL query strings. `X-Request-ID` lets a failed response be correlated with a log entry.

- `/health/live`: process is serving requests.
- `/health/ready`: database is reachable, state schema exists and the content catalog loaded. Use this for deployment readiness and an external uptime monitor.
- Optional Sentry DSNs activate backend and frontend error reporting. Personal data collection is disabled by default; frontend user fields are removed. No session replay is configured. Configure an error alert and an uptime alert to your preferred destination in the provider dashboards.

Do not send secrets or database credentials into logs. Render's dashboard owns production environment values. The browser receives an unverified profile identifier; it is not a password or bearer credential.

## Backups and recovery

Use the managed Supabase backup plan configured during setup. Check that backups actually exist; a successful app deployment does not configure a database backup plan. The app containers store no durable user state. Back up content and code through the private Git repository as well: database backups do not include the repository's YAML, images or PDFs.

For an additional encrypted off-provider copy, export only the private application schema using provider tooling or `pg_dump` into a secure location. Use a supported PostgreSQL client, a password manager or environment secret injection; do not paste secrets into shell history. Keep retention and access under your control.

For recovery, restore to a separate project/database, run migrations if required, verify topic progress/reactions/finished records, then switch `DOOMER_DATABASE_URL` in Render and redeploy. Keep the previous database until verification completes. Rehearse recovery periodically.

## Adding topics

Run the project's reel-it workflow. It writes complete packages under `dooms/<source-id>/`. Validate the collection, commit the new files in a private repository and let CI/deployment run. Restart the local preview to load changes without deploying.

The startup catalog validates every collection. A malformed YAML file, missing image or invalid source reference fails startup rather than partially publishing a broken topic. Stable topic slugs and doom IDs preserve personal history. Do not rename existing IDs during cosmetic edits.

## Updating the app

Review dependency updates monthly and when a relevant security advisory appears. Update through a branch, regenerate `uv.lock` / `frontend/package-lock.json`, run the checks in README and inspect the mobile feed before deployment. Keep the pinned Docker uv version aligned with the tooling used to update the lockfile.

Alembic revisions belong in `backend/migrations/versions/`. Use additive changes when possible. Back up before a destructive migration. Rolling back an app deployment does not automatically roll back a database migration; maintain compatibility or restore a verified database copy.

To investigate a failed deployment, inspect the startup/migration logs and `/health/ready`. For an email-profile setup failure, check the configured owner email, PostgreSQL connectivity and whether Alembic revision 002 ran. There is no mail provider or authentication redirect in this flow. For a 409 progress conflict, use the app's Retry action to restore the latest saved position. For failed saves, restore connectivity and retry before closing the page.

## Operational limits

This release has no offline write queue, web sockets, administrator UI or content upload endpoint. Email profiles intentionally do not verify identity. Anyone entering the configured email can use that profile. Changing the remembered email clears local reader state and image object URLs, while saved progress, reactions and completion stay in PostgreSQL. Backend routes scope data to a profile identifier but do not provide account authentication.
