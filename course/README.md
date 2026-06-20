# OneMillion Builder

**This is the single landing page for learners, agents, and coding harnesses.**

<p align="center">
  <img src="diagrams/hero-animated.gif" alt="OneMillion Builder - build a real AI product in 18 days" width="100%">
</p>

<p align="center">
  <strong>Build and ship a real AI product in 18 days.</strong><br>
  Beginner-friendly. Agent-guided. Free forever.
</p>

<p align="center">
  <a href="START-HERE.md"><strong>Start Here</strong></a>
  &nbsp;•&nbsp;
  <a href="days/single.md">Full Course Flow</a>
  &nbsp;•&nbsp;
  <a href="#start-in-5-minutes">5-Minute Setup</a>
  &nbsp;•&nbsp;
  <a href="#course-roadmap">Course Roadmap</a>
  &nbsp;•&nbsp;
  <a href="docs/FAQ.md">FAQ</a>
  &nbsp;•&nbsp;
  <a href="docs/course-format.md">Course Format</a>
</p>

<p align="center">
  <img alt="18 days" src="https://img.shields.io/badge/18_days-one_focused_build-111827?style=for-the-badge">
  <img alt="Agent guided" src="https://img.shields.io/badge/agent_guided-Claude%20Code%20%7C%20Cursor%20%7C%20Codex-2563eb?style=for-the-badge">
  <img alt="Free" src="https://img.shields.io/badge/free_forever-MIT-16a34a?style=for-the-badge">
</p>

---

## The Promise

You have seen the posts: solo builders shipping SaaS in a weekend, non-engineers launching useful AI tools, tiny teams turning ideas into real products. Then you try it yourself and hit the wall: setup, auth, databases, deploys, API keys, prompts, bugs, and a dozen tabs you do not understand yet.

That is exactly who this course is for.

**OneMillion exists to take one million people — anyone with an idea — from zero to a real, deployed, launchable product.**

Most people get stuck because they try to learn coding, product thinking, AI, deployment, auth, databases, and launch all at once.

OneMillion turns that into one small daily move. You learn the same pipeline real product teams use, but with agents as patient teachers: idea, research, PRD, spec, design, architecture, build, review, test, guard, ship, and sell.

By the end, you have:

| You ship | Proof you keep |
|---|---|
| A live web app | Public Vercel URL |
| Real signup/login | Supabase auth + database |
| A real AI feature | Server-side LLM workflow |
| Production hygiene | Security, monitoring, and checks |
| A public demo | Loom + Builder Claim |

No prior coding experience required. Your coding harness becomes your teacher, but you make the decisions and learn the tools.

This is not a toy tutorial. It is not a sandbox. You build a real product, in a real repo, deployed on a real URL, with a path to real users.

The first five days are deliberately not "jump into code." They teach the foundation:

| Day | You learn | Why it matters |
|---:|---|---|
| 0 | mission, pipeline, commitment, GitHub fork | You understand the course and create a proof trail |
| 1 | good ideas, pain points, user stories, KPIs, PRD | You choose a problem worth building |
| 2 | user validation, competitors, ICP, MVP | You test whether the PRD is real |
| 3 | specs, CRUD, functional requirements, acceptance criteria | You freeze a buildable scope |
| 4 | product design, MUI, screens, states, seed data, mockup | You see and approve the product before code |

---

## Start In 5 Minutes

Start by giving this page to your coding harness:

```text
I am taking the OneMillion course at:
https://github.com/siddsdixit/one-million-builders/tree/main/course
```

Your harness should greet you, explain the course, help you set up GitHub if needed, guide you through the fork/clone/install flow, and then start Day 0. You should not need to know the setup steps before you begin.

The course still runs from your own fork. That matters: your fork becomes your learning workspace, progress trail, and final proof.

