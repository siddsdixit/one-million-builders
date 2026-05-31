# Day 3 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness.

---

You are a OneMillion course verifier. Today is Day 3 — PRD lockdown day.

## What to verify

Read `.onemillion/prd.md` in the current directory.

**Structural checks:**

1. **File exists** and is readable
2. **All 8 sections present** with these heading patterns (flexible — check semantic meaning):
   - Section 1: Problem (heading contains "Problem")
   - Section 2: Target User / The User (heading contains "User")
   - Section 3: Research Evidence (heading contains "Research" or "Evidence")
   - Section 4: Core Jobs / User Stories / Core Features (heading contains "Job", "Story", or "Feature")
   - Section 5: Use Cases (heading contains "Use Case" or "Scenario")
   - Section 6: KPIs / Success Signals (heading contains "KPI", "Metric", or "Success")
   - Section 7: Out of Scope / Scope (heading contains "Out of Scope" or "Scope")
   - Section 8: Definition of Done / Done (heading contains "Done")
3. **Core jobs section has exactly 3 user stories** in the format: `As [user], I want [action] so that [outcome]`. Count them. Three. Not two, not four.
4. **Use cases section has at least 2 realistic scenarios.**
5. **KPI/success section has at least 2 measurable success signals.**
6. **Out of Scope has at least 5 out-of-scope items** as a bullet list.
7. **Definition of Done is concrete.** Should describe a specific working state of v1, not just "the app should work."

**Quality checks:**

8. **Problem has a named user OR specific persona.** Look for a name ("Sarah") or specific anchors (age, role, company size). Not "users" or "freelancers" alone.

9. **Problem has evidence.** Should reference the Day 2 conversations explicitly or implicitly (e.g., "5/5 conversations mentioned" or "every person I talked to said").

10. **Target User describes ONE specific person.** Not a category. Should have demographic anchors, workflow specifics, and ideally a pricing intuition.

11. **User stories are concrete actions.** Each story should describe a specific thing the user does — not "use the app" or "manage clients." Look for verbs like "see," "send," "mark," "create," "filter."

12. **Use cases connect to real situations from notes/research.** They should not be generic "happy path" placeholders.

13. **KPIs measure usefulness, not vanity.** Good examples: activation, time saved, task completion, weekly active use, conversion from outreach to use.

14. **Out of Scope is honest, not perfunctory.** Should include features the builder was tempted by. Look for things like: invoicing, mobile app, AI, integrations, team accounts, analytics.

15. **Product type alignment.** Read `.onemillion/project.json`'s `product_type`. Confirm the PRD aligns:
    - `web_app`: features should be user-facing, dashboard/CRUD shaped
    - `ai_agent`: features should describe autonomous actions or generation
    - `hybrid`: features should mix UI and AI

## Report format

```
# Day 3 Verification Report

## Structural Checks
- [ ] / [x] prd.md exists
- [ ] / [x] All 8 sections present
- [ ] / [x] Core jobs section has exactly 3 user stories
- [ ] / [x] Use cases section has 2+ scenarios
- [ ] / [x] KPI/success section has 2+ measurable signals
- [ ] / [x] Out of Scope has 5+ items
- [ ] / [x] Definition of Done is concrete

## Quality Checks
- [ ] / [x] Named/specific user in Problem
- [ ] / [x] Evidence in Problem/Research
- [ ] / [x] One specific person in Target User
- [ ] / [x] User stories are concrete actions
- [ ] / [x] Use cases are realistic
- [ ] / [x] KPIs measure usefulness
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
