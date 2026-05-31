# Day 2 — Validate The PRD

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 1-6 | ~60-120 min | Still no code**

Day 1 created a first PRD. Day 2 makes it real.

You are not creating a pile of new files today. You are improving one important file:

```text
.onemillion/prd.md
```

The question is:

```text
After talking to users, looking at alternatives, and thinking about MVP scope,
does this PRD still describe the right thing to build?
```

---

## Learning Frame

- **Mental model:** A PRD is a hypothesis until users, competitors, and scope pressure-test it.
- **What can go wrong:** You defend the PRD because AI wrote it nicely.
- **What to ignore today:** Ignore code. Today is about product truth.

## What You'll Have After Today

- the same `.onemillion/prd.md`, but reviewed and improved
- validation evidence inside the PRD
- a clearer ICP: ideal customer profile
- a clearer MVP: first useful build, not the full product
- a Day 2 verdict: Keep, Refine, or Pivot

---

## Part 1: Own The PRD

Open `.onemillion/prd.md` and read it as the product owner.

Ask:

- Do I agree with the target customer?
- Do I agree with the pain point?
- Do the user stories match what I want to build?
- Are the KPIs useful?
- Are the market claims honest?
- What is missing, inflated, vague, or wrong?

Do not preserve AI-written text you do not believe. Edit it.

## Part 2: Validate The Pain

Talk to potential users or customers. If possible, show them the workflow described in the PRD.

Do not ask:

```text
Would you use this?
Do you like this?
Would you pay for this?
```

Ask:

```text
When was the last time this problem happened?
What did you do?
What tools, files, or data were involved?
What made it annoying, expensive, slow, or risky?
What would an ideal fix look like?
Here is the workflow my PRD proposes. What feels right or wrong?
What would make this useless?
```

If you cannot get live calls today, document serious outreach attempts, async replies, workflow observations, or public threads from people with the same pain.

## Part 3: Define ICP

ICP means **Ideal Customer Profile**.

Bad ICP:

```text
Teachers.
```

Better ICP:

```text
Independent K-5 teachers who write weekly parent updates from informal classroom notes and spend 30+ minutes per week turning notes into clear messages.
```

Your ICP should be specific enough that you know where to find the person.

## Part 4: Compare Alternatives

Competitors are not only startups.

They include:

- spreadsheets
- Notion docs
- email flags
- assistants
- agencies
- manual checklists
- existing SaaS tools
- doing nothing

For each alternative, ask:

- What job does it solve?
- What does it do well?
- Why is it not enough?
- What should the PRD learn from it?

## Part 5: Sanity-Check Market Size

TAM/SAM/SOM should not be treated as magic numbers.

| Term | Simple meaning |
|---|---|
| TAM | The broad market category |
| SAM | The segment this product can realistically serve |
| SOM | The first reachable group you can actually reach |

For this course, SOM matters most. If you cannot reach the first users, the PRD is still too abstract.

## Part 6: Decide MVP Versus Full Product

MVP means **Minimum Viable Product**.

It does not mean tiny, broken, ugly, or embarrassing.

It means:

```text
the smallest version that proves the core user value
```

The full product may eventually include teams, billing, analytics, integrations, mobile apps, advanced AI, admin dashboards, templates, notifications, and permissions.

The MVP should include only the first useful loop.

Ask:

- What is the smallest build that lets the target user feel the core value?
- What can be removed without killing that value?
- What is v2, not v1?
- What does the user do first?
- What data does the first version need?
- What does success look like for the initial build?

Example:

```text
Full product: teacher progress-update platform with roster import, parent portal, translation, scheduled sending, admin dashboard, analytics, and templates.

MVP: teacher pastes notes, selects students, gets draft updates, edits them, and marks them ready to send.
```

---

## What Should Be True After Day 2

- [ ] `.onemillion/prd.md` has been opened and edited.
- [ ] The PRD includes a Day 2 learner review.
- [ ] The PRD includes validation evidence or serious outreach/research attempts.
- [ ] The PRD includes ICP.
- [ ] The PRD includes competitor/workaround notes.
- [ ] The PRD includes TAM/SAM/SOM sanity notes.
- [ ] The PRD includes full product versus MVP.
- [ ] The PRD includes a Keep, Refine, or Pivot verdict.

---

## Verify Your Day 2

Ask your harness to run the OneMillion verifier for this day. It will review `.onemillion/prd.md` and decide whether it is ready for Day 3.

---

## Share It

```text
Day 2 of OneMillion done.

Today I tested whether my PRD is real.

Verdict: Keep / Refine / Pivot
ICP: [specific customer profile]
MVP: [first useful build]
Biggest learning: [one sentence]

Tomorrow: lock the validated spec.
#BuildingWith1M
```

---

→ **Next:** [Day 3 — Lock The Spec](../day-03-spec/learn.md)
