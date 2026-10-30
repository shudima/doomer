# Hosted setup: Render + Supabase

The local app is built and usable. Live email login, cross-device sync and managed backups require your own service accounts. No account, paid resource or public deployment has been created automatically.

## 1. Put the source in a private Git repository

Use `/home/dima/projects/doomer` as the repository root. Include application code, lockfiles, `dooms/`, the skill schema, `Dockerfile` and `render.yaml`. Exclude `.env`, `.tools`, `.venv`, `data/`, build output and `node_modules` (already covered by `.gitignore`).

Connect that private repository to Render when prompted. GitHub Actions is already configured in `.github/workflows/checks.yml`.

## 2. Create one Supabase project

Choose a region near the Render service. Save the database password in your password manager. For managed daily backups with accessible recovery, select a plan that includes them; Supabase currently documents seven days of daily backups for Pro. Verify current plan terms before purchasing. [Backup documentation](https://supabase.com/docs/guides/platform/backups).

From the project dashboard collect:

- Project URL, such as `https://your-project.supabase.co`.
- Publishable key from API keys. This key is intentionally visible to the browser. A legacy anon key is also accepted by the JS client. Do not use a service-role or secret key here.
- PostgreSQL connection URI from **Connect → Session pooler**, usually port 5432. Use session mode for this long-running backend and append `sslmode=require`. Percent-encode special characters in the password inside a URI. [Connection guide](https://supabase.com/docs/guides/database/connecting-to-postgres).

In Authentication:

1. Enable Email sign-in and keep the Magic Link email template using its confirmation URL.
2. Use an asymmetric JWT signing key (ES256 or RS256). New keys must be active and visible in the project's JWKS endpoint.
3. Create your owner account through **Authentication → Users → Add user / Invite user**. The app uses `shouldCreateUser: false`, so an unknown email cannot register through its login form. After the owner exists, disable new signups in Auth settings.
4. Configure a reliable SMTP provider for production email. Supabase's built-in sender is for testing, restricted to project-team addresses and rate-limited; it is not a production mail service. [SMTP guide](https://supabase.com/docs/guides/auth/auth-smtp).
5. After Render supplies the app URL, set **Site URL** to that HTTPS origin and add the exact origin plus `/` to allowed redirect URLs. The app returns sign-in links to its own root page. Open each link on the device you want to sign in.

Do not expose the `doomer` database schema through the Supabase Data API. Alembic creates that schema through the backend connection; browser data access goes through FastAPI.

## 3. Create the Render service from the blueprint

In Render choose **New → Blueprint**, select the private repository and review `render.yaml`. It defines one paid Starter Docker web service with `/health/ready` as its health check. Docker packages the application; you do not manage Docker servers. [Render Docker deployment](https://render.com/docs/docker).

Enter the dashboard environment variables:

| Variable | Value |
| --- | --- |
| `DOOMER_ENVIRONMENT` | `production` (blueprint sets this) |
| `DOOMER_AUTH_MODE` | `supabase` (blueprint sets this) |
| `DOOMER_DATABASE_URL` | Supabase session-pooler PostgreSQL URI with `sslmode=require` |
| `DOOMER_OWNER_EMAIL` | Exactly the owner's verified Supabase email |
| `DOOMER_SUPABASE_URL` | Project HTTPS URL, without `/auth/v1` |
| `DOOMER_SUPABASE_PUBLISHABLE_KEY` | Publishable key; never the service-role key |
| `DOOMER_ALLOWED_HOSTS` | Optional comma-separated custom hostnames. Render's own hostname is detected automatically from `RENDER_EXTERNAL_HOSTNAME`. No scheme or slash. |
| `DOOMER_SENTRY_DSN` | Optional backend Sentry DSN; leave empty to disable |
| `DOOMER_FRONTEND_SENTRY_DSN` | Optional separate browser Sentry DSN; leave empty to disable |
| `DOOMER_RELEASE` | Optional release ID/commit; default is the code's development label until set |

The default Render URL works without setting `DOOMER_ALLOWED_HOSTS`. Add that variable only for additional custom hostnames, such as `read.example.com`. Host checking still rejects unrelated domains; the app does not add an `*.onrender.com` wildcard.

Startup runs `alembic upgrade head` before Uvicorn. The service reads `PORT` from Render. A failed migration or missing production configuration stops startup. Readiness checks both database access and the application table. The initial content is packaged from `dooms/` during the Docker build.

Auto-deploy is configured to wait for CI checks. Review current service/database/email-provider costs in their dashboards; no paid plan has been activated by this project.

## 4. Verify the hosted behavior

1. Open the HTTPS URL on your iPhone. It should show the email sign-in screen.
2. Send a link to your owner email and open it on that iPhone. An unapproved account must receive a private-account denial from the API.
3. Advance a few dooms and wait for **Synced**. Sign in to the same email on a second device and confirm that this topic resumes there.
4. Like a doom, reload and confirm the reaction. Replace it with dislike; both must never appear active simultaneously.
5. Finish a disposable test topic and reload. It must remain absent. If only the real survey exists, avoid finishing it just for this check unless you intend to remove it from your feed.
6. Confirm `/health/ready` returns 200 and add an external uptime check against it.
7. Confirm backup availability in Supabase and test restoring a copy of the database before relying on it.

On iPhone Safari, choose **Share → Add to Home Screen** for the standalone reading experience. The app has a manifest and icons; it does not claim offline functionality. A physical iPhone/Safari test remains part of this hosted check.

## Optional local production-style check

After Docker Desktop is running, build the image:

```bash
docker build -t doomer .
docker run --rm --env-file .env.production -p 127.0.0.1:8000:8000 doomer
```

Create `.env.production` privately with the production variables above, include `localhost,127.0.0.1` in allowed hosts for this test and configure local redirect URLs in your test Supabase project. This uses the real configured PostgreSQL database; use a staging project rather than a live personal database for destructive tests. `.env.production` is ignored by Git. Never put credentials into a Dockerfile or build arguments.
