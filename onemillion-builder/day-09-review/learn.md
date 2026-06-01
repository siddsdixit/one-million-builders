# Day 9 — Implementation Review

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `review`
**Supporting agents:** build

Day 9 is a pause before more building. You inspect the useful sprint from Day 8 and ask: did we build the right thing, does it feel right, and should we keep building on top of it?

Working software can still be the wrong software. Today combines implementation review with manual product inspection.

## Learning Frame

- **Mental model:** review is where you compare the built product against the spec, the design, the target user's pain, and your own product taste before adding more code.
- **Input:** PRD, refined PRD, design spec, architecture, Day 8 sprint brief, built code, and live app.
- **Output:** `.onemillion/review-findings.md`, manual inspection notes, and fixes or explicit deferrals for blockers.
- **What can go wrong:** the learner only asks "does it compile?" and misses that the flow is confusing, ugly, off-spec, insecure, or not actually solving the target user's pain.
- **What to ignore today:** do not add new features unless they fix a review finding. Do not start AI. Do not polish randomly.

## What You Learn

- what implementation review means
- how to compare implementation to PRD, refined spec, design, architecture, and sprint brief
- how to inspect the UI manually
- how to evaluate whether the flow feels simple and natural
- how to look through the shoes of the target user
- how to ask whether the product alleviates the pain point or unmet need
- how to sharpen the product before continuing
- how to classify blockers, bugs, gaps, edge cases, and observations
- how to decide fix now, defer, or keep building

## Core Concepts

### Implementation Review

Implementation review asks: did we build what the spec said?

The review agent compares code against:

- PRD and refined PRD
- design spec and screen specs
- architecture and sprint brief
- acceptance criteria
- auth, tenancy, RBAC, and RLS decisions

Spec drift is a finding even if the code seems to work.

### Manual Product Inspection

The learner must also open the app and inspect it like a product owner.

Ask:

- Does the UI look like what I had in mind?
- Does the page feel clear or confusing?
- Does the flow move naturally from one step to the next?
- Is it simple enough for the target user?
- Does the product speak to me as the builder?
- If I were the target user, would I understand what to do?
- Does this actually alleviate the pain point or unmet need from Day 1?
- What is sharper now that I can see the product?
- What feels unnecessary, missing, or awkward?

This is not vague "vibes." It is product judgment. A usable product should feel obvious to the intended user.

### Target User Lens

Review from the shoes of the target user. If the target user is a teacher, manager, founder, parent, clinician, recruiter, or student, inspect the app as that person.

Ask:

- What job are they trying to get done?
- What anxiety or friction brought them here?
- Does the first useful sprint reduce that friction?
- Is the language familiar to them?
- Are the fields asking for information they actually have?
- Are there too many steps?
- Would they trust this product with their data?

### Finding Severity

Findings should be classified so the learner can keep momentum.

| Severity | Meaning | Action |
|---|---|---|
| Blocker | Prevents useful workflow, creates security/data risk, or violates core spec | Fix before continuing |
| Bug | Incorrect behavior or broken UX state | Usually fix now |
| Gap | Missing piece that matters but can be scheduled | Decide fix now or sprint later |
| Edge case | Less common path not handled | Decide based on risk |
| Observation | Taste, clarity, minor improvement | Note, do not derail |

### Keep Building

Review is not a reason to freeze. It is a way to sharpen the product and keep building with confidence.

Fix blockers. Fix the obvious high-value bugs. Defer non-critical work with a reason. Then keep building.

## What You Produce

- `.onemillion/review-findings.md`
- manual product inspection notes inside the review findings
- blocker fixes or explicit deferrals

## Human Decisions

- what to fix now
- what to defer
- whether drift is intentional
- whether the UI matches the learner's product intent
- whether the flow feels simple for the target user
- whether the Day 8 sprint actually addresses the pain point
- what should be sharpened before continuing

## Done Checklist

- [ ] .onemillion/review-findings.md exists
- [ ] manual UI/product inspection is included
- [ ] target-user pain-point fit is assessed
- [ ] blockers are fixed or explicitly deferred with reason
- [ ] any deferrals have a next sprint or reason
- [ ] code still builds
- [ ] Day 8 core workflow still works locally or live

## Verify Your Day 9

When the checklist is true, ask your harness to run the OneMillion verifier for Day 9. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 10 — QA + Tests](../day-10-qa-tests/learn.md)
