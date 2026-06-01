# Day 10 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
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
I am on OneMillion Day 10: QA + Tests.

Act as the `test` agent for this day.
First teach me QA and testing in plain language:
- what good QA means
- manual QA versus automated QA
- how acceptance criteria become test cases
- frontend/component testing
- backend testing when the architecture has a backend service
- API testing for route handlers, server actions, or FastAPI endpoints
- Playwright and Selenium-style E2E browser testing
- auth, RLS, tenant, and RBAC permission testing
- live deployed URL testing
- how to record evidence, limitations, and a pass/fail verdict

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Read .onemillion/refined-prd.md, .onemillion/review-findings.md, .onemillion/architecture.md, and the completed Day 8 sprint brief.
Generate a test plan and test cases before running tests.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Copy-Paste QA Prompts

Use these prompts one by one.

### Prompt 1: Generate Test Plan

```text
I am on OneMillion Day 10: QA + Tests.

Generate .onemillion/test-plan.md before running tests.
Read:
- .onemillion/refined-prd.md
- .onemillion/review-findings.md
- .onemillion/architecture.md
- .onemillion/sprints/
- current app code

Map acceptance criteria to test cases.
Include:
- manual QA checklist
- automated test candidates
- happy paths
- edge cases
- negative cases
- auth/RLS/tenant/RBAC permission checks
- live deployed URL checks
- review findings that need regression checks

Do not mark anything as passed yet. This is the plan.
```

### Prompt 2: Manual QA Checklist

```text
Create a manual QA checklist for the Day 8 core workflow.

Include exact steps I should perform in the browser:
- local app URL
- live deployed URL
- signup/login/logout if auth exists
- create/read/update/delete or archive
- loading/empty/error/success states
- permission denied state
- second-user isolation if private data exists
- mobile-width and desktop-width checks

For each step, write:
Action:
Expected result:
Pass/fail:
Evidence to capture:
```

### Prompt 3: Run Manual QA With Me

```text
Walk me through the manual QA checklist one step at a time.

Do not rush.
After each step, ask me what I observed.
Record pass/fail, evidence, and notes.
If something fails, classify it as blocker, bug, gap, edge case, or observation.
At the end, summarize whether we can continue or must fix something first.
```

### Prompt 4: Generate Automated Tests

```text
Generate the smallest useful automated test suite for this MVP.

Prefer the course stack:
- Playwright for E2E browser tests
- Playwright request tests or Vitest for Next.js route/server behavior when useful
- pytest + httpx only if the architecture selected FastAPI
- accessibility checks where easy

Cover:
- core workflow happy path
- validation failure
- unauthenticated access
- second-user or tenant isolation
- any Day 9 blocker/bug fixes as regression tests

Do not overbuild. Create tests that a beginner can understand and rerun.
```

### Prompt 5: Run Automated Tests

```text
Run the automated tests that exist for this app.

Use the repo's package scripts if available.
If scripts are missing, inspect package.json and choose the smallest correct command.
Run Playwright in Chromium only.
If tests fail, diagnose whether it is a test bug, app bug, environment issue, or missing setup.
Fix only critical issues needed for Day 10.
Record exact commands and results for .onemillion/test-results.md.
```

### Prompt 6: Permission QA

```text
Test auth and permission boundaries.

Check:
- logged-out user cannot access protected pages
- User A cannot see User B's private records
- tenant A cannot see tenant B data if multi-tenant
- member cannot perform owner/admin actions if RBAC exists
- service-role keys and AI keys are not exposed in browser code

Record which checks passed, which were not applicable, and which need fixes.
```

### Prompt 7: Live Deployment QA

```text
Test the live deployed URL.

Confirm:
- live URL loads
- live UI matches the current local source/build
- Day 8 core workflow works live
- auth redirect URLs work live if auth exists
- data persists in Supabase
- no obvious console/build error is visible

Record the live URL, test time, evidence, failures, and limitations.
```

### Prompt 8: Final QA Report

```text
Write .onemillion/test-results.md.

Include:
- verdict: PASS / PASS WITH LIMITATIONS / BLOCKED
- manual QA results
- automated test commands and results
- acceptance criteria coverage
- auth/RLS/tenant/RBAC permission results
- live URL QA result
- bugs found
- bugs fixed
- bugs deferred with reasons
- limitations and next actions

Do not claim skipped tests passed.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- critical paths to test manually
- acceptable risk
- QA evidence
- which tests should be automated now
- which checks can remain manual for MVP
- which failures block progress

## Step 3: Produce The Day Output

Expected output today:

- `.onemillion/test-results.md`
- `.onemillion/test-plan.md`
- manual QA checklist/results
- automated test files/results where appropriate

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: External Tools

- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git docs: https://vercel.com/docs/deployments/git
- Vercel env vars: https://vercel.com/docs/projects/environment-variables
- Vercel domains docs: https://vercel.com/docs/domains
- Vercel Analytics: https://vercel.com/docs/analytics
- Supabase dashboard: https://supabase.com/dashboard
- Supabase project shortcut: https://database.new
- Supabase Next.js Auth: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Supabase API keys: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `onemillion-builder/docs/account-setup.md`.

## Step 5: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 10.
Inspect .onemillion/test-plan.md, .onemillion/test-results.md, app code, deployment links, manual QA evidence, automated test output, permission checks, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 10 complete
- **Last verified day:** Day 10
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 11.

## What Should Be True After Day 10

- [ ] `.onemillion/test-plan.md` exists
- [ ] acceptance criteria are mapped to manual or automated test cases
- [ ] manual QA checklist is completed
- [ ] automated tests run where the repo supports them
- [ ] auth/RLS/tenant/RBAC permission checks are covered
- [ ] live app passes critical path QA
- [ ] failures are fixed or explicitly deferred with reason
- [ ] `.onemillion/test-results.md` records evidence, limitations, and verdict

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 10: QA + Tests.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 11 — AI Feature Spec](../day-11-ai-spec/learn.md)
