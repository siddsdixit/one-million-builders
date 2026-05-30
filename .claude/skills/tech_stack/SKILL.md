# OneMillion Locked Tech Stack & Sprint Rules

> This file is the single source of truth for architecture decisions on this platform.
> These are NOT preferences. They are optimized for zero DevOps overhead in a 2.5-week build.
> Any mode writing or reviewing architecture must read this file first.

---

## Clarification: Infrastructure Services vs Integration SDKs

Before applying any rules below, understand this distinction:

**Infrastructure services** (things you operate and manage):

- Vercel (frontend hosting)
- Railway or Fly.io (backend hosting)
- MongoDB Atlas (database)

**Integration SDKs** (things you call via API — not infrastructure):

- Stripe, SendGrid, Anthropic, Sentry, Cloudinary, Vercel Blob
- These are installed as packages. They add zero ops overhead.
- They are NOT counted in the 3-Service Rule.

This distinction matters. The 3-Service Rule governs infrastructure only.
Stripe is not infrastructure. Sentry is not infrastructure. They are SDK calls.

---

## 3-Service Rule (MANDATORY for all MVP plans)

A 2.5-week MVP uses exactly **3 infrastructure services**:

1. Frontend host → Vercel
2. Backend host → Railway or Fly.io
3. Database → MongoDB Atlas

Count your infrastructure services. If you have more than 3, remove the extras.
Integration SDKs (Stripe, SendGrid, Sentry, Anthropic, Cloudinary) do not count.

---

## Banned Technologies

Before writing any architecture document, scan your draft for these banned
technologies and replace them. Never present architecture containing these.

| Banned                               | Replace With              | Reason                                                                            |
| ------------------------------------ | ------------------------- | --------------------------------------------------------------------------------- |
| PostgreSQL / MySQL / SQLite          | MongoDB Atlas             | Zero migrations, no DevOps. Exception: see MongoDB section below.                 |
| Redis / Memcached                    | FastAPI BackgroundTasks   | Not needed for MVP. See Async section below.                                      |
| Kubernetes / Docker Compose / ECS    | Railway or Fly.io         | Push-to-deploy, zero infra setup                                                  |
| AWS / Azure / GCP (backend hosting)  | Railway or Fly.io         | Same                                                                              |
| S3 / MinIO (self-managed storage)    | Cloudinary or Vercel Blob | See File Storage section below                                                    |
| ELK / Prometheus / Grafana / Datadog | Sentry (free tier)        | See Error Tracking section below                                                  |
| RabbitMQ / Kafka / Redis Streams     | FastAPI BackgroundTasks   | See Async section below                                                           |
| WebSockets                           | REST polling or SSE       | Simpler for MVP. Use SSE via FastAPI StreamingResponse if PRD requires real-time. |
| Tailwind CSS                         | MUI (Material UI v6+)     | M3 design system via MUI. No utility classes needed — MUI handles theming, responsive, components. |
| shadcn/ui                            | MUI (Material UI v6+)     | MUI implements M3 natively. shadcn requires manual styling for every component.   |
| Chakra UI / Ant Design / Bootstrap   | MUI (Material UI v6+)     | MUI is the standard M3 implementation for React.                                  |

---

## Phase 1: Architecture & Stack Selection

### Web App Stack (LOCKED)

- **Frontend:** Next.js (latest stable) + TypeScript + MUI (Material UI v6+, implements Material Design 3) + Emotion (CSS-in-JS, comes with MUI) + TanStack Query (React Query) + react-hook-form + Zod
- **Design System:** Material Design 3 via MUI — NO Tailwind CSS, NO shadcn/ui. MUI provides all components, theming, and responsive utilities. See `material3` skill for token reference.
- **Backend:** Python 3.13 + FastAPI + Pydantic v2 + Motor (async MongoDB driver)
- **Database:** MongoDB Atlas (Free Tier)
- **Auth:** JWT + Argon2 password hashing — no OAuth providers in MVP
- **Error Tracking:** Sentry (free tier) — add to frontend and backend in Sprint S0
- **Testing:** pytest + httpx (backend), Playwright + @axe-core/playwright (frontend E2E + accessibility), Vitest + React Testing Library (frontend unit/component)
- **CI/CD:** GitHub Actions — add lint + test workflow in Sprint S0
- **Deployment:** Frontend → Vercel | Backend → Railway or Fly.io | DB → MongoDB Atlas

