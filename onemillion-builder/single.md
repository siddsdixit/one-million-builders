# OneMillion Builder: Complete Day-By-Day Course Flow

This is the single narrative guide for the OneMillion Builder course.

If you are a coding harness such as Codex, Claude Code, Cursor, Gemini, Antigravity, Copilot, or another agentic coding tool, read this file before teaching the course. Use it to explain the whole journey so the learner never feels like the days are random.

## What This Course Is

OneMillion is an 18 build-day course where a learner goes from an idea to a deployed AI product.

The learner will:

- set up a real GitHub course fork
- choose a specific product idea
- validate the problem with real conversations
- write a small PRD
- build a Next.js app
- deploy to Vercel
- add Supabase auth and database
- build one real core feature
- add a Claude-powered AI feature
- stream AI output
- let AI use safe tools
- ground AI in user data
- add quality gates and a cost budget
- audit production risk
- add monitoring
- create a landing page
- reach out to users
- record a Loom demo
- submit a Builder Claim

The point is not to watch AI build alone. The point is to learn how to direct AI agents while touching real tools.

## The OneMillion Agent System

OneMillion is literal about agents. The learner is not just taking a course; they are learning how to run a product-building agent system.

The orchestrator is the teacher. It reads the course, tracks state, explains the day, routes the learner to the right agent mode, and verifies the gate before moving on.

The core build flow is:

```text
idea -> spec -> validate-spec -> design -> plan -> validate-plan -> build -> review -> test -> guard -> ship -> sell
```

The support flow is:

```text
ask -> debug -> refactor -> revise -> brand -> persona-test
```

The learner should understand the agents before they depend on them:

| Agent | What it teaches the learner |
|---|---|
| `idea` | How to nurture a vague idea into a specific user, pain, promise, and product type. |
| `spec` | How to turn product thinking into a PRD, use cases, user stories, acceptance criteria, and KPIs. |
| `validate-spec` | How to reject vague, unbuildable, or oversized requirements before code starts. |
| `design` | How to translate requirements into screens, flows, copy, states, and usable UX. |
| `plan` | How to turn a spec into architecture, data model, milestones, and sprint-sized work. |
| `validate-plan` | How to catch missing architecture, impossible sequencing, and hidden dependencies. |
| `build` | How to implement the next smallest working slice. |
| `review` | How to compare code against the spec and catch drift. |
| `test` | How to prove behavior with tests and manual QA. |
| `guard` | How to check secrets, auth, RLS, privacy, costs, and production risk. |
| `ship` | How to deploy, verify, rollback, and keep a product alive. |
| `sell` | How to explain the product, find first users, and launch with evidence. |

## Spec Development

The course teaches spec-driven development before it teaches coding. The learner should hear this early:

```text
Do not ask AI to "build an app."
Teach AI the user, the pain, the promise, the constraints, and the definition of done.
Then ask it to build the next verified slice.
```

The OneMillion development pipeline is the course spine:

1. **Idea:** Who is this for, what painful moment do they have, and why now?
2. **Research:** What evidence proves the pain is real? What are competitors doing? What do users already hack together?
3. **PRD:** What will this product do, for whom, and what is out of scope?
4. **User stories:** What jobs must the user complete?
5. **Use cases:** What real scenarios must the product handle?
6. **KPIs:** How will the builder know the product is useful?
7. **Design:** What screens, states, and flows make the product easy to use?
8. **Plan:** What architecture and sprint sequence makes it buildable?
9. **Build:** What is the next smallest working slice?
10. **Review/Test/Guard:** Does the product match the spec, work correctly, and avoid dangerous mistakes?
11. **Ship/Sell:** Can real users reach it, understand it, trust it, and give feedback?

Short form:

```text
idea -> research -> PRD -> validate spec -> design -> plan -> build -> review -> test -> guard -> ship -> sell
```

Artifact rule:

```text
Do not create paperwork just to prove learning.
Each day should advance the active OneMillion pipeline artifact.
Create a separate file only when the pipeline naturally needs one, such as a PRD, design spec, implementation plan, test report, deployment record, or launch asset.
```

Tools arrive just in time. External tools enter only when the pipeline needs them:

| Stage | Tool introduced | Why then |
|---|---|---|
| Course workspace | GitHub | The learner needs a fork, clone, progress trail, and proof of work before anything else. |
| First deploy | Vercel | Deployment matters once there is a real app shell to deploy. |
| Data/auth | Supabase | Database and auth matter once the product needs users and persistent data. |
| AI feature | Anthropic | API keys matter once the product has a defined AI job. |
| Production | Sentry, Vercel Analytics, UptimeRobot | Monitoring matters once real people can use the product. |

## The AI/Human Contract

```text
Agent guides.
Learner decides.
Learner touches real tools.
Agent verifies.
```

The harness should:

- greet and orient the learner
- explain the current day before assigning work
- provide exact links, commands, prompts, and copy-ready text
- run local commands and verifiers when possible
- preserve `.onemillion/` state
- stop when a gate is incomplete
- advance only after verification

The learner must:

- make product decisions
- create accounts
- click through external dashboards
- create API keys and environment variables
- send messages or talk to real people
- review generated code
- confirm manual steps the harness cannot inspect

## How To Start

The learner should be able to say only:

```text
I am taking the OneMillion course at:
https://github.com/siddsdixit/teach-one-million/tree/main/onemillion-builder
```

The harness should then:

1. Read `AGENTS.md`.
2. Read `onemillion-builder/AGENTS.md` if starting from the subdirectory.
3. Read `onemillion-builder/course-manifest.json`.
4. Read `onemillion-builder/docs/teaching-protocol.md`.
5. Read this file: `onemillion-builder/single.md`.
6. Guide the learner through GitHub account, star, fork, clone, and install if needed.
7. Enforce preflight.
8. Start Day 0.

This is the **Preflight Gate**: the course does not start from a downloaded zip, loose folder, or Sid's upstream clone. It starts from the learner's forked git clone.

Key Day 0 setup links:

- GitHub signup: https://github.com/signup
- Course repo: https://github.com/siddsdixit/teach-one-million
- Fork course repo: https://github.com/siddsdixit/teach-one-million/fork
- GitHub CLI: https://cli.github.com/
- Git setup docs: https://docs.github.com/en/get-started/git-basics/set-up-git

## Course Shape

The course has Day 0 plus 18 build days.

- **Day 0:** orientation, OneMillion mission, pipeline, commitment, and GitHub workspace
- **Days 1-6:** foundation: idea agent, PRD draft, research, validation, stack, auth, core feature
- **Days 7-12:** make it AI: AI spec, first call, streaming, tools, RAG, quality gates
- **Days 13-18:** ship and sell: hygiene, domain, monitoring, landing page, users, demo

The harness should not compress days unless the learner explicitly asks and the completion gates are already satisfied.

## Day 0: Orientation + Commitment + GitHub Workspace

**Purpose:** welcome the learner into the OneMillion mission, explain the pipeline, create accountability, and set up the learner's GitHub course workspace.

**Why it matters:** most learners do not quit because they are incapable. They quit because the path feels random and the work becomes invisible. Day 0 makes the mission clear, shows the map, creates a public or private accountability loop, and gives the learner a real GitHub proof trail.

**What the learner does:**

- understands what OneMillion is and why it exists
- learns the full OneMillion pipeline at a high level
- answers three Day 0 reflection questions
- creates or opens a GitHub account
- stars the upstream repo
- forks the repo
- clones their fork
- runs the installer
- posts publicly or privately commits to 5 real people

**What the harness does:**

- greets the learner warmly and explains the OneMillion mission
- explains the OneMillion development pipeline at a high level
- explains what the learner will have by the end: real app or agent, deployed URL, GitHub proof trail, Loom demo, Builder Claim, and builder credential/certificate path
- explains that the product repo comes later when there is a real app; Day 0 only needs the course fork
- explains why the fork-first workflow matters
- gives exact setup links for GitHub
- previews that Vercel, Supabase, Anthropic, and monitoring accounts are introduced later when the pipeline needs them
- verifies the repo is a real git clone
- verifies root `AGENTS.md` and course manifest exist
- verifies `origin` points to the learner's fork
- verifies `upstream` points to Sid's repo
- gives full copy-ready LinkedIn, X, and private-message templates
- saves `.onemillion/day-00-reflection.md`
- updates `.onemillion/state.json` after the commitment is confirmed

