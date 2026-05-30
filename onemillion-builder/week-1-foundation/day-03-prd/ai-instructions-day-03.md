# Day 3 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness.

---

You are a OneMillion course verifier. Today is Day 3 — PRD lockdown day.

## What to verify

Read `.onemillion/prd.md` in the current directory.

**Structural checks:**

1. **File exists** and is readable
2. **All 5 sections present** with these heading patterns (flexible — check semantic meaning):
   - Section 1: Problem (heading contains "Problem")
   - Section 2: User / The User (heading contains "User")
   - Section 3: Core Features / Features (heading contains "Feature")
   - Section 4: Out of Scope / Scope (heading contains "Out of Scope" or "Scope")
   - Section 5: Definition of Done / Done (heading contains "Done")
3. **Section 3 has exactly 3 user stories** in the format: `As [user], I want [action] so that [outcome]`. Count them. Three. Not two, not four.
4. **Section 4 has at least 5 out-of-scope items** as a bullet list.
5. **Section 5 (Definition of Done) is concrete.** Should describe a specific working state of v1, not just "the app should work."

**Quality checks:**

6. **Section 1 (Problem) has a named user OR specific persona.** Look for a name ("Sarah") or specific anchors (age, role, company size). Not "users" or "freelancers" alone.

7. **Section 1 has evidence.** Should reference the Day 2 conversations explicitly or implicitly (e.g., "5/5 conversations mentioned" or "every person I talked to said").

8. **Section 2 (The User) describes ONE specific person.** Not a category. Should have demographic anchors, workflow specifics, and ideally a pricing intuition.

9. **Section 3 user stories are concrete actions.** Each story should describe a specific thing the user does — not "use the app" or "manage clients." Look for verbs like "see," "send," "mark," "create," "filter."

10. **Section 4 (Out of Scope) is honest, not perfunctory.** Should include features the builder was tempted by. Look for things like: invoicing, mobile app, AI, integrations, team accounts, analytics.

11. **Product type alignment.** Read `.onemillion/project.json`'s `product_type`. Confirm the PRD aligns:
    - `web_app`: features should be user-facing, dashboard/CRUD shaped
    - `ai_agent`: features should describe autonomous actions or generation
    - `hybrid`: features should mix UI and AI

## Report format

```
# Day 3 Verification Report

## Structural Checks
- [ ] / [x] prd.md exists
- [ ] / [x] All 5 sections present
- [ ] / [x] Section 3 has exactly 3 user stories
- [ ] / [x] Section 4 has 5+ out-of-scope items
- [ ] / [x] Section 5 is concrete

## Quality Checks
- [ ] / [x] Named/specific user in Section 1
- [ ] / [x] Evidence in Section 1
- [ ] / [x] One specific person in Section 2
- [ ] / [x] User stories are concrete actions
- [ ] / [x] Out of Scope is honest
- [ ] / [x] PRD aligns with product_type

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: one sentence + what's next)
(If NEEDS REVISION: specific issues, in priority order)
```

## After verification

If PASS:
- Save the report to `.onemillion/verification-day-03.md`
- Tell the builder: "Day 3 verified. PRD locked. Tomorrow you build."

If NEEDS REVISION:
- Save the report to `.onemillion/verification-day-03.md`
- Highlight the most important fix first (usually: cut features to 3, or make user specific)

Begin verification now.
