# Day 14 - Security + Trust Review

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 14. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 14 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 14: Security + Trust Review.

Act as the `guard` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-14-security-trust-review/learn.md, course/days/day-14-security-trust-review/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- single-tenant, multi-tenant, or public/community data stance
- whether RBAC is needed now
- roles/actions if RBAC is needed
- what data AI may receive
- RAG/tool use skipped or justified
- acceptable cost/rate limits

## External Tools

- Supabase
- Vercel
- Anthropic

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Done Checklist

- [ ] auth routes and protected pages behave correctly
- [ ] owner, tenant, or RBAC checks exist where needed
- [ ] Supabase RLS policies protect user/tenant data
- [ ] no server-only secret is exposed to client code or git
- [ ] AI route receives only allowed, minimal context
- [ ] RAG/tool use is skipped or justified by the product
- [ ] cost/rate/abuse controls are present or consciously deferred with reason
- [ ] critical trust blockers are fixed before Day 15

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 14: Security + Trust Review"
```

## Next

After this day is verified, continue to Day 15.
