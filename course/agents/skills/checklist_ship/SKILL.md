# OneMillion Deployment Guide & Checklists

> Reference for the Ship agent. Use this with `.onemillion/architecture.md`; do not assume a separate backend unless FastAPI was selected.

---

## Deployment Targets

### Default Web App / Hybrid App

- **App:** Vercel connected to GitHub
- **Database/auth:** Supabase project
- **AI:** server-side route/action in the app, with `ANTHROPIC_API_KEY` in server env only
- **Monitoring:** Sentry/Vercel Analytics/uptime monitor when production day requires them

### Optional FastAPI Backend

Only if `.onemillion/architecture.md` selected FastAPI:

- deploy backend to the architecture-selected backend host, such as Railway, Fly.io, Render, or another justified provider
- set `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `ANTHROPIC_API_KEY`, `CORS_ORIGINS`
- verify health endpoint and CORS from the Vercel domain

---

## Pre-Deployment Checklist

### Code & Tests

- [ ] App builds locally: `npm run build`
- [ ] Relevant tests pass
- [ ] No open Critical/High security findings
- [ ] No hardcoded secrets in source or git history
- [ ] `.env.local` is gitignored and not committed
- [ ] `.env.example` contains placeholders only
- [ ] Package lockfile is committed

### Environment Variables

- [ ] Vercel has all required public values, such as `NEXT_PUBLIC_SUPABASE_URL`
- [ ] Vercel has all required server-only values, such as `ANTHROPIC_API_KEY`
- [ ] No secret is prefixed with `NEXT_PUBLIC_`
- [ ] Supabase service-role key is never used in browser code
- [ ] FastAPI-only env vars are set only if FastAPI is selected

### Supabase

- [ ] Supabase project is reachable
- [ ] Required tables exist
- [ ] RLS enabled on user-owned or tenant-owned tables
- [ ] Policies enforce `owner_id`, `tenant_id`, `organization_id`, or public/community rules
- [ ] Auth redirect URLs include the Vercel production URL when auth redirects are used
- [ ] Backup/export posture documented for the current Supabase plan

---

## Deployment Steps

### 1. Supabase Preparation

1. Confirm project exists.
2. Confirm schema and RLS policies match `.onemillion/architecture.md`.
3. Confirm anon key and URL are available for client-side Supabase.
4. Confirm service-role key is used only server-side when truly needed.

### 2. Vercel Deploy

1. Open Vercel import: https://vercel.com/new
2. Import the product GitHub repo.
3. Set environment variables.
4. Deploy.
5. Verify live URL returns 200.
6. Push a small commit and confirm Vercel redeploys.

### 3. Optional FastAPI Deploy

Only run this if architecture selected FastAPI.

1. Deploy backend to the architecture-selected backend host, such as Railway, Fly.io, Render, or another justified provider.
2. Set backend env vars.
3. Verify health endpoint.
4. Set `CORS_ORIGINS` to the Vercel URL.
5. Verify the Vercel app can call the backend.

### 4. Domain & SSL

1. Add custom domain in Vercel project settings.
2. Add DNS records at registrar.
3. Verify DNS propagation.
4. Verify HTTPS/SSL.
5. Update Supabase Auth redirect URLs if auth is used.

---

## Post-Deployment Verification

- [ ] Live app returns 200
- [ ] Live app content matches local source markers
- [ ] Signup/login works if auth is included
- [ ] Protected routes reject unauthenticated users
- [ ] Second-user isolation passes when user-owned data exists
- [ ] Core workflow works on the live URL
- [ ] AI route works live if included
- [ ] Sentry receives a test error if Sentry is configured
- [ ] Uptime monitor is green if monitoring is configured

## Rollback

- **Vercel:** Dashboard -> Deployments -> select last working -> Promote to Production
- **Supabase:** Document backup/restore path for current plan
- **FastAPI backend, if used:** redeploy previous working release on the selected backend host

After rollback, verify the live app and document the root cause before redeploying.
