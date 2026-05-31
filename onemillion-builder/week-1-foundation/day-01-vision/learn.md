# Day 1 — OneMillion Pipeline + Idea Lab

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Week 1 | ~45–75 min | No code today**

> 💜 **First, the most important thing about this course:** you will miss days. That's normal. The 18 days are units of progress, not calendar days. Skip a day, take a week off, come back when life lets you. **No shame, no streaks, no badges taken away.** Builder #N gets earned when you finish, not by when you finish. The only way to fail is to never come back.

---

## Learning Frame

- **Mental model:** The OneMillion pipeline turns a vague idea into a shipped product through small verified stages.
- **What can go wrong:** You pick an idea that is too broad or too vague.
- **What to ignore today:** Ignore Vercel, Supabase, API keys, design polish, auth, and AI implementation today.

## What You'll Have After Today

- A picked **product type** (web app / AI agent / hybrid)
- An **initial idea** written down in your project folder
- A plain-English understanding of the OneMillion development pipeline
- A map of which OneMillion agents help at each stage
- A mental model of how software actually works — the four parts every product has

Today is the day you go from "course-taker" to "builder who understands the system." You are not just picking an idea. You are learning the pipeline you will use for every product after this one.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: The OneMillion Development Pipeline (~15 min read)

OneMillion is built around a simple belief:

```text
Do not ask AI to "build an app."
Give AI a clear pipeline, a clear spec, and a clear verification gate.
```

The pipeline is:

```text
idea -> research -> PRD -> validate spec -> design -> plan -> build -> review -> test -> guard -> ship -> sell
```

Each stage has a job:

| Stage | Agent | What happens |
|---|---|---|
| Idea | `idea` | Turn a vague thought into a specific user, painful moment, and product direction. |
| Research | `idea` + `research` | Learn from real conversations, competitors, substitutes, and current workarounds. |
| PRD | `spec` | Write the product promise, target user, core jobs, user stories, use cases, KPIs, out-of-scope, and done criteria. |
| Validate spec | `validate-spec` | Catch vague, oversized, contradictory, or unbuildable requirements before code. |
| Design | `design` | Turn requirements into screens, flows, states, copy, and UX rules. |
| Plan | `plan` | Decide architecture, data model, routes, milestones, and build sequence. |
| Validate plan | `validate-plan` | Catch missing dependencies and impossible sequencing before implementation. |
| Build | `build` | Implement the next smallest working slice. |
| Review | `review` | Compare code against the spec and catch drift. |
| Test | `test` | Prove behavior locally and in the browser. |
| Guard | `guard` | Check secrets, auth, RLS, privacy, prompt safety, rate limits, and production risk. |
| Ship | `ship` | Deploy, verify, and keep rollback/recovery clear. |
| Sell | `sell` | Explain the product, reach real users, collect feedback, and submit your demo. |

This is why the days are ordered the way they are. You are not doing random tasks. You are walking the OneMillion pipeline once, slowly, with the harness teaching each stage.

External tools arrive only when the pipeline needs them:

| Tool | When it appears | Why |
|---|---|---|
| GitHub | Day 0 | Your fork is the course workspace and proof trail. |
| Vercel | Day 4 | You have an app shell worth deploying. |
| Supabase | Day 5 | You need auth, users, and persistent data. |
| Anthropic | Day 8 | Your AI feature has a spec. |
| Sentry, analytics, uptime | Day 15 | Your product is live enough to monitor. |

Today uses the `idea` agent. Its job is not to pick the idea for you. Its job is to help you sharpen the idea until it names a specific person, a specific pain, and a product shape small enough to finish.

---

## Part 2: How Every Software Product Actually Works (~10 min read)

This is the most important 10 minutes of the entire course. If you skip it, every day after gets harder.

Every digital product — Netflix, Notion, ChatGPT, the website where you order pizza — has the same four parts. That's not an exaggeration. It's not "mostly the same with exceptions." It's **the same four parts**, every time.

Imagine a restaurant. You've been to one. The mental model is already in your head.

