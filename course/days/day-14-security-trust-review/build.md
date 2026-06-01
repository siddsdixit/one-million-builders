# Day 14 — Build Guide

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
I am on OneMillion Day 14: Security + Trust Review.

Act as the `guard` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Do not skip my human decisions.
Do not create paperwork-only files.
Inspect and fix the actual app. Update existing architecture/refined PRD only if security behavior changes.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- single-tenant, multi-tenant, or public/community data stance
- whether RBAC is needed now
- which roles/actions exist if RBAC is needed
- what data AI may receive
- whether RAG/tool use is necessary or skipped
- acceptable cost/rate limits
- which risks block production

## Step 3: Produce The Day Output

Expected output today:

- fixed or confirmed auth, RLS, RBAC/tenant, secret, AI data, and cost/rate posture
- updated existing architecture/refined PRD only if security behavior changed

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: Security + Trust Prompts

### Auth And Authorization Review

```text
Review the app's auth and authorization behavior.

Check:
- which routes require login
- which actions require the current user
- whether data is scoped by owner_id, organization_id, tenant_id, or role
- whether RBAC is needed now
- what happens if a second user tries to access another user's data

Teach me the difference between authentication and authorization before making changes.
Fix production-blocking issues in the smallest safe way.
```

### Supabase RLS Review

```text
Review Supabase table access and RLS assumptions for this app.

Check:
- which tables contain user data
- whether RLS is enabled where needed
- whether policies use auth.uid() or tenant membership correctly
- whether service-role keys are only used server-side when truly needed
- whether anon keys are used only in the intended public client path

If you cannot inspect Supabase directly, give me the exact SQL/dashboard checks to run and tell me what result to paste back.
```

### AI Data Privacy Review

```text
Review the Day 12 AI route/action for privacy and trust.

Check:
- what data is sent to the model
- whether the current user is allowed to see that data
- whether the app sends more data than necessary
- whether user-provided content could contain prompt injection instructions
- whether AI output can change data or trigger actions without review
- whether RAG/tool use is skipped or truly justified

Keep the simplest AI data path that solves the user problem.
```

### Secret And Cost Scan

```text
Run a secret and cost/rate review.

Check:
- .env.local is ignored
- .env.example has placeholders only
- no Anthropic/OpenAI/Google/Supabase service keys are committed
- no server-only key is prefixed with NEXT_PUBLIC_
- AI routes have basic rate/cost/abuse protection or a conscious MVP deferral

Fix critical leaks immediately.
```

## Step 5: External Tools

- Supabase dashboard: https://supabase.com/dashboard
- Supabase project shortcut: https://database.new
- Supabase Next.js Auth: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Supabase API keys: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 14.
Inspect the existing architecture/refined PRD, app code, Supabase auth/RLS assumptions, AI route, env handling, deployment links, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 14 complete
- **Last verified day:** Day 14
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 15.

## What Should Be True After Day 14

- [ ] auth routes and protected pages behave correctly
- [ ] owner, tenant, or RBAC checks exist where needed
- [ ] Supabase RLS policies protect user/tenant data
- [ ] no server-only secret is exposed to client code or git
- [ ] AI route receives only allowed, minimal context
- [ ] RAG/tool use is skipped or justified by the product
- [ ] cost/rate/abuse controls are present or consciously deferred with reason

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 14: Security + Trust Review.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 15 — QA + Production Readiness](../day-15-qa-production-readiness/learn.md)
