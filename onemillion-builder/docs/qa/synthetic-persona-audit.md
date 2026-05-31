# Synthetic Persona Course Audit

Date: 2026-05-30

This report captures a Codex-led synthetic QA pass of the OneMillion Builder course using both automated simulators and read-only subagent persona audits.

## Scope

The audit asked whether a learner can start from the GitHub course page, fork and clone correctly, open the repo in a coding harness, install the course adapters, complete Day 0/Day 1, and continue with a clear mental model of the course.

Personas covered:

- Non-technical operator / first-time builder
- Product manager / founder
- Designer-founder
- Experienced engineer
- Career changer

## Automated Result

`simulate_personas.py` passed all 5 personas:

- fork-like clone install succeeds
- Day 0 state is created
- Claude `/onemillion` command adapter is installed
- Day 1 project artifacts are created
- Day 1 schema verification passes

The generated machine report lives at:

```text
onemillion-builder/docs/qa/persona-simulation-report.md
```

The broader simulator also passed:

- downloaded/plain-folder install is blocked
- upstream-origin install is blocked
- fork-like clone install succeeds
- Day 0 state is created
- Day 1 schema verifier passes
- Day 4 deployment/source matching verifier passes against a mock live URL

## Subagent Findings

### Non-Technical Builder

Main risks found:

- fork, clone, origin, upstream, and downstream needed plain-English definitions
- `my-onemillion-build` location was not obvious enough
- harness docs could bypass Day 0 by saying "start Day 1"
- one harness guide cloned Sid's upstream directly
- Day 1 Vercel URL language made an optional psychological win sound like a hard verifier gate

Fixes made:

- added a tiny Git glossary to `START-HERE.md`
- made `teach-one-million/my-onemillion-build` the explicit workspace model
- changed harness prompts to start at Day 0 and enforce preflight
- changed harness README clone command to use the learner fork
- reframed the Day 1 Vercel template deploy as optional stretch/disposable proof

### Product Manager / Founder

Main risks found:

- Day 0 was mandatory but not clearly modeled as a verified preflight day
- course fork, product repo, Day 1 URL, Day 4 URL, and optional custom domain could compete as "the proof"
- Week 2 could feel like all advanced AI concepts are mandatory
- Day 17 could imply real feedback even when only outreach was sent
- Builder Claim issue template was missing fields from the claim packet

Fixes made:

- added `preflight_day` to `course-manifest.json`
- updated `AGENTS.md` so `day done` can verify Day 0 and advance to Day 1
- clarified Day 1 Vercel URL as optional/disposable
- split Day 17 result into `PASS_WITH_FEEDBACK` and `OUTREACH_SENT_PENDING_FEEDBACK`
- added missing claim fields to `.github/ISSUE_TEMPLATE/builder-claim.yml`

Remaining recommendation:

- add a future "minimum shippable AI path" note to Week 2 that distinguishes one required useful AI action from optional streaming/RAG/tool depth.

### Experienced Engineer

Main risks found:

- manifest starts at Day 0 but `days` begins at Day 1
- Claude Code docs promised `/onemillion`, but installer did not create `.claude/commands/onemillion.md`
- verification docs implied 18 automated checks even though schema-backed CLI checks currently exist for Days 1-6
- API key doc suggested a temporary text file

Fixes made:

- represented Day 0 as `preflight_day` outside the 18 build-day list
- added `.claude/commands/onemillion.md` generation to `install-agents.sh`
- added uninstall cleanup for the command adapter
- updated verification docs to distinguish schema-backed Days 1-6 from prompt/human-reviewed Days 7-18
- removed temporary text-file API key guidance

## Current QA Commands

Run these before publishing major course changes:

```bash
python3 -m json.tool onemillion-builder/course-manifest.json >/tmp/course-manifest.checked
python3 onemillion-builder/tools/course_quality_check.py
python3 onemillion-builder/tools/simulate_course.py
python3 onemillion-builder/tools/simulate_personas.py --report onemillion-builder/docs/qa/persona-simulation-report.md
```

## Residual Risks

- Days 7-18 are not schema-backed yet. The course is honest about this now, but future Builder Wall automation should add machine checks for the later days.
- Week 2 may still feel heavy for true beginners. The course should eventually provide a minimum shippable AI path and mark streaming/RAG/tool depth as product-dependent.
- A real end-to-end learner simulation should eventually create a throwaway Next.js app, push to a test GitHub repo, deploy to Vercel, and verify Supabase/API-key setup with disposable credentials.

## Follow-Up: Harness Teaching Experience

A real dry run showed a major experience gap: after preflight, the harness could still respond like a task runner instead of a teacher. The bad pattern was:

```text
Preflight passed. You are at Day 0. Make a commitment, then say day done.
```

The course now treats this as a regression. The required behavior is:

- greet the learner properly
- explain what OneMillion is
- explain the AI/human contract
- introduce the current day
- provide copy-ready actions
- define what counts as done
- tell the learner when to say `day done`

The canonical rule lives in `onemillion-builder/docs/teaching-protocol.md`, and `simulate_personas.py` now checks for the required teaching-surface terms.
