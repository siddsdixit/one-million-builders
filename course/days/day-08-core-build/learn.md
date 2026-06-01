# Day 8 — Core Build

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** debug

Day 8 is where the app becomes useful. Today you complete **one useful sprint** from the plan: one vertical slice that a real user can open, use, save, and come back to.

Do not build a pile of disconnected screens. Do not start AI yet. Finish one meaningful non-AI workflow end to end.

## Learning Frame

- **Mental model:** one useful sprint is a vertical slice: UI, data, auth, validation, states, tests, deploy, and verification all working together.
- **Input:** `.onemillion/architecture.md`, `.onemillion/sprints/`, Day 7 auth/database/RLS, and the live Vercel URL.
- **Output:** one completed core sprint, committed, deployed, and verified locally and live.
- **What can go wrong:** the harness builds too much, skips verification, breaks auth/RLS, ignores the sprint brief, or creates a feature that looks real but does not save useful data.
- **What to ignore today:** ignore AI, redesign, extra features, new architecture decisions, and broad polish. Complete one useful sprint.

## What You Learn

- what a useful sprint is
- vertical slice thinking
- how a sprint brief becomes working code
- CRUD in practice: create, read, update, delete or archive
- how forms, validation, database rows, and UI state fit together
- how to keep auth/RLS working while adding features
- how to verify local behavior and live deployed behavior
- how to review a small commit before moving on

## Core Concepts

### One Useful Sprint

A useful sprint is not a task list. It is a small product outcome.

By the end of the sprint, the user should be able to:

1. open the app
2. complete one real job
3. save data
4. leave and come back
5. see that the app remembered it securely

### Vertical Slice

A vertical slice cuts through the whole product stack. It includes:

- UI screen or component
- form or user action
- validation
- server action or route handler
- Supabase table writes/reads
- ownership or tenant checks
- loading, empty, error, success, and permission states
- verification locally and live

This is better than building "backend first" or "frontend first" because the learner can test real usefulness after each sprint.

### CRUD In Practice

CRUD means create, read, update, delete. In real products, delete may be archive, complete, cancel, or deactivate.

CRUD shows up as:

- create form
- list page
- detail page
- edit action
- status change
- archive/delete action
- validation and error messages

### Sprint Brief As Contract

The build agent should follow one sprint brief from `.onemillion/sprints/`. The sprint brief is the contract. If the brief is unclear, fix the brief or ask the learner before improvising.

### Security Continuity

Day 7 auth does not stop mattering. Every new feature must preserve:

- protected routes
- ownership or tenant boundaries
- RLS policies
- second-user isolation
- no secret leakage

### Definition Of Done

Done means the feature works locally, works live, persists data, handles basic states, respects auth/RLS, and is committed. A feature that only works on the developer machine is not done.

## What You Produce

- one completed useful sprint from `.onemillion/sprints/`
- one core workflow working end to end
- real Supabase data persistence
- local verification
- live Vercel verification after deploy
- one meaningful git commit
- updated `.onemillion/state.json`

## Human Decisions

- core entity fields
- minimum usable workflow
- which sprint brief is the Day 8 target
- which route/screen proves the workflow is useful
- what create/read/update/delete or archive actions are in scope
- which states must be visible today: loading, empty, error, success, permission denied
- what to defer

## Done Checklist

- [ ] exactly one useful sprint is selected and completed
- [ ] core create/read/update/delete or archive workflow works locally
- [ ] data persists in Supabase
- [ ] loading, empty, error, and success states are handled for the core workflow
- [ ] protected routes still reject unauthenticated users
- [ ] second user cannot see first user data when private data exists
- [ ] deployed app works after the feature is pushed
- [ ] live deployed workflow matches the local source/build
- [ ] one meaningful sprint commit exists

## Verify Your Day 8

When the checklist is true, ask your harness to run the OneMillion verifier for Day 8. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 9 — Implementation Review](../day-09-review/learn.md)
