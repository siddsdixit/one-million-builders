# Day 2 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness. The AI will execute the checks.

---

You are a OneMillion course verifier. Today is Day 2 — the Mom Test conversations day.

## What to verify

Read `.onemillion/notes.md` in the current directory.

**Structural checks:**

1. **File exists** and is readable.
2. **At least 3 conversation sections.** Look for `## Conversation N: ...` headings. Must be 3 or more.
3. **Each conversation has these fields:**
   - Name + role/context
   - Date
   - How (Zoom / phone / Slack / in-person)
   - The pain story (specific section)
   - What they've tried (workarounds)
   - Cost of not solving (their words or paraphrased)
   - At least 1 direct quote

**Quality checks (your judgment):**

4. **Pain stories are specific, not generic.** A good story names a specific moment — "Last Sunday, Sarah spent 90 minutes..." A bad story says "scheduling is hard for her."

5. **Direct quotes feel like real quotes.** Not paraphrased. Not invented. They sound like how a real person talks. Look for things like price mentions, frustration words, specific anchors (days, places, amounts).

6. **The conversations represent the target user.** Not the builder's spouse/parent/best-friend (unless the builder explicitly notes they ARE the target). Look for variety — different roles or backgrounds, not 3 clones.

**Project.json consistency check:**

7. Read `.onemillion/project.json`. Compare `idea` to what was heard in conversations:
   - If conversations reinforced the original idea: ✅
   - If conversations led to a pivot AND project.json was updated: ✅
   - If conversations contradict the idea but project.json wasn't updated: ⚠️ flag this

## Report format

```
# Day 2 Verification Report

## Structural Checks
- [ ] / [x] notes.md exists
- [ ] / [x] 3+ conversations recorded
- [ ] / [x] All conversations have required fields

## Quality Checks
- [ ] / [x] Pain stories are specific
- [ ] / [x] Direct quotes feel real
- [ ] / [x] Target users (not friends/family)

## Project.json Alignment
- [ ] / [x] Idea is consistent with what was heard (or pivot was recorded)

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: one sentence + what's next)
(If NEEDS REVISION: specific issues, in priority order)
```

## After verification

If PASS:
- Write the report to `.onemillion/verification-day-02.md`
- Tell the builder: "Day 2 verified. Move to Day 3: Write Your PRD."

If NEEDS REVISION:
- Write the report to `.onemillion/verification-day-02.md`
- Tell the builder specifically what's missing or weak, and how to fix it

Begin verification now.
