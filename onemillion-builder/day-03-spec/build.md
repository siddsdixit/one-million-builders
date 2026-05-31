# Day 3 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Last no-code day.** Today the Spec agent turns `.onemillion/prd.md` into `.onemillion/refined-prd.md`: the engineering-ready blueprint for design, architecture, planning, and build agents.

---

## Before You Start

- [ ] Day 2 verified.
- [ ] `.onemillion/prd.md` includes Day 2 validation evidence and MVP decision.
- [ ] You are in your `my-onemillion-build` folder.

---

## Step 1: Ask The Harness To Teach Spec Lock

Paste this:

```text
I am on OneMillion Day 3.

Teach me what a buildable spec is.

Explain:
- requirement vs idea
- functional requirements
- CRUD: create, read, update, delete
- how CRUD breaks software into buildable blocks
- MVP vs post-MVP feature tags
- complete core flow: trigger -> steps -> outcome
- data schema and business rules
- assumptions vs clarifying questions
- user story vs use case
- acceptance criteria
- KPI / success signal
- out of scope
- definition of done
- why scope lock matters before code
- how the spec becomes input to design, architecture, and planning
- what the validate-spec agent checks

Then guide me one step at a time.
Use .onemillion/prd.md as the single source of truth.
Create .onemillion/refined-prd.md as the Day 3 pipeline artifact.
Do not create extra Day 3 paperwork files beyond the pipeline artifacts.
```

---

## Step 2: Create The Refined PRD

Open `.onemillion/prd.md`. Then create `.onemillion/refined-prd.md`.

Use this structure:

```markdown
# Refined PRD

Spec locked on: 2026-05-31

Source PRD: .onemillion/prd.md

## Day 3 Locked Spec

### MVP Summary
[One paragraph: the smallest useful version we are building first.]

### Feature Inventory
| Feature | Scope | Why |
|---|---|---|
| [Feature] | [MVP or POST-MVP] | [why it belongs there] |
| [Feature] | [MVP or POST-MVP] | [why it belongs there] |

### Functional Requirements
- [Observable product behavior]
- [Observable product behavior]
- [Observable product behavior]

### Core Entities And CRUD
| Entity | Create | Read | Update | Delete / Archive |
|---|---|---|---|---|
| [Entity] | [what can be added] | [what can be viewed] | [what can be changed] | [what can be removed/archived] |
| [Entity] | [what can be added] | [what can be viewed] | [what can be changed] | [what can be removed/archived] |

### Complete Core Flow
Trigger: [what starts the journey]
1. [First user action]
2. [Second user action]
3. [Third user action]
Outcome: [useful result at the end]

### Core User Stories
1. As [specific user], I want [specific action] so that [specific outcome].
2. As [specific user], I want [specific action] so that [specific outcome].
3. As [specific user], I want [specific action] so that [specific outcome].

### Use Cases
- [Real usage moment 1]
- [Real usage moment 2]
- [Optional usage moment 3]

### Acceptance Criteria
- Given [context], when [action], then [observable result].
- Given [context], when [action], then [observable result].
- Given [context], when [action], then [observable result].

### Data Schema
- [Entity]: [field: type], [field: type], [field: type]
- [Entity]: [field: type], [field: type], [field: type]

### Business Rules
- [Rule that must always be true]
- [Rule that must always be true]
- [Rule that must always be true]

### KPIs / Success Signals
- [Measurable usefulness signal]
- [Measurable usefulness signal]

### Out Of Scope For MVP
- [Tempting feature not in v1]
- [Tempting feature not in v1]
- [Tempting feature not in v1]
- [Tempting feature not in v1]
- [Tempting feature not in v1]

### Definition Of Done
[Concrete paragraph describing exactly what v1 can do when complete.]

### Assumptions
- [Decision made because the PRD was unclear, or "No unresolved assumptions."]

### Agent Build Rule
Build agents may implement only the MVP above. If a requested change conflicts with this locked spec, stop and ask before changing scope.
```

---

## Step 3: Use The Spec Agent

Ask your harness:

```text
Act as the OneMillion spec agent.

Read .onemillion/prd.md.
Create .onemillion/refined-prd.md as the Day 3 engineering requirements document.

Rules:
- exactly 3 core user stories
- functional requirements must be observable
- CRUD should identify the core MVP entities and actions
- tag each feature as MVP or POST-MVP
- include one complete core flow as Trigger -> numbered steps -> Outcome
- include simple data schema with field names and types for MVP entities
- include business rules for the MVP entities
- ask at most 2 clarifying questions; mark other decisions as Assumption
- each story must use: As [user], I want [action] so that [outcome]
- use cases must be real moments, not feature names
- acceptance criteria must be testable
- KPIs must measure usefulness, not vanity
- out of scope must include at least 5 items
- definition of done must describe the concrete v1 product state

Ask me one question at a time where my PRD is unclear.
Do not add new features beyond the Day 2 MVP decision.
When complete, update .onemillion/state.json so current_phase is spec and status is completed.
Do not paste the full refined PRD in chat; write it to file and summarize what changed.
```

