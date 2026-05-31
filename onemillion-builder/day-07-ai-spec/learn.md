# Day 7 — What Is An AI Feature

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 7-12 | ~30–60 min | The thinking before the AI**

---

## Learning Frame

- **Mental model:** An AI feature needs a spec before it needs a model call.
- **What can go wrong:** You describe the AI vaguely and cannot judge quality later.
- **What to ignore today:** Ignore implementation; lock role, goal, inputs, constraints, output, and quality bar.

## What You'll Have After Today

- A clear answer to "what AI feature am I adding to my app?"
- A 1-page **AI Feature Spec** inside `.onemillion/prd.md`
- An understanding of three AI patterns and which one fits your product
- A locked decision — no scope creep on AI features for the rest of Days 7-12

Today is no-code again. We pick what you'll build, the same way Day 1 picked the product. Pick well now → Days 8-12 fly. Pick badly → spend Days 8-12 reworking.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Three Patterns Of AI Features (~15 min read)

When people say "I want to add AI" they usually mean one of three things. The patterns look similar from the outside but require very different code. Pick the wrong one and you'll spend a week building the wrong thing.

### Pattern A: Text Generation
**The AI writes text for the user, who then uses it.**

Examples:
- "Draft a follow-up email to this client" (CRM tool)
- "Write a summary of this week's deliverables" (project tool)
- "Suggest 3 names for my new product" (brainstorming tool)
- "Rewrite this paragraph more professionally" (writing tool)

The user provides context. The AI generates text. The user reviews + edits + uses the output. **AI is an assistant, not an agent.** Lowest complexity to build.

**Build cost (Days 7-12):** 1-2 days of the 6.

### Pattern B: Decision-Maker
**The AI looks at data and chooses something for the user.**

Examples:
- "Which of my 30 unread emails actually need a reply?" (inbox tool)
- "Which of my 50 leads should I follow up with today?" (CRM)
- "Which of my projects is most at risk of missing deadline?" (PM tool)
- "Which articles should I read first?" (reading tool)

The user provides data. The AI applies judgment + reasoning. The user trusts (or overrides) the choice. **AI is a co-pilot with opinions.** Medium complexity.

**Build cost:** 2-3 days.

### Pattern C: Agent
**The AI takes actions in the world, not just suggests them.**

Examples:
- "Automatically reply to scheduling emails with my available times" (calendar agent)
- "Watch competitor pricing pages every Monday and email me a diff" (monitor agent)
- "Read my Slack and post a Monday morning summary to my team channel" (digest agent)
- "When a new lead lands in my CRM, do this 5-step enrichment workflow" (workflow agent)

The user defines goals + permissions. The AI acts autonomously. The user reviews the actions taken (and rolls back if wrong). **AI is doing the work.** Highest complexity.

**Build cost:** 3-4 days. Also the most exciting outcome.

---

## Part 2: Which Pattern Fits Your Product? (~10 min read)

Look at your PRD from Day 3. Look at your 3 user stories.

### If your user stories sound like:
- "...so they can write..." → Pattern A (Text Generation)
- "...so they can quickly review and decide..." → Pattern A or B
- "...so they can know what to focus on..." → Pattern B (Decision-Maker)
- "...so they don't have to do X manually..." → Pattern C (Agent)
- "...without me having to be involved..." → Pattern C

### Real Examples From Previous Builders

| Product | Days 1-6 (No AI) | Days 7-12 AI Feature | Pattern |
|---------|----------------|-------------------|---------|
| Freelance Deliverable Dashboard | CRUD on deliverables | "Draft a status update to client X about deliverable Y" | A (Text Generation) |
| Habit Tracker | CRUD on habits | "Tell me which habit I'm slipping on and why, based on my last 30 days" | B (Decision-Maker) |
| Inbox Triage Tool | CRUD on emails saved | "Auto-categorize emails as Urgent / Reply / Archive based on sender + content" | B (Decision-Maker) |
| Daily Briefing Tool | CRUD on data sources | "Every morning at 7am, generate my briefing automatically and email it to me" | C (Agent) |
| Recipe Saver | CRUD on recipes | "Tell me what I can cook tonight from the ingredients I have, drawing from my saved recipes" | B (Decision-Maker, with retrieval) |

> 💡 **Most first products use Pattern A or B.** Pattern C (agents) is more exciting but harder. If you're not sure, pick A or B — you can always add agent behavior later (your next product).

---

## Part 3: Why The Spec Matters (~5 min read)

Same lesson as Day 3 (the PRD), restated for AI:

**Vague prompt → vague AI output.**

If your AI feature spec says "AI helps the user write emails," your code on Day 8 will produce mediocre results because the AI doesn't know what *kind* of emails, in what *tone*, with what *constraints*, in what *format*.

If your spec says: *"Generate a follow-up email to a freelance client who hasn't responded to my last 2 messages. Tone: friendly-but-professional. Format: 3 paragraphs max, end with a clear next step + a deadline. Always include the deliverable name and the date it was sent."* — your code on Day 8 produces something useful immediately.

Same code. Different spec. Wildly different output quality.

This is the second pillar of agentic SDLC in action: **spec before code, especially for AI.**

---

## Today's Assignment

Add `## AI Feature Spec` to `.onemillion/prd.md` with these sections:

```markdown
# AI Feature Spec

## Pattern (pick one)
[ ] A — Text Generation
[ ] B — Decision-Maker
[ ] C — Agent

## What It Does
[One paragraph. Specific. With the named user from your PRD.]

## When It Runs
[On-demand? When user clicks button? Automatically every morning? On data change?]

## Input
[What context does the AI receive?
- User's profile? 
- A specific entity (e.g., one deliverable, one habit)?
- Multiple entities (their last 30 days)?
- External data (current date, etc.)?
- A user prompt?]

## Output
[What does the AI return?
- Plain text?
- Structured data (JSON)?
- A list of options the user picks from?
- A boolean (yes/no decision)?
- An action it took?]

## Quality Criteria
[How will I know the AI is doing well?
- "Output is under 150 words" (measurable)
- "Output mentions the client's name" (verifiable)
- "Output suggests a specific next action" (verifiable)
- "When user gives feedback 'this is wrong,' AI explains why" (graceful failure)]

## Out Of Scope
[What this AI feature will NOT do — same logic as the PRD's Out Of Scope]

## Cost Budget
[Expected cost per AI call. Most builders: $0.01-0.05/call. Set a max: "If a call costs more than $0.10, alert me."]
```

---

## What Good Looks Like

Here's a real AI feature spec from a previous builder, building on the Sarah-the-freelancer example:

```markdown
# AI Feature Spec — Client Status Update Generator

## Pattern
[x] A — Text Generation

## What It Does
When Sarah clicks "Draft Update" on a deliverable in her dashboard, Claude
generates a 3-paragraph email to that client. The email summarizes what's
been done, what's outstanding, and proposes a clear next step + deadline.
Sarah reviews + edits + sends manually (we don't auto-send).

## When It Runs
On-demand. User clicks a "Draft Update" button on any deliverable.

## Input
- The deliverable name + status + last update date
- The client name + history of deliverables for this client
- Sarah's typical tone (loaded from her profile — set once during onboarding)
- Current date (so AI can write "Following up on..." or "Quick check-in...")

## Output
Plain text email, 3 paragraphs:
1. Opening (1 sentence acknowledging context)
2. Middle (status + what's outstanding)
3. Closing (proposed next step + specific deadline + sign-off)

Output is editable in a text area. Sarah sends manually.

## Quality Criteria
- Output is 80-200 words (auto-truncate if over)
- Output mentions the client by name (verify with substring check)
- Output proposes a specific next action with a date (verify with regex for date pattern)
- Tone matches Sarah's profile setting (subjective — Sarah grades 1-5)
- If feedback says "wrong tone," AI explains what it picked up and adjusts

## Out Of Scope
- Auto-sending emails (manual review required, always)
- Cross-client batching (one email at a time)
- Multilingual support (English only for v1)
- Tone learning over time (just uses initial profile setting)
- Attaching files
- Following email threads (treats each as a fresh draft)

## Cost Budget
- Expected: $0.02 per email draft (Claude Haiku) or $0.10 (Claude Sonnet)
- Max: $0.15. Alert me if a single call exceeds this.
- Daily limit: Sarah generates ~10 drafts/day → ~$0.50/day → ~$15/month
```

That's the level of detail you want. Specific. Testable. Bounded.

---

## Common Mistakes (Today)

1. **Picking Pattern C because it sounds cooler.** Agents are harder. If you can solve your user's problem with Pattern A or B, do it. Save Pattern C for product #2.

2. **Vague "What It Does."** "AI helps the user" is not a spec. Name the user, name the input, name the output, name the moment.

3. **No Quality Criteria.** Without measurable criteria, you'll spend Days 8-12 unable to tell if your AI is working or hallucinating.

4. **No Cost Budget.** AI calls aren't free. Without a budget you'll be surprised by your Anthropic bill. (You also need this for Day 17 when you launch — uncapped AI is how startups burn through $50K in a weekend.)

5. **Out Of Scope is empty.** Same trap as the PRD. Force yourself to list things the AI will NOT do.

---

## What Should Be True After Day 7

- [ ] `.onemillion/prd.md` includes `## AI Feature Spec`
- [ ] You've picked one pattern (A, B, or C) and marked it
- [ ] Each section has at least 2-3 sentences
- [ ] Quality criteria are measurable (not subjective)
- [ ] Cost budget has a per-call number and a max
- [ ] Out Of Scope has at least 4 items
- [ ] You've read your AI Feature Spec aloud and it sounds buildable
- [ ] Verification passed ✅

---

## Verify Your Day 7

Ask your harness to run the OneMillion verifier for this day.
- Check the PRD includes the AI feature spec with all sections
- Validate the pattern matches your PRD's user stories
- Check Quality Criteria are measurable
- Check Cost Budget has numbers
- Report pass / needs revision

---

## Share It

```
✅ Day 7 done: AI feature locked. Pattern [A/B/C]: [one-sentence description]
🎯 Tomorrow: writing my first prompt
#BuildingWith1M
```

---

## Go Deeper

- **[Anthropic's Cookbook — building with Claude](https://github.com/anthropics/anthropic-cookbook)** — real patterns from Anthropic engineering
- **[OpenAI's Guide to Prompt Design](https://platform.openai.com/docs/guides/prompt-engineering)** — universal principles
- **[The Three Types of AI Apps](https://www.latent.space)** — useful taxonomy for thinking about AI features

---

→ **Next:** [Day 8 — First AI Call + Prompt Design](../day-08-first-ai-call/learn.md)
