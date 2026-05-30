# Course QA Tools

Use these tools before publishing major course changes.

## Full Course Quality Check

```bash
python3 onemillion-builder/tools/course_quality_check.py
```

Checks internal links, day file structure, manifest integrity, harness entrypoints, and required course architecture.

## Synthetic Learner Simulation

```bash
python3 onemillion-builder/tools/simulate_course.py
```

This creates throwaway repos under `/tmp` and simulates:

- downloaded/plain-folder install is blocked
- upstream-origin install is blocked
- fork-like clone install succeeds
- Day 0 preflight state is created
- Day 1 artifacts pass schema verification
- deployment/source matching verification works against a mock live URL

Keep the temp directory for debugging:

```bash
python3 onemillion-builder/tools/simulate_course.py --keep
```

Passing the simulator does not prove the whole 18-day course is perfect. It proves the most important learner entry path, preflight gate, and verifier plumbing are not broken.

## Persona Simulation

```bash
python3 onemillion-builder/tools/simulate_personas.py --report onemillion-builder/docs/qa/persona-simulation-report.md
```

This runs the course entry path as several synthetic target learners:

- non-technical operator
- product manager
- designer-founder
- experienced engineer
- career changer

It creates throwaway local course forks, runs the installer, creates Day 1 artifacts, runs verification, and scans the course for persona-specific friction. The markdown report is intended to be checked before publishing major course changes.
