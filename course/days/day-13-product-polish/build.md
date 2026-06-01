# Day 13 — Build Guide

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
I am on OneMillion Day 13: Product Polish + UX Finish.

Act as the `build` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Do not skip my human decisions.
Do not create paperwork-only files.
Improve the actual app and update existing pipeline artifacts only if behavior changes.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- what the app should feel like for the target user
- what UX problems must be fixed now versus deferred
- whether AI output is displayed, saved, reviewed, edited, or accepted
- what the user should see while AI is working
- what the user should see when AI fails
- what success should look like after the main workflow completes

## Step 3: Produce The Day Output

Expected output today:

- polished MVP flow in the actual app
- improved AI feature UX where Day 12 added AI
- complete empty/loading/error/success states for the core workflow
- mobile and desktop fixes where needed

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: Product Polish Prompts

Use these prompts with your harness as needed.

### Inspect The Product Like The Target User

```text
Inspect the current app as my target user.

Use the PRD/refined PRD, design spec, architecture, Day 8 build, Day 9 review, Day 10 QA results, and Day 12 AI feature.

Tell me:
1. What the user is trying to accomplish
2. Where the current UI creates confusion or friction
3. Which empty/loading/error/success states are missing
4. Whether the AI feature feels useful, understandable, and reviewable
5. The smallest set of fixes that will make the MVP feel complete

Do not add a new major feature. Focus on polish, flow, copy, states, and layout.
```

### Improve UX States

```text
Improve the app's UX states for the core workflow.

Add or improve:
- empty state
- loading state
- error state
- success state
- partial state if the user has started but not finished

Use clear product copy. Make the next action obvious. Keep the implementation small and aligned with the existing MUI design system.
```

### Improve AI UX

```text
Improve the Day 12 AI feature UX.

The user should understand:
- what the AI is doing
- what data the AI is using
- what to do while waiting
- what the output means
- how to retry or edit
- whether accepting the output changes anything

If AI output can update data or trigger an action, add a user review/confirm step.
Do not add streaming unless it clearly improves this product.
```

### Mobile And Desktop Pass

```text
Review the main flow on mobile and desktop.

Fix obvious layout issues:
- overlapping text
- buttons that wrap badly
- crowded mobile screens
- missing responsive behavior
- unclear hierarchy

Keep the visual language consistent with MUI and the Day 4 design system.
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

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 13.
Inspect the relevant pipeline artifacts, app code, product UI, AI feature UX, responsive behavior, deployment links, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 13 complete
- **Last verified day:** Day 13
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 14.

## What Should Be True After Day 13

- [ ] main MVP flow is easy to understand without explanation
- [ ] empty/loading/error/success states are present where needed
- [ ] AI feature has clear waiting, output, retry, and review behavior
- [ ] mobile and desktop layouts do not overlap or break
- [ ] target-user pain point still feels central to the product

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 13: Product Polish + UX Finish.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 14 — Security + Trust Review](../day-14-security-trust-review/learn.md)