**Exact links:**

- GitHub signup: https://github.com/signup
- Course repo: https://github.com/siddsdixit/teach-one-million
- Fork course repo: https://github.com/siddsdixit/teach-one-million/fork
- LinkedIn post composer: https://www.linkedin.com/feed/
- Sid's LinkedIn profile: https://www.linkedin.com/in/siddharthdixit
- X post composer: https://x.com/compose/post

**Done means:**

- repo is cloned from learner fork
- `origin` points to learner fork
- `upstream` points to `siddsdixit/teach-one-million`
- upstream repo is starred
- `.onemillion/day-00-reflection.md` exists
- public or private commitment was made

## Day 1: Idea Agent + PRD Draft

**Purpose:** teach how good ideas work and use the Idea agent to turn the learner's raw idea into a reviewed PRD draft.

**Why it matters:** good products start with unmet user needs, not technology gimmicks. Day 1 teaches the learner how to describe a user, pain point, data source, ideal solution, user stories, success criteria, KPIs, and first-pass market shape before building anything.

**What the learner learns:**

- what makes an idea good
- unmet user needs and pain points
- data sources and formats
- ideal solution visualization
- usage moments and roles
- user stories
- success criteria and KPIs
- TAM/SAM/SOM
- how the Idea agent creates a first PRD

**What the learner does:**

- creates `my-onemillion-build/`
- answers the Idea agent interview
- creates `.onemillion/project.json`
- creates and reviews `.onemillion/prd.md` with the idea brief embedded
- creates `.onemillion/state.json`

**What the harness does:**

- teaches idea generation before asking for fields
- acts as the Idea agent
- interviews the learner one question at a time
- explains user stories, success criteria, KPIs, and TAM/SAM/SOM
- drafts the PRD from the learner's answers
- marks unverified market claims as assumptions
- asks the learner to open, review, edit, and save the PRD

**Done means:**

- `my-onemillion-build/.onemillion/project.json` exists
- `.onemillion/prd.md` exists with the idea brief and first PRD
- PRD includes user, pain, unmet need, data sources, ideal solution, usage moment, user stories, success criteria, KPIs, competitive alternatives, TAM/SAM/SOM, and assumptions for Day 2
- learner reviewed and saved the PRD
- orchestrator state is updated

## Day 2: Validate The PRD

**Purpose:** take the Day 1 PRD, read it as the product owner, validate it against real users/customers and market reality, then decide the first MVP.

**Why it matters:** a PRD is a hypothesis until the learner and real users pressure-test it. Day 2 prevents the learner from blindly following AI-written product text, building for a vague audience, or trying to build the whole company instead of the first useful loop.

**What the learner learns:**

- how to review and edit the Day 1 PRD until it feels like their document
- what "validating a PRD" means
- Mom Test-style user/customer questions
- how to separate pain evidence from politeness
- what ICP means and why it must be specific
- what competitive and workaround research means for a beginner
- how to sanity-check TAM/SAM/SOM without pretending guesses are facts
- the difference between full product vision and MVP
- how to decide the first build loop

**What the learner does:**

- opens `.onemillion/prd.md`
- edits anything they disagree with
- identifies people to talk to
- asks about their real past behavior and reaction to the proposed PRD workflow
- adds Day 2 sections directly inside `.onemillion/prd.md`
- records validation evidence, competitors/workarounds, ICP, TAM/SAM/SOM sanity, full product versus MVP, and the Keep/Refine/Pivot verdict inside the PRD

**What the harness does:**

- teaches PRD validation before assigning research tasks
- explains that the learner owns the PRD, not the AI
- helps write non-leading questions
- helps structure notes and outreach
- checks that evidence is not just compliments
- helps compare alternatives and workarounds
- explains ICP, TAM/SAM/SOM, MVP, and full product vision in simple language
- helps update the PRD from evidence without inventing evidence
- does not create sidecar paperwork files unless the pipeline actually needs them

**Done means:**