### Agent Stack

- **LLM Provider:** Use the best available model for the task (e.g., Claude, GPT, Gemini). Choose based on quality, cost, and latency for the specific use case.
- **Agent Framework:** Choose exactly one based on complexity:
    - Single tool use or simple flows → LLM provider SDK directly (no framework overhead)
    - Single agent, stateful workflow with loops or conditional branching → LangGraph
    - Multiple specialized agents collaborating on a task → CrewAI
    - External service integration via MCP → MCP SDK (Python or TypeScript)
- **Vector Search:** MongoDB Atlas Vector Search — use when PRD requires semantic
  search, RAG, or persistent agent memory. Runs on the same Atlas cluster.
  Does not add a fourth infrastructure service.
- **Backend:** Python 3.13 + FastAPI
- **Database:** MongoDB Atlas (for conversation logs, memory, agent state)
- **Error Tracking:** Sentry (free tier)
- **Testing:** pytest + httpx (backend)
- **CI/CD:** GitHub Actions
- **Deployment:** Railway or Fly.io

### Hybrid Stack

Next.js frontend + FastAPI backend with agent endpoint at `/api/v1/chat`.
All web app stack rules apply. Agent runs as a FastAPI route in the same backend.
Deploy together: Vercel (frontend) + Railway (backend with embedded agent).

---

## Architecture Patterns

1. **Web App** — Modular Monolith. Frontend calls backend API. Backend owns
   business logic and DB. Default for all web_app products.
2. **Single Agent + Tools** — FastAPI + LLM API directly. Agent is a single
   Python class with tool definitions. No framework unless workflow complexity
   requires it.
3. **Agent + MCP Server** — Agent connects to MCP servers for external
   capabilities. Use MCP SDK.
4. **Hybrid: Web App + Embedded Agent** — Web app UI with `/api/v1/chat`
   endpoint in the FastAPI backend.

---

## MongoDB — Default Database

MongoDB over PostgreSQL for every standard MVP. Reasons:

- No migration files. No schema evolution overhead.
- Flexible document model ships faster.
- Even relational-feeling data works fine at MVP scale.
- Zero DevOps setup with Atlas Free Tier.

**If you feel the urge to use PostgreSQL because "the data is relational" — use MongoDB.**

**Exception — use PostgreSQL on Railway only when ALL of these are true:**

1. The PRD involves financial ledger data (double-entry bookkeeping, payment
   reconciliation, audit trails requiring strict balance integrity)
2. Multi-document ACID transactions are required by the business logic
3. The builder explicitly understands this adds schema migration overhead

This exception is narrow. A standard payments feature (Stripe charges, order
totals, subscription billing) does NOT qualify — Stripe handles the financial
integrity, MongoDB stores the records. Only use this exception for products
where the application itself is the financial ledger.

When the exception is used: state it explicitly in the architecture doc with
a one-line justification.

---

## File Storage

**Default:** Remove file storage from MVP scope unless the PRD core flow
requires uploads (e.g., document management tool, image sharing app,
resume parser, file processing agent). Do not add it speculatively.

**When file uploads are required by the core flow:**

- Images and media → Cloudinary (free tier, 25GB storage, transformation API)
- General file uploads → Vercel Blob (free tier, simple REST API)
- Both integrate as SDK calls — zero infrastructure to operate
- Neither counts toward the 3-Service Rule

