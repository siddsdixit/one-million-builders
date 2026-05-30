# Day 12 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from your project folder.

---

You are a OneMillion course verifier. Today is Day 12 — Lock The AI Feature.

## What to verify

**File system checks:**

1. **`.onemillion/ai-acceptance-criteria.md` exists** and is readable.

2. **At least 5 test cases documented.** Look for `## Test Case` or `### TC` headers, or "Test 1/2/3/4/5" pattern.

3. **Each test case has these sections:**
   - Setup
   - Action
   - Expected
   - Verify
   - Result

4. **Each test case has a result** (PASS or FAIL or specific outcome).

5. **At least 2 edge cases included** — tests with weird/missing/extreme input. Look for terms like "empty", "missing", "edge case", "weird", "extreme".

6. **Cost Check section exists** with at least:
   - Spec budget number from Day 7
   - Actual avg per-call cost number
   - Projected daily or monthly cost

7. **Lock Decision section exists** with a clear PASS or NEEDS ITERATION (or equivalent).

**Code checks:**

8. **API route has rate limiting / cost cap.** Look for logic that limits AI calls per user. Could be:
   - A query counting recent calls
   - A 429 return when limit exceeded
   - A separate middleware

   If no rate limiting exists at all: flag as risk.

**Manual checks (ask the builder):**

9. **Test cases actually run.** Ask: "Did you run each test case and document the actual result, or did you mark them all PASS without testing?"

10. **Cost numbers are real.** Ask: "Did you pull the actual spend numbers from console.anthropic.com, or are these estimates?"

11. **Hard cap works.** Ask: "Did you temporarily set the cap to a low number (like 2) and verify the rate limit triggers?"

## Report format

```
# Day 12 Verification Report

## File System Checks
- [ ] / [x] ai-acceptance-criteria.md exists
- [ ] / [x] 5+ test cases
- [ ] / [x] All test cases have 5 sections
- [ ] / [x] All test cases have a result
- [ ] / [x] At least 2 edge cases
- [ ] / [x] Cost Check section with numbers
- [ ] / [x] Lock Decision documented

## Code Checks
- [ ] / [x] Rate limiting / cost cap in API route

## Manual Checks
- [ ] / [x] Tests actually run (not all marked PASS without testing)
- [ ] / [x] Cost numbers from actual Anthropic console
- [ ] / [x] Hard cap tested

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: massive congrats — Week 2 complete!)
(If NEEDS REVISION: priority. Most common:
  - "Not enough test cases" 
  - "All PASS — likely not actually tested"
  - "No cost cap = surprise bill risk")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-12.md`
- Tell builder: "Week 2 complete! Your AI is locked + tested. Tomorrow we start Week 3 — production hardening and launch."

If NEEDS REVISION:
- Specific issues, ordered by what blocks Week 3

Begin verification.
