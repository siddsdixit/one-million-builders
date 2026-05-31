# Day 12 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 45-90 min. Write tests, run them, lock the AI.**

---

## Before You Start

- [ ] Day 11 verified — RAG working
- [ ] Open the AI feature section in `.onemillion/prd.md` from Day 7 to reference Quality Criteria
- [ ] Anthropic console open in browser to check cost

---

## Step 1: Create The Acceptance Criteria File

In your editor, create `tests/ai-quality.test.ts` or an equivalent eval test in the codebase. Use this template:

```markdown
# AI Feature — Acceptance Criteria + Test Log

## Test Cases

### TC1: [name from Quality Criteria #1]
Setup: [data/context needed]
Action: [what user does]
Expected: [what should be true about output]
Verify: [how to check — automated or manual]
Result: ___

### TC2: ...
### TC3: ...
### TC4 (edge case): ...
### TC5 (edge case): ...

## Cost Check
- Spec budget (Day 7): $___/call
- Actual avg: $___/call
- Daily projected: $___
- Notes:

## Lock Decision
[PASS / NEEDS ITERATION]
[Specific issues if any]

Signed off: [your name] 2026-MM-DD
```

Add 5 test cases. Drag at least 3 from your Day 7 Quality Criteria. Add 2 edge cases (weird input, missing data).

---

## Step 2: Run Each Test Case

For each TC:

1. Set up the test data (sign in as a test user, create the right entities)
2. Trigger the AI feature
3. Look at the output
4. Compare to "Expected"
5. Document PASS / FAIL with a note

Examples:

```markdown
### TC1: Word count (80-200)
Setup: Logged in as test@example.com. Have deliverable "Acme website" due 2026-06-01.
Action: Clicked "Draft Update" on Acme website.
Expected: Output is 80-200 words.
Verify: Pasted output into Word's word count. Got 142.
Result: PASS (142 words)
```

```markdown
### TC4 (edge case): Empty / missing context
Setup: Logged in as new test user with NO data yet.
Action: Tried to click the AI button on... wait, the button doesn't show because there's no data.
Expected: AI should handle this gracefully if reachable.
Verify: Manually. Output: "Please add a deliverable first before generating updates."
Result: PASS — UI correctly hides the button. Defense in depth.
```

Be honest. Some tests will fail. Document the failures.

---

## Step 3: Calculate Cost

Open [console.anthropic.com](https://console.anthropic.com) → **Usage** tab.

Look at the last 7 days. Calculate:

```
Total spend / Total calls = Average cost per call
Average per call × 100 calls/day = Daily projected
Daily projected × 30 = Monthly projected
```

Compare to your Day 7 budget. Document in the Cost Check section.

If you're 2x+ over budget: troubleshoot.

---

## Step 4: Add A Hard Cost Cap

In your API route, add a per-user daily limit:

```bash
claude
```

```
I'm on Day 12 of OneMillion. Add a per-user daily AI call limit to my route at
app/api/ai/[my-feature]/route.ts.

Logic:
1. Before calling the AI, count this user's calls in the last 24 hours
2. If count >= 100, return 429 with message "Daily AI limit reached"
3. After successful call, increment the count (you can use a simple
   `ai_call_log` table in Supabase OR just count from existing data)

Show me the implementation.
```

Test it: temporarily set the limit to 2 and trigger 3 AI calls. The 3rd should fail with the rate limit message.

Then set it back to 100 (or your real limit).

---

## Step 5: Make The Lock Decision

Look at your test results:
- 4-5 of 5 passing → ✅ PASS — lock and move to Days 13-18
- 3 of 5 passing → ⚠️ Decide: iterate prompt (1 hour) or ship with known issues
- ≤2 of 5 passing → ❌ Iterate prompt before Days 13-18. Otherwise Days 13-18 (production hardening) is wasted on a broken AI

Write your decision in the "Lock Decision" section.

---

## Step 6: Commit + Verify

```bash
git add tests/
git add app/api/ai/  # if you updated the route with rate limit
git commit -m "Day 12: AI feature locked + tested"
git push
```

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.

---

## What Should Be True After Day 12

- [ ] AI quality tests/evals exist with 5+ test cases
- [ ] Each test case has all 5 sections + a result
- [ ] Cost check documented with actual numbers
- [ ] Hard cost cap added to API route
- [ ] Lock decision made and committed
- [ ] Verification passed ✅

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 12 complete
- **Last verified day:** Day 12
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 13.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 12.

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
| All 5 tests pass on first try | Tests are too easy. Add harder edge cases. |
| Multiple tests fail | Don't panic. Most are prompt issues. Re-tune system prompt. |
| Cost way over budget | Switch model to Haiku, OR reduce context size in RAG, OR cap output tokens. |
| Can't decide if PASS or NEEDS ITERATION | If 4+/5 pass and cost is sane: PASS. Real users beat perfect tests. |
| Hard cap blocking me during testing | Set limit to a high number during dev (e.g., 1000), lower for production. |

---

## You Just Finished Days 7-12

If you're reading this and your AI is locked: **take 10 minutes. You did Days 7-12.**

You now have:
- A web app (Days 1-6)
- Real authentication (Days 1-6)
- A real database with RLS (Days 1-6)
- A real CRUD feature (Days 1-6)
- A streaming AI feature (Days 7-12)
- AI that takes actions (Days 7-12)
- AI that reads your user's data (Days 7-12)
- Acceptance criteria + cost caps (Days 7-12)

This is more than most products that have a team and a year. You did it in 12 days.

Days 13-18 takes you to production: custom domain, monitoring, landing page, first users.

→ **Next:** [Day 13 — Production Hygiene](../day-13-production-hygiene/learn.md)
