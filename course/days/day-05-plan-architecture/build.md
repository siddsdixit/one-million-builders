# Day 5 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

## Before You Start

- [ ] Day 4 is verified in `.onemillion/state.json`.
- [ ] `.onemillion/refined-prd.md` exists.
- [ ] `.onemillion/design-spec.md` exists.
- [ ] `.onemillion/design-system.md` exists.
- [ ] `.onemillion/screens/` exists.
- [ ] You have read [learn.md](./learn.md).

## Step 1: Ask The Harness To Teach Architecture

Paste this:

```text
I am on OneMillion Day 5: Plan Architecture.

Act as the `plan` agent for this day.
First teach me architecture in plain language:
- what architecture means
- why architecture comes after PRD/spec/design and before code
- how to decide frontend, backend, database, and AI boundaries
- when to build a web app, mobile-first web app, agent, or hybrid
- how to decide whether the product needs single-tenancy, multi-tenancy, and RBAC
- what RBAC means, and how owner/admin/member/viewer permissions affect architecture
- when a lightweight backend is enough
- when FastAPI or a heavier backend is justified
- how secure architecture works
- what single-tenant vs multi-tenant means
- how scalability, cost, compliance, reliability, and integrations shape architecture
- why sprint briefs are build contracts for LLMs

Then read the current pipeline artifacts and guide me one decision at a time.
Do not start coding.
Do not create external accounts.
Do not skip my human decisions.
Do not create paperwork-only files.
```

## Step 2: Review Inputs

The harness should read:

- `.onemillion/refined-prd.md`
- `.onemillion/design-spec.md`
- `.onemillion/design-system.md`
- `.onemillion/screens/`
- `.onemillion/seed-data.json`
- `.onemillion/state.json`
- the course tech stack rules

If any required artifact is missing, stop and fix the previous day before planning.

## Step 3: Make The Architecture Decisions

Before the harness writes `architecture.md`, answer these.

### Product Shape

- Is this a web app, mobile-first responsive app, agent, or hybrid?
- Who uses it most often?
- What device do they probably use first?
- Does the product need app screens, conversation, automation, or all of these?

### Frontend Boundary

- What pages exist?
- Which screens are public?
- Which screens require login?
- Which UI states from Day 4 must be implemented first?
- Which MUI components matter most: tables, cards, forms, chips, dialogs, drawers, tabs, charts, etc.?

### Backend Boundary

Choose one:

```text
Default: Supabase + Next.js route handlers/server actions
Optional: FastAPI + Supabase + selected backend host only when the product has a real backend reason
```

Use FastAPI if the PRD/design makes the product genuinely backend-heavy: complex Python logic, background jobs, heavy integrations, enterprise API boundaries, long-running workflows, webhook orchestration, high-volume server processing, or Python libraries.

If FastAPI is selected, the harness must record:

- why the default Supabase/Next.js path is not enough
- backend host/deployment target, such as Railway, Fly.io, Render, or another justified provider
- API boundary and CORS rules
- auth/session strategy between the frontend, Supabase, and backend
- health check
- server-side env vars
- test strategy
- which sprint creates the backend

### Database Boundary

- What are the main entities?
- Who owns each entity?
- Which records are public, private, or tenant-owned?
- What fields support filtering, sorting, search, and status?
- What audit fields are needed?

### Tenancy

Choose one:

- single-user ownership
- team/multi-tenant ownership
- public/community data model

If the customer is a company, school, clinic, agency, or team, strongly consider multi-tenant from the beginning.

### Security

- What requires login?
- What auth method fits the product: email/password, magic link, OAuth, invite-only, admin-created users, or team roles?
- Does the product need multi-tenancy now or soon?
- Does the product need RBAC now or soon?
- If RBAC is needed, which roles exist and what can each role do?
- What requires owner permission?
- What requires admin or manager permission?
- What data must never cross user or tenant boundaries?
- Which secrets exist?
- Which server routes call AI?
- What needs rate limits or cost limits?

### Scalability And Operations

- How many users or tenants do you expect first?
- How much data per user or tenant?
- Which tables may grow fastest?
- Will the product need search, files, scheduled jobs, webhooks, or integrations?
- What would break if 10 people used it tomorrow? What about 1,000?
- What can be deferred without making the MVP unsafe?

## Step 4: Produce The Day Output

Expected output:

- `.onemillion/architecture.md`
- `.onemillion/sprints/`

The architecture should include:

- product type
- stack
- backend path
- tenancy model
- auth model
- RBAC model
- security model
- data model
- API/server action boundaries
- AI boundary if applicable
- deployment topology
- environment variables
- module map
- data flow
- scalability and operational assumptions
- explicit deferred decisions

Each sprint brief should include:

- context
- entities and fields
- backend/server actions
- frontend pages/components
- design notes
- acceptance criteria
- verification gate
- expected commit message

The build agent should be able to read one sprint brief and know exactly what to build and how to verify it.

## Step 5: Validate The Plan

Ask the harness:

```text
Run validate-plan thinking for Day 5.
Check that the refined PRD, design spec, architecture, and sprint briefs tell one coherent story.
Find contradictions, missing security/tenancy decisions, oversized sprints, missing design notes, and features that drift from the MVP.
Fix the plan before Day 5 is marked done.
```

## Step 6: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 5.
Inspect .onemillion/architecture.md and .onemillion/sprints/.
Confirm product type, backend path, tenancy model, security model, data model, and sprint build contracts are present.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 5 complete
- **Last verified day:** Day 5
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 6.

## What Should Be True After Day 5

- [ ] `.onemillion/architecture.md` exists
- [ ] `.onemillion/sprints/` exists
- [ ] product type decision is recorded
- [ ] backend path decision is recorded
- [ ] tenancy model is recorded
- [ ] RBAC decision is recorded, even if the decision is "no RBAC for MVP"
- [ ] security model is recorded
- [ ] data model and ownership boundaries are recorded
- [ ] scalability and cost assumptions are recorded
- [ ] sprint briefs are small, self-contained build contracts
- [ ] validate-plan passes or findings are resolved

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 5: Plan Architecture.
I am stuck on this architecture decision:
[product type / backend path / tenancy / security / database / sprint sequence / other]

Here is what the PRD says:
[paste relevant part]

Here is what the design implies:
[paste relevant part]

Help me choose the simplest architecture that is secure enough, scalable enough, and buildable in small sprint briefs. Teach the concept before giving the recommendation.
```

---

-> **Next:** [Day 6 — App Shell + First Deploy](../day-06-app-shell/learn.md)