**Never use:** S3, MinIO, or any self-managed storage in MVP.

---

## Async Processing

**Default:** FastAPI BackgroundTasks for all async work in MVP.
Covers: email sending, webhook processing, PDF generation, notification
dispatch, post-request data enrichment.

Usage pattern:

```python
@router.post("/endpoint")
async def handler(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, recipient, content)
    return {"status": "ok"}
```

**Escalate to Celery (Full Product only) when ALL are true:**

1. Tasks regularly exceed 30 seconds
2. Retry logic with backoff is required
3. Task queuing and monitoring are explicitly needed

**Never use in MVP:** RabbitMQ, Kafka, Redis Streams, Celery.

---

## Error Tracking

**Standard:** Sentry free tier in every project. Add to both frontend and
backend in Sprint S0. This is not a monitoring stack — it is a 2-line SDK
install per service. It does not count toward the 3-Service Rule.

Backend (FastAPI):

```python
import sentry_sdk
sentry_sdk.init(dsn=settings.SENTRY_DSN)
```

Frontend (Next.js): `npx @sentry/wizard@latest -i nextjs`

**Never use:** ELK Stack, Prometheus, Grafana, Datadog. Railway and Vercel
provide built-in logs. Sentry catches runtime errors. That is sufficient
for MVP.

---

## CI/CD

**Standard:** GitHub Actions in every project. Add in Sprint S0.

Minimum workflow for MVP:

```yaml
name: CI
on: [push]
jobs:
    test:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4
            - name: Run backend lint
              run: cd backend && pip install ruff && ruff check .
            - name: Run frontend lint
              run: cd frontend && npm ci && npm run lint
```

Vercel and Railway auto-deploy on push to main — no additional deploy
step required in the workflow for MVP.

**Full Product:** Add test suite runs, coverage checks, staging environment
deploy step, and PR preview deployments via Vercel.

---

## Security Tooling (Guard Mode)

> These tools are required by Guard mode for enterprise-grade security scanning.
> Plan mode's S0 sprint MUST install them during project setup so Guard doesn't waste turns installing.

### Required Tools (install in S0 pre-flight)

**Python security tools** — add to backend dev requirements:
```
pip install trufflehog3 pip-audit bandit semgrep
```

**System-level tools** (install via package manager or pip):
- `trufflehog3` — secret scanning across git history and working directory
- `pip-audit` — Python dependency vulnerability scanning (CVE database)
- `bandit` — Python SAST (static application security testing)
- `semgrep` — multi-language SAST with OWASP rulesets

**Frontend security tools** — already built-in:
- `npm audit` — Node.js dependency vulnerability scanning (built into npm)

**Optional deep scan tools** (install only if builder requests):
- `trivy` — cross-ecosystem vulnerability scanner (requires separate install: `brew install trivy` or `curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh`)
- `safety` — alternative Python dependency checker

### S0 Integration

Add to the S0 Foundation sprint's pre-flight tasks:
```bash
# Backend security tools (add to requirements-dev.txt)
pip install trufflehog3 pip-audit bandit semgrep

# Verify installation
trufflehog3 --version
pip-audit --version
bandit --version
semgrep --version
```

Guard mode will assume these tools are available. If any tool is missing at Guard time, Guard should install it on the fly — but S0 pre-install avoids wasting Guard's token budget on installation.

---

## Phase 2: Module Architecture

### Web App Backend Structure

```
backend/
  routers/       # FastAPI route handlers (one file per domain)
  models/        # Pydantic models + MongoDB document schemas
  services/      # Business logic (no DB calls here)
  repositories/  # All DB operations via Motor async
  middleware/    # Auth, rate limiting, error handling
  config/        # Settings, env vars via pydantic-settings
```

### Agent Structure

```
agent/
  agents/        # Agent class definitions
  tools/         # Tool function implementations
  prompts/       # System prompts versioned as v{n}_system.md
  mcp/           # MCP server/client connections
  middleware/    # Cost controls, logging, guardrails
```

