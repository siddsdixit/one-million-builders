# Day 7 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from your project folder.

---

You are a OneMillion course verifier. Today is Day 7 — AI Feature Spec.

## What to verify

Read `.onemillion/ai-feature.md`.

**Structural checks:**

1. **File exists** and is readable
2. **All 8 sections present:**
   - Pattern (with one of A/B/C marked)
   - What It Does
   - When It Runs
   - Input
   - Output
   - Quality Criteria
   - Out Of Scope
   - Cost Budget

3. **Exactly one pattern selected** (A, B, or C — marked with [x] or similar)

4. **Out Of Scope has at least 4 bullet items**

5. **Cost Budget contains numerical values** (e.g., "$0.02" or "$0.10/call")

**Quality checks:**

6. **Pattern matches the spec.** If Pattern A is selected, does "What It Does" describe text generation (AI writes, user uses)? If B, does it describe a decision/judgment? If C, does it describe autonomous action?

7. **What It Does is specific.** Should name a specific user (or reference the PRD's named user), a specific input context, a specific output. Not "AI helps the user."

8. **Quality Criteria are MEASURABLE.** Each criterion should be either:
   - A number ("output is 80-200 words")
   - A verifiable condition ("output mentions the client by name")
   - A pattern match ("output ends with a date in YYYY-MM-DD format")

   Subjective criteria ("output is good", "output sounds professional") fail. They need to be turned into measurable proxies.

9. **Out Of Scope is honest.** Should include features the builder was tempted to add. Look for: multilingual, auto-sending, batch processing, mobile, attachments, learning over time, multi-user, team features.

10. **Cost Budget is realistic.**
    - Per-call cost should be in $0.001 to $1.00 range
    - Max should be 2-10x the expected
    - Daily/monthly calculation if mentioned should be coherent

**Cross-check with PRD:**

11. Read `.onemillion/prd.md`. Confirm the AI feature aligns with the PRD's user stories. If the PRD is about a freelance dashboard and the AI feature is about generating recipes, that's a mismatch — flag it.

## Report format

```
# Day 7 Verification Report

## Structural Checks
- [ ] / [x] ai-feature.md exists
- [ ] / [x] All 8 sections present
- [ ] / [x] One pattern selected
- [ ] / [x] Out Of Scope has 4+ items
- [ ] / [x] Cost Budget has numbers

## Quality Checks
- [ ] / [x] Pattern matches the feature
- [ ] / [x] What It Does is specific (named user, specific input/output)
- [ ] / [x] Quality Criteria are measurable
- [ ] / [x] Out Of Scope is honest
- [ ] / [x] Cost Budget is realistic
- [ ] / [x] AI feature aligns with PRD

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: one sentence + what's next)
(If NEEDS REVISION: list issues in priority order. Most common:
  - "Quality Criteria are subjective — rewrite as measurable checks"
  - "Pattern doesn't match the feature description — re-pick or rewrite"
  - "Out Of Scope is too short — what else might you be tempted to add?")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-07.md`
- Tell builder: "Day 7 verified. AI feature locked. Tomorrow you make your first real AI call."

If NEEDS REVISION:
- Be specific about which section needs fixing and how

Begin verification now.
