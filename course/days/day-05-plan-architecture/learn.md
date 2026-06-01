# Day 5 — Plan Architecture

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `plan`
**Supporting agents:** `validate-plan`

Day 5 is one of the most important days in the course. You have a refined PRD and a product design. Today you decide how the system should be built.

Architecture is not a diagram for show. Architecture is the set of technical decisions that make the product possible, secure, maintainable, scalable enough, and buildable in small verified steps.

## Learning Frame

- **Mental model:** architecture is the bridge between product intent and working code.
- **Input:** `.onemillion/refined-prd.md`, `.onemillion/design-spec.md`, `.onemillion/design-system.md`, `.onemillion/screens/`, `.onemillion/seed-data.json`.
- **Output:** `.onemillion/architecture.md` and `.onemillion/sprints/`.
- **What can go wrong:** the harness jumps into coding, over-engineers the backend, ignores tenant/security boundaries, or writes vague sprint briefs that are too large for an LLM to build and test safely.
- **What to ignore today:** do not create accounts, deploy, or write product code. Day 5 is a planning gate.

## What Architecture Means

Architecture answers these questions:

- What type of product are we building: web app, mobile app, agent, or hybrid?
- What runs in the browser?
- What runs on the server?
- What lives in the database?
- How do users authenticate?
- Who can see or change which data?
- What happens when the product has more users, more data, more integrations, or more AI calls?
- What is simple enough to build now but not careless?
- How do we break the work into small build contracts?

Good architecture is not the most complex architecture. Good architecture is the simplest structure that can satisfy the product requirements, security needs, expected scale, and learning goal.

## Product Type Decisions

Day 5 should revisit the product type from Day 1 and Day 3.

| Product type | Use when | Architecture shape |
|---|---|---|
| **Web app** | Users need screens, forms, dashboards, CRUD, collaboration, or workflow tracking | Next.js + MUI frontend, Supabase auth/database, Vercel deploy |
| **Mobile app** | The core use happens on a phone, with camera, location, push, offline, or daily habit usage | Usually start as responsive web/PWA in this course; native mobile can be a later path |
| **AI agent** | The product is mostly a conversation, automation, tool runner, or assistant workflow | Agent interface, tool permissions, memory/data boundaries, server-side AI calls |
| **Hybrid** | Users need both app screens and AI help inside the workflow | Web app foundation plus AI endpoints, review boundaries, and safe tool/data access |

For this course, the default build target is a responsive web app or hybrid product. A native mobile app is usually not the first build unless the PRD proves phone-only capabilities are essential.

## Frontend, Backend, And Database

Architecture decides boundaries.

### Frontend

The frontend is what users see and touch:

- pages and routes
- app shell and navigation
- forms and validation
- dashboards, tables, cards, charts
- loading, empty, error, partial, full, and success states
- client-side interactions and optimistic updates

In this course, frontend means **Next.js + React + MUI / Material Design 3**.

### Database

The database stores product truth:

- users
- tenant or organization records
- product entities
- ownership fields
- audit fields
- status/history
- AI outputs that need to be saved

In this course, database means **Supabase Postgres** with **Row Level Security** for user and tenant boundaries.

### Backend

The backend enforces rules that should not live only in the browser:

- authentication/session checks
- authorization
- writes to the database
- server-side AI calls
- secret handling
- integrations and webhooks
- background jobs
- rate limiting and cost protection

In this course, the default backend path is **Supabase + Next.js route handlers/server actions**. Add **FastAPI + Supabase** only when there is a real reason, and then choose a backend host such as Railway, Fly.io, Render, or another provider the architecture can defend.

## Lightweight Backend Vs Heavy Backend

Use a lightweight backend when:

- the product is mostly CRUD, forms, dashboards, and simple workflows
- Supabase auth/database/RLS cover the core security model
- server-side AI calls are simple request/response
- no long-running jobs are needed
- integrations are limited
- the MVP should ship quickly

Use a heavier backend such as FastAPI when the architecture stage determines the product is genuinely backend-heavy:

- Python libraries are essential
- workflows are long-running or asynchronous
- background jobs, queues, or scheduled processing are central
- multiple third-party integrations need orchestration
- enterprise API boundaries are needed
- complex permissions or approval workflows are hard to express with simple route handlers
- the AI system needs deeper tool orchestration
- the product is webhook-heavy
- the product needs a clean public/internal API boundary
- the backend has enough independent complexity that separating it reduces risk

If unsure, choose the lightweight path. But if the PRD truly needs a backend-heavy system, choose FastAPI confidently and make it explicit in the architecture, sprint briefs, tests, backend hosting choice, and deployment plan.

## Secure Architecture

Security is not something to add at the end. Day 5 must decide the security model before coding.

Teach the learner to ask:

- What data is public?
- What data is private to one user?
- What data belongs to an organization or tenant?
- Which actions require login?
- Which auth method fits the learner's product: email/password, magic link, OAuth, invite-only, admin-created users, or team roles?
- Does the product need multi-tenancy now or soon?
- Does the product need RBAC now or soon?
- If RBAC is needed, which roles exist: owner, admin, member, viewer, approver, manager, or product-specific roles?
- Which actions require ownership?
- Which actions require admin/manager roles?
- What secrets exist, and where are they stored?
- Could a user access another user's data by changing an ID?
- Could AI reveal private data or act outside the user's permissions?
- What needs rate limits or cost limits?

For this course:

- Never expose service-role keys in the browser.
- Never expose `ANTHROPIC_API_KEY` as `NEXT_PUBLIC_*`.
- Use Supabase Row Level Security for user-owned or tenant-owned tables.
- Server-side routes must verify the current user before reading/writing protected data.
- AI actions must run with the invoking user's permissions.

