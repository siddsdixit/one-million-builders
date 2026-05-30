# Day 2 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Still no code.** Today's "build" is having 3 conversations and writing down what you heard.

If you're nervous about reaching out to people, that's normal. Push through it. By tomorrow you'll be glad you did.

---

## Before You Start

- [ ] Day 1 verified ✅
- [ ] You've read [learn.md](./learn.md) (especially Part 2 — the good vs bad questions)
- [ ] You've identified 3+ people to talk to (read on for help)

---

## Step 1: Identify 3 People To Talk To

You need people who have the problem. Not people who like you.

### Where to find them

**For consumer products** (productivity tools, fitness apps, etc.):
- Friends of friends who match your target — "Hey, do you know anyone who's freelance? I'm researching a tool for them."
- Reddit communities related to the problem — search the subreddit, find recent posts complaining about your problem, DM the poster
- Twitter/X search — search the phrase "I wish there was a tool for..." and DM people venting

**For B2B products** (CRM, internal tools, etc.):
- LinkedIn DMs — search for the job title, DM 10 people, expect ~2 responses
- Friends who work at companies with the problem
- Indie Hackers community

**For products solving your own problem:**
- You already know people with this problem. Reach out to them.

### How to ask for the conversation

A good DM/email:

```
Hey [name],

I'm researching a problem I think you've experienced — [the pain in one sentence].

Not selling anything. I'm not even sure I'm going to build it. Just trying to understand the pain better.

Got 15 minutes this week for a call? Even a 10-minute voice message would be helpful.
```

That's it. Don't pitch your idea. Don't promise to follow up with the product. Just ask for the conversation.

> 💡 **Acceptable response rate is 1 in 3.** If you message 10 people, expect 3 conversations. That's normal. Don't get discouraged.

---

## Step 2: Have The Conversations

### Format
- 15-30 minutes, voice or video preferred (text is ok if necessary)
- They talk 80% of the time. You ask questions and listen.
- Record audio if you can (with their permission) — even just for your own notes

### The structure
1. **First 2 minutes:** Thank them, restate why you're talking ("trying to understand the problem, not pitching anything")
2. **Next 20 minutes:** Mom Test questions. Walk through their experience. Ask "what happened next?" relentlessly.
3. **Last 5 minutes:** Ask if there's anyone else they think you should talk to (referrals = gold)

### What you're listening for
- **Specific moments** — not "scheduling is hard" but "last Sunday I spent 90 minutes on..."
- **Workarounds** — what they currently do instead. This is your competition.
- **Cost** — time, money, emotional toll. Quantify the pain.
- **Volunteer pricing** — if they mention what they'd pay, write it down. Big signal.

---

## Step 3: Write Down What You Heard

In your editor, create `.onemillion/notes.md`. For each conversation, add an entry:

```markdown
# Conversation Notes

## Conversation 1: Sarah, Freelance UX Designer
**Date:** 2026-05-19
**How:** 25-min Zoom call

### The pain story (specific):
Last Sunday she spent an hour and a half cross-referencing Notion, email, and Slack
trying to figure out which of her 4 clients she still owed mockups to. She wasn't
sure she'd remembered everything.

### What she's tried to solve it:
- Notion templates (works for tracking, but doesn't notify her)
- Calendar reminders (gets ignored under the noise)
- A whiteboard in her office (only works when she's at her desk)

### Cost of not solving:
- 90 min every Sunday on review
- Lost a client last year ($8K project) by forgetting to send files

### Direct quotes:
- "I'd pay $50/month to never feel that Sunday panic again."
- "I just want one place to see everything I owe."
- "The worst part is I KNOW I'm forgetting something."

### Vibes:
Real pain. She's been thinking about it for months. Already has a workaround budget
in her head ($50/mo). Would buy if I built it.

---

## Conversation 2: ...

## Conversation 3: ...
```

Don't worry about perfect formatting. Capture what was said.

---

## Step 4: Reflect On Your Idea

After 3 conversations, ask yourself:

1. **Do these people actually have the problem I thought they had?**
   - If yes: continue with Day 1 idea
   - If no: pivot (it happens, that's the data working)

2. **Is the problem severe enough that they'd pay or take time to use a solution?**
   - If yes: continue
   - If no: pivot to a more painful problem

3. **What did I hear that I didn't expect?**
   - This is often the most valuable insight. Surprise = learning.

If you pivot, update `.onemillion/project.json` with the new `idea` field.

---

## Step 5: Run Day 2 Verification

```bash
claude
```

Paste the contents of [`ai-instructions-day-02.md`](./ai-instructions-day-02.md).

Claude will read `notes.md`, count conversations, check structure, and report pass / needs revision.

---

## What Should Be True After Day 2

- [ ] `.onemillion/notes.md` exists with 3+ structured conversation records
- [ ] Each conversation has: name, date, pain story, workarounds, direct quotes
- [ ] You either confirmed Day 1 idea or pivoted (and updated project.json)
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 2 complete
- **Last verified day:** Day 2
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 3.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 02.

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
| Nobody responded to my DMs | Cast a wider net (DM 20 not 10). Or try Reddit/Discord communities — strangers respond more than you think. |
| The people I talked to didn't really have the problem | Pick different people. Or your target user is wrong — reflect, then pivot. |
| All three conversations felt fake (they said nice things, no specifics) | You were probably pitching, not listening. Re-read Part 2 of learn.md. Try again with a different person. |
| Conversations took forever | 15 min is fine. Don't apologize for ending. People appreciate brevity. |
| I'm scared to reach out to strangers | Normal. Do it anyway. The fear gets smaller after the first one. Promise. |

---

→ **Done with Day 2?** Move to [Day 3 — Write Your PRD](../day-03-prd/learn.md).
