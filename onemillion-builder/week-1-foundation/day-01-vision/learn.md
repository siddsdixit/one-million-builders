# Day 1 — Idea Agent + PRD Draft

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Week 1 | ~60-90 min | No code today**

Day 1 is about ideas. Not filling a form. Not rushing into code. Not asking AI to invent a startup for you.

Today you learn how good product ideas work, how to describe one clearly, how to turn it into user stories and success criteria, and how the OneMillion Idea agent turns your raw idea into a first PRD.

---

## Learning Frame

- **Mental model:** A good idea is a response to an unmet user need or painful workflow.
- **What can go wrong:** You describe a solution before you understand the user, pain, data, and success criteria.
- **What to ignore today:** Ignore code, Vercel, Supabase, auth, UI polish, and API keys.

## What You'll Have After Today

- An idea brief in `.onemillion/idea-brief.md`
- A project profile in `.onemillion/project.json`
- A first PRD draft in `.onemillion/prd.md`
- A plain-English understanding of user stories, success criteria, KPIs, and TAM/SAM/SOM
- A reviewed PRD that you either agree with or have edited

---

## Part 1: What Makes A Good Idea?

A good OneMillion idea usually starts with an unmet user need or pain point.

Bad ideas often sound like:

- "An AI app for productivity."
- "A marketplace for everyone."
- "A tool that helps teachers."
- "Something like Notion but better."

These are not bad because they are impossible. They are bad because the user, pain, data, and outcome are unclear.

A stronger idea says:

```text
Teachers lose 30-45 minutes after school turning messy classroom observations into parent-ready progress notes. I want to build a tool that takes short notes, groups them by student, and drafts clear updates the teacher can review before sending.
```

That idea has:

- a specific user: teachers
- a painful moment: after-school progress notes
- a real workflow: messy observations into parent updates
- likely data: classroom notes, student names, learning goals
- a clear solution shape: drafts the teacher reviews

## Part 2: The Idea Inputs

Before the Idea agent can help, it needs raw material from you.

You should be able to describe:

| Input | Question |
|---|---|
| User | Who has the problem? |
| Pain point | What annoying, expensive, risky, or repetitive moment do they experience? |
| Unmet need | What do they wish existed? |
| Current workaround | What do they do today instead? |
| Data | What information, files, systems, or formats would the product use? |
| Ideal solution | If you closed your eyes, what would the finished solution look like? |
| Usage moment | When the solution exists, how would the user actually use it? |
| Success criteria | What must be true for you to say v1 worked? |
| KPI | What measurable signal tells you the product is useful? |

Data can be simple. It might be:

- spreadsheet rows
- PDFs
- emails
- calendar events
- notes
- form submissions
- chat messages
- images
- database records
- user-entered text

The point is to know what the product uses to create value.

## Part 3: User Stories

A user story is a simple way to describe what a user wants and why.

Format:

```text
As a [type of user], I want to [do something] so that [outcome].
```

Example for teachers:

```text
As a teacher, I want to paste rough classroom notes so that I can turn them into organized student updates.

As a teacher, I want to review and edit each drafted update so that I stay in control of what parents receive.

As a teacher, I want to see which students are missing updates so that nobody gets overlooked.
```

User stories matter because they stop the product from becoming vague. They connect the product to real user behavior.

## Part 4: Success Criteria And KPIs

Success criteria describe what must be true for v1 to count as working.

Example:

```text
A teacher can paste rough notes, generate a draft update for each student, edit the draft, and mark it ready to send.
```

KPIs are measurable signals that the product is useful.

Examples:

- A teacher creates 10 student updates in one session.
- Drafting time drops from 45 minutes to under 15 minutes.
- 80% of generated drafts need only light editing.
- A user comes back the next week and uses it again.

Avoid vanity KPIs on Day 1. "Lots of users" is not useful yet. Focus on signals that prove the product solves the painful moment.

## Part 5: TAM, SAM, SOM

The Idea agent may estimate TAM, SAM, and SOM.

These are market-sizing concepts:

| Term | Meaning | Plain English |
|---|---|---|
| TAM | Total Addressable Market | Everyone who could theoretically need this category of solution. |
| SAM | Serviceable Available Market | The part of the market your product could realistically serve. |
| SOM | Serviceable Obtainable Market | The small part you could realistically reach first. |

For this course, SOM matters most. You do not need to win a billion-dollar market on Day 1. You need a reachable first audience with a real pain.

## Part 6: What The Idea Agent Does

Today the Idea agent helps you turn your raw thinking into a first PRD.

It should:

- interview you about the user, pain, data, ideal solution, usage moment, user stories, success criteria, and KPIs
- identify likely competitors and alternatives
- explain TAM/SAM/SOM at a simple level
- draft a PRD
- ask you to open and review the PRD
- revise the PRD until you agree with it

The Idea agent should not force an idea on you. It should help you think clearly.

---

## What Good Looks Like

By the end of Day 1, your idea is not "perfect." It is clear enough to investigate and build from.

Good:

```text
Independent yoga studio owners lose revenue because they forget to follow up with students who attend one class but do not rebook. The product reads class attendance exports and drafts approval-based follow-up messages the owner can review and send.
```

Too vague:

```text
An AI tool for yoga studios.
```

Good:

```text
Teachers spend 30-45 minutes turning messy classroom observations into parent-ready progress updates. The product takes short notes, groups them by student, and drafts updates the teacher reviews before sending.
```

Too vague:

```text
An app for teachers.
```

---

## What Should Be True After Day 1

- [ ] You understand what makes an idea good in OneMillion.
- [ ] `.onemillion/idea-brief.md` exists.
- [ ] `.onemillion/project.json` exists.
- [ ] `.onemillion/prd.md` exists.
- [ ] The PRD includes user, pain, unmet need, data sources, ideal solution, usage moment, user stories, success criteria, KPIs, competitive alternatives, and TAM/SAM/SOM.
- [ ] You opened the PRD, reviewed it, edited anything you disagreed with, and saved it.

---

## Verify Your Day 1

Paste the contents of [`ai-instructions-day-01.md`](./ai-instructions-day-01.md) into your coding harness. It will check the local artifacts and ask whether you reviewed the PRD.

---

## Share It

If you are building in public:

```text
Day 1 of OneMillion done.

I learned how to turn an idea into a product direction and created my first PRD draft.

Building for: [target user]
Pain point: [painful moment]

Tomorrow: research and evidence.
#BuildingWith1M
```

---

## Go Deeper

- **The Mom Test** by Rob Fitzpatrick — useful for Day 2 research.
- **Y Combinator's "Make Something People Want"** — useful framing for unmet needs.
- **Day 1 Loom note** — Sid should show a real Idea agent session and PRD review.

---

→ **Next:** [Day 2 — Validate The PRD](../day-02-problem/learn.md)
