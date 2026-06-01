# Day 6 — Build Guide

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
I am on OneMillion Day 6: App Shell + First Deploy.

Act as the `build` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- product repo name
- project name
- Vercel project ownership

## Step 3: Produce The Day Output

Expected output today:

- product app shell
- Vercel URL

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: External Tools

- GitHub signup: https://github.com/signup
- GitHub new repo: https://github.com/new
- GitHub CLI: https://cli.github.com/
- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git docs: https://vercel.com/docs/deployments/git
- Vercel env vars: https://vercel.com/docs/projects/environment-variables
- Vercel domains docs: https://vercel.com/docs/domains
- Vercel Analytics: https://vercel.com/docs/analytics

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 5: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 6.
Inspect the relevant artifacts, app code, deployment links, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 6 complete
- **Last verified day:** Day 6
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 7.

## What Should Be True After Day 6

- [ ] GitHub product repo exists
- [ ] local app runs
- [ ] Vercel deployment URL returns 200
- [ ] live homepage matches local source markers

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 6: App Shell + First Deploy.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 7 — Auth + Database](../day-07-auth-db/learn.md)