- `.onemillion/prd.md` includes a Day 2 Learner Review
- `.onemillion/prd.md` includes validation evidence with real names/roles, clear anonymized identifiers, or explicit serious outreach/research attempts
- `.onemillion/prd.md` includes competitor/workaround insight
- `.onemillion/prd.md` includes ICP and TAM/SAM/SOM sanity
- the learner knows whether to keep, refine, or pivot the PRD
- the learner knows the full product vision and the first MVP
- `.onemillion/prd.md` includes the Day 2 verdict and MVP decision

## Day 3: Lock The Spec

**Purpose:** use the Spec agent to turn the validated PRD into a detailed build blueprint with functional requirements, CRUD building blocks, user stories, use cases, acceptance criteria, KPIs, and scope lock.

**Why it matters:** Day 1 and Day 2 decide what is worth building. Day 3 makes it buildable. Without a locked spec, the build agents invent missing requirements or quietly expand scope.

**What the learner learns:**

- requirements before code
- the difference between idea, functional requirement, user story, use case, acceptance criterion, and KPI
- CRUD: create, read, update, delete
- how CRUD breaks software into buildable blocks
- exactly 3 core user stories
- testable acceptance criteria
- out-of-scope list
- definition of done
- validate-spec thinking

**What the learner does:**

- uses `.onemillion/prd.md` as the validated product input
- calls the Spec agent to generate `.onemillion/refined-prd.md`
- reviews the generated spec and moves items in or out of MVP
- reruns the Spec agent when something is wrong or missing
- lists functional requirements
- maps core MVP entities to CRUD actions
- locks exactly 3 core user stories
- writes 2-3 real use cases
- writes acceptance criteria
- defines 2-3 KPIs or success signals
- writes what is out of scope
- confirms the MVP is small enough for the course
- commits the spec lock

**What the harness does:**

- acts as Spec agent
- uses the validated PRD as input
- asks clarifying questions
- drafts and revises `.onemillion/refined-prd.md`
- uses Validate Spec to check scope
- checks that design, architecture, planning, and build agents can use the spec
- avoids sidecar spec files beyond the pipeline artifact `.onemillion/refined-prd.md`

**Done means:**

- `.onemillion/refined-prd.md` exists
- `.onemillion/refined-prd.md` includes `Day 3 Locked Spec`
- functional requirements are listed
- core MVP entities and CRUD actions are listed
- exactly 3 core user stories are listed
- use cases are real scenarios
- acceptance criteria are testable
- KPIs are measurable
- out-of-scope list has at least 5 items
- definition of done is concrete

## Day 4: Stack + First Deploy

**Purpose:** create the real app, push it to GitHub, and deploy it to Vercel.

**Why it matters:** the learner stops being a planner and becomes a builder with a live URL.

**What the learner learns:**

- Next.js app structure
- Git basics
- GitHub app repo
- Vercel deployment loop

**What the learner does:**

- creates a Next.js app inside `my-onemillion-build`
- customizes the homepage
- initializes git for the product app
- creates a GitHub product repo
- deploys to Vercel
- verifies push-to-deploy works

**Exact links:**

- GitHub signup: https://github.com/signup
- GitHub CLI: https://cli.github.com/
- GitHub new repo: https://github.com/new
- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git docs: https://vercel.com/docs/deployments/git

**What the harness does:**

- explains every command
- helps fix setup errors
- edits simple homepage text
- checks local app and deployed URL

**Done means:**

- product GitHub repo exists
- app runs locally
- Vercel deployment URL works
- live homepage matches local code

## Day 5: Auth + Database

**Purpose:** add real signup/login and a real database.

**Why it matters:** useful products remember users and protect their data. Day 5 introduces auth, tables, env vars, and RLS.

**What the learner learns:**

- Supabase project setup
- environment variables
- auth flow
- Row Level Security

**What the learner does:**

- creates Supabase project
- stores public Supabase env vars locally and in Vercel
- scaffolds signup/login/logout/dashboard
- creates first table
- enables RLS

**Exact links:**

- Supabase dashboard: https://supabase.com/dashboard
- Supabase project shortcut: https://database.new
- Supabase Next.js Auth: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Supabase API keys: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Vercel dashboard: https://vercel.com/dashboard
- Vercel env vars: https://vercel.com/docs/projects/environment-variables

**What the harness does:**

- helps scaffold auth code
- checks `.env.local` is not committed
- checks signup/login/logout behavior
- reminds learner not to paste secrets

