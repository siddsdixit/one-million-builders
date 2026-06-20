# Day 6 - If You Are Stuck

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

Day 6 problems are usually setup, git, or deploy-loop problems. Do not ask the harness to rewrite the app until you know which layer failed.

## Recovery Prompt

Paste this into your harness:

```text
I am on OneMillion Day 6: App Shell + First Deploy.
I am stuck.

Layer that seems broken:
[local app / git / GitHub / Vercel / not sure]

What I tried:
[paste command or step]

What I expected:
[describe]

What happened:
[paste error, build log, URL behavior, or screenshot text]

Please diagnose the smallest next action.
Teach the missing concept briefly.
Do not rebuild unrelated parts of the app.
Do not advance Day 6 until the live URL returns 200 and the live page matches the source marker.
```

## First Checks

- Confirm you are in the product app folder, not only the course folder.
- Confirm the product repo is separate from the course fork.
- Confirm the local app runs before debugging Vercel.
- Confirm the live app has the unique Day 6 source marker.
- Read the Vercel build log before changing code.

## Common Day 6 Issues

| Problem | Likely Cause | Smallest Fix |
|---|---|---|
| `npm run dev` fails | dependencies missing or wrong folder | run install in the product app folder and retry |
| Browser cannot open localhost | dev server not running or wrong port | check terminal output for the actual local URL |
| Git push fails | auth or wrong remote | run `git remote -v` and verify GitHub login |
| Vercel import cannot find repo | repo not pushed or wrong GitHub account | push to GitHub and refresh Vercel import |
| Vercel build fails | local build would also fail | run `npm run build` locally and fix first error |
| Live page is old | deployment not triggered or wrong branch | push latest commit and check Vercel production branch |
| Live page is default template | source marker not committed/deployed | commit marker, push, wait for deployment |

## What Not To Do

- Do not add auth, database, or AI today.
- Do not keep changing code without reading the exact build error.
- Do not accept a live URL that does not show your source marker.
- Do not say `day done` if the Vercel URL only works for you while logged into Vercel.

## Recovery Order

1. Re-read [learn.md](./learn.md) for the deploy-loop concept.
2. Re-open [build.md](./build.md) and find the first unchecked requirement.
3. Identify the failing layer: local, git, GitHub, or Vercel.
4. Fix only that layer.
5. Re-run the local or live check.
6. Run the Day 6 verifier only after the done checklist is true.
