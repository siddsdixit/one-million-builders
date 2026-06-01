# Day 15 — Build Guide

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

## Step 1: Ask The Harness To Teach The Day

Paste this:

```text
I am on OneMillion Day 15: QA + Production Readiness.

Act as the `test` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Do not skip my human decisions.
Do not create paperwork-only files.
Test the actual app and update the existing verification trail. Do not create a new paperwork system.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- critical paths that must pass before shipping
- which tests should be automated now
- which tests can remain manual for MVP
- AI pass/fail examples and quality threshold
- what defects block Day 16
- what non-critical risks can be accepted temporarily

## Step 3: Produce The Day Output

Expected output today:

- final QA evidence for the MVP
- tests or manual checks for the highest-risk flows
- fixes for production blockers
- ready-for-production decision for Day 16

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: QA + Readiness Prompts

### Final QA Plan From Existing Artifacts

```text
Create the final Day 15 QA pass from the existing PRD/refined PRD, design spec, architecture, test plan, review findings, and app code.

Do not create a new paperwork system.
Use existing .onemillion/test-plan.md and .onemillion/test-results.md if they exist.

Tell me:
1. The critical paths that must pass before production
2. The manual QA checks I should perform
3. The automated tests that are worth adding now
4. The AI feature pass/fail examples
5. The production blockers, if any
```

### Manual QA Pass

```text
Guide me through a manual QA pass.

Cover:
- signup/login/logout
- main workflow
- data create/read/update/delete/archive where applicable
- AI feature success and failure
- mobile and desktop layout
- empty/loading/error/success states
- live deployment critical path

Ask me for evidence you cannot inspect directly. Record only the result in the existing verification trail/state.
```

### Automated Test Pass

```text
Inspect the repo and choose the smallest useful automated test set for production readiness.

Prefer tests that cover:
- core workflow behavior
- auth/authorization boundaries
- API route or server action behavior
- AI route error handling
- E2E happy path if Playwright or equivalent is available

Add tests only where the repo supports them cleanly. Run the relevant commands and fix production-blocking failures.
```

### Production Readiness Decision

```text
Make a Day 15 production readiness decision.

Classify findings as:
- BLOCKER: must fix before Day 16
- FIX NOW: should fix today if small
- ACCEPT FOR MVP: known risk with reason
- DEFER: not needed for this MVP

Do not move to Day 16 while a blocker remains.
```

## Step 5: External Tools

- Supabase dashboard: https://supabase.com/dashboard
- Supabase project shortcut: https://database.new
- Supabase Next.js Auth: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Supabase API keys: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git docs: https://vercel.com/docs/deployments/git
- Vercel env vars: https://vercel.com/docs/projects/environment-variables
- Vercel domains docs: https://vercel.com/docs/domains
- Vercel Analytics: https://vercel.com/docs/analytics
- Anthropic Console: https://console.anthropic.com/
- Anthropic API docs: https://docs.anthropic.com/en/api/overview

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 15.
Inspect the existing test plan/results, app code, automated test output, manual QA confirmations, live deployment, AI feature behavior, Day 14 guard status, and production-readiness decision.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 15 complete
- **Last verified day:** Day 15
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 16.

## What Should Be True After Day 15

- [ ] local build/test commands pass or failures are understood and fixed/deferred
- [ ] manual QA covers the main user journey, auth, data, AI feature, and error states
- [ ] automated tests cover the highest-risk behavior the repo can support
- [ ] live deployment is checked for the critical path
- [ ] AI pass/fail examples produce acceptable behavior
- [ ] no Day 14 critical security/trust blocker remains
- [ ] production-blocking bugs are fixed before Day 16

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 15: QA + Production Readiness.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 16 — Ship Production](../day-16-ship-production/learn.md)
