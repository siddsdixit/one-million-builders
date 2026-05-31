# Day 7 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**No code today.** Pure spec writing. Use Claude to help draft.

---

## Before You Start

- [ ] Days 1-6 complete + verified
- [ ] You've read [learn.md](./learn.md) (especially Part 1 — the 3 patterns)
- [ ] You know your product's main user story from your PRD

---

## Step 1: Open your coding harness In Your Project

```bash
cd ~/my-onemillion-build
claude
```

---

## Step 2: Draft Your AI Feature Spec

Paste this prompt into Claude:

```
I'm on Day 7 of OneMillion (Days 7-12 — Make It AI). I need to write an AI
Feature Spec for my product.

Here's my PRD:
[paste contents of .onemillion/prd.md]

Help me draft an AI feature for this product. Walk me through it section
by section. Push back on vagueness. The output goes in
the AI feature section in `.onemillion/prd.md` and has these sections:

- Pattern (A / B / C — see Day 7 learn.md)
- What It Does
- When It Runs
- Input
- Output
- Quality Criteria (must be measurable)
- Out Of Scope (minimum 4 items)
- Cost Budget (per call + max)

Start by asking me which of the 3 patterns best matches my PRD's user stories.
```

Claude asks questions. You answer. Claude drafts. Iterate.

---

## Step 3: Sanity Check

Read your spec aloud. Ask yourself:

- **Specificity check:** Could a stranger read this and build the AI feature without asking me clarifying questions?
- **Pattern fit:** Does the pattern (A/B/C) actually match what the feature does?
- **Quality check:** Are my Quality Criteria things I can MEASURE, or are they wishes?
- **Scope check:** Is "Out Of Scope" honest? Does it include things I was tempted to add?
- **Budget check:** Did I do the math on cost? (Calls per day × cost per call = monthly burn)

If any answer is no, ask Claude to revise that section.

---

## Step 4: Save And Lock

Once it's solid:

```
Save the final version into `.onemillion/prd.md` under `## AI Feature Spec`.
```

Then commit it:

```bash
git add .onemillion/prd.md
git commit -m "Day 7: AI feature locked"
```

From this point: no scope creep on the AI feature. If you think of something cool to add, it goes to "Out Of Scope" or "v2", not into the current build.

---

## Step 5: Verify

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.

---

## What Should Be True After Day 7

- [ ] `.onemillion/prd.md` includes `## AI Feature Spec` with all 8 sections
- [ ] One pattern selected (A, B, or C)
- [ ] Quality Criteria are measurable (numbers or verifiable conditions)
- [ ] Cost Budget includes per-call cost AND a max
- [ ] Out Of Scope has 4+ items
- [ ] You committed the spec to git
- [ ] Verification passed ✅

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 7 complete
- **Last verified day:** Day 7
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 8.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 07.

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
| Claude wrote a 10-section spec | Tell it: "Reduce to exactly these 8 sections: [list]. No more." |
| I can't decide between Pattern A and Pattern B | Pick A. Simpler. You can add B-style judgment in v2. |
| My Quality Criteria are vague ("output is good") | Ask Claude: "Rewrite Quality Criteria as measurable checks. Each one a number or a verifiable condition." |
| I don't know the cost per call | Claude knows. Ask: "What's the cost for my use case using Claude Haiku vs Sonnet?" |
| I'm tempted to add more features | Add them to Out Of Scope. Don't expand v1. |

---

→ **Done with Day 7?** Move to [Day 8 — First AI Call + Prompt Design](../day-08-first-ai-call/learn.md).
