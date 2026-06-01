# Day 4 — Build Guide

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
I am on OneMillion Day 4: Design The Product.

Act as the `design` agent for this day.
First teach me how product design works in plain language:
- what good design means
- how design depends on user audience and product type
- how web app, mobile-first, and desktop-first design differ
- how MUI / Material Design 3 helps us create a buildable design language
- why loading, empty, error, partial, full, and success states matter

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Read .onemillion/refined-prd.md before proposing screens.
Do not skip my human decisions.
Do not create paperwork-only files.
Do not start architecture or app code today.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- **Primary user flow:** what is the one flow the product must make excellent?
- **Primary device:** mobile-first, desktop-first, or balanced responsive web?
- **Audience:** beginner, power user, enterprise team, consumer, creator, operator, student, or something else?
- **Visual direction:** calm, premium, playful, operational, editorial, bold, clinical, technical, etc.
- **Seed color:** one bold hex color or a plain-language preference.
- **Heading font:** let the agent suggest options, or provide one.
- **Density:** compact, comfortable, or spacious.
- **Navigation pattern:** sidebar, top nav, bottom tabs, command-style, or agent chat-first.
- **MUI component choices:** cards, tables, lists, chips, tabs, dialogs, drawers, forms, skeletons, snackbars.
- **Screen priority:** which screens matter for the MVP?
- **Copy tone:** friendly, expert, concise, warm, direct, premium, etc.

## Step 3: Produce The Day Output

Expected output today:

- `.onemillion/design-spec.md`
- `.onemillion/design-system.md`
- `.onemillion/globals.css`
- `.onemillion/screens/`
- `.onemillion/seed-data.json`
- `.onemillion/mockup/index.html` for web app or hybrid products
- `.onemillion/assets/design-spec.pdf` when PDF generation is available

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

The harness should teach and then create:

- a screen inventory derived from the refined PRD
- one primary user flow
- screen-level layout notes
- responsive behavior for mobile, tablet, and desktop
- MUI component mapping
- theme tokens: color, typography, spacing, radius, elevation, motion, dark mode
- all content states: loading, empty, error, partial, full, success
- realistic seed data that makes the product look active
- a visual mockup preview

## Step 4: External Tools

- No new external account is required today.
- If you already have a Figma file, you may provide it. Otherwise, the design agent generates the design from the refined PRD.
- If using Figma, the exact link is https://www.figma.com/developers/api and the needed token is a Figma personal access token stored as `FIGMA_TOKEN`.

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 5: Preview And Approve

For a web app or hybrid product, ask the harness:

```text
Generate and serve the Day 4 HTML mockup preview.
Open the local preview URL if possible.
Walk me through what I should inspect: visual direction, primary flow, mobile/desktop behavior, content states, and seed data.
Do not mark Day 4 done until I explicitly approve or request revisions.
```

Approve only if the design matches the product you want to build. If not, give specific feedback and ask the design agent to revise the artifacts.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 4.
Inspect .onemillion/design-spec.md, .onemillion/design-system.md, .onemillion/screens/, .onemillion/seed-data.json, the mockup if applicable, and my explicit design approval.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 4 complete
- **Last verified day:** Day 4
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 5.

## What Should Be True After Day 4

- [ ] .onemillion/design-spec.md exists
- [ ] .onemillion/design-system.md exists
- [ ] .onemillion/screens/ contains main screen specs
- [ ] .onemillion/seed-data.json exists
- [ ] .onemillion/mockup/index.html exists for web app or hybrid products
- [ ] main screens and states are described
- [ ] responsive behavior is described
- [ ] MUI component patterns are named
- [ ] realistic seed data exists
- [ ] learner approved the design direction

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 4: Design The Product.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 5 — Plan Architecture](../day-05-plan-architecture/learn.md)