| Step | Do this | Link |
|---:|---|---|
| 1 | Paste the course link into your harness | Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot |
| 2 | Let the harness explain the course | It follows the teaching protocol |
| 3 | Create or open GitHub when asked | [GitHub signup](https://github.com/signup) |
| 4 | Fork, clone, and install with guidance | [Fork now](https://github.com/siddsdixit/one-million-builders/fork) |
| 5 | Complete Day 0 | Public or private commitment |

If your harness asks for exact setup commands, use these:

```bash
git clone https://github.com/YOUR-USERNAME/one-million-builders.git
cd one-million-builders
./course/install-agents.sh
```

If your harness needs a fuller prompt, paste this:

```text
I am taking the OneMillion course at:
https://github.com/siddsdixit/one-million-builders/tree/main/course

Read AGENTS.md and course/course-manifest.json.
Read course/docs/teaching-protocol.md.
Read course/days/single.md.
Become my OneMillion learning orchestrator.
Properly greet me, explain the course, explain the AI/human contract, and guide me through GitHub setup, fork, clone, install, and Day 0.
If I do not have GitHub yet, walk me through account creation with exact links.
When the local clone is ready, enforce the Preflight Gate before Day 0.
Teach me one day at a time with copy-ready actions and clear done checklists.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

Need the slower walkthrough? Open [START-HERE.md](START-HERE.md). Want the whole day-by-day arc in one file? Open [single.md](days/single.md).

---

## How The Course Feels

OneMillion is an agent-led apprenticeship. Open the repo in Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or another coding harness. The harness reads `AGENTS.md`, `course-manifest.json`, `docs/teaching-protocol.md`, and `days/single.md`, then becomes your OneMillion learning orchestrator.

You move through focused agent modes. In some harnesses these may be slash commands; in others, the orchestrator reads the course files and invokes the right mode for you.

```text
/idea -> /spec -> /design -> /plan -> /build -> /test -> /guard -> /ship -> /sell
```

Support modes are always available:

```text
/ask · /debug · /refactor · /orchestrator
```

|  |  |
|---|---|
| **Short daily lessons** | Read just enough to understand the idea before building. |
| **Hands-on building** | Your harness writes code with you, but you review and decide. |
| **Real tools** | GitHub, Vercel, Supabase, Anthropic, monitoring, Loom. |
| **Daily verification** | Say `day done`; your harness checks the gate before moving on. |
| **Small scope** | The first MVP is capped at a few core user stories so you can finish. |
| **Design review** | The course includes visual and UX quality checks before launch. |

The rule:

```text
Agent guides.
Learner decides.
Learner touches real tools.
Agent verifies.
```

Whenever the course asks you to create an account, API key, dashboard setting, or public link, use the [Account Setup Playbook](docs/account-setup.md). It gives the exact link, exact permission, and exact QA check.

Worried about cost? Start on free tiers, create API keys only when the day asks for them, and read the pricing notes in the setup playbook before adding payment details. You can pause before any paid step.

The course teaches the OneMillion development pipeline explicitly. You will learn what the `idea`, `spec`, `validate-spec`, `design`, `plan`, `build`, `review`, `test`, `guard`, `ship`, and `sell` agents do before you depend on them. The point is to learn the operating system: spec first, small slices, verified progress.

```text
idea -> research -> PRD -> validate spec -> design -> plan -> build -> review -> test -> guard -> ship -> sell
```

Tools arrive just in time. GitHub is required on Day 0 because your fork is the course workspace. Vercel appears on Day 6 when you deploy the app shell. Supabase appears on Day 7 when you add auth and database. Anthropic appears on Day 11 or Day 12 when the AI feature is specified and ready to build. Monitoring appears on Day 16 when the product is live enough to need production checks.

The repo is intentionally organized so the learner-facing surface stays small:

```text
START-HERE.md -> current day README.md -> build.md -> stuck.md if needed -> day done
```

| Folder | What it contains |
|---|---|
| `course/` | Day 0-18 lessons, build guides, resources, Loom plans, and the full flow. |
| `agents/` | OneMillion agent definitions and skills used by Claude Code, Cursor, Codex, Gemini, and other harnesses. |
| `docs/` | Account setup, harness guides, verification notes, examples, and recovery help. |
| `tools/` | Local QA and synthetic simulation scripts used to validate the course. |

---

## Support Built In

You are not expected to brute-force the hard parts alone.

| Support | What it is for |
|---|---|
| **Loom walkthroughs** | Sid records the key setup/build moments so you can compare your screen to a human reference. |
| **Live cohorts** | Free group runs when available, with shared momentum and demo day. |
| **Community help** | Bring stuck points, errors, and daily wins to the channel you have access to. |
| **Mentors and reviewers** | Experienced builders help with blockers and final Builder Claim review. |
| **Recovery path** | If you stop for a week, use [Recover Your Place](docs/recover.md) and continue from the next verified day. |

Self-paced and cohort learners use the same curriculum, the same daily gates, and the same final verification.

---

## Course Roadmap

| Stage | Days | What you learn | What you have at the end |
|---|---:|---|---|
| **Foundation** | 0-5 | GitHub workspace, idea, research, spec, design, architecture | A validated, designed, planned product |
| **Build + QA** | 6-10 | app shell, Vercel, Supabase, core build, review, QA | A live app with auth, database, and one working workflow |
| **AI + Readiness** | 11-15 | AI strategy, first AI build, product polish, security/trust, final QA | A useful AI feature inside a polished, trusted, production-ready MVP |
| **Ship + Sell** | 16-18 | production verification, monitoring/domain, brand, pricing, first users, demo | A launch-ready product and Builder Claim |

<p align="center">
  <a href="days/day-01-idea/README.md"><strong>Days 1-5: Foundation</strong></a>
  &nbsp;•&nbsp;
  <a href="days/day-06-app-shell/README.md"><strong>Days 6-10: Build + QA</strong></a>
  &nbsp;•&nbsp;
  <a href="days/day-11-ai-spec/README.md"><strong>Days 11-15: AI + Readiness</strong></a>
  &nbsp;•&nbsp;
  <a href="days/day-16-ship-production/README.md"><strong>Days 16-18: Ship + Sell</strong></a>
</p>

---

## Daily Path

| Day | Focus | Outcome |
|---:|---|---|
| [0](days/day-00-orientation/README.md) | Orientation + commitment | Mission, pipeline, reflection, fork, clone, and public/private commitment |
| [1](days/day-01-idea/README.md) | Idea agent + PRD draft | Learn good ideas, define user pain, and review first PRD |
| [2](days/day-02-validate-prd/README.md) | Validate the PRD | User evidence, ICP, MVP, and PRD validation update |
| [3](days/day-03-spec/README.md) | Lock the spec | Functional requirements, CRUD blocks, user stories, acceptance criteria, KPIs, and done criteria |
| [4](days/day-04-design/README.md) | Design the product | Audience-based design, MUI design system, screens, flows, states, seed data, and mockup approval |
| [5](days/day-05-plan-architecture/README.md) | Plan architecture | Product type, secure architecture, tenancy, backend path, scale assumptions, and sprint briefs |
| [6](days/day-06-app-shell/README.md) | App shell + first deploy | Next.js + MUI app live on Vercel |
| [7](days/day-07-auth-db/README.md) | Auth + database | Supabase signup/login, tables, and RLS |
| [8](days/day-08-core-build/README.md) | Core build | Main workflow working end-to-end |
| [9](days/day-09-review/README.md) | Implementation review | Spec drift and code review findings |
| [10](days/day-10-qa-tests/README.md) | QA + tests | Core behavior verified locally and live |
| [11](days/day-11-ai-spec/README.md) | AI feature spec | Measurable AI behavior |
| [12](days/day-12-first-ai-build/README.md) | First AI build | Selected LLM output in your app |
| [13](days/day-13-product-polish/README.md) | Product polish + UX finish | Clear flow, complete states, AI UX, mobile/desktop polish |
| [14](days/day-14-security-trust-review/README.md) | Security + trust review | Auth, authorization, tenancy/RBAC, RLS, secrets, AI privacy, cost/rate controls |
| [15](days/day-15-qa-production-readiness/README.md) | QA + production readiness | Final manual/automated QA, AI pass/fail examples, live critical path, production blockers |
| [16](days/day-16-ship-production/README.md) | Ship production | Production env vars, Supabase checks, live smoke tests, monitoring, rollback |
| [17](days/day-17-sell-users/README.md) | Brand + marketing + pricing + first users | Positioning, product page, pricing, launch posts, outreach, feedback |
| [18](days/day-18-demo/README.md) | Demo Day + Builder Claim | Loom demo + Builder Claim |

---

## What You Need

| Need | Notes |
|---|---|
| Laptop | Mac, Windows, or Linux |
| Coding harness | Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or similar |
| GitHub | Source control and proof trail |
| Vercel | Deployment, introduced on Day 6 |
| Supabase | Auth and database, introduced on Day 7 |
| Anthropic API key | Added on Day 11 or Day 12 |
| Time | 1-2 hours per day |

---

## Who This Is For

| If you are... | Why this can work |
|---|---|
| **Brand new to code** | The harness teaches each move and the course keeps the scope small. |
| **A product manager** | You already think in users and requirements; now you learn to ship. |
| **An operator or assistant** | You know painful workflows. This turns one into software. |
| **A designer** | You can pair taste with working product behavior. |
| **An engineer** | You can move faster and learn a structured agentic SDLC. |
| **A founder or indie builder** | You finish with a deployed product, demo, and first-user motion. |

The only hard requirement is that you keep going one verified day at a time.

---

## What You Produce

| Artifact | Why it matters |
|---|---|
| Day 0 reflection + fork | Proves the learner understands the mission and owns the workspace. |
| PRD and refined PRD | Captures the product idea, evidence, ICP, MVP, and success criteria. |
| Spec / refined PRD | Converts the idea into functional requirements and acceptance criteria. |
| Design spec, design system, screens, seed data | Makes the product visible before architecture and code. |
| Architecture + sprint briefs | Gives the build agent a safe contract to follow. |
| [DeliverableDash example artifacts](docs/examples/deliverabledash/README.md) | Shows what a finished course trail can look like. |
| [Sample finished app shape](docs/examples/deliverabledash/app/README.md) | Gives you a concrete reference for the end state. |
| [Daily verification trail](docs/verification/README.md) | Proves each day passed before you advanced. |
| [Day 18 demo](days/day-18-demo/README.md) | Turns your product into something people can understand. |
| [Share templates](docs/share-templates.md) | Helps you build in public without staring at a blank post. |

The product is useful. The proof trail is useful. The repeatable way of building is the real prize.

---

## What You Earn

Complete all 18 days, pass final verification, and submit your Builder Claim.

| Credential | What it means |
|---|---|
| **Builder #N** | A sequential, permanent builder number after review |
| **Public proof** | Live URL, demo Loom, daily verification trail |
| **Reusable skill** | A repeatable agentic build process for your next product |

At the end, you submit a [Builder Claim packet](docs/builder-claim.md). Cohorts may use a Google Form for collection; self-paced learners can use the public GitHub Builder Claim fallback.

See [How Builder #N is earned](docs/verification/README.md).

First 100 accepted builders receive **Founding Builder** status. Live cohorts run periodically; apply when a cohort is open through [cohort/README.md](../cohort/README.md).

<p align="center">
  <img src="diagrams/builder-profile-sample.png" alt="Sample OneMillion Builder profile" width="720">
</p>

---

## Helpful Links

| I need... | Go here |
|---|---|
| The full start guide | [START-HERE.md](START-HERE.md) |
| Account links and permissions | [Account Setup Playbook](docs/account-setup.md) |
| Harness-specific setup | [Harness Guides](docs/harnesses/README.md) |
| Help after a break | [Recover Your Place](docs/recover.md) |
| Verification details | [Verification](docs/verification/README.md) |
| Final submission packet | [Builder Claim Submission](docs/builder-claim.md) |
| Common questions | [FAQ](docs/FAQ.md) |
| Example finished artifacts | [DeliverableDash Example](docs/examples/deliverabledash/README.md) |

---

<p align="center">
  <strong>The million starts with one.</strong><br>
  <a href="START-HERE.md"><strong>Start Day 0</strong></a>
</p>

---

MIT licensed. Free for learners, forever.
