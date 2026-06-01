# Day 9 — Build Guide

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
I am on OneMillion Day 9: Implementation Review.

Act as the `review` agent for this day.
First teach me implementation review in plain language:
- what it means to compare built code against PRD, refined spec, design, architecture, and sprint brief
- why "it works" is different from "it matches the product intent"
- how to manually inspect the UI
- how to decide whether the flow looks right and feels simple
- how to review from the shoes of the target user
- how to ask whether the sprint alleviates the pain point or unmet need
- how to classify blockers, bugs, gaps, edge cases, and observations
- how to fix what matters, defer what can wait, and keep building

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- what to fix now
- what to defer
- whether drift is intentional
- whether the UI looks like what I had in mind
- whether the flow is simple and natural
- whether the target user would understand what to do
- whether the Day 8 sprint alleviates the pain point from Day 1
- what should be sharpened before continuing

## Step 3: Produce The Day Output

Expected output today:

- `.onemillion/review-findings.md`
- manual UI/product inspection notes inside the review findings
- fix-now/defer/keep-building decisions

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: Manual Product Inspection

Open the local app or deployed URL and inspect the Day 8 workflow manually.

Use this checklist:

- Does the UI look like what I had in mind?
- Does the main flow move naturally?
- Is the first action obvious?
- Is the language familiar to the target user?
- Are the fields useful, necessary, and understandable?
- Are loading, empty, error, success, and permission states reasonable?
- Does the workflow reduce the pain point or unmet need from Day 1?
- Would the target user trust this with their data?
- What is the smallest change that would make it sharper?

## Step 5: External Tools

- No new external account is required today.

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 9.
Inspect the relevant artifacts, app code, deployment links, review findings, manual UI/product inspection notes, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 9 complete
- **Last verified day:** Day 9
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 10.

## What Should Be True After Day 9

- [ ] .onemillion/review-findings.md exists
- [ ] manual UI/product inspection is included
- [ ] target-user pain-point fit is assessed
- [ ] blockers are fixed or explicitly deferred with reason
- [ ] any deferrals have a next sprint or reason
- [ ] code still builds
- [ ] Day 8 core workflow still works locally or live

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 9: Implementation Review.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 10 — QA + Tests](../day-10-qa-tests/learn.md)
