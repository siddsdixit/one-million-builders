# OneMillion Course Tech Stack & Sprint Rules

> Single source of truth for architecture decisions in the OneMillion Builder course.
> Optimized for beginner-friendly setup, low DevOps, real deployment, and agent-readable build slices.

---

## Course Default Stack

For the current OneMillion Builder course, default to:

- **App/frontend:** Next.js latest stable + TypeScript + React + MUI / Material Design 3 + Emotion
- **Design system:** Material Design 3 via MUI. Do not choose Tailwind CSS, shadcn/ui, Bootstrap, Chakra, or Ant Design as defaults.
- **Database/auth:** Supabase Postgres + Supabase Auth + Row Level Security
- **Deployment:** Vercel for the app/frontend
- **AI:** Claude from server-side code only
- **Validation/forms:** Zod + react-hook-form when useful
- **Testing:** Playwright for E2E, Vitest/React Testing Library for frontend units, Supabase/RLS behavioral checks for data boundaries
- **Monitoring:** Sentry / Vercel Analytics / uptime monitoring on production day, not mandatory in S0

## Backend Path Decision

Use the simplest backend that satisfies the PRD and security model.

### Default: Supabase + Next.js

Use Supabase + Next.js route handlers/server actions when:

- the app is CRUD, dashboards, forms, workflows, or simple AI request/response
- Supabase Auth and RLS can enforce the data boundary
- integrations are limited
- no long-running jobs are core to the MVP
- beginner setup speed matters

### Backend-Heavy Path: FastAPI + Supabase

Use FastAPI when Day 5 architecture determines the product is genuinely backend-heavy. The decision must be recorded in `.onemillion/architecture.md` with the reason, deployment target, API boundary, CORS rules, auth/session strategy, health check, and testing implications.

- complex Python logic or Python-only libraries
- long-running jobs or background processing
- heavy third-party integration orchestration
- enterprise API boundary
- advanced agent/tool orchestration
- workflows that are awkward or unsafe in route handlers alone
- high-volume server-side processing
- webhook-heavy products
- multi-step transactional workflows
- strict separation between frontend app and backend API team/boundary

If unsure, choose the default Supabase + Next.js path.

When FastAPI is selected, it is a first-class architecture path, not an exception to apologize for. The plan agent must produce FastAPI-specific sprint tasks, tests, env vars, deployment topology, CORS rules, health checks, and backend host instructions. Railway, Fly.io, Render, or another backend host may be selected when the architecture justifies it.

## Product Type Architecture

| Product type | Course default |
|---|---|
| Web app | Next.js + MUI + Supabase + Vercel |
| Mobile-first app | Responsive/PWA-style Next.js first; native mobile later unless phone-only capabilities are essential |
| Agent | Server-side agent endpoint/tool flow; persist state in Supabase if needed |
| Hybrid | Web app foundation plus server-side AI endpoints and strict permission boundaries |

## Default Vs Optional Choices

These choices are not forbidden. They are simply not the default path for this course. Use the default unless the PRD, security model, scale, integrations, or learner's product genuinely requires the optional choice.

| Do not choose by habit | Course default | When the optional choice is legitimate |
|---|---|---|
| MongoDB Atlas | Supabase Postgres | Use a document store only when the architecture explains why Postgres/RLS is a poor fit |
| Railway/Fly.io/Render/backend host by habit | No separate backend unless FastAPI is selected during architecture | Use a backend host for a FastAPI service, worker, or API boundary the product truly needs |
| Tailwind CSS | MUI / Material Design 3 | Use another UI system only if inheriting an existing codebase and the course owner accepts the tradeoff |
| shadcn/ui | MUI / Material Design 3 | Use only if the product is intentionally outside the course design system |
| JWT + Argon2 custom auth | Supabase Auth | Use custom auth only for a serious enterprise/security reason and document the extra risk |
| FastAPI for every app | Next.js route handlers/server actions | Use FastAPI when backend-heavy criteria are met |
| Redis/Celery/Kafka | Defer or use simple provider features | Use when queues, cache, streams, or background jobs are central to the MVP |

