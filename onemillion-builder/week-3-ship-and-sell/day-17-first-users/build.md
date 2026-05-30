# Day 17 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 45-90 min. Most of this is communication, not coding.**

---

## Step 1: List 10 People To Reach Out To (10 min)

In `.onemillion/outreach-list.md`:

```markdown
## Outreach List — Day 17

### Tier 1 (warm)
1. [Name] — [why they're a fit, Day 2 conversation context]
2. [Name] — [...]
...

### Tier 2 (broader network)
6. [Name] — [...]
...

### Tier 3 (cold, optional)
9. [Name] — [...]
10. [Name] — [...]
```

Aim for 7-10 Tier 1/2 people. Cold outreach is bonus.

---

## Step 2: Send Outreach Messages (30-45 min)

For each person:
- Use the template from learn.md
- Customize the "specifically you because..." line for each one
- Send via the channel they use (Slack, LinkedIn, text, email)

Don't batch-blast. Personalize each message.

Track who you sent to:

```markdown
## Outreach Status

| # | Name | Tier | Sent? | Responded? | Signed up? |
|---|------|------|-------|------------|------------|
| 1 | Sarah | 1 | ✅ | ✅ | ✅ |
| 2 | Mike | 1 | ✅ | ⏳ | - |
...
```

---

## Step 3: Walk Anyone Who Responds Through Signup (15-30 min per)

If someone responds and is willing to try:

**Option A — Async (most common):**
- Send them your URL
- "Click Sign Up, takes 2 minutes. Then try [main feature]. Then send me a screenshot or 2-3 sentences on what you think."

**Option B — Live (10x better, harder to schedule):**
- 15-min call / Zoom
- Share your screen OR their screen
- Watch them sign up + use it WITHOUT instructing them
- Don't help them when they get confused — note where they got confused
- After 10 min, ask: "What was confusing? What would you change?"

Option B reveals 5x more than Option A. Worth pushing for, even with 1-2 people.

---

## Step 4: Capture Feedback (15-20 min)

In `.onemillion/feedback.md`, use the template from learn.md.

Capture:
- Direct quotes (gold)
- What they tried
- What worked
- What didn't
- What's missing
- Your interpretation

---

## Step 5: Categorize Feedback (10 min)

Sort each piece into:

**P0 (fix before Day 18):** Critical bugs, broken signup, security issues
**P1 (fix Week 4):** Confusion that affects multiple users likely, missing features users explicitly asked for
**P2 (later):** Nice-to-haves, edge cases, individual preferences
**Ignore:** Outside scope, only 1 person, doesn't match your PRD

Don't fix anything today (except P0 actual bugs). Just sort. You ship Day 18 first.

---

## Step 6: Verify

```bash
claude
```

Paste contents of [`ai-instructions-day-17.md`](./ai-instructions-day-17.md).

---

## What Should Be True After Day 17

- [ ] `.onemillion/outreach-list.md` exists with 10 people
- [ ] You sent 10 outreach messages
- [ ] At least 1 response received
- [ ] At least 1 person actually signed up + tried it
- [ ] `.onemillion/feedback.md` has at least 1 entry with direct quotes
- [ ] Feedback categorized (P0/P1/P2/Ignore)
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 17 complete
- **Last verified day:** Day 17
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 18.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 17.

Here is the step I was trying to complete:
[paste the step heading or instructions]

Here is what happened:
[paste the error, terminal output, or describe what I see]

Diagnose the likely cause and give me the next smallest action.
Do not rewrite unrelated code.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Nobody responded yet | Some people respond in days, not hours. Don't panic. Send 5 more messages tomorrow. |
| Person responded but got stuck signing up | Walk them through it. Document where they got stuck. |
| All feedback is "looks great!" | You're talking to wrong people OR not asking specific enough questions. Use Mom Test framework — ask about past behavior. |
| Critical bug discovered (P0) | Pause the day. Fix the bug. Then resume outreach. |
| Tempted to add features mid-conversation | Don't. Note the feedback, ship Day 18 first, iterate later. |

---

→ **Done with Day 17?** Move to [Day 18 — Demo Day → Builder #N](../day-18-demo/learn.md). Almost there.
