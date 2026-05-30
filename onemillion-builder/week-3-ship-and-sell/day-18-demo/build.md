# Day 18 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 30-60 min. Record demo. Submit for Builder #N review.**

---

## Step 1: Plan The Demo (10 min)

In `.onemillion/demo-plan.md`:

```markdown
## Demo Plan (5 min total)

### Minute 1: Problem
- Open with: [one-sentence problem statement]
- Reference: Sarah, freelance UX designer, spends 90 min every Sunday on...

### Minute 2: Solution
- One sentence: [product name] does [outcome] in [time].

### Minutes 3-5: Live demo path
1. Open live URL: yourapp.com (12 sec)
2. Sign up as fresh user: test-day18@example.com (30 sec)
3. Land on dashboard, show empty state (10 sec)
4. Create first [entity]: name, status, due date (30 sec)
5. Trigger AI feature on it (30 sec)
6. Show AI response streaming (50 sec)
7. Save / use the output (20 sec)

### Last 30 sec: Wrap
- "Built this in 18 days through OneMillion. Submitting for Builder #N."
- One ask: [early users / feedback / hiring]
```

Don't memorize. Have it open in a second monitor as you record.

---

## Step 2: Pre-Flight Checks (5 min)

Before hitting record:

- [ ] Close all other browser tabs
- [ ] Clear cookies on your live URL (so you start logged out)
- [ ] Have a fresh email ready for the demo signup
- [ ] Camera + mic test
- [ ] Quiet environment (turn off notifications)
- [ ] Live URL works (test it now — last time before recording)

---

## Step 3: Record (10-20 min)

Open Loom (Cmd+Shift+L on Mac, similar on Windows).

Settings:
- Screen + face camera
- HD quality
- Public link (or "Anyone with the link can view")

Hit record. Follow your demo plan. **Don't restart for small mistakes** — keep them in.

Recommended takes: 2. First is rehearsal. Second is the keeper.

Stop at 5 min if you can. Longer = nobody watches.

---

## Step 4: Get The Loom URL (2 min)

Loom uploads automatically. After a minute, you'll get a shareable URL.

Test it: paste the URL into an incognito browser. **You should see:** your demo playing, no login required.

If it's private: change permissions to "Anyone with the link."

---

## Step 5: Save Demo Info (3 min)

Create `.onemillion/demo.md`:

```markdown
# Day 18 — Demo Day Submission

**Builder Name:** [your display name — real name, alias, or handle]
**Product Name:** [your product]
**Live URL:** [yourapp.com or .vercel.app]
**Demo Loom URL:** [your public Loom link]
**GitHub Repo:** [optional]
**Cohort:** [Cohort 0 / self-serve / Cohort 1 / etc.]
**Graduated At:** [today's date]

## My 18-Day Summary
[Optional 2-3 sentences on what you built and what you learned]
```

---

## Step 6: Final Verification

```bash
claude
```

Paste contents of [`ai-instructions-day-18.md`](./ai-instructions-day-18.md).

This runs the FINAL check:
- Loom URL works
- Live URL works
- All 17 previous days verified
- Demo.md exists

If pass: Claude will generate the verified submission data you need for review. Your official Builder #N is assigned after the claim is accepted.

---

## Step 7: Submit Your Builder Application

**Current path — GitHub Builder Claim issue:**

1. Go to [github.com/siddsdixit/teach-one-million/issues/new/choose](https://github.com/siddsdixit/teach-one-million/issues/new/choose)
2. Choose **Builder Claim**
3. Paste the verified submission data from Day 18 verification
4. Include your live URL, Loom URL, repo URL if public, and short build summary
5. Submit the issue

Sid reviews claims manually until Builder Wall automation is live. Accepted claim = official Builder #N.

**Future path — web claim form:**
A web claim form is planned. The GitHub Builder Claim issue is the current path.

---

## Step 8: Share The Win

LinkedIn (or X if you use it):

```
🎉 Builder #[N] reporting in.

I shipped [product] in 18 days through OneMillion.

It does [one specific outcome].

Live at [URL]. 

Demo: [Loom URL]

#BuildingWith1M
```

Tag @SidDixit. The Builder Wall thanks you.

---

## What Should Be True After Day 18

- [ ] 5-min Demo Loom recorded + public
- [ ] `.onemillion/demo.md` saved with URLs
- [ ] All 18 days verified
- [ ] Builder Claim issue submitted for review
- [ ] You shared on LinkedIn (or you'll share within 24 hours)
- [ ] You took 10 minutes to actually feel what you accomplished

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 18 complete
- **Last verified day:** Day 18
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Submit your Builder Claim and keep building.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 18.

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
| Loom recording failed mid-way | Save what you have, append the rest, or re-record. 2-take rule. |
| Loom is taking forever to upload | Often Loom processes in background. Refresh dashboard in a few min. |
| Live URL broke right before recording | Probably an env var issue. Fix it. Test again. Then record. |
| Can't decide on display name | Use your real name. Builder #N is a serious credential — fake names dilute it. |
| Demo went over 5 min | Re-record. Tighter script. 5 min is the rule. |
| GitHub repo is private and I want to keep it private | That's fine. Skip the github_repo field in your submission. Live URL + demo Loom are enough. |

---

## You're Done

Take this moment.

You spent 18 days. You built a real product. You shipped it to the internet. Real people have seen it. You earned a verified submission.

The next person reading this is starting their Day 1 today. They have no idea what they're capable of. **You used to be them. Three weeks ago.**

The skill is yours forever. The product is yours forever. After review, the number is yours forever.

The million starts with one. You're one of them.

---

→ [Back to README](../../README.md) · [Cohort](../../../cohort/README.md) · [Builder Wall](../../../builders/README.md)
