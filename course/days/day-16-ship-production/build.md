# Day 16 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

## Before You Start

- [ ] Previous day is verified in `.onemillion/state.json`.
- [ ] You are in the correct product/course workspace.
- [ ] You have read [learn.md](./learn.md).
- [ ] Day 15 has no unresolved production blocker.

## Step 1: Ask The Harness To Teach The Day

Paste this:

```text
I am on OneMillion Day 16: Ship Production.

Act as the `ship` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, the ship agent, and the current pipeline artifacts.
Read .onemillion/state.json, .onemillion/architecture.md, .onemillion/test-results.md if present, and the Day 14/15 verification trail.
Do not skip my human decisions.
Do not create paperwork-only files.
Prefer live verification, state updates, and the smallest useful deployment notes.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- production URL to publicize
- custom domain now or later
- monitoring choice: Sentry, Vercel Analytics, UptimeRobot, or documented MVP skip
- alert email/contact
- optional FastAPI backend host if architecture selected FastAPI
- acceptable production blockers versus deferrals

## Step 3: Produce The Day Output

Expected output today:

- verified production URL
- production env var checklist by name
- Supabase production auth/RLS confirmation
- optional backend deployment result if architecture selected FastAPI
- live smoke-test result
- monitoring/analytics/uptime status
- custom domain status
- rollback path
- `.onemillion/state.json` updated with `live_url`

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: Ship Agent Prompts

### Pre-Ship Gate

```text
Run the Day 16 pre-ship gate.

Check:
- Day 15 has no unresolved BLOCKER
- local build/test commands still pass, or failures are known non-blockers
- .env.local is gitignored
- .env.example has placeholders only
- no likely API keys or secrets are committed
- architecture says whether this is Supabase-only/Next.js or optional FastAPI

Stop if a production blocker remains. Teach me why it blocks shipping.
```

### Production Environment Variable Audit

```text
Create a production environment variable checklist from the app code and .env.example.

For each variable, tell me:
- variable name
- why it is needed
- whether it belongs in Vercel Production, Supabase, or optional backend host
- whether it is public client config or server-only secret
- how I verify it is set without pasting the secret value

Never ask me to paste secret values into chat.
```

### Vercel Production Deploy

```text
Guide me through Vercel production deployment.

Use:
- Vercel dashboard: https://vercel.com/dashboard
- New/import project: https://vercel.com/new
- Environment variables docs: https://vercel.com/docs/projects/environment-variables

Check:
- project is connected to the correct GitHub repo
- production branch is correct
- build succeeds
- required production env vars are set
- live URL returns 200
- page does not show "Application error"
- live page includes a unique marker from the current product source
```

### Supabase Production Checks

```text
Guide me through Supabase production checks.

Use:
- Supabase dashboard: https://supabase.com/dashboard
- Auth redirect URL docs: https://supabase.com/docs/guides/auth/redirect-urls
- RLS docs: https://supabase.com/docs/learn/auth-deep-dive/auth-row-level-security

Check:
- Site URL is the production URL if auth is used
- Redirect URLs include the production URL and local development URL where needed
- RLS is enabled on user-owned tables
- policies still scope data by owner, tenant, or role
- auth works on the live URL
```

### Optional FastAPI Backend Deploy

```text
Check whether Day 5 architecture selected a separate FastAPI backend.

If no separate backend was selected, record: "No separate backend selected; app uses Next.js/Supabase path."

If FastAPI was selected:
- use the backend host chosen in architecture
- set required backend env vars
- deploy the backend before final frontend verification
- verify health endpoint returns 200
- verify CORS allows the production frontend URL
- update the frontend production API URL if needed

Do not introduce FastAPI today if architecture did not select it.
```

### Live Smoke Test

```text
Run a production smoke test on the live URL.

Cover what applies:
- homepage loads
- signup/login/logout works
- protected pages are protected
- main workflow works end-to-end
- data create/read/update/delete/archive works if the product has CRUD
- second-user or tenant isolation still holds where applicable
- AI feature works or fails with a useful error
- no application error is visible

Use automated checks where possible, and ask me for manual confirmations only where the harness cannot inspect.
```

### Monitoring, Analytics, Uptime

```text
Set up or intentionally defer production observability.

