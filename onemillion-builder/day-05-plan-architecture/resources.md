# Day 5 — Resources

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

## Course Sources

- [Full Course Flow](../single.md)
- [Teaching Protocol](../docs/teaching-protocol.md)
- [Account Setup Playbook](../docs/account-setup.md)
- [Agent Flow](../docs/agent-flow.md)

## Primary Agent

- `plan` in `../../onemillion-agents/agents/plan.md`

## Agent Concepts To Notice

- Architecture converts PRD + design into technical decisions.
- Default course stack: Next.js + React + MUI, Supabase Auth/Postgres/RLS, Vercel, Claude from server-side code.
- Backend path is a decision: Supabase/Next.js first, FastAPI only when justified.
- Product type affects architecture: web app, mobile-first responsive app, agent, or hybrid.
- Tenancy affects every table and permission boundary.
- Security architecture starts before code: auth, authorization, secrets, RLS, AI permissions, rate/cost limits.
- Scalability means choosing simple structures that handle expected users, data, integrations, and AI volume.
- Sprint briefs are self-contained build contracts for the build agent.
- Smaller sprints are easier for LLMs to contextualize, test, debug, and review.
- `validate-plan` checks coherence across PRD, design, architecture, and sprint briefs.

## External Links

- No new external account is required today.
- Supabase docs for later reference: https://supabase.com/docs
- Supabase Row Level Security docs for later reference: https://supabase.com/docs/guides/database/postgres/row-level-security
- Next.js docs for later reference: https://nextjs.org/docs
- FastAPI docs for optional backend reference: https://fastapi.tiangolo.com/
