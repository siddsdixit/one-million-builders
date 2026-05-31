# Day 12 — Lock The AI Feature

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 7-12 | ~45-90 min | The Days 7-12 checkpoint**

---

## Learning Frame

- **Mental model:** An AI feature is shippable when quality, cost, and failure modes are bounded.
- **What can go wrong:** You rely on vibes instead of acceptance criteria.
- **What to ignore today:** Ignore new capabilities; lock what already works.

## What You'll Have After Today

- Measurable AI quality criteria represented in tests or evals in the codebase
- A **cost budget check** — confirmed you're within the budget from Day 7's spec
- A **test log** showing 5+ real AI interactions and their pass/fail against criteria
- **Lock decision:** AI feature is good enough → move to Days 13-18 (Ship & Sell), OR needs more work → iterate

This is your Days 7-12 checkpoint. Before adding production hygiene + custom domain + monitoring (Days 13-18), confirm the AI feature actually works.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why Lock? (~10 min read)

You've spent 5 days adding AI to your app. Streaming, tool use, RAG — all working. Tempting to call it done and move to Days 13-18.

**But you don't know how well it actually works.** You know it produces output. You don't know:
- Does the output meet your Quality Criteria from Day 7?
- Does it fail gracefully when input is weird?
- Does it stay within your cost budget?
- Will it embarrass you in front of real users?

Today is your gut check. Run real tests. Document the results. Decide: ship it, or iterate.

The pillar in action: **validation gates.** Every phase has acceptance criteria. The AI doesn't advance to Days 13-18 (production hardening) until Days 7-12 (functionality) passes.

---

## Part 2: From Quality Criteria → Test Cases (~15 min read)

Open the AI feature section in `.onemillion/prd.md` from Day 7. Look at your Quality Criteria. Each one becomes a test case.

### Example Quality Criteria (from Day 7)
- "Output is 80-200 words"
- "Output mentions the client by name"
- "Output proposes a specific next action with a date"
- "Tone matches Sarah's profile setting"

### Becomes Test Cases (today)

Each test case has:
- **Setup:** what context / data exists
- **Action:** what does the user do
- **Expected:** what should be true about the output
- **How to verify:** word count check? substring check? regex? manual review?

Example:

```markdown
### Test Case 1 — Word count
Setup: Sarah has a deliverable for client Acme due in 5 days, status "in-progress"
Action: Sarah clicks "Draft Update" on the Acme deliverable
Expected: Output is between 80-200 words
Verify: Count words in output. Pass if 80 ≤ count ≤ 200.
Result: ___

### Test Case 2 — Client name mentioned
Setup: Same as above
Action: Same as above
Expected: Output contains the string "Acme" at least once
Verify: substring check
Result: ___

### Test Case 3 — Next action with date
Setup: Same as above
Action: Same as above
Expected: Output contains a date in some recognizable format
Verify: regex for date pattern (\d{4}-\d{2}-\d{2}, "next Friday", "by Tuesday", etc.)
Result: ___

### Test Case 4 — Edge case: minimal context
Setup: Sarah just signed up. Has 1 client, 1 deliverable, no message history
Action: Sarah clicks "Draft Update"
Expected: AI asks for more info OR produces a reasonable first-contact email
Verify: manual review
Result: ___

### Test Case 5 — Edge case: weird input
Setup: Sarah's deliverable name is "????????" (clearly placeholder/typo)
Action: Sarah clicks "Draft Update"
Expected: AI either asks for clarification OR notes the unusual deliverable name
Verify: manual review — should NOT confidently make up details
Result: ___
```

---

## Part 3: Cost Budget Reality Check (~10 min read)

Go to your Anthropic console. Look at your usage for the past few days.

Calculate:
- **Average cost per AI call:** total cost / number of calls
- **Daily burn:** how much you spent in the last 24 hours
- **Projected monthly:** daily × 30

Compare to your Day 7 budget. If you're within: great. If you're over by >2x: you have a cost problem to solve before launch.

### Common Cost Problems
- **Using Sonnet/Opus when Haiku would do.** Swap the model in your route — one line change.
- **Context too big.** Trim the RAG retrieval to only what's needed.
- **Calling AI on every render / form change.** Check your UI isn't accidentally calling the AI route multiple times per user action.
- **No max output tokens.** Set `maxOutputTokens: 400` (or whatever fits) to cap each response.

### Set A Hard Cap In Code

Add this to your API route:

```typescript
// At top of route handler
const dailyCallCount = await getDailyCallCount(user.id);
if (dailyCallCount > 100) {  // your limit
  return Response.json({ 
    error: 'Daily AI limit reached. Resets at midnight.' 
  }, { status: 429 });
}
```

Better: do this per-user, per-day. Stops a single user from burning your whole month's budget.

