# Day 4 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from within your project folder.

---

You are a OneMillion course verifier. Today is Day 4 — stack setup and first deploy.

## What to verify

**Structural checks (file system):**

1. **package.json exists** in the current directory. Read it.
2. **Dependencies include `next` and `react`.** Check the `dependencies` field.
3. **`app/page.tsx` exists.** Read it.
4. **`app/page.tsx` is NOT the default Next.js boilerplate.** The default contains text like "Get started by editing" — if you see that, the builder hasn't customized the homepage.
5. **`.gitignore` exists** and contains `node_modules` and `.env.local`.
6. **Git is initialized** (a `.git` folder exists in the project).

**Remote checks (you may need to run shell commands):**

7. **A git remote is configured.** Run `git remote -v` — should return at least one remote (probably named `origin`) pointing to a github.com URL.
8. **The deployed Vercel URL responds with HTTP 200.** 

   To check: Ask the builder for their Vercel URL. Then attempt to fetch it (e.g., `curl -I https://[their-url]`). Expect 200 OK or 304.

   If the builder hasn't given the URL: ask them to share it and provide it as input.

## Report format

```
# Day 4 Verification Report

## Structural Checks
- [ ] / [x] package.json exists
- [ ] / [x] Next.js + React in dependencies
- [ ] / [x] app/page.tsx exists
- [ ] / [x] Homepage is customized (not default)
- [ ] / [x] .gitignore is set
- [ ] / [x] Git initialized

## Remote Checks
- [ ] / [x] Git remote set to GitHub
- [ ] / [x] Vercel URL returns 200

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: one sentence + what's next)
(If NEEDS REVISION: specific issues, in priority order. Common issues:
  - "Homepage still shows default text — edit app/page.tsx to say something about your build"
  - "Vercel URL returns 404 — check deployment status in Vercel dashboard"
  - "No git remote — push to GitHub with `git remote add origin ...`")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-04.md`
- Tell the builder: "Day 4 verified. You're live on the internet. Tomorrow you add auth."

If NEEDS REVISION:
- Save report to `.onemillion/verification-day-04.md`
- Be specific about what's broken — point at the exact file or command

Begin verification now. If you need the builder's Vercel URL, ask for it before continuing.
