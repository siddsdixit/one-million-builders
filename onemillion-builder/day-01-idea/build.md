# Day 1 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**No code today.** Today you run an Idea agent session and create your first PRD.

The harness should not begin with a short intake form. That is too abrupt. Day 1 starts with teaching.

---

## Before You Start

- [ ] Day 0 verified.
- [ ] You are in the cloned course fork.
- [ ] You have read [learn.md](./learn.md).
- [ ] You are ready to think out loud with the Idea agent.

---

## Step 1: Create Your Product Workspace

From the root of your cloned course fork:

```bash
mkdir -p my-onemillion-build/.onemillion
cd my-onemillion-build
```

Keep the product folder inside the cloned course repo unless your harness deliberately updates `.onemillion/state.json`.

---

## Step 2: Ask The Harness To Teach Idea Generation

Paste this:

```text
I am on OneMillion Day 1.

Do not ask me for a short form yet.

Teach me what makes a good product idea:
- unmet user need
- pain point
- user and usage moment
- data sources or formats
- ideal solution
- user stories
- success criteria
- KPIs

Then interview me one question at a time as the OneMillion Idea agent.
Your goal is to help me create:
1. .onemillion/project.json
2. .onemillion/prd.md

After drafting the PRD, ask me to open it, review it, edit anything I disagree with, and save it.
```

The harness should explain before it asks.

---

## Step 3: Answer The Idea Agent Interview

The Idea agent should ask you about these topics one at a time.

Answer in plain language. Rough notes are fine.

```markdown
# Idea Brief

## Raw Idea
[What are you thinking of building?]

## User
[Who has this problem?]

## Pain Point / Unmet Need
[What painful or unmet need drives the idea?]

## Current Workaround
[What do they do today instead?]

## Data Sources / Formats
[What data, files, systems, or formats will the product use?]

## Ideal Solution
[If you close your eyes, what does the finished solution look like?]

## Usage Moment
[When the solution exists, how do users use it?]

## People / Roles
[Who are the users or stakeholders?]

## User Stories
- As a [user], I want to [action] so that [outcome].
- As a [user], I want to [action] so that [outcome].
- As a [user], I want to [action] so that [outcome].

## Success Criteria
[What must be true for v1 to count as working?]

## KPIs
- [Measurable usefulness signal 1]
- [Measurable usefulness signal 2]
- [Measurable usefulness signal 3]
```

The harness should put this into the top of `.onemillion/prd.md` as the idea brief section:

```text
.onemillion/prd.md
```

---

## Step 4: Create `project.json`

The harness should create `.onemillion/project.json` from the idea brief section in the PRD.

Required shape:

```json
{
  "product_type": "web_app",
  "idea": "One or two clear sentences describing the user, pain, and proposed solution.",
  "target_user": "Specific user or role",
  "builder_name": "Your Name",
  "started_at": "2026-05-31"
}
```

`product_type` must be one of:

- `web_app`
- `ai_agent`
- `hybrid`

If you are unsure, choose the smallest honest option. Many first products are `web_app` or `hybrid`.

---

## Step 5: Have The Idea Agent Draft The PRD

Ask the harness:

```text
Use my idea brief to act as the OneMillion Idea agent.

Create a first PRD at .onemillion/prd.md.

The PRD must include:
1. Product summary
2. User and pain point
3. Unmet need
4. Data sources and formats
5. Ideal solution
6. Usage moment
7. User stories
8. Success criteria
9. KPIs
10. Competitive alternatives and market notes
11. TAM/SAM/SOM explained simply
12. Assumptions to validate on Day 2

Do not pretend the research is proven yet. Mark competitor and market sections as first-pass assumptions if you cannot verify them.
```

The Idea agent can use general reasoning and any local context. If it performs web research, it should cite sources in the PRD. If it cannot research live, it should clearly mark market notes as assumptions for Day 2.

---

## Step 6: Review The PRD

Open:

```bash
code .onemillion/prd.md
```

Read it like the product owner.

Ask:

- Do I agree with the user?
- Is the pain real enough?
- Are the data sources realistic?
- Does the ideal solution match what I imagine?
- Do the user stories sound like real behavior?
- Are the KPIs measurable?
- Are TAM/SAM/SOM reasonable enough as first-pass thinking?
- What assumptions need to be tested on Day 2?

Edit anything you disagree with. Then save the file.

---

## Step 7: Update Orchestrator State

Ask the orchestrator to update `.onemillion/state.json`:

```json
{
  "current_day": 1,
  "last_verified_day": 1,
  "product": {
    "builder_name": "[Your name]",
    "product_name": "[Product name or not named yet]",
    "target_user": "[Specific user]"
  },
  "current_blocker": null,
  "next_smallest_action": "Open Day 2"
}
```

---

## Step 8: Run Day 1 Verification

In your terminal, in `my-onemillion-build`:

```bash
claude
```

Ask your harness to run the OneMillion verifier for Day 1.

---

## What Should Be True After Day 1

- [ ] `teach-one-million/my-onemillion-build/` exists.
- [ ] `.onemillion/project.json` exists and is valid JSON.
- [ ] `.onemillion/prd.md` exists with the idea brief and first PRD.
- [ ] PRD includes user, pain, unmet need, data, ideal solution, user stories, success criteria, KPIs, competitive alternatives, TAM/SAM/SOM, and assumptions for Day 2.
- [ ] You opened, reviewed, edited if needed, and saved the PRD.
- [ ] Verification passed.

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 1 complete
- **Last verified day:** Day 1
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 2.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 01.

Here is the step I was trying to complete:
[paste the step heading or instructions]

Here is what happened:
[paste the error, terminal output, or describe what I see]

Diagnose the likely cause and give me the next smallest action.
Do not rewrite unrelated code.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| The harness asks for a short form immediately | Tell it: "Teach idea generation first, then interview me one question at a time." |
| I do not know the data sources yet | Guess honestly and mark them as assumptions to validate on Day 2. |
| TAM/SAM/SOM feels abstract | Keep it directional. SOM, the reachable first audience, matters most right now. |
| The PRD invents facts | Edit them into assumptions or ask the harness to mark them for Day 2 validation. |
| `code` is not found | Open VS Code manually, then open the `my-onemillion-build` folder. |

---

→ **Done with Day 1?** Move to [Day 2 — Validate The PRD](../day-02-validate-prd/learn.md).
