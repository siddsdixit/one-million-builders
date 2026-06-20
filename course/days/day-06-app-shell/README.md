# Day 6 - App Shell + First Deploy

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

Day 6 is the first real code-and-deploy day. By the end, your product has a separate app repo, a local app shell, and a live Vercel URL that matches the code on your machine.

## Outcome

You are not building the product yet. You are creating the shell where the product will live:

- product GitHub repo
- local Next.js/MUI app shell
- Vercel project
- live URL returning 200
- visible marker proving the live page came from today's source code

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) why app shell and deploy loop matter.
- [Build](./build.md) one step at a time.
- [Recover](./stuck.md) if GitHub, Vercel, local dev, or deploy fails.
- [Resources](./resources.md) are optional after the day is complete.

## What Good Looks Like

Before saying `day done`, you should be able to show:

1. A GitHub product repo separate from the course fork.
2. A local app running in the product workspace.
3. A Vercel deployment URL that opens in an incognito browser.
4. A unique text marker on the live homepage, such as:

```text
OneMillion Day 6 - [Product Name] - [today's date]
```

That marker matters. It proves the live deployment is current, not an old or default page.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 6: App Shell + First Deploy.

Act as the `build` agent for this day.
First teach me the deploy loop in plain language: local app -> git commit -> GitHub -> Vercel -> live URL.
Then guide me one step at a time using course/days/day-06-app-shell/learn.md, course/days/day-06-app-shell/build.md, course/days/single.md, and course/course-manifest.json.

Before creating or changing code, ask me for:
- product repo name
- project name
- Vercel project ownership

Use my Day 3-5 artifacts to keep the shell aligned with the product, but do not build core product features yet.
Make the app shell minimal, branded enough to recognize, and easy to verify.
Add a unique source marker to the homepage so we can prove the live deployment matches local code.
Show what changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- Product repo name.
- Project name.
- Vercel account/team/project ownership.
- Whether the product app lives in the default `my-onemillion-build/` folder or a deliberate alternate path recorded in `.onemillion/state.json`.

## External Tools

- GitHub
- Vercel
- terminal

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Common Checks

Run or ask the harness to run the relevant checks:

```bash
git remote -v
npm run dev
npm run build
```

Then open:

- local URL, usually `http://localhost:3000`
- live Vercel URL

Both should show the Day 6 source marker.

## Done Checklist

- [ ] GitHub product repo exists
- [ ] local app runs
- [ ] Vercel deployment URL returns 200
- [ ] live homepage matches local source markers

## Commit

After the verifier passes, commit meaningful work:

```bash
git add .
git commit -m "Day 6: app shell and first deploy"
```

## Next

After Day 6 is verified, continue to Day 7: Auth + Database.