**The dining room — that's the frontend.** What the customer sees. Menus, tables, lighting, the way the waiter takes the order. In software, this is your app — the screens, buttons, forms, the thing the user touches. We'll build yours with **Next.js**.

**The kitchen — that's the backend.** The engine the customer doesn't see. Orders come in from the dining room, food goes out, the chef talks to suppliers when they run low on tomatoes. In software, this is the code that runs when someone clicks a button. It does the work, then sends the result back to the frontend. Also Next.js — same codebase as the dining room. That's a modern trick most apps used to need two separate codebases for.

**The pantry and order history — that's the database.** Where the restaurant remembers everything. What's in the fridge, what every regular customer ordered last week, every receipt from the past year. In software, this is where every user, every piece of data, every record persists. We use **Supabase** — think of it as a spreadsheet in the sky that your app can read from and write to.

**The chef who improvises — that's AI.** A world-class chef who can invent a new dish based on a customer's description. "I want something spicy, not too heavy, vegetarian, and it should remind me of my grandmother's cooking." The chef thinks, makes choices, produces something new each time. In software, this is the LLM — **Claude** in our case. It reads, reasons, writes, and acts on your behalf. We'll add Claude to your app in Week 2.

Then there's **the address — the hosting.** A restaurant with no address can't take customers. Software with no URL can't either. We use **Vercel** to give your app a real URL on the internet, in about 30 seconds.

How they connect:

```
User types something
  → Frontend receives it
    → Backend processes it
      → Supabase stores or retrieves data    OR    Claude thinks and responds
        → Result goes back to Frontend
          → User sees the result
```

That's it. Every product follows this loop. Once you internalize this, software stops being magic. It becomes a thing you can build.

> 🔧 **Engineers:** Yes, this is reductive. Yes, there are queues, caches, edge functions, CDNs. None of that matters for a first product. The restaurant analogy is what gets a non-technical builder to ship in 18 days.

---

## Part 3: Three Things You Can Build (~10 min read)

Before Day 3 (your PRD), you need to know which of three product shapes you're aiming for. The shape determines every decision after.

### Web App
**Heavy on frontend + database. The user does the work. The app organizes it.**

Examples:
- A booking system for a yoga studio
- A client portal for freelance designers
- A daily habit tracker with charts
- A job board for a niche industry

Ask yourself: *Does someone log in every day to get work done, and the app's main job is to help them organize it?* If yes, this is a web app.

### AI Agent
**Heavy on backend + AI. The AI does the work. The human reviews.**

Examples:
- An AI that monitors 5 competitors' pricing and emails you a weekly summary
- An AI that reads your Slack and generates a Monday morning digest
- An AI that reads academic papers and answers questions about them
- An AI that reads job descriptions and tailors your resume to each one

Ask yourself: *Is the main value in AI doing something automatically, without me sitting in front of an app to use it?* If yes, this is an agent.

### Hybrid
**Both. A web app where AI is the core of the value, not decoration.**

Examples:
- A CRM where AI drafts personalized follow-ups based on the customer's history
- A writing tool where AI gives feedback as you type
- A PM tool where AI suggests priorities based on user data + deadlines

Ask yourself: *Do users need a full interface AND AI is essential — not just a nice-to-have?* If both, this is a hybrid.

> 💡 **Most builders' first product is a Web App.** It's the most contained shape — easier to scope, easier to deploy, easier to put real users on. You can always add an AI feature on Day 7 and turn your Web App into a Hybrid. Many do.

### What If You're Genuinely Unsure?

That's okay. Pick whichever resonates most when you read the examples. We'll confirm it on Day 3 when you write the PRD. Many builders start thinking "Hybrid" and realize on Day 3 that what they actually want is a Web App with one AI feature on top — which is fine. The product type is a starting decision, not a permanent one.

---

## Today's Assignment

You're going to do three things. Pen and paper is fine. So is a Notion doc. So is `.onemillion/project.json` in your project folder.

### Thing 1: Pick a product type
Write down one of: `web_app`, `ai_agent`, `hybrid`.

### Thing 2: Write down an initial idea
Two sentences. What's the problem you're solving and who's it for? Don't optimize. First instinct is fine.

