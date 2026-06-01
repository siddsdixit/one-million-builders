# Day 6 — App Shell + First Deploy

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** debug, ship

Day 6 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** App Shell + First Deploy turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- create the app from the plan
- understand repo structure
- apply MUI baseline
- deploy frontend to Vercel
- verify live source matches local code

## Core Concepts

- First deploy creates the feedback loop: local code -> GitHub -> Vercel -> live URL.
- The app shell should reflect the design system before feature work begins.
- A deployment only counts if the live page plausibly matches local source.

## What You Produce

- product app shell
- Vercel URL

## Human Decisions

- product repo name
- project name
- Vercel project ownership

## Done Checklist

- [ ] GitHub product repo exists
- [ ] local app runs
- [ ] Vercel deployment URL returns 200
- [ ] live homepage matches local source markers

## Verify Your Day 6

When the checklist is true, ask your harness to run the OneMillion verifier for Day 6. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 7 — Auth + Database](../day-07-auth-db/learn.md)