**Done means:**

- Supabase project exists
- signup/login/logout work
- protected dashboard works
- table has RLS enabled
- deployed app still works

## Day 6: Core Feature

**Purpose:** build the main non-AI workflow.

**Why it matters:** AI is not the product if the basic workflow does not work. Day 6 makes the app useful before adding AI.

**What the learner learns:**

- CRUD workflow
- API routes
- UI connected to database
- cross-user data safety

**What the learner does:**

- defines the main entity fields
- builds create/read/update/delete
- tests locally
- deploys and tests live
- runs a second-user RLS test

**Exact links:**

- Supabase dashboard: https://supabase.com/dashboard
- Vercel dashboard: https://vercel.com/dashboard

**What the harness does:**

- breaks work into data, API, UI, and review
- reviews generated code
- blocks progress if cross-user data leaks

**Done means:**

- core feature works locally and live
- CRUD works end to end
- second user cannot see first user's data
- Days 1-6 are verified

## Day 7: AI Feature Spec

**Purpose:** define the AI feature before writing AI code.

**Why it matters:** "add AI" is not a feature. Day 7 turns AI into a measurable job with clear inputs, output, constraints, and failure modes.

**What the learner learns:**

- useful AI behavior
- prompt role/goal/tone/constraints/format
- measurable acceptance criteria
- cost awareness

**What the learner does:**

- adds the AI feature spec to `.onemillion/prd.md`
- defines one useful AI job
- writes quality criteria
- documents failure modes and cost budget

**What the harness does:**

- acts as Spec agent
- challenges vague AI ideas
- validates the AI feature against the product's real user problem

**Done means:**

- AI feature spec exists
- criteria are measurable
- the AI feature is core to the product, not decoration

## Day 8: First AI Call

**Purpose:** make the app call Claude from a secure server route.

**Why it matters:** the learner sees real AI output inside their product while keeping the API key server-side.

**What the learner learns:**

- server-side AI calls
- Anthropic API key handling
- Vercel AI SDK
- prompt construction

**What the learner does:**

- creates Anthropic API key
- stores `ANTHROPIC_API_KEY` locally and in Vercel
- builds server route
- adds UI button
- tests AI output locally and live

**Exact links:**

- Anthropic Console: https://console.anthropic.com/
- Anthropic API docs: https://docs.anthropic.com/en/api/overview
- Vercel dashboard: https://vercel.com/dashboard
- Vercel env vars: https://vercel.com/docs/projects/environment-variables

**What the harness does:**

- creates the route only after showing the plan
- checks the key is never exposed with `NEXT_PUBLIC_`
- reviews prompt construction

**Done means:**

- server route exists
- AI output appears in app
- live app AI feature works
- API key is not exposed to client code

## Day 9: Streaming UI

**Purpose:** make AI output appear progressively instead of all at once.

**Why it matters:** streaming changes how AI feels. It makes the product feel responsive even when the model is still working.

**What the learner learns:**

- streaming responses
- loading states
- error states
- latency perception

**What the learner does:**

- changes route from non-streaming to streaming
- updates UI to show token-by-token output
- adds loading and error behavior
- tests local and live streaming

**What the harness does:**

- explains streaming before editing
- keeps the previous Day 8 behavior intact
- verifies loading/error states are not broken

**Done means:**

- output streams token by token
- loading and error states work
- deployed app still works

## Day 10: Tool Use

**Purpose:** let AI take one scoped action in the app.

**Why it matters:** AI becomes more useful when it can act, but actions must be bounded and safe.

**What the learner learns:**

- tool boundaries
- safe database writes
- human review
- authorization inside tool execution

**What the learner does:**

- chooses one AI tool/action
- implements the tool
- tests successful action
- tests cross-user denial

**Exact links:**

- Supabase dashboard: https://supabase.com/dashboard

**What the harness does:**

- refuses broad unsafe tools
- ensures user permission is checked inside the tool
- reviews generated code

**Done means:**

- AI can use at least one tool
- tool action is scoped
- User B cannot manipulate User A's data

## Day 11: RAG

**Purpose:** ground the AI in the user's app data.

**Why it matters:** generic AI output is not enough. The product becomes useful when AI uses the user's own records safely.