## Single-Tenant Vs Multi-Tenant

This decision should happen from the beginning.

| Model | Meaning | Use when |
|---|---|---|
| **Single-user / single-tenant** | Each user owns only their own data | Personal tools, solo workflows, simple MVPs |
| **Team / multi-tenant** | Many users belong to one organization/workspace/tenant | SaaS, schools, clinics, agencies, teams, B2B workflows |
| **Public marketplace/community** | Some data is public, some is private | Directories, communities, marketplaces, social products |

If the real buyer or user is a team, school, business, clinic, agency, or customer account, plan tenant boundaries from Day 5. Retrofitting tenancy later is painful.

Common tenant fields:

- `owner_id` for single-user ownership
- `tenant_id` or `organization_id` for team ownership
- `role` or membership table for admin/member/viewer permissions
- `created_by`, `updated_by`, `created_at`, `updated_at`

## RBAC Decision

RBAC means **Role-Based Access Control**. It answers: what can each role do?

Day 5 should explicitly ask whether the product needs RBAC. If the answer is no, record why simple owner-based access is enough for the MVP. If the answer is yes, define the initial roles and permissions before Day 7 builds auth/database.

Common roles:

| Role | Typical permissions |
|---|---|
| Owner | billing, workspace settings, delete workspace, invite admins |
| Admin | invite members, manage records, change operational settings |
| Member | create and update assigned work |
| Viewer | read permitted records only |

RBAC affects tables, RLS policies, routes, UI controls, tests, and future support. Do not let the build agent invent roles during implementation.

## Scalability

Scalability does not mean building for millions of users on Day 5. It means avoiding decisions that obviously break the first time the product works.

Consider:

- expected users in the first month
- expected records per user or tenant
- largest table
- search/filter needs
- file/image storage needs
- AI request volume and cost
- background processing
- latency expectations
- audit/history requirements
- backup/export needs

The right question is not "Can this scale to a million users?" The right question is "What scale do we reasonably expect, and what simple architecture handles that without blocking the MVP?"

## Other Architecture Drivers

Also consider:

- **Compliance:** health, finance, children, education, employment, or regulated data.
- **Privacy:** PII, sensitive notes, user-generated content, deletion/export needs.
- **Reliability:** what must never be lost, duplicated, or sent twice.
- **Observability:** logs, errors, analytics, and audit trail.
- **Cost:** AI calls, database usage, file storage, and background jobs.
- **Performance:** dashboard load time, table filtering, AI response time.
- **Data import/export:** CSV, integrations, APIs, webhooks.
- **Admin operations:** moderation, support access, tenant management.
- **Future product path:** what should be easy to add later without overbuilding now.

## Sprint Briefs As Build Contracts

The second major output of Day 5 is sprint briefs.

A sprint brief is a small contract for the build agent. It says:

- what this slice builds
- which entities and fields are involved
- which routes/pages/components are needed
- which backend/server actions are needed
- which design notes apply
- which acceptance criteria must pass
- exactly how to verify the slice

Breaking the build into smaller sprints matters because:

- LLMs work better with smaller context.
- Each sprint has a clear goal.
- Bugs are easier to locate.
- Testing is easier.
- The learner can review progress instead of trusting one giant build.
- The build agent can read one self-contained brief instead of juggling every course artifact.
- The review/test agents can verify one slice at a time.

Day 5 is where you turn a product into a build sequence.

## What Else You Should Learn Today

Day 5 should also teach:

- architecture is a set of tradeoffs, not one "correct" diagram
- every architecture decision should trace back to PRD, design, security, scale, or cost
- defaults are powerful: use the course stack unless the product gives a reason not to
- backend complexity should be earned, not assumed
- tenant boundaries and permissions are product decisions, not just database details
- sprints should be thin vertical slices, not giant layers
- validation matters before build: `validate-plan` checks that PRD, design, architecture, and sprints tell one coherent story

## What You Produce

- `.onemillion/architecture.md`
- `.onemillion/sprints/S0-foundation.md`
- `.onemillion/sprints/S1-auth-db.md` when auth/database is part of the MVP. Auth is a first-class module: login, logout, session state, protected routes, redirect URLs, profile/team membership shape, RLS, and second-user isolation.
- `.onemillion/sprints/S2-...md` and beyond for core product slices
- `.onemillion/assets/architecture.pdf` when PDF generation is available

## Human Decisions

- product type: web app, mobile-first responsive app, agent, or hybrid
- backend path: Supabase-only or FastAPI + Supabase
- tenancy model: single-user, team/multi-tenant, or public/community
- auth model: public/anonymous, login required, invite-only, team roles, admin roles, or mixed public/private access
- RBAC model: no RBAC, simple owner/admin/member/viewer, or product-specific roles
- data model and ownership fields
- security and permission boundaries
- AI/server-side boundary
- expected scale and cost assumptions
- sprint sequence and MVP technical scope
- what to defer until after MVP

## Done Checklist

- [ ] `.onemillion/architecture.md` exists
- [ ] `.onemillion/sprints/` exists
- [ ] backend path decision is recorded
- [ ] product type decision is recorded
- [ ] tenancy model is recorded
- [ ] security model is recorded
- [ ] data model and ownership boundaries are recorded
- [ ] sprint briefs are small, self-contained build contracts
- [ ] validate-plan passes or findings are resolved

## Verify Your Day 5

When the checklist is true, ask your harness to run the OneMillion verifier for Day 5. The verifier should inspect the architecture, sprint briefs, security/tenancy decisions, and validate-plan outcome. There is no deployment gate today.

---

-> **Next:** [Day 6 — App Shell + First Deploy](../day-06-app-shell/learn.md)
