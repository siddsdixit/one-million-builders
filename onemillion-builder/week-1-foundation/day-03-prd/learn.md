# Day 3 — Write Your PRD

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Week 1 | ~45–90 min | Still no code (last day before we start building)**

---

## Learning Frame

- **Mental model:** A PRD turns messy intent into buildable constraints.
- **What can go wrong:** You write a wish list instead of a small, frozen scope.
- **What to ignore today:** Ignore nice-to-have features and future versions.

## What You'll Have After Today

- A **locked PRD** in `.onemillion/prd.md` with 8 sections
- A scoped product type, locked user stories, use cases, KPIs, and out-of-scope
- A clear answer to "is this done?" that you can hold yourself to
- The end of "what if I added..." — scope is locked from here forward

By tomorrow (Day 4) you build. Today you lock what you build.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why PRDs Exist (~10 min read)

**PRD** stands for Product Requirements Document. Every tech company writes one before building. It's not bureaucracy. It's the difference between shipping in 18 days and shipping in 6 months.

A PRD does three things:
1. **Forces you to make decisions** before you start coding
2. **Locks scope** — you can't add features mid-build without a real conversation
3. **Tells the AI exactly what to build** — agentic SDLC depends on a good spec

That last one is the whole game. Vague PRDs produce vague code. The AI is great at executing a clear spec; it's terrible at guessing what you meant. **The quality of your PRD determines the quality of everything that comes after.**

This is the first pillar of agentic engineering: **spec before code**. Never let AI generate without a spec it can validate against.

> 🔧 **Engineers:** You've seen PRDs before. The OneMillion PRD is intentionally lighter than corporate PRDs, but it still includes the pieces agents need: evidence, user stories, use cases, KPIs, scope, and done criteria. Heavier PRDs trigger paralysis in non-engineers. This version is the minimum useful spec.

---

## Part 2: The Eight-Section PRD (~15 min read)

Yours has 8 sections. No more. No less.

### Section 1: Problem
**One paragraph.** Specific pain. Who experiences it. Evidence it's real.

*Not:* "Scheduling is hard for freelancers."
*Yes:* "Freelance designers like Sarah spend ~90 minutes every Sunday cross-referencing Notion, email, and Slack to figure out which deliverables they owe which clients. In my 5 conversations, all 5 mentioned this Sunday-night ritual specifically. One lost an $8K client last year by forgetting to send final files."

What changes between bad and good:
- Named user (Sarah, not "freelancers")
- Specific moment (Sunday night, not "always")
- Specific time (~90 minutes, not "a lot")
- Evidence (5/5 mentioned it, with a specific consequence)

### Section 2: The User
**One specific person.** Not a category. Not "all freelancers." One human, fleshed out.

*Not:* "Freelancers."
*Yes:* "Sarah, 34, freelance UX designer for 3 years. Has 4–6 active clients at a time. Uses Notion to track projects, email + Slack for client communication. Lost a major client last year due to a missed deliverable. Active in r/freelance. Charges $80/hr. Would pay $50/month for a tool that eliminates the Sunday review."

What's in there:
- Demographic anchors (age, role, experience)
- Workflow specifics (Notion, email, Slack — your competition)
- A failure story (gives you the emotional anchor)
- Pricing intuition (anchors what you can charge)

### Section 3: Research Evidence

**What did you learn from Day 2?** Summarize conversation patterns, alternatives, substitutes, workarounds, and competitor gaps.

*Example:*
- 5/5 designers already use Notion or spreadsheets to track deliverables.
- 4/5 said the painful moment is Sunday night review, not daily task entry.
- Existing project management tools feel too broad; the gap is a simple client-deliverable view.

### Section 4: Core Jobs / User Stories — Exactly 3
**Format:** *As [user], I want [action] so that [outcome].*

Three. Not five. Not seven. Three. This is the most important constraint in the entire PRD.

Why three? Because the AI can ship three features cleanly in 6 days (Week 1). It cannot ship seven cleanly in 6 days. People who try to ship seven ship zero. People who ship three ship a product.