**Module Contract Standard (required for every module):**
Every module in the architecture document must include:

- Responsibilities: what this module owns (2-4 bullets)
- Public Interface: functions or endpoints it exposes to other modules
- Pattern: Repository Pattern for data access. Service Layer for business logic.
  Routes never contain business logic.

---

## Environment Setup (orchestrator reads this section)

The orchestrator's pre-flight checks this section and installs/verifies everything before any agent runs. Items marked `[auto]` are installed automatically. Items marked `[manual]` require builder action (account creation, API keys).

### Core Runtime
| Tool | Check | Install | Required By |
|------|-------|---------|-------------|
| Node.js 20+ | `node -v` | [manual] Install via nvm: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh \| bash && nvm install 20` | All agents |
| Python 3.11+ | `python3 --version` | [manual] Install via brew: `brew install python@3.13` | Backend, test, guard |
| Git | `git --version` | [manual] Install via brew: `brew install git` | All agents |
| pnpm (optional) | `pnpm --version` | [auto] `npm install -g pnpm` | Frontend build |

### CLI Tools
| Tool | Check | Install | Required By |
|------|-------|---------|-------------|
| GitHub CLI | `gh --version` | [auto] `brew install gh` or `npm install -g gh` | Ship agent (PR, releases) |
| Vercel CLI | `vercel --version` | [auto] `npm install -g vercel` | Ship agent (frontend deploy) |
| Railway CLI | `railway --version` | [auto] `npm install -g @railway/cli` | Ship agent (backend deploy) |
| MongoDB Shell | `mongosh --version` | [auto] `brew install mongosh` or `npm install -g mongosh` | Test agent (seed data, verify) |
| Supabase CLI | `supabase --version` | [auto] `brew install supabase/tap/supabase` | Only if using Supabase |

### Design & Documentation Tools
| Tool | Check | Install | Required By |
|------|-------|---------|-------------|
| M3 MCP Server | `npm list -g @weppa-cloud/material3-mcp-server` | [auto] `npm install -g @weppa-cloud/material3-mcp-server` | Design agent (M3 tokens, components) |
| M3 Color Utility | `node --input-type=module -e "import '@material/material-color-utilities'"` | [auto] `npm install -g @material/material-color-utilities@0.3.0` | Design agent (palette generation) |
| reportlab (Python) | `python3 -c "import reportlab"` | [auto] `pip3 install reportlab` | All agents (PDF generation) |
| Mermaid CLI | `npx mmdc --version` | [auto] `npm install -g @mermaid-js/mermaid-cli` | Plan, spec agents (diagrams) |
| Playwright | `npx playwright --version` | [auto] `npm install -g playwright && npx playwright install chromium` | Test agent (E2E tests) |

### Python Packages (auto-installed by agents as needed)
```
fastapi uvicorn[standard] motor pydantic pydantic-settings
python-jose[cryptography] argon2-cffi httpx
pytest pytest-asyncio pytest-cov
sentry-sdk[fastapi]
reportlab
```

### Accounts & API Keys [manual — builder must create]
| Service | URL | Env Var | When Needed |
|---------|-----|---------|-------------|
| MongoDB Atlas | mongodb.com/cloud/atlas | `MONGODB_URI` | Build phase (S0) |
| Vercel | vercel.com | `VERCEL_TOKEN` | Ship phase |
| Railway | railway.app | `RAILWAY_TOKEN` | Ship phase |
| Sentry | sentry.io | `SENTRY_DSN` | Build phase (S0) |
| GitHub | github.com | `GITHUB_TOKEN` | Ship phase (optional, for gh CLI) |
| Figma | figma.com/developers | `FIGMA_TOKEN` | Design phase (only if providing Figma) |
| Cloudinary | cloudinary.com | `CLOUDINARY_URL` | Build phase (only if app has image uploads) |

### Orchestrator Pre-Flight Behavior

1. Read this tech stack skill
2. Run each `[auto]` check command
3. If check fails, run the install command
4. For `[manual]` items, check if available and warn the builder if missing
5. For accounts/API keys, check env vars and warn (don't block — they're needed later in the pipeline, not immediately)
6. Write `.roo/mcp.json` with M3 and MUI MCP servers (see orchestrator prompt)
7. Print a summary table: tool, status (installed/missing/warning)

---

## Phase 3: Sprint Planning Rules

### Sprint Cap Rule (MANDATORY)

Read `build_timeline_weeks` from `.onemillion/state.json`. Apply the hard cap:

| Build Timeline | Max Sprints | Fixed Sprints       | Available for Features |
| -------------- | ----------- | ------------------- | ---------------------- |
| 2.5 weeks      | 5–6         | S0 + S1 + Final = 3 | 2–3 feature sprints    |
| 3 weeks        | 6–7         | S0 + S1 + Final = 3 | 3–4 feature sprints    |
| 4 weeks        | 8–9         | S0 + S1 + Final = 3 | 5–6 feature sprints    |

Formula: `floor(build_timeline_weeks × 2.2)` sprints max. Default 2.5 weeks if unset.

**DO NOT** create more sprints than the cap — collapse features into existing sprints.
**DO NOT** expand the timeline to fit features — defer to POST-MVP instead.

### Sprint Templates by Product Type

**Web App:**

- S0: Project setup (repo, env, DB, health endpoint, Sentry, GitHub Actions)
- S1: Authentication (register, login, JWT + Argon2, protected routes)
- S2–Sn: Feature sprints (one feature group per sprint, frontend complete + backend)
- Final: Polish, error handling, deploy verification

**Agent:**

- S0: Project setup (repo, FastAPI scaffold, LLM API connection, Sentry, GitHub Actions)
- S1: Core agent behavior (system prompt, basic tool calls, happy path end-to-end)
- S2–Sn: Additional tools/capabilities (one per sprint)
- Final: Guardrails, cost controls, token budget enforcement, deploy

**Hybrid:**

- S0: Full setup (Next.js + FastAPI + MongoDB + Sentry + GitHub Actions)
- S1: Authentication
- S2: Core web app feature
- S3: Agent integration (embed /api/v1/chat endpoint)
- S4–Sn: Additional features
- Final: Polish, cost controls, deploy

### Sprint Composition (Every Sprint — Required Fields)

Each sprint definition must include ALL of the following. A developer must
be able to execute the sprint having read nothing else:

- **Objectives:** What "done" means for this sprint
- **User Stories:** "As a [persona], I can [action], so that [benefit]."
- **Entities touched:** Field schema from refined-prd.md (paste verbatim)
- **Backend tasks:** HTTP method + path + one-line description per endpoint
- **Frontend tasks:** Page or component name + what it renders + what API it calls
- **Acceptance criteria:** Given/When/Then verbatim from refined-prd.md
- **Verification gate:** Exact user action builder must perform and confirm
- **Git commit:** "feat: [feature-name]"
- **README update:** One line describing what to add

### Prompt Architecture Section (Agent and Hybrid Sprints Only)

Any sprint that adds or modifies agent behavior must include:

- **System prompt:** What the agent is told, and why each instruction is there
- **Tool definitions:** Name, description, parameters, return format per tool
- **Few-shot examples:** 2–3 input/output pairs for the happy path
- **Prompt versioning:** Save as `prompts/v{n}_system.md` — increment `n`
  every time the system prompt changes

### Sprint Execution Protocol

- Interactive: complete task → instruct builder to test → wait for explicit
  "confirmed" → only then advance to next task
- POST-MVP features never appear in MVP sprints
- Version control: main branch only. Push after all tasks in sprint are confirmed.
- README updated every sprint without exception
