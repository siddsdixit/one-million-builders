# Executive Assistant Persona Audit

This report captures a deeper synthetic pass for executive assistant learners.

## Why This Persona Matters

Executive assistants are a core OneMillion audience because they know painful operational workflows but may be new to terminal, Git, deployment, database, and AI-key concepts.

The EA path must handle:

- browser/spreadsheet-first confidence
- low terminal confidence
- high fear of breaking production-looking systems
- many external accounts
- confidentiality and redaction concerns
- approval-based AI output, never automatic sending by default
- clear visible daily progress
- strong recovery prompts

## Persona Set

The reusable persona file is:

```text
course/tools/personas-executive-assistant.json
```

It includes:

- Maria: first-time builder EA
- Danielle: confidentiality-sensitive EA
- Priya: calendar/operations power-user EA

## Latest Result

Command:

```bash
python3 course/tools/simulate_personas.py \
  --personas course/tools/personas-executive-assistant.json \
  --report course/docs/qa/executive-assistant-persona-report.md
```

Expected pass condition:

- installer passes in fork-like clone
- Day 0 state is created
- Claude `/onemillion` adapter is installed
- Day 1 artifacts pass schema verification
- no unresolved persona-specific friction is found by the scanner

## Interpretation

A passing EA simulation does not prove the entire 18-day course is perfect for EAs. It proves the entry path, Day 0/Day 1 artifacts, and major course surfaces do not currently contradict the EA learning needs encoded in the persona file.

Manual review should still focus on:

- Day 6 app shell and deploy anxiety
- Day 7 auth/database/RLS vocabulary
- Day 11-12 AI privacy and redaction
- Day 14 security/trust review
- Day 18 public-vs-private proof expectations