*Example (good):*
- As Sarah, I want to see all deliverables I owe across all clients in one dashboard so I never miss a deadline.
- As Sarah, I want to send a quick status update to a client from the same dashboard so I stop switching between Notion and email.
- As Sarah, I want clients to mark a deliverable approved so there's no dispute about whether I finished the work.

*Example (bad — too many, too vague):*
- Tool should help freelancers
- Track time
- Manage clients
- Send invoices
- Get reminders
- Show analytics
- Mobile app

The bad example is what gets you stuck on Day 12 with nothing working. The good example is what gets you shipped on Day 18.

### Section 5: Use Cases

**Real scenarios the product must handle.** These are not features. They are moments from the user's life.

*Example:*
- Sunday review: Sarah opens the dashboard and sees every deliverable due this week, sorted by client and due date.
- Client follow-up: Sarah marks a deliverable sent and sends a status update without opening three separate tools.
- Approval dispute: Sarah can see whether a client approved a deliverable and when.

### Section 6: KPIs / Success Signals

**How you know the product is useful.** Keep these measurable and connected to the pain.

*Example:*
- A new user creates 3+ deliverables in the first session.
- A user sends at least one status update from the dashboard.
- Sarah's weekly review drops from 90 minutes to under 20 minutes.

### Section 7: Out of Scope
**The features you explicitly will NOT build in v1.**

This is as important as the 3 core jobs. Every idea that isn't in Core Jobs goes here. This is where you write down every feature that's tempting but doesn't make the cut.

*Example:*
- **Out of scope (v2 or later):** Invoicing, time tracking, client self-service portal, mobile app, calendar integration, automated follow-ups, AI suggestions, multi-currency, team accounts.

You will be tempted to add these mid-build. The PRD says no. The PRD wins. Add to "v2 or later" wishlist instead.

> 💡 The phrase you'll say out loud most often during the build: **"That's a v2 feature."** Practice it now. It's how you actually ship.

### Section 8: Definition of Done
**What does v1 look like, exactly?** A few sentences. Concrete enough that you'll know when you're done.

*Example:*
> "A freelancer can sign up, add up to 4 clients, create a project under each client with a name + due date, mark deliverables as in-progress / sent / approved, and send a one-click status update via email. The dashboard shows everything they owe, sorted by due date. That's v1. No invoicing. No mobile."

You read this on Day 14 when you're tempted to add "just one more feature." It tells you whether you're done.

---

## Part 3: How To Run Your PRD With AI (~5 min read)

You're going to use your coding harness to help draft your PRD. Two ways to do it:

### Approach 1: Direct draft
You write a rough PRD, Claude critiques it.

```
I'm starting Day 3 of the OneMillion course. Here is my validated PRD from
Day 2: [paste .onemillion/prd.md]. Help me tighten it into a locked PRD with
8 sections: Problem, Target User, Research Evidence,
3 Core Jobs/User Stories, Use Cases, KPIs, Out of Scope, Definition of Done.
Don't add fluff. Push back if any section is vague.
```

Claude will draft. You'll review. Iterate 2-3 times. Done.

### Approach 2: Interview mode
Claude asks you questions, then drafts based on answers.

```
I'm starting Day 3 of OneMillion. Help me write a PRD by asking me
questions one at a time. Section 1 first: the Problem. Ask me what
specific pain my user feels, with evidence.
```

Better for builders who feel stuck. The questions surface things you didn't know to write.

> 💡 **Engineers:** Try Approach 1. EAs and PMs: try Approach 2 first.

After drafting, save to `.onemillion/prd.md`. Don't write directly — let Claude write, then review what came out.

---

## Today's Assignment

1. Draft your PRD using your coding harness (~30 minutes)
2. Save to `.onemillion/prd.md`
3. Lock it — no more pivots from here
4. Run the Day 3 verification

---

## What Good Looks Like (Real Example)

Here's a complete PRD from a previous cohort builder:

```markdown
# DeliverableDash — PRD

## 1. Problem
Freelance designers spend ~90 minutes every Sunday cross-referencing Notion,
email, and Slack to figure out which deliverables they owe which clients.
This causes missed deadlines and lost clients. In my 5 conversations, all 5
mentioned this Sunday review specifically. One lost a $8K client last year
by forgetting to send final files for 2 weeks.

## 2. The User
Sarah, 34, freelance UX designer for 3 years. Has 4–6 active clients at a
time. Uses Notion to track projects, email + Slack for client communication.
Lost a major client last year due to a missed deliverable. Charges $80/hr.
Would pay $50/month for a tool that eliminates the Sunday review.

## 3. Research Evidence
- 5/5 conversation participants described a weekly review ritual.
- 4/5 use Notion or spreadsheets today.
- 3/5 said general project management tools are too heavy for client deliverables.
- The gap is a focused client-deliverable dashboard with low-friction status updates.

## 4. Core Jobs / User Stories
- As Sarah, I want to see all deliverables I owe across all clients in one
  dashboard so I never miss a deadline.
- As Sarah, I want to send a quick status update to a client from the same
  dashboard so I stop switching tools.
- As Sarah, I want clients to mark a deliverable approved so there's no
  dispute about whether I finished the work.

## 5. Use Cases
- Sunday review: Sarah opens the dashboard and sees all deliverables due this week.
- Status update: Sarah marks a deliverable sent and sends a client update from the same screen.
- Approval record: Sarah can tell whether a client approved a deliverable and when.

## 6. KPIs / Success Signals
- A new user creates 3+ deliverables in the first session.
- A user sends one client status update from the app.
- Weekly review time drops from 90 minutes to under 20 minutes.

## 7. Out of Scope (v2 or later)
- Invoicing
- Time tracking
- Client self-service portal
- Mobile app
- Calendar integration
- Automated follow-ups
- AI suggestions (might be added Week 2)
- Team accounts

## 8. Definition of Done
A freelance designer can sign up, add up to 4 clients, create a project
under each client with a name + due date, mark deliverables as in-progress
/ sent / approved, and send a one-click status update via email. The
dashboard shows everything they owe, sorted by due date.

Product type: web_app
```

Two to three pages. Eight sections. Everything decided.

---

## Common Mistakes (Today)

1. **Too many features.** If you have 5+ in the Core Jobs section, you'll fail. Cut to 3. Brutally. The rest go to Out of Scope.

2. **Vague users.** "Freelancers" or "small business owners" — too broad. Pick ONE specific human. The product gets shaped by who you're building for.

3. **No Definition of Done.** Without it, you'll never feel finished. You'll keep adding features and never ship.

4. **Out of Scope is empty.** This means you haven't actually decided what NOT to build. Force yourself to list at least 5 things that aren't in v1.

5. **Skipping the AI assist.** Trying to write this in a vacuum. Use Claude. It's good at this. The point of agentic SDLC is to use the tool.

---

## What Should Be True After Day 3

- [ ] `.onemillion/prd.md` exists
- [ ] All 8 sections present and filled in
- [ ] Core Jobs has exactly 3 user stories in proper format
- [ ] Use Cases has at least 2 realistic scenarios
- [ ] KPIs has at least 2 measurable success signals
- [ ] Out of Scope has at least 5 items
- [ ] You've read your PRD aloud and it sounds like a real product
- [ ] You commit: scope is locked from here

---

## Verify Your Day 3

Paste the contents of [`ai-instructions-day-03.md`](./ai-instructions-day-03.md) into your coding harness. The verifier will:
- Validate all 8 sections exist
- Validate Core Jobs has exactly 3 user stories
- Spot-check quality (named user? specific problem? research evidence? use cases? KPIs? Definition of Done concrete?)
- Report pass / needs revision

---

## Share It

```
✅ Day 3 done: PRD locked with 8 sections + 3 core jobs
🎯 Tomorrow: stack setup + first deploy 🚀
#BuildingWithOneMillion
```

---

## Go Deeper

- **[Marty Cagan on PRDs](https://www.svpg.com/principles-vs-techniques/)** — long-form on what PRDs should and shouldn't do
- **[Linear's PRD template](https://linear.app/method)** — modern, lightweight PRD example
- **[Stripe's "Product Engineering" essay](https://stripe.com/blog)** — what good specs look like

---

→ **Next:** [Day 4 — Stack + First Deploy](../day-04-stack/learn.md)
