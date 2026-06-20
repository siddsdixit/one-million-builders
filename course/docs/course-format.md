# Course Format

OneMillion is a GitHub-native, harness-taught course. The repo is the source of truth, and the learner's coding harness acts as the tutor.

The learning surface should stay small:

```text
START-HERE.md -> current day README.md -> build.md -> stuck.md if needed -> day done
```

## Roles

| Layer | Job |
|---|---|
| GitHub repo | Source of truth, fork, proof trail, public artifact. |
| Coding harness | Tutor, guide, implementer, verifier. |
| `course/course-manifest.json` | Machine-readable course map and completion gates. |
| `course/days/single.md` | Narrative explanation of the whole journey. |
| Day `README.md` | Learner cockpit for the day. |
| Day `learn.md` | Conceptual explanation. |
| Day `build.md` | Step-by-step work guide. |
| Day `stuck.md` | Recovery prompts and common failures. |
| `.onemillion/state.json` | Progress, verification status, and resume point. |

## Daily Learner Loop

Every day should feel the same:

1. Open the day `README.md`.
2. Read the outcome, decisions, and done checklist.
3. Ask the harness to teach the day.
4. Follow `build.md` one step at a time.
5. Use `stuck.md` when blocked.
6. Review artifacts or code before accepting them.
7. Say `day done`.
8. Harness verifies the manifest gate.
9. Commit meaningful progress.

The repeated loop is intentional. Predictability reduces cognitive load.

## Harness Behavior

The harness is a tutor, not a silent worker.

It should:

- teach before building
- ask for product decisions
- guide external tool steps instead of hiding them
- make small inspectable changes
- show what changed
- verify before advancing

It should not:

- invent learner decisions
- skip the current day cockpit
- create unnecessary paperwork
- advance on incomplete gates
- treat file existence as proof of learning

## Maintainer Rule

When adding or changing a day, update these together:

1. `course/course-manifest.json`
2. `course/days/single.md`
3. `course/days/day-XX-*/README.md`
4. `course/days/day-XX-*/learn.md`
5. `course/days/day-XX-*/build.md`
6. `course/days/day-XX-*/stuck.md`

If those files disagree, the learner and harness will disagree too.
