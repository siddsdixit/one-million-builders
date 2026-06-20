# Day 16 - Ship Production

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 16. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 16 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 16: Ship Production.

Act as the `ship` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-16-ship-production/learn.md, course/days/day-16-ship-production/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- production URL to publicize
- custom domain or skip
- monitoring choice
- alert email/contact
- optional FastAPI backend host if architecture selected FastAPI
- acceptable production blockers versus deferrals

## External Tools

- Vercel
- Supabase
- Sentry
- Vercel Analytics
- UptimeRobot
- domain registrar if needed

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Done Checklist

- [ ] production URL returns 200 and does not show an application error
- [ ] live app matches the current local/product source with a unique product marker
- [ ] Vercel production environment variables are set by name, with no secret values committed
- [ ] Supabase Site URL and redirect URLs include the production URL where auth is used
- [ ] RLS/auth/tenant assumptions from Day 14 still hold in production
- [ ] optional FastAPI backend is deployed and health-checked, or explicitly skipped because architecture did not select it
- [ ] live smoke test covers the main flow, auth, data, and AI feature where applicable
- [ ] monitoring/analytics/uptime is configured or intentionally deferred with reason
- [ ] custom domain works or is explicitly skipped
- [ ] rollback path is known and accessible
- [ ] .onemillion/state.json includes the production live_url

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 16: Ship Production"
```

## Next

After this day is verified, continue to Day 17.
