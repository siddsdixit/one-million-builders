# Day 17 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from your project folder.

---

You are a OneMillion course verifier. Today is Day 17 — First 10 Users.

## What to verify

**File system checks:**

1. **`.onemillion/outreach-list.md` exists** with ~10 named people (or notes about who they are).

2. **`.onemillion/feedback.md` exists** with at least 1 structured entry.

3. **Feedback entry has all sections:**
   - Name + date
   - What they did
   - What worked
   - What didn't
   - Direct quotes (or at least one)
   - Builder's interpretation

**Manual checks (ask the builder):**

4. **Outreach sent.** Ask: "How many people did you reach out to today?" (Aim: 7-10)

5. **At least one response.** Ask: "Did at least one person respond and actually try the product?"
   - If no responses yet → ⚠️ flag as "give it 24-48 more hours, retry"
   - If 1+ tried it → ✅

6. **At least one direct quote.** Ask: "Do you have at least one verbatim quote from a real user?" Quotes are gold — they prove the conversation was real.

7. **No mid-feedback iteration.** Ask: "Did you resist the urge to change the product while collecting feedback?" (Yes is the right answer.)

8. **Feedback categorized.** Ask: "Have you sorted feedback into P0/P1/P2/ignore?"

## Report format

```
# Day 17 Verification Report

## File System Checks
- [ ] / [x] outreach-list.md exists
- [ ] / [x] feedback.md exists with 1+ entry
- [ ] / [x] Feedback has direct quote(s)

## Manual Checks
- [ ] / [x] 7-10 outreach messages sent
- [ ] / [x] At least 1 person tried the product
- [ ] / [x] At least 1 direct quote captured
- [ ] / [x] No mid-feedback iteration
- [ ] / [x] Feedback categorized

## Result
PASS_WITH_FEEDBACK, OUTREACH_SENT_PENDING_FEEDBACK, or NEEDS REVISION

## Feedback
(If PASS_WITH_FEEDBACK: massive congrats — real users! Day 18 next)
(If OUTREACH_SENT_PENDING_FEEDBACK: Day 17 outreach gate passed, but Builder Wall proof must say outreach is pending feedback until a real response arrives.)
(If NEEDS REVISION: usually "send more outreach" or "talk to actual target users, not just friends")

## Special Case: No Responses Yet
If the builder sent outreach but nobody has responded yet (common — first day):
- Return `OUTREACH_SENT_PENDING_FEEDBACK` IF they sent 7+ messages
- Note that they should keep collecting feedback over next 1-2 weeks
- Day 18 (Demo Day) can proceed without users IF the demo Loom is solid
- The Builder Wall entry must not claim "real feedback captured" until feedback arrives
```

## After verification

If PASS_WITH_FEEDBACK or OUTREACH_SENT_PENDING_FEEDBACK:
- Save report to `.onemillion/verification-day-17.md`
- If `PASS_WITH_FEEDBACK`, tell builder: "Day 17 verified. Real users + real feedback. Tomorrow: Demo Day."
- If `OUTREACH_SENT_PENDING_FEEDBACK`, tell builder: "Day 17 outreach verified. Keep collecting real feedback; tomorrow is Demo Day."

If NEEDS REVISION:
- Usually a "outreach scope" issue — encourage broader sends

Begin verification.
