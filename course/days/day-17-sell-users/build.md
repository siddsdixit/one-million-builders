# Day 17 — Build Guide

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
- [ ] Day 16 production URL works or the ship blocker is explicit.

## Step 1: Ask The Harness To Teach The Day

Paste this:

```text
I am on OneMillion Day 17: Brand + Marketing + Pricing + First Users.

Act as the `sell` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, the sell agent, and the current pipeline artifacts.
Read .onemillion/state.json and use the live_url in every CTA if it exists.
Do not skip my human decisions.
Do not create paperwork-only files.
Prefer updating the actual product/landing page and the existing verification trail.
Create separate marketing files only when they are useful launch assets.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- product name and tone
- category and differentiator
- target buyer/user
- CTA
- pricing stance
- who to contact first
- where to post without spamming
- which feedback changes the product, copy, or Builder Claim

## Step 3: Produce The Day Output

Expected output today:

- positioning statement
- landing/product page copy or live app page update
- pricing stance
- launch posts and outreach messages
- first-user outreach evidence or queued send plan
- feedback or pending-response status

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: Sell Agent Prompts

### Positioning

```text
Use the sell agent to create product positioning.

Read the PRD/refined PRD, design spec, architecture, live URL, and current app copy.

Produce:
- product category
- target user
- pain point in the user's language
- key benefit
- top alternative or current workaround
- differentiator
- one-line positioning statement:
  For [target user] who [pain], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].

Keep it specific. No jargon.
```

### Landing/Product Page Copy

```text
Write or improve the landing/product page copy for the live app.

Include:
- benefit-first headline
- subheadline
- primary CTA
- problem section
- solution section
- 3-4 key features
- proof/demo section using the live URL or app state
- pricing section
- final CTA
- SEO title, meta description, and OG title/description

If the app already has a landing page, update the actual app code. If not, add the smallest product page that fits the current app.
```

### Pricing Stance

```text
Help me choose the MVP pricing stance.

Teach the options:
- free beta
- waitlist
- one-time payment
- subscription
- usage-based
- demo-call first

Recommend the simplest stance for my product and explain why.
Make the pricing copy honest and low-friction.
```

### Launch Content

```text
Create ready-to-send launch content.

Produce:
- LinkedIn post with a personal builder narrative and live URL
- X post or short thread with live URL
- community post in a Show HN / Reddit / Slack style without sounding spammy
- two cold email or DM variants

Every message needs:
- the pain
- what the product does
- who it is for
- the live URL
- a clear ask
```

### First-User Outreach

```text
Create a first-user outreach plan.

List 5-10 specific people or communities I can contact.
For each, state:
- why they are relevant
- which message to use
- what the ask is
- how I will record signal

Do not fake that messages were sent. Ask me to confirm sent, queued, or skipped.
```

### Feedback Capture

```text
Set up a simple feedback capture method for Day 17.

Use the simplest option:
- direct replies
- email replies
- a short form
- GitHub issue
- product feedback field if already built

Track signal as:
- interested
- confused
- objection
- requested feature
- willing to pay
- no response yet

Update the existing verification trail/state with the status. Do not create extra files unless useful.
```

## Step 5: External Tools

- Gmail: https://mail.google.com/
- LinkedIn feed: https://www.linkedin.com/feed/
- X post composer: https://x.com/compose/post
- Reddit submit: https://www.reddit.com/submit
- Hacker News submit: https://news.ycombinator.com/submit
- Discord: https://discord.com/
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Analytics: https://vercel.com/docs/analytics
- Plausible Analytics: https://plausible.io/
- Umami: https://umami.is/

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 17.
Inspect the positioning, landing/product page, live URL, CTA, SEO metadata, pricing stance, outreach messages, sent/queued outreach confirmations, and feedback status.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 17 complete
- **Last verified day:** Day 17
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 18.

## What Should Be True After Day 17

- [ ] positioning statement is specific and benefit-first
- [ ] landing/product page has headline, pain, solution, proof/demo, CTA, and basic SEO metadata
- [ ] pricing stance is explicit, even if it is free beta
- [ ] outreach list includes 5-10 real people or relevant communities
- [ ] at least 3 direct outreach messages or posts are sent, or queued with a concrete send time
- [ ] every outreach message includes the live URL and a clear ask
- [ ] feedback signal or pending-response status is recorded honestly

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 17: Brand + Marketing + Pricing + First Users.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 18 — Demo Day + Builder Claim](../day-18-demo/learn.md)
