# Day 3 — Lock The Spec

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 1-6 | ~60-90 min | Last no-code day before building**

Day 1 created the first PRD. Day 2 validated it. Day 3 turns it into a buildable spec.

Today moves the pipeline from the Day 1/2 PRD into the Day 3 engineering spec:

```text
.onemillion/prd.md          -> input PRD
.onemillion/refined-prd.md  -> output engineering requirements
```

Today answers:

```text
Can an agent read this PRD, understand the functional building blocks, and prepare design, architecture, and plan without guessing?
```

---

## Learning Frame

- **Mental model:** A spec is a detailed blueprint between the PRD and the build plan.
- **What can go wrong:** You leave fuzzy requirements, so the build agent fills gaps with guesses.
- **What to ignore today:** Ignore UI polish, provider setup, Vercel, Supabase, and AI APIs. Today is about functional requirements and scope, not implementation polish.

## What You'll Have After Today

- `.onemillion/refined-prd.md` created as the locked Day 3 engineering requirements document
- functional requirements broken into buildable blocks
- CRUD actions for the core entities
- MVP and post-MVP features tagged clearly
- one complete core flow from trigger to outcome
- data schema and business rules for the MVP entities
- exactly 3 core user stories
- 2-3 real use cases
- acceptance criteria for the MVP
- measurable KPIs or success signals
- a clear out-of-scope list
- a concrete definition of done
- an explicit spec-lock note saying what agents may and may not build

---

## Part 1: What Is A Spec?

A PRD explains the product. A spec makes the product buildable.

The spec is the detailed blueprint that lets the next agents do their jobs:

- **Design agent:** what screens, states, and flows are needed?
- **Plan agent:** what architecture, data model, and sequence are needed?
- **Build agent:** what functional blocks must be implemented?
- **Review/test agents:** what behavior should be checked?

A good spec tells the build agent:

- who the product is for
- what pain it solves
- what evidence supports it
- what the MVP includes
- what the MVP does not include
- what the user must be able to do
- what data or entities exist
- what the user can create, read, update, and delete
- what counts as correct behavior
- what counts as done

Bad prompt:

```text
Build my app.
```

Better prompt:

```text
Build the MVP described in .onemillion/refined-prd.md. Do not add features outside the 3 locked user stories. If the spec is ambiguous, stop and ask.
```

This is the point of OneMillion: the learner uses agents, but the learner controls the spec.

## Part 2: Functional Requirements

A functional requirement is a behavior the product must support.

Weak requirement:

```text
The app should be easy to use.
```

Buildable requirement:

```text
The teacher can paste classroom notes, select a student, generate a parent-update draft, edit the draft, and mark it ready to send.
```

Requirements should be:

- observable
- specific
- small enough to build
- connected to the validated pain
- limited to the MVP

## Part 3: CRUD

CRUD means:

| Letter | Meaning | Simple question |
|---|---|---|
| C | Create | What can the user add? |
| R | Read | What can the user view or retrieve? |
| U | Update | What can the user edit or change? |
| D | Delete | What can the user remove or archive? |

Most software products are built from these actions.

Example for a parent-update tool:

| Entity | Create | Read | Update | Delete / Archive |
|---|---|---|---|---|
| Student | add student | view student list | edit student name/context | archive student |
| Note | paste note | view notes by student | edit note | delete note |
| Draft | generate draft | view saved drafts | edit draft | archive draft |

CRUD helps the learner break an idea into functional building blocks. It also helps the plan agent design the data model and the build agent implement the first slices.

Not every MVP needs all four actions for every entity. The spec should say what is required now and what waits.

## Part 4: What The Spec Agent Adds

The OneMillion Spec agent does more than rewrite your PRD. It turns the PRD into an engineering handoff.

Inside the agent, this means:

- **Extract every feature:** explicit ideas and implied features both get captured.
- **Tag scope:** each feature becomes `[MVP]` or `[POST-MVP]`. Post-MVP means later, not deleted.
- **Run the CRUD chain:** every entity gets the operations it needs.
- **Write the complete core flow:** Trigger -> numbered steps -> outcome.
- **Add acceptance criteria:** important behavior becomes `Given / When / Then`.
- **Add data schema:** important entities get fields and types.
- **Add business rules:** constraints and permissions are made explicit.
- **Resolve ambiguity:** the agent may ask up to 2 high-value questions; everything else becomes an explicit assumption.

The philosophy is simple:

```text
Questions are investments in correctness.
Ambiguity is cheap to fix before code and expensive to fix after code.
The spec records decisions, not ongoing deliberation.
```

## Part 5: Entity Types

The Spec agent thinks about different entities differently. A student note is not the same as a payment record.

| Entity type | Normal operations | Why it matters |
|---|---|---|
| User-generated content | create, read, update, delete/archive, list | Users usually control their own content. |
| Financial records | create, read, list, audit | Editing/deleting money records can break trust. |
| Communication | create, read, update, list, history kept | Messages often need history instead of hard delete. |
| Configuration | create, read, update, delete, reset default | Settings need recovery paths. |
| System data | read, list, export | System-generated data is usually not manually edited. |

You do not need to memorize this table. You need to know why the Spec agent asks: "What kind of thing is this entity, and what should users be allowed to do with it?"

