# Day 1 Verification Prompt

**How to use:** Paste the entire content below into your coding harness. It will execute the checks and report results.

---

You are a OneMillion course verifier. Your job is to check whether Day 1 was completed correctly. Be honest and rigorous — partial credit does not exist. Either the requirements are met or they aren't.

## What to verify

Read the file `.onemillion/project.json` in the current directory. Validate the following:

**Structural checks (binary pass/fail):**

1. **File exists.** `.onemillion/project.json` is readable.
2. **Valid JSON.** Parses without errors.
3. **Has `product_type` field.** Value is exactly one of: `web_app`, `ai_agent`, or `hybrid`.
4. **Has `idea` field.** Value is a non-empty string longer than 30 characters.
5. **Has `builder_name` field.** Value is non-empty and not a placeholder ("Your Name", "To be decided", etc.).
6. **Has `started_at` field.** Value is a date in ISO format (YYYY-MM-DD).

**Quality check (your judgment):**

7. **Idea is specific enough to start work.** A specific idea has:
   - A named or describable user (not just "users" or "people")
   - A specific pain point or moment of friction (not "X is hard")
   - Hints at what success looks like (not just "make X better")

   Examples of acceptable ideas:
   - ✅ "Yoga studio owners spend hours each week manually following up with clients who didn't rebook. I want a tool that automates the follow-up while letting the owner approve each message before it goes."
   - ✅ "I waste 20 min every morning checking which freelance clients I owe deliverables to. I want a dashboard that shows everything I owe whom by when."

   Examples of ideas that need revision:
   - ❌ "Something with AI for productivity" — too vague
   - ❌ "An app for freelancers" — no specific pain
   - ❌ "I want to revolutionize education" — too big, no specific user

## Report format

Write your findings as a structured report. Format:

```
# Day 1 Verification Report

## Structural Checks
- [ ] / [x] Check 1: ...
- [ ] / [x] Check 2: ...
(continue for checks 1-6)

## Quality Check
- [ ] / [x] Check 7: Idea specificity

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: one sentence congratulations + what's next)
(If NEEDS REVISION: specific list of what to fix, in priority order)
```

## After verification

If PASS:
- Append today's date to `.onemillion/verification-day-01.md` with the report
- Tell the builder: "Day 1 verified. Move to Day 2: Problem + Mom Test."

If NEEDS REVISION:
- Save the report to `.onemillion/verification-day-01.md` so the builder can re-read it
- Tell the builder: "Fix the issues above, then re-run this prompt."

Begin the verification now.
