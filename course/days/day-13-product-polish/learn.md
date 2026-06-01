# Day 13 — Product Polish + UX Finish

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** review, design

Day 13 is where the product stops feeling like a raw build and starts feeling usable. The learner reviews the whole app, sharpens the UX, improves the AI feature experience, and makes the core flow easier for the target user.

## Learning Frame

- **Mental model:** product polish is not decoration. It is the work of making the product understandable, forgiving, and credible.
- **What can go wrong:** the app technically works, but the target user does not know what to do, cannot recover from errors, or does not trust the AI output.
- **What to ignore today:** do not add a new major feature. Improve the current MVP flow.

## What You Learn

- how to inspect the product from the target user's point of view
- what good empty, loading, error, success, and partial states do
- how copy, labels, hierarchy, and navigation reduce confusion
- how mobile and desktop polish differ
- how AI UX fits inside the product rather than taking over the product
- when AI output should be reviewed, edited, accepted, retried, or discarded
- how accessibility basics make the product easier for everyone

## Core Concepts

- **Polish means removing friction.** The learner should look for moments where a real user would pause, guess, misclick, or lose confidence.
- **States are part of the product.** Empty screens, loading screens, errors, and success confirmations are not edge cases; they are common user experiences.
- **Copy is interface.** Button labels, headings, helper text, and error messages should tell the user what is happening and what to do next.
- **AI output needs a home.** The app should show when AI is working, what it produced, what the user can do with it, and what happens if it fails.
- **Review boundaries matter.** If AI output can change data, send a message, make a recommendation, or affect another person, the user should confirm the action.
- **Mobile is not an afterthought.** The main flow should be usable on a phone unless the architecture explicitly chose desktop-first.

## What You Produce

- a polished MVP flow in the actual app
- improved AI feature UX where Day 12 added AI
- clearer copy and navigation
- complete empty/loading/error/success states for the core workflow
- mobile and desktop fixes where needed

## Human Decisions

- what the app should feel like for the target user
- which UX problems must be fixed now versus deferred
- whether AI output is displayed, saved, reviewed, edited, or accepted
- what the user should see while AI is working
- what the user should see when AI fails
- what success should look like after the main workflow completes

## Done Checklist

- [ ] main MVP flow is easy to understand without explanation
- [ ] empty, loading, error, success, and partial states are present where needed
- [ ] AI feature has clear waiting, output, retry, and review behavior
- [ ] buttons, labels, and page headings are specific and user-friendly
- [ ] mobile and desktop layouts do not overlap or break
- [ ] target-user pain point still feels central to the product
- [ ] existing refined PRD/spec is updated only if the intended product behavior changed

## Verify Your Day 13

When the checklist is true, ask your harness to run the OneMillion verifier for Day 13. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 14 — Security + Trust Review](../day-14-security-trust-review/learn.md)