---

## Part 4: The Lock Decision (~5 min read)

After running your 5+ test cases, make the call:

### Pass Criteria For Locking
- ✅ At least 4 of 5 test cases pass
- ✅ Edge cases either pass OR fail gracefully (no hallucinated data)
- ✅ Cost budget is within Day 7 spec (or you've adjusted the spec realistically)
- ✅ Cross-user data isolation works (RLS confirmed)

### If You Pass
Lock the AI behavior. Commit the tests or evals. Move to Days 13-18 (Ship & Sell).

You can come back and improve the AI later. v1 is good enough. **Shipping > perfect.**

### If You Fail (Some Tests Fail)
You have 3 options:

1. **Iterate the prompt.** Most failures are prompt issues. Spend 30 min tightening Constraints, Tone, Format.
2. **Iterate the spec.** If your Day 7 criteria were too aggressive, soften them honestly (e.g., "output is 80-200 words" → "output is 50-300 words"). Document the change.
3. **Move to Days 13-18 anyway.** With a list of known issues. You can iterate in production. Real users will surface real problems faster than your test cases.

The principle: **honest "good enough" beats fake "perfect."**

---

## Today's Assignment

In [build.md](./build.md):
1. Create `tests/ai-quality.test.ts` or an equivalent eval test in the codebase with at least 5 test cases derived from Day 7 Quality Criteria
2. Run each test case. Document pass/fail.
3. Check your cost in Anthropic console. Compare to budget.
4. Add a hard cost cap to your API route (per-user daily limit).
5. Make the lock decision: ship or iterate.
6. Run Day 12 verification.

---

## What Good Looks Like

A locked AI quality test/eval looks like:

```markdown
# AI Feature — Acceptance Criteria + Test Log

## Test Cases

### TC1: Word count (80-200)
Result: PASS — 142 words on test run 2026-05-12

### TC2: Client name mentioned
Result: PASS — "Acme" mentioned 3x

### TC3: Specific date proposed
Result: PASS — "by next Friday" found

### TC4: Edge case — minimal context
Result: PASS — AI asked: "What status would you like to communicate?"

### TC5: Edge case — typo in deliverable name
Result: PASS — AI noted "I noticed the deliverable name looks unusual..."

## Cost Check
- Spec budget (Day 7): $0.02/call
- Actual avg: $0.03/call (Sonnet, 600 tokens avg)
- Acceptable (close to spec). Will monitor in Days 13-18.
- Hard cap added: 100 calls/user/day.

## Lock Decision
✅ AI feature passes 5/5 test cases.
✅ Cost within tolerance.
✅ Ready for Days 13-18.

Signed off: [your name] 2026-05-12
```

---

## Common Mistakes (Today)

1. **Too few test cases.** Three test cases means you have three blind spots. Aim for 5+, including 2 edge cases.

2. **All test cases pass — suspicious.** If everything passes on the first try, you probably wrote weak test cases. Add harder ones (weird inputs, missing data, deliberately ambiguous requests).

3. **Skipping the cost check.** Builders launch with no idea what their AI costs. They get a surprise Anthropic bill in week 4. Add the hard cap today.

4. **Pretending failures are passes.** Be honest with yourself. If TC3 says "output must propose a date" and the output sometimes doesn't, that's a FAIL. Document it. Decide if it's a blocker.

5. **Trying to perfect before shipping.** v1 doesn't need to be perfect. Real users surface real bugs. Lock something reasonable and ship.

---

## What Should Be True After Day 12

- [ ] AI quality tests/evals exist with 5+ test cases
- [ ] Each test case has setup + action + expected + verify method + result
- [ ] Cost check is documented (actual vs spec budget)
- [ ] Hard cost cap added to API route
- [ ] Lock decision made (PASS or iterate plan documented)
- [ ] Committed to git
- [ ] Verification passed ✅

---

## Verify Your Day 12

Ask your harness to run the OneMillion verifier for this day.

---

## Share It

```
✅ Days 7-12 done: AI feature locked + tested. Real users next week.
🎯 Days 13-18: production hygiene + custom domain + landing page + first users
#BuildingWith1M
```

You're 2/3 done. Take the win. The hardest week is behind you.

---

## Go Deeper

- **[Eval-Driven Development](https://hamel.dev/blog/posts/evals/)** — Hamel Hussain on evaluating AI systems
- **[LLM Acceptance Testing](https://www.braintrust.dev/docs)** — Braintrust's approach (good when you scale beyond 5 tests)
- **[Cost Optimization Patterns](https://www.anthropic.com/customers)** — Anthropic on prompt caching, batch APIs, etc.

---

→ **Next:** [Day 13 — Production Hygiene](../day-13-production-hygiene/learn.md)