**Example (good):**
> Yoga studio owners spend hours each week manually following up with clients who didn't rebook. I want to build a tool that automates the follow-up while letting the owner approve each message before it goes.

**Example (also good, even if vague):**
> I'm tired of forgetting which clients I owe deliverables to. I want a dashboard that shows what I owe whom by when.

**Example (too vague — try again):**
> Something with AI for productivity.

### Thing 3: Create your project folder

In your terminal, from the root of your cloned course fork:

```bash
cd /path/to/teach-one-million
mkdir my-onemillion-build
cd my-onemillion-build
mkdir .onemillion
```

Then create a file called `.onemillion/project.json` with this content (replace the placeholders):

```json
{
  "product_type": "web_app",
  "idea": "Yoga studio owners spend hours each week manually following up with clients who didn't rebook. I want to build a tool that automates the follow-up while letting the owner approve each message before it goes.",
  "builder_name": "Your Name",
  "started_at": "2026-05-18"
}
```

That's it. Tomorrow you'll talk to real users about whether this idea solves a real pain.

---

## What Good Looks Like

A good Day 1 idea has three things:

1. **A specific person you can name.** Not "users." Not "freelancers." A specific human — Sarah, a 34-year-old UX designer with 4-6 freelance clients who uses Notion to track deliverables and lost two clients last year to miscommunication.

2. **A specific pain you can describe.** Not "scheduling is hard." A specific moment — "every Sunday night, Sarah spends 90 minutes manually checking which clients she still owes deliverables to, cross-referencing Notion with her email."

3. **Evidence the pain is real.** You've felt this yourself, or you've watched someone live it, or you've read 20 forum posts complaining about it. Not "I bet people would want this."

Don't worry if you're not there yet. Day 2 is literally about making your idea real.

---

## Common Mistakes (Today)

1. **Solving a problem nobody has.** "An AI that suggests good Netflix shows." Netflix already suggests. Nobody is asking for this. Pick a problem you've personally watched someone struggle with, not one that sounds clever.

2. **Picking too big.** "An AI that runs my entire business." Too vague. Narrow it. "An AI that drafts my weekly investor update from my CRM data" is shippable. The big version is not.

3. **Picking too small.** "A button that turns my mouse cursor pink." Too small to need a backend or AI or anything. Stretch up. "A productivity dashboard that integrates my todo list, calendar, and Slack notifications" is buildable.

4. **Optimizing too early.** Don't try to pick the *best* idea today. Pick *an* idea. You can pivot through Day 3. Many do.

---

## What Should Be True After Day 1

- [ ] I have a project folder created inside my cloned course fork (e.g., `teach-one-million/my-onemillion-build/`)
- [ ] I have a `.onemillion/project.json` file with my `product_type` and `idea`
- [ ] I can articulate my idea in 2 sentences to a friend
- [ ] I've picked one of: `web_app`, `ai_agent`, `hybrid`
- [ ] My dev environment is verified working (from getting-started.md)

If all 5 are true, you're done. If any are false, fix that before tomorrow.

---

## Verify Your Day 1

Paste the contents of [`ai-instructions-day-01.md`](./ai-instructions-day-01.md) into your coding harness. It will:
- Check your project.json structure
- Validate your idea is specific enough
- Report pass/needs-revision

If "pass," your Day 1 is locked. If "needs revision," it'll tell you exactly what to fix.

---

## Share It

If you're in a cohort or want to build in public, post in Slack or on LinkedIn:

```
✅ Day 1 done: Picked product type (___) + idea
🎯 Tomorrow: Talking to real users about it
#BuildingWithOneMillion
```

---

## Go Deeper

- **[The Mom Test](https://www.momtestbook.com/)** by Rob Fitzpatrick — short, transforms how you talk to users
- **[Y Combinator's "Make Something People Want"](https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice)** — short essay on why specificity matters
- **Day 1 walkthrough recording note** — Sid should pick his own Day 1 idea live and narrate the process

---

→ **Next:** [Day 2 — Problem + Research](../day-02-problem/learn.md)
