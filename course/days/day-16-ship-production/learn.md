# Day 16 — Ship Production

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `ship`
**Supporting agents:** guard, test, debug

Day 16 turns the MVP into a production product people can actually visit. The learner verifies the app on the live URL, checks production environment variables, confirms Supabase production settings, sets up monitoring, and documents rollback.

## Learning Frame

- **Mental model:** shipping is not "Vercel says deployed." Shipping means the live product is reachable, configured, observable, smoke-tested, and recoverable.
- **What can go wrong:** local works but production fails because env vars, auth redirects, RLS, CORS, API keys, or build settings differ.
- **What to ignore today:** do not add new features. Fix production blockers only.

## What You Learn

- production versus preview deployments
- why production environment variables matter
- how Vercel, Supabase, and optional backend hosting fit together
- Supabase Auth Site URL and redirect URLs
- production smoke tests
- monitoring, analytics, logs, and uptime checks
- optional custom domains and DNS
- rollback thinking
- what to record before moving into selling

## Core Concepts

- **Production is a different environment.** Your local `.env.local` does not automatically exist on Vercel. Production variables must be set in the deployment platform.
- **Preview and production are different.** Preview deployments are useful for checking changes. Production is the URL real users receive.
- **Auth must know the production URL.** Supabase Site URL and redirect URLs should include the live app so login, magic links, password resets, and OAuth flows return to the right place.
- **RLS must still protect production data.** Day 16 confirms the same auth/RLS assumptions from Days 7 and 14 still hold after deployment.
- **FastAPI is optional.** Deploy a separate backend only if Day 5 architecture selected it. Most course apps stay Next.js + Supabase.
- **Smoke tests prove the live path.** The learner should verify the real URL, not just the local app.
- **Monitoring is how production talks back.** Uptime checks, logs, analytics, and error tracking help the builder notice issues.
- **Rollback is part of shipping.** The learner should know how to return to a previous deployment before users arrive.

## What You Produce

- verified production URL
- confirmed production environment variable checklist
- confirmed Supabase production auth/RLS setup
- optional backend deployment if architecture selected FastAPI
- live smoke-test results
- monitoring/analytics/uptime setup or documented skip
- optional custom domain setup or documented skip
- rollback path
- `.onemillion/state.json` updated with `live_url` for Day 17

## Human Decisions

- production URL to publicize
- custom domain now or later
- monitoring choice: Sentry, Vercel Analytics, UptimeRobot, or documented MVP skip
- alert email/contact
- optional FastAPI backend host if architecture selected FastAPI
- acceptable production blockers versus deferrals

## Done Checklist

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

## Verify Your Day 16

When the checklist is true, ask your harness to run the OneMillion verifier for Day 16. The verifier should inspect the relevant pipeline artifacts, app code, production URL, env var names, Supabase confirmations, smoke-test output, monitoring confirmations, rollback path, and manual confirmations for this day.


---

-> **Next:** [Day 17 — Brand + Marketing + Pricing + First Users](../day-17-sell-users/learn.md)
