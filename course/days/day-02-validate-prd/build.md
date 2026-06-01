# Day 2 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Still no code.** Today you improve one artifact:

```text
.onemillion/prd.md
```

---

## Before You Start

- [ ] Day 1 verified.
- [ ] `.onemillion/prd.md` exists.
- [ ] You have at least one potential user, customer, community, or public thread to learn from.

---

## Step 1: Ask The Harness To Teach PRD Validation

Paste this:

```text
I am on OneMillion Day 2.

Teach me how to validate my Day 1 PRD.

Explain:
- why the PRD is a hypothesis
- how to review and edit the PRD as the product owner
- how to validate pain with real users
- how to ask non-leading questions
- how to compare competitors and manual workarounds
- what ICP means
- what TAM/SAM/SOM means in simple terms
- what MVP means
- how MVP differs from the full product
- when to Keep, Refine, or Pivot the PRD

Then guide me one step at a time.
Use .onemillion/prd.md as the single source of truth for today's work.
```

---

## Step 2: Open And Edit The PRD

Open `.onemillion/prd.md`.

Read it fully. Edit anything you disagree with.

Then add this section near the top:

```markdown
## Day 2 Learner Review

Reviewed on: 2026-05-31
Status: Confirmed / Needs refinement / Pivot needed

What I changed:
- [Change]
- [Change]

What I still need to validate:
- [Question]
- [Question]
```

Do not continue until the PRD feels like your current best understanding of the product.

---

## Step 3: Talk To Users Or Study Real Workflows

Try to talk to 3 people who match or are close to the target user.

If you cannot get 3 live conversations today, document serious outreach attempts and do at least one of:

- one live conversation
- one detailed async response
- one workflow observation
- one public forum/thread analysis from people with the same pain

Add this section to `.onemillion/prd.md`:

```markdown
## Day 2 Validation Evidence

### Evidence 1: [Name or anonymized profile], [role/context]
Date:
How: Phone / Zoom / Slack / email / forum / observation

Current workflow:

Pain evidence:

Reaction to PRD workflow:

Missing use cases:

Data reality:

Direct quote or specific observation:

PRD implication: Keep / Refine / Pivot because...

### Evidence 2

### Evidence 3
```

Use anonymized names if needed, but be specific enough that the evidence is believable.

---

## Step 4: Add Competitor And Workaround Notes

Add this section to `.onemillion/prd.md`:

```markdown
## Day 2 Competitors And Workarounds

| Alternative | What it solves | What it does well | Gap | PRD implication |
|---|---|---|---|---|
| [Tool/workaround] | [job] | [strength] | [gap] | [what to change/keep] |
| [Tool/workaround] | [job] | [strength] | [gap] | [what to change/keep] |
| [Tool/workaround] | [job] | [strength] | [gap] | [what to change/keep] |
```

Include manual workarounds. A spreadsheet can be a competitor.

---

## Step 5: Add ICP And Market Sanity

Add this section to `.onemillion/prd.md`:

```markdown
## Day 2 ICP And Market Sanity

### Ideal Customer Profile
[Specific first customer profile.]

### Painful Workflow
[What workflow hurts?]

### Current Workaround
[What do they do today?]

### Data They Have
[What files, tools, formats, or systems exist?]

### Why They Care Now
[Why this matters enough to act.]

### Why They Are Reachable
[Where/how the builder can find them.]

### TAM / SAM / SOM
- TAM: [broad category, marked as assumption if not verified]
- SAM: [realistic segment]
- SOM: [first reachable group]
```

---

## Step 6: Add Full Product Versus MVP

Add this section to `.onemillion/prd.md`:

```markdown
## Day 2 MVP Decision

### Full Product Vision
[If this became a mature product, what would it eventually include?]

### Minimum Viable Product
[The smallest version that proves the core user value.]

### First Build Loop
1. [User does this]
2. [Product does this]
3. [User gets this value]

### Must Have For MVP
- [Feature/workflow/data requirement]
- [Feature/workflow/data requirement]
- [Feature/workflow/data requirement]

### Not In MVP
- [Full product feature that waits]
- [Full product feature that waits]
- [Full product feature that waits]

### MVP Success Criteria
- [What must be true for the first build to count as useful?]

### KPI / Key Goal For MVP
- [Measurable signal]
```

Keep it small. The MVP is the first useful build, not the whole company.

---

## Step 7: Add The Day 2 Verdict

Add this final section to `.onemillion/prd.md`:

```markdown
## Day 2 Validation Update

Verdict: Keep / Refine / Pivot

What the evidence confirmed:
- [Confirmed point]

What the evidence challenged:
- [Challenged point]

Missing use cases:
- [Use case or "None found yet"]

PRD changes made:
- [Change]

MVP decision:
- [What the first build includes]
- [What moved out of MVP]

Final decision:
[One paragraph explaining why the PRD is ready or what changed.]
```

---

## Step 8: Run Day 2 Verification

From your project folder, ask your harness to run the OneMillion verifier for Day 2.

The verifier should read `.onemillion/prd.md` only and decide whether the PRD is good enough to continue.

---

## What Should Be True After Day 2

- [ ] `.onemillion/prd.md` includes a Day 2 learner review.
- [ ] `.onemillion/prd.md` includes validation evidence.
- [ ] `.onemillion/prd.md` includes competitors/workarounds.
- [ ] `.onemillion/prd.md` includes ICP and TAM/SAM/SOM sanity.
- [ ] `.onemillion/prd.md` includes full product versus MVP.
- [ ] `.onemillion/prd.md` includes a Day 2 verdict.
- [ ] Verification passed.

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 2 complete
- **Last verified day:** Day 2
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 3.

## If You Are Stuck

Open your coding harness from your project folder and paste this:

```text
I am on OneMillion Day 02.

Here is the step I was trying to complete:
[paste the step heading or instructions]

Here is what happened:
[paste the error, terminal output, or describe what I see]

Diagnose the likely cause and give me the next smallest action.
Do not create extra Day 2 paperwork files.
Keep .onemillion/prd.md as the single source of truth for Day 2.
Ask for one missing detail at a time if needed.
```

---

→ **Done with Day 2?** Move to [Day 3 — Lock The Spec](../day-03-spec/learn.md).