Teach me what each tool does:
- Sentry: errors and exceptions
- Vercel Analytics: traffic and page analytics
- UptimeRobot: external uptime checks
- Vercel logs: deployment/runtime logs

Use exact links:
- Sentry signup: https://sentry.io/signup/
- Sentry Next.js docs: https://docs.sentry.io/platforms/javascript/guides/nextjs/
- Vercel Analytics: https://vercel.com/docs/analytics
- UptimeRobot signup: https://uptimerobot.com/signUp
- UptimeRobot first monitor: https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor

For MVP, at minimum configure one uptime or analytics/error signal, or document why it is deferred.
```

### Custom Domain And DNS

```text
Decide whether to connect a custom domain today.

If yes:
- use Vercel domains docs: https://vercel.com/docs/domains
- choose registrar if needed: Cloudflare, Porkbun, or Namecheap
- add the domain in Vercel
- update DNS records at the registrar
- verify with DNS Checker: https://dnschecker.org
- verify HTTPS works
- update Supabase redirect URLs to include the custom domain

If no:
- record that the Vercel production URL is the public Day 17 URL for now.
```

### Rollback Path

```text
Teach and verify the rollback path.

Use:
- Vercel rollback CLI docs: https://vercel.com/docs/cli/rollback
- Vercel instant rollback docs: https://vercel.com/docs/deployments/instant-rollback

Record:
- current git SHA
- current production URL
- where previous deployments are visible
- how to promote or roll back a prior deployment
- what cannot be fixed by rollback alone, such as changed environment variables or database migrations

Do not perform a destructive rollback unless I explicitly approve it. Confirm I can access the dashboard path.
```

## Step 5: External Tools

- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git deployments: https://vercel.com/docs/deployments/git
- Vercel environment variables: https://vercel.com/docs/projects/environment-variables
- Vercel domains: https://vercel.com/docs/domains
- Vercel Analytics: https://vercel.com/docs/analytics
- Vercel rollback CLI: https://vercel.com/docs/cli/rollback
- Vercel instant rollback: https://vercel.com/docs/deployments/instant-rollback
- Supabase dashboard: https://supabase.com/dashboard
- Supabase Auth redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls
- Supabase RLS: https://supabase.com/docs/learn/auth-deep-dive/auth-row-level-security
- Sentry signup: https://sentry.io/signup/
- Sentry Next.js docs: https://docs.sentry.io/platforms/javascript/guides/nextjs/
- UptimeRobot signup: https://uptimerobot.com/signUp
- UptimeRobot first monitor: https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor
- Cloudflare Registrar: https://www.cloudflare.com/products/registrar/
- Porkbun: https://porkbun.com
- Namecheap: https://www.namecheap.com
- DNS Checker: https://dnschecker.org

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 16.
Inspect the production URL, current git SHA, env var checklist by name, Supabase auth/RLS confirmations, optional backend health if applicable, live smoke-test output, monitoring status, custom-domain status, rollback path, and .onemillion/state.json live_url.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 16 complete
- **Last verified day:** Day 16
- **Current blocker:** None, or the exact blocker to resume from
- **Live URL:** The production URL to use on Day 17
- **Next smallest action:** Open Day 17.

## What Should Be True After Day 16

- [ ] production URL returns 200 and does not show an application error
- [ ] live app matches the current local/product source with a unique product marker
- [ ] Vercel production environment variables are set by name, with no secret values committed
- [ ] Supabase Site URL and redirect URLs include the production URL where auth is used
- [ ] RLS/auth/tenant assumptions from Day 14 still hold in production
- [ ] optional FastAPI backend is deployed and health-checked, or explicitly skipped because architecture did not select it
- [ ] live smoke test covers the main flow, auth, data, and AI feature where applicable
- [ ] monitoring/analytics/uptime is configured or intentionally deferred with reason
- [ ] custom domain works or is explicitly skipped
- [ ] rollback path is known and accessible
- [ ] `.onemillion/state.json` includes the production `live_url`

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 16: Ship Production.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 17 — Brand + Marketing + Pricing + First Users](../day-17-sell-users/learn.md)
