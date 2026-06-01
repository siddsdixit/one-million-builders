# Day 10 — QA + Tests

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `test`
**Supporting agents:** debug, build

Day 10 proves the core product works reliably. Day 9 asked whether the product is the right thing. Day 10 asks whether it keeps working under real use.

This is where the learner creates a test plan, turns acceptance criteria into test cases, runs manual QA, adds or runs automated tests, tests the live URL, and records evidence.

## Learning Frame

- **Mental model:** QA is evidence. A product that opened once has not passed QA. A product passes QA when important behaviors are checked, failures are recorded, and critical risks are resolved.
- **Input:** PRD, refined PRD, acceptance criteria, Day 8 workflow, Day 9 review findings, app code, Supabase data, and live Vercel URL.
- **Output:** `.onemillion/test-plan.md`, manual QA checklist, automated test results where appropriate, and `.onemillion/test-results.md`.
- **What can go wrong:** the learner only clicks the happy path once, skips permission checks, tests local but not live, writes tests that do not map to requirements, or treats skipped tests as passing.
- **What to ignore today:** do not start new features or AI. Test the core workflow and fix only critical QA failures.

## What You Learn

- what good QA means
- manual QA versus automated QA
- how acceptance criteria become test cases
- how to generate a test plan and test cases
- happy path, edge case, negative, permission, and live deployment testing
- frontend/component testing
- backend testing when the architecture has a backend service
- API testing for route handlers, server actions, or FastAPI endpoints
- E2E browser testing with Playwright or Selenium-style tools
- auth, RLS, tenant, and RBAC testing
- accessibility, responsive, performance, and regression testing basics
- how to decide what must be automated now and what can remain manual for MVP

## Core Concepts

### What Good QA Means

Good QA is not "try the app and see if it feels fine." Good QA is a structured attempt to prove the product works for the target user and fails safely when something goes wrong.

Good QA checks:

- the main user workflow
- acceptance criteria from the spec
- validation and error messages
- auth and permission boundaries
- single-user or tenant data isolation
- RBAC behavior when roles exist
- local behavior and live deployed behavior
- usability across realistic screen sizes
- regressions after fixes

### Manual QA

Manual QA is a human walking through the product with a checklist.

Manual QA is best for:

- first-time product feel
- flow clarity
- copy and labels
- visual layout
- confusing states
- "does this make sense to the target user?"
- verifying live deployment manually before automated coverage is mature

The learner should manually test the Day 8 core workflow locally and live.

### Automated QA

Automated QA is code that checks behavior repeatedly.

Automated QA is best for:

- preventing regressions
- checking many cases quickly
- validating APIs and data rules
- proving auth/RLS/tenant isolation
- running in CI on every push

Not every MVP needs every test type on Day 10, but every learner should understand what each type is for.

### Test Plan And Test Cases

A test plan says what will be tested, why it matters, and what evidence proves it passed.

A test case is a concrete check:

```text
Given I am logged in as User A
When I create a task named "Follow up with parent"
Then I can see that task in my list
And User B cannot see that task
```

Acceptance criteria from the refined PRD should become test cases. Review findings from Day 9 should become regression checks.

### Types Of Testing

| Test type | What it checks | Common tools |
|---|---|---|
| Manual QA | Human-visible flow, clarity, live behavior | Browser, checklist, screenshots |
| Frontend/component tests | Components render and respond correctly | Vitest, React Testing Library |
| E2E browser tests | User workflow through the real UI | Playwright, Selenium |
| API tests | Route handlers, server actions, FastAPI endpoints | Playwright request, curl, pytest/httpx |
| Backend tests | Business logic, services, FastAPI routes when used | pytest, httpx |
| Database/RLS tests | User/tenant isolation and data rules | Supabase test project, SQL checks, E2E users |
| Accessibility tests | Keyboard, labels, contrast, screen-reader basics | Playwright, axe |
| Responsive tests | Core flow on mobile and desktop widths | Playwright viewports, manual browser checks |
| Performance smoke tests | Page/API response time and obvious slowness | curl timing, Lighthouse, Playwright |
| Regression tests | Bugs fixed once stay fixed | Any automated or manual test case |

### Playwright And Selenium

Playwright and Selenium are browser automation tools. They open the app, click buttons, type into forms, and verify what a user would see.

For this course, prefer **Playwright** because it is modern, fast, and works well with Next.js. Selenium is worth knowing because many companies still use it, but learners do not need both for the MVP.

### API Testing

API testing checks the server boundary directly. For the default Next.js/Supabase path, this may mean Playwright request tests against route handlers or testing server actions through UI flows. For FastAPI-path projects, this usually means pytest + httpx tests against backend endpoints.

API tests should check:

- success response
- validation failure
- unauthenticated request
- unauthorized request
- another user's private record
- malformed input

### Permission Testing

For OneMillion products, permission testing matters early.

Check:

- logged-out users cannot access protected pages
- User A cannot see User B's records
- tenant A cannot see tenant B's records
- member cannot do owner/admin actions when RBAC exists
- service-role keys are never exposed in browser code

### QA Evidence

Day 10 should leave evidence. Evidence can be command output, screenshots, test files, manual checklist results, live URL checks, and known limitations.

Skipped or impossible checks are not passes. They should be written as limitations with a reason and next action.

## What You Produce

- `.onemillion/test-plan.md`
- manual QA checklist and results
- automated test files/results where appropriate
- `.onemillion/test-results.md`

## Human Decisions

- critical paths to test manually
- acceptable risk
- QA evidence
- which tests should be automated now
- which checks can remain manual for MVP
- which review findings need regression checks
- whether a failure blocks progress or can be deferred

## Done Checklist

- [ ] `.onemillion/test-plan.md` exists
- [ ] acceptance criteria are mapped to manual or automated test cases
- [ ] manual QA checklist is completed for the core workflow
- [ ] automated tests run where the repo supports them
- [ ] auth/RLS/tenant/RBAC permission checks are covered
- [ ] live app passes critical path QA
- [ ] failures are fixed or explicitly deferred with reason
- [ ] `.onemillion/test-results.md` records evidence, limitations, and verdict

## Verify Your Day 10

When the checklist is true, ask your harness to run the OneMillion verifier for Day 10. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 11 — AI Feature Spec](../day-11-ai-spec/learn.md)