## Data Model Rules

Every architecture must decide:

- product type
- backend path
- single-user, multi-tenant, or public/community data model
- ownership fields: `owner_id`, `tenant_id`, `organization_id`, membership tables where needed
- auth model: anonymous/public, login required, invite-only, team membership, admin roles, or mixed public/private access
- RBAC model: no RBAC for MVP, simple owner/admin/member/viewer, or product-specific roles. If RBAC exists, define permissions before build.
- public vs private fields
- RLS policy intent
- indexes for tenant, owner, status, date, search/filter fields
- audit fields: `created_at`, `updated_at`, `created_by`, `updated_by`, `deleted_at` when needed

## Security Rules

- Never expose Supabase service-role keys in browser code.
- Never expose `ANTHROPIC_API_KEY` as `NEXT_PUBLIC_*`.
- Enable RLS on every user-owned or tenant-owned table.
- Server-side code must check the current user before protected reads/writes.
- AI actions operate with the invoking user's permissions.
- Add rate/cost limits to AI routes.
- Keep `.env.local` out of git; commit `.env.example` with placeholders.

## Sprint Planning Rules

Sprints are build contracts for LLMs. Each sprint must be small enough to build, review, and test in isolation.

### Required Sprint Brief Sections

Each sprint file in `.onemillion/sprints/` must include:

- Context
- Product Decisions Used
- Entity Schemas
- Supabase Tasks, when data is involved
- Server Tasks, when server actions/routes/AI/integrations are involved
- Frontend Tasks
- Design Notes
- Security Notes
- Acceptance Criteria
- Verification Gate
- Git Commit

### Standard Sprint Shape

- **S0-foundation:** Next.js + MUI app shell, env examples, Supabase utilities if needed, design baseline, seed-data path.
- **S1-auth-db:** A first-class learning/build module when the product needs login, private data, tenant data, saved user state, or admin roles. Supabase Auth, protected routes, callback handling, RLS, first tables, profile/membership shape, and second-user isolation checks.
- **S2+ feature sprints:** One vertical slice per sprint. Include UI, data/server work, acceptance criteria, and verification.
- **Final/polish sprint:** Error states, accessibility, responsive checks, deployment readiness, cleanup.

Do not create giant layer-based sprints like "backend only" then "frontend only" unless the PRD makes that unavoidable. Prefer vertical slices.

## Environment Setup

### Core Tools

| Tool | Required |
|---|---|
| Node.js 20+ | Yes |
| Git | Yes |
| GitHub CLI | Helpful for fork/repo operations |
| Vercel CLI | Helpful for deploy verification |
| Supabase CLI | Optional; dashboard/SQL editor is acceptable for learners |
| Python 3.11+ | Only required for optional FastAPI, scripts, or PDF/report generation |
| Playwright | Required for app QA |

### Manual Accounts

| Service | Introduced | Purpose |
|---|---:|---|
| GitHub | Day 0 | Course fork and proof trail |
| Vercel | Day 6 | App deployment |
| Supabase | Day 7 | Auth/database/RLS |
| Anthropic | Day 11/12 | AI feature |
| Sentry / monitoring | Day 16 | Production checks |
| Loom | Day 18 | Demo |

## Optional Services

Add only when justified by PRD/architecture:

- Vercel Blob or Cloudinary for file/image uploads
- Sentry for production errors
- UptimeRobot/Better Stack for uptime checks
- FastAPI backend host such as Railway, Fly.io, Render, or another justified provider when Day 5 architecture selects the backend-heavy path
- Vector retrieval only when app data or user task truly requires retrieval

## Guardrails For Agents

- Plan agent must read this file before writing architecture.
- Build agent must follow the selected backend path in `.onemillion/architecture.md`.
- Ship agent must not assume Railway, Fly.io, Render, or a separate backend unless architecture selected FastAPI or another explicit backend service.
- Guard agent must audit Supabase RLS and Vercel env boundaries.
- Review/test agents must verify the implemented app matches the sprint brief, not just that code exists.