**What the learner learns:**

- retrieval
- grounding
- RLS-safe server-side Supabase access
- avoiding hallucinated context

**What the learner does:**

- selects which data should ground the AI
- fetches relevant rows before calling AI
- includes retrieved context in the prompt
- tests with user-specific data
- re-runs cross-user checks

**Exact links:**

- Supabase dashboard: https://supabase.com/dashboard
- Supabase RLS docs: https://supabase.com/docs/guides/database/postgres/row-level-security

**What the harness does:**

- helps choose retrieval scope
- prevents service-role shortcuts
- checks that RLS still protects user data

**Done means:**

- AI uses app data
- AI answers are grounded in user records
- RLS still prevents cross-user leaks

## Day 12: Lock The AI

**Purpose:** make AI quality measurable.

**Why it matters:** AI features drift. Day 12 creates acceptance criteria, examples, evals, rate limits, and cost budget.

**What the learner learns:**

- AI acceptance criteria
- manual evals or tests
- cost budget
- rate limits

**What the learner does:**

- adds measurable AI quality criteria to tests/evals and PRD
- writes pass/fail examples
- documents budget
- verifies rate/cost limits

**What the harness does:**

- acts as Test agent
- turns vague quality into observable checks
- helps run tests or manual evals

**Done means:**

- acceptance criteria exist
- tests or manual evals pass
- cost/rate budget is documented

## Day 13: Production Hygiene

**Purpose:** audit the product before treating it as shippable.

**Why it matters:** a working demo can still leak secrets, expose data, or fail silently. Day 13 catches the dangerous stuff.

**What the learner learns:**

- secrets audit
- RLS audit
- abuse prevention
- error handling

**What the learner does:**

- runs secret scan
- audits every table's RLS policy
- re-runs cross-user tests
- fixes critical risks and leaves evidence in code/config

**Exact links:**

- Supabase dashboard: https://supabase.com/dashboard
- Vercel dashboard: https://vercel.com/dashboard

**What the harness does:**

- acts as Guard agent
- blocks on critical leaks
- helps document non-critical risks

**Done means:**

- no exposed secrets
- RLS audit is visible in Supabase policy/code/config checks
- critical guard checks pass

## Day 14: Custom Domain

**Purpose:** optionally connect a custom domain, or deliberately decide to stay on the Vercel URL.

**Why it matters:** domains teach deployment reality: DNS, SSL, redirects, and production URLs. But a custom domain is optional.

**What the learner learns:**

- DNS basics
- Vercel domain setup
- SSL
- auth redirect URL updates

**What the learner does:**

- chooses to buy a domain or skip with a documented reason
- connects domain in Vercel if buying
- configures DNS at registrar
- verifies HTTPS
- updates Supabase redirect URLs if needed

**Exact links:**

- Vercel dashboard: https://vercel.com/dashboard
- Vercel domains docs: https://vercel.com/docs/domains
- Cloudflare Registrar: https://www.cloudflare.com/products/registrar/
- Porkbun: https://porkbun.com
- Namecheap: https://www.namecheap.com
- DNS Checker: https://dnschecker.org
- Supabase dashboard: https://supabase.com/dashboard
- Supabase redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls

**What the harness does:**

- explains DNS records
- helps copy Vercel's required records
- documents skip decision if the learner stays on `.vercel.app`

**Done means:**

- custom domain works with HTTPS, or skip is documented
- auth redirect URLs are updated if auth uses redirects

## Day 15: Monitoring

**Purpose:** add error monitoring, analytics, and uptime checks.

**Why it matters:** production means knowing when the app breaks. Day 15 gives the learner eyes on errors and downtime.

**What the learner learns:**

- Sentry error monitoring
- Vercel Analytics
- UptimeRobot uptime checks
- alert email verification

**What the learner does:**

- creates Sentry project
- adds Sentry config and DSN
- enables Vercel Analytics
- creates UptimeRobot monitor
- tests an alert

**Exact links:**

- Sentry signup: https://sentry.io/signup/
- Sentry Next.js docs: https://docs.sentry.io/platforms/javascript/guides/nextjs/
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Analytics: https://vercel.com/docs/analytics
- UptimeRobot signup: https://uptimerobot.com/signUp
- UptimeRobot first monitor: https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor

