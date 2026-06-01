# Day 14 — Security + Trust Review

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `guard`
**Supporting agents:** review, build, test

Day 14 is the trust checkpoint before final QA and production shipping. The learner reviews the product's security, privacy, tenant boundaries, auth behavior, AI data handling, and cost/abuse risks.

## Learning Frame

- **Mental model:** security is product quality. Users trust the product only if their data, identity, and actions are protected.
- **What can go wrong:** the app works for the happy path but leaks data across users, exposes secrets, skips authorization, or sends too much private data to AI.
- **What to ignore today:** do not add new features. Fix trust blockers and document only the risks needed for shipping decisions.

## What You Learn

- why authentication is not the same as authorization
- how RBAC differs from simple owner-based access
- how single-tenant and multi-tenant products change security design
- how Supabase RLS protects data when written correctly
- why API keys and service-role keys must stay server-side
- how AI data privacy works: send only the minimum useful context
- prompt injection basics for user-provided and retrieved content
- cost, rate-limit, and abuse controls
- what counts as a production-blocking security issue

## Core Concepts

- **Auth answers "who are you?"** Login proves identity.
- **Authorization answers "what can you do?"** Owner checks, tenant checks, and RBAC decide access.
- **RBAC means role-based access control.** Roles such as owner, admin, member, viewer, or customer determine which actions are allowed.
- **Tenant boundaries are product boundaries.** In a multi-tenant app, one team or customer must not see another team's data.
- **RLS is a database safety net, not a decoration.** Policies should enforce ownership or tenant access even if application code makes a mistake.
- **Secrets are production assets.** Provider API keys, Supabase service keys, and webhooks must not be committed or exposed to browser code.
- **AI must follow the same boundaries as the app.** The AI route should only receive data the current user is allowed to see.
- **RAG and tool use remain optional.** If the product does not need retrieval or tool actions, skip them and keep the AI path simple.

## What You Produce

- fixed or confirmed security/trust posture in the app
- updated existing architecture/refined PRD only if security behavior changed
- guard evidence in `.onemillion/state.json` or the existing verification trail
- a clear decision on whether RAG/tool use is skipped or justified

## Human Decisions

- single-tenant, multi-tenant, or public/community data stance
- whether RBAC is needed now
- which roles/actions exist if RBAC is needed
- what data AI may receive
- whether RAG/tool use is necessary or skipped
- acceptable cost/rate limits
- which risks block production

## Done Checklist

- [ ] auth routes and protected pages behave correctly
- [ ] owner, tenant, or RBAC checks exist where needed
- [ ] Supabase RLS policies protect user/tenant data
- [ ] no server-only secret is exposed to client code or git
- [ ] AI route receives only allowed, minimal context
- [ ] RAG/tool use is either explicitly skipped or justified by the product
- [ ] cost/rate/abuse controls are present or consciously deferred with reason
- [ ] critical trust blockers are fixed before Day 15

## Verify Your Day 14

When the checklist is true, ask your harness to run the OneMillion verifier for Day 14. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 15 — QA + Production Readiness](../day-15-qa-production-readiness/learn.md)