## Part 6: Scope Budget

If the builder chooses MVP scope, the Spec agent enforces a small scope budget:

```text
max MVP user stories = floor(build_timeline_weeks x 2)
```

In this course, Day 3 is stricter: exactly 3 core user stories.

That constraint is intentional. It makes the first build small enough to finish and real enough to learn from.

## Part 7: User Stories

User stories describe what the user wants to do and why.

Format:

```text
As [specific user], I want [specific action] so that [specific outcome].
```

Day 3 requires exactly 3 user stories.

Not 5. Not 12. Exactly 3.

Why? Because the next days need a small build target. Too many stories make the build random.

Good:

```text
As a K-5 teacher, I want to paste rough classroom notes so that I can start from what I already capture during the week.
```

Weak:

```text
As a user, I want to manage everything so that my life is easier.
```

## Part 8: Complete Core Flow

The complete core flow is the main journey through the product.

Use this format:

```text
Trigger: [what starts the user journey]
1. [first action]
2. [second action]
3. [third action]
Outcome: [what useful result exists at the end]
```

Example:

```text
Trigger: Friday afternoon, the teacher needs parent updates before leaving school.
1. The teacher opens the app and selects the class.
2. The teacher pastes rough notes from the week.
3. The teacher selects a student and generates a draft.
4. The teacher edits the draft and saves it as ready.
Outcome: A usable parent-update draft exists for the selected student.
```

This flow is important because design, planning, build, review, and testing agents all need the same mental map.

## Part 9: Use Cases

Use cases are real moments from the user's life.

They answer:

```text
When does the user use this product?
What happens before, during, and after?
```

Example:

```text
Weekly parent update: On Friday afternoon, the teacher pastes rough notes from the week, selects three students, generates draft updates, edits tone, and marks each update ready to send.
```

Use cases stop the spec from becoming abstract.

## Part 10: Acceptance Criteria

Acceptance criteria define what must be true for a feature to count as working.

Example:

```text
Given a teacher has pasted notes and selected a student,
When they click Generate Draft,
Then the app creates a parent-update draft that references that student's notes and can be edited before sending.
```

You do not need a large test suite today. You need the spec to contain testable behavior.

## Part 11: Data Schema And Business Rules

A data schema says what information the app stores.

Example:

```text
Student: id, name, grade, guardian_contact, created_at
Note: id, student_id, note_text, week_of, created_at
Draft: id, student_id, draft_text, status, updated_at
```

Business rules say what must always be true.

Examples:

- A draft must belong to one student.
- A teacher can edit a draft before it is marked ready.
- Archived students do not appear in the default student list.
- The app must not send messages automatically in the MVP.

You are not designing the database perfectly today. You are giving the next agents enough structure to avoid guessing.

## Part 12: KPIs

KPIs are not vanity metrics. They should measure whether the product solves the pain.

Weak KPI:

```text
Get many users.
```

Better KPI:

```text
A teacher creates 3 usable parent-update drafts in under 10 minutes.
```

Good early KPIs usually measure:

- time saved
- successful task completion
- draft acceptance
- repeat usage
- reduced manual work

## Part 13: Out Of Scope

Out of scope is where good builders win.

Every tempting feature that is not part of the MVP goes here.

Examples:

- mobile app
- billing
- team accounts
- admin dashboard
- automated sending
- integrations
- analytics
- advanced permissions

If an agent tries to add these during the build, the spec says no.

## Part 14: Definition Of Done

Definition of Done is the exact state where v1 counts as complete.

Example:

```text
A teacher can sign up, paste classroom notes, select a student, generate a draft parent update, edit it, save it, and view saved drafts later. No automatic sending. No parent portal. No roster import.
```

If this sentence is vague, the build will drift.

---

## What Should Be True After Day 3

- [ ] `.onemillion/refined-prd.md` exists.
- [ ] The refined PRD includes `Day 3 Locked Spec`.
- [ ] The refined PRD includes functional requirements.
- [ ] The refined PRD includes CRUD actions for the core MVP entities.
- [ ] The refined PRD tags features as MVP or post-MVP.
- [ ] The refined PRD includes one complete core flow.
- [ ] The refined PRD includes a simple data schema and business rules.
- [ ] The MVP has exactly 3 core user stories.
- [ ] Each user story uses the format `As [user], I want [action] so that [outcome]`.
- [ ] The refined PRD has at least 2 real use cases.
- [ ] The refined PRD has acceptance criteria for the MVP.
- [ ] The refined PRD has 2+ measurable KPIs or success signals.
- [ ] The refined PRD has 5+ out-of-scope items.
- [ ] The refined PRD has a concrete Definition of Done.
- [ ] The learner has committed the spec lock to git.

---

## Verify Your Day 3

Ask your harness to run the OneMillion verifier for Day 3. It should review `.onemillion/prd.md`, `.onemillion/refined-prd.md`, and `.onemillion/state.json`.

---

## Share It

```text
Day 3 of OneMillion done.

Spec locked.

MVP: [one sentence]
3 core stories: [short summary]
Out of scope: [biggest thing I cut]

Tomorrow: first app + first deploy.
#BuildingWith1M
```

---

→ **Next:** [Day 4 — Stack + First Deploy](../day-04-first-deploy/learn.md)