**What the harness does:**

- guides the setup in three small chunks
- verifies packages/config files
- asks for manual confirmation where dashboards cannot be inspected

**Done means:**

- Sentry configured and receives test error
- Vercel Analytics enabled
- UptimeRobot monitor active
- alert email works

## Day 16: Landing Page

**Purpose:** turn the product into something a stranger can understand.

**Why it matters:** a product without positioning is hard to share. Day 16 makes the root URL explain what the product does and for whom.

**What the learner learns:**

- positioning
- proof
- CTA
- landing page structure

**What the learner does:**

- writes headline and one-liner
- adds product explanation
- adds CTA
- adds proof and demo links if available
- deploys landing page

**Exact links:**

- Vercel dashboard: https://vercel.com/dashboard

**What the harness does:**

- acts as Sell plus Build
- helps write positioning
- reviews landing page clarity

**Done means:**

- landing page is live
- CTA works
- copy is specific about target user and pain

## Day 17: First 10 Users

**Purpose:** get the product in front of real people.

**Why it matters:** shipping is not only deploys. The learner needs signal from humans, even if the first signal is silence.

**What the learner learns:**

- outreach
- feedback capture
- interpreting no-response
- not changing the product mid-feedback

**What the learner does:**

- creates outreach list
- sends 7-10 messages
- reflects response learnings in product copy, PRD, or Builder Claim notes
- documents whether feedback was captured or outreach is pending

**Exact links:**

- LinkedIn feed: https://www.linkedin.com/feed/
- X post composer: https://x.com/compose/post

**What the harness does:**

- helps write outreach messages
- keeps the learner from over-editing the product before feedback
- records `PASS_WITH_FEEDBACK` or `OUTREACH_SENT_PENDING_FEEDBACK`

**Done means:**

- outreach list exists
- feedback file exists
- 7-10 outreach messages sent or equivalent
- at least one real feedback signal, or documented pending-feedback status

## Day 18: Demo Day + Builder Claim

**Purpose:** package the build into a public demo and submit proof.

**Why it matters:** the course ends with a product, a demo, a proof packet, and a review path for Builder #N.

**What the learner learns:**

- demo storytelling
- final verification
- public proof
- Builder Claim submission

**What the learner does:**

- plans a 5-minute demo
- records Loom
- tests Loom public sharing
- prepares claim data from `.onemillion/state.json`, the live URL, and Loom URL
- runs final verification
- submits Builder Claim issue or form
- shares the win

**Exact links:**

- Loom: https://www.loom.com/
- Loom sharing help: https://loomhelp.zendesk.com/hc/en-us/articles/360002208157-How-to-share-your-recording
- Builder Claim issue: https://github.com/siddsdixit/teach-one-million/issues/new/choose
- LinkedIn feed: https://www.linkedin.com/feed/
- Sid's LinkedIn profile: https://www.linkedin.com/in/siddharthdixit
- X post composer: https://x.com/compose/post

**What the harness does:**

- checks all previous verifications
- checks live app URL
- checks public Loom URL
- generates verified Builder Claim packet
- reminds learner that official Builder #N is assigned after review

**Done means:**

- Loom URL is public
- live app URL works
- final verification passes
- Builder Claim submitted

## What The Harness Should Do At The Start Of Each Day

Use this order every time:

1. State the current day and title.
2. Explain how it fits the whole course arc.
3. Explain what the learner will learn today.
4. Explain what the learner will do today.
5. Provide exact links for any external service.
6. Provide exact commands or copy-ready prompts.
7. Ask for human decisions before making product choices.
8. End with the done checklist.
9. Tell the learner to say `day done` only when the checklist is true.

## What The Harness Should Never Do

Do not say:

```text
Do Day 1.
Do Day 2.
Run the verifier.
Go to Vercel.
Open Supabase.
Submit the form.
```

Instead, explain the day, provide links and copy-ready material, and define done.

## Recovery

If the learner returns after a break:

1. Read `.onemillion/state.json`.
2. Read the verification history inside `.onemillion/state.json`.
3. Inspect the current PRD/app state.
4. Summarize where they are.
5. Give the next smallest action.

Do not shame missed days. The 18 days are units of progress, not calendar days.