---

## Step 4: Use The Validate-Spec Agent

Ask your harness:

```text
Act as the OneMillion validate-spec agent.

Review .onemillion/refined-prd.md for Day 3.
Cross-check it against .onemillion/prd.md so the refined PRD does not drift from the original validated vision.

Check:
- Is the MVP small enough?
- Does the spec list functional requirements?
- Does the spec identify core entities and CRUD actions?
- Are features tagged MVP or POST-MVP?
- Is there a complete core flow from trigger to outcome?
- Are data schema and business rules present?
- Are assumptions explicit where the PRD was unclear?
- Are there exactly 3 core user stories?
- Are the use cases real scenarios?
- Are acceptance criteria testable?
- Are KPIs measurable?
- Is out of scope strong enough?
- Is Definition of Done concrete?
- Would a build agent know what to build next without guessing?

If it is weak, give me the smallest edits needed.
If it is strong, say it is ready to lock.
Record the validation result in .onemillion/state.json.
```

Inspect the spec. If something looks wrong, too large, or forgotten, move it into or out of MVP, rerun the Spec agent, and then rerun Validate-Spec. Make the final edits in `.onemillion/refined-prd.md`.

---

## Step 5: Read It Aloud

Read `.onemillion/refined-prd.md` aloud.

If any sentence sounds like:

```text
make it easy
manage everything
support all users
smart dashboard
AI-powered workflow
```

rewrite it into observable behavior.

---

## Step 6: Commit The Spec Lock

From `my-onemillion-build`:

```bash
git add .onemillion/prd.md .onemillion/refined-prd.md .onemillion/state.json
git commit -m "Day 3: lock MVP spec"
```

If git is not initialized yet:

```bash
git init
git add .onemillion/prd.md .onemillion/refined-prd.md .onemillion/state.json
git commit -m "Day 3: lock MVP spec"
```

---

## Step 7: Run Day 3 Verification

Ask your harness:

```text
Run the OneMillion verifier for Day 3.

Review .onemillion/prd.md, .onemillion/refined-prd.md, and .onemillion/state.json.
Do not create extra course verifier markdown files.
Record the result in .onemillion/state.json.
```

---

## What Should Be True After Day 3

- [ ] `.onemillion/refined-prd.md` exists.
- [ ] `.onemillion/refined-prd.md` includes `## Day 3 Locked Spec`.
- [ ] Features are tagged MVP or POST-MVP.
- [ ] Functional requirements are listed.
- [ ] Core MVP entities and CRUD actions are listed.
- [ ] Complete core flow is listed.
- [ ] Data schema and business rules are listed.
- [ ] The locked spec has exactly 3 core user stories.
- [ ] Each user story uses the correct format.
- [ ] Use cases are real scenarios.
- [ ] Acceptance criteria are testable.
- [ ] KPIs are measurable.
- [ ] Out of scope has at least 5 items.
- [ ] Definition of Done is concrete.
- [ ] Spec lock is committed to git.
- [ ] Verification passed.

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 3 complete
- **Last verified day:** Day 3
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 4.

## If You Are Stuck

Open your coding harness from your project folder and paste this:

```text
I am on OneMillion Day 03.

Here is the spec section I am stuck on:
[paste section]

Here is what feels unclear:
[describe issue]

Help me make the smallest edit that turns this into a buildable spec.
Do not create extra files.
Keep .onemillion/prd.md as the validated product input and .onemillion/refined-prd.md as the Day 3 engineering spec.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| I have more than 3 stories | Pick the 3 required for the first useful loop. Move everything else to Out of Scope. |
| My use cases sound like features | Rewrite them as real moments from the user's day. |
| Acceptance criteria feel hard | Use: Given [context], when [action], then [result]. |
| KPIs are vague | Measure time saved, task completion, accepted output, repeat usage, or reduced manual work. |
| I want to pivot again | Only pivot if Day 2 evidence forced it. Otherwise lock and build. |

---

→ **Done with Day 3?** Move to [Day 4 — Stack + First Deploy](../day-04-first-deploy/learn.md).
