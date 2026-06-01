# Day 15 — QA + Production Readiness

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `test`
**Supporting agents:** guard, build, debug

Day 15 is the final quality gate before production shipping. The learner proves the product works, fixes critical bugs, and prepares the app for Day 16 production verification.

## Learning Frame

- **Mental model:** QA is evidence. A product is not ready because it looks done; it is ready when the important paths have been tested and known risks are understood.
- **What can go wrong:** the learner fixes random bugs without testing the full flow, or ships with broken auth, deploy, AI, or data behavior.
- **What to ignore today:** no new feature work unless a production-blocking bug forces it.

## What You Learn

- how to turn acceptance criteria into a final QA pass
- how manual QA and automated tests support each other
- when to use unit, component, API, E2E, Playwright, Selenium-style, and backend tests
- how to test the live app, not only local code
- how to test AI behavior with pass/fail examples
- how to decide what blocks production versus what can be deferred
- how to prepare environment variables and deployment assumptions for Day 16

## Core Concepts

- **Manual QA catches experience problems.** The learner should click the product like a real user and inspect what happens.
- **Automated tests catch regressions.** Tests should cover the core workflow and the highest-risk boundaries.
- **E2E tests prove journeys.** Playwright or Selenium-style tests are useful when the app has multi-step UI behavior.
- **API/backend tests prove contracts.** If the product has Next.js routes, server actions, Supabase calls, or FastAPI, important behaviors should be exercised.
- **AI quality needs examples.** Good and bad inputs should show whether the AI feature is helpful, bounded, and recoverable.
- **Production readiness is a gate.** Broken critical paths, exposed secrets, auth leaks, and failed deployment checks block Day 16.

## What You Produce

- final QA evidence for the MVP
- automated or manual tests for the highest-risk flows
- bug fixes for production blockers
- updated test results in the existing verification trail
- a ready-for-production decision for Day 16

## Human Decisions

- critical paths that must pass before shipping
- which tests should be automated now
- which tests can remain manual for MVP
- AI pass/fail examples and quality threshold
- what defects block Day 16
- what non-critical risks can be accepted temporarily

## Done Checklist

- [ ] local build/test commands pass or failures are understood and fixed/deferred
- [ ] manual QA covers the main user journey, auth, data, AI feature, and error states
- [ ] automated tests cover the highest-risk behavior the repo can support
- [ ] live deployment is checked for the critical path
- [ ] AI pass/fail examples produce acceptable behavior
- [ ] no Day 14 critical security/trust blocker remains
- [ ] production-blocking bugs are fixed before Day 16
- [ ] accepted risks are explicit in the existing state/verification trail

## Verify Your Day 15

When the checklist is true, ask your harness to run the OneMillion verifier for Day 15. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 16 — Ship Production](../day-16-ship-production/learn.md)
