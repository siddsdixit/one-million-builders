# Day 4 — Stack + First Deploy

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 1-6 | First real code day** ⚡

**Honest time bands:**
- Engineers: 45–60 min
- PMs / semi-technical: 1.5–2.5 hr
- Non-technical (first time deploying): 3–4 hr — give yourself a weekend morning

If you take longer than the band, that's fine. Day 4 is the steepest learning curve. The deploy loop you learn here saves you 100+ hours over the next 14 days.

---

## Learning Frame

- **Mental model:** A deploy loop makes your product real because every change can reach users.
- **What can go wrong:** Local setup, GitHub auth, or Vercel deployment breaks and drains momentum.
- **What to ignore today:** Ignore app polish; ship the smallest visible page.

## What You'll Have After Today

- A **Next.js app running on your laptop** at `http://localhost:3000`
- The same app **deployed live at a real URL** like `your-app-name.vercel.app`
- A working git repo on GitHub with your code
- The deploy loop: change code → push → live in 30 seconds
- The most important "Aha!" moment of the entire course

This is the most important day of Days 1-6. Once you've seen your own URL work, you're a different person.

> ⚠️ **Honest expectation setting:** This day takes 1 hour for engineers, 1.5–2.5 hours for everyone else. Give yourself a buffer. If you hit a wall, troubleshooting tables are extensive. Sid's Loom shows every step.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Quick Note: Why These Tools, Why Not Others (For Engineers)

> 🔧 **If you're an engineer wondering "why Next.js + Supabase + Vercel and not [X]":**
> - **Next.js over Remix/SvelteKit:** Largest community, best AI generator support (Claude knows it better than anything else), Vercel-native.
> - **Supabase over Postgres/Neon/PlanetScale:** Built-in auth + RLS in one service. You can swap to raw Postgres post-course; Supabase concepts map cleanly.
> - **Vercel over Railway/Fly/Render:** Zero-config Next.js, automatic preview deploys, free tier covers thousands of users.
>
> The lock isn't religious — it's pragmatic. The course optimizes for "ship in 18 days." If you want to swap mid-course: the patterns transfer, but you're on your own. Save the divergence for product 2.

## Part 1: Why These Tools (~10 min read)

Remember the restaurant analogy from Day 1? Frontend (dining room), backend (kitchen), database (pantry), AI (chef). Today you set up the dining room + kitchen + the address. Database comes Day 5. AI comes Days 7-12.

### Next.js — your dining room + kitchen, in one codebase
**What:** A framework for building web apps. Handles both the frontend (what users see) and the backend (the logic) in one project. You write code in one folder; Next.js figures out which parts run in the browser vs on the server.

**Why we picked it:** Largest community of any web framework. Netflix, Notion, half the internet use it. Best documentation. Deploys to Vercel in 30 seconds. Free.

**The mental model:** Your `app/` folder contains pages (frontend) and API routes (backend). Each `page.tsx` is a URL someone can visit. Each `route.ts` in `api/` is a thing your code can call.

### Vercel — your address
**What:** A hosting service that takes your code from GitHub and puts it on the internet. Connect GitHub once, push code, your app auto-deploys.

**Why we picked it:** Made by the same team as Next.js. Deploys in 30 seconds. Free tier covers your entire course (and the first few thousand users). No "DevOps" knowledge required.

**The mental model:** Vercel = the building your restaurant operates out of. It gives you a URL (the address). Customers come to that URL.

### GitHub — your time machine
**What:** Stores your code in the cloud. Tracks every change. Connects to Vercel for auto-deploys.

**Why we picked it:** Industry standard. Free for personal projects. Vercel reads from it directly.

**The mental model:** GitHub = the cloud copy of your code. Your laptop has a local copy; GitHub has the master. When you "push," you sync your local changes up to GitHub. Vercel watches GitHub and rebuilds your app every time you push.

> 🔧 **Engineers:** This is intentionally basic. The course assumes most readers have never deployed anything. You can skim Part 1 and go straight to build.md.

---

## Part 2: The Deploy Loop (~5 min read)

Here's the loop you'll use for the next 14 days:

```
1. Open code in your editor
2. Run `claude` in terminal — give it a task
3. Claude writes code, you review
4. Save the file
5. In terminal: git add . && git commit -m "what changed" && git push
6. Vercel auto-deploys (30 sec)
7. Refresh your URL — change is live
```

That's it. Six steps. Memorize this. Every feature, every bug fix, every iteration: the same loop.

The first time you do it, it feels like magic. By Day 18 it'll feel like breathing.

---

## Part 3: What You're About To Build (~5 min read)

By the end of today you'll have a Next.js project with **one page** — the homepage — saying something like "Hello from [your name]'s OneMillion build." That page will be:

- Running on your laptop at `http://localhost:3000`
- Stored in a GitHub repo
- Deployed to `your-app-name.vercel.app` (a real public URL)

That's it. No auth yet (Day 5). No database (Day 5). No core feature (Day 6). Just: **prove you can ship.**

The first deploy is the psychological turning point. Once a real URL shows your code on the internet, the rest gets easier.

---

## Today's Assignment

Follow [build.md](./build.md) step by step. Every command is there. Every expected output is there. Every error has a fix.

By the end you should be able to send a friend a link like `https://my-onemillion-build.vercel.app` and they should see your page.

---

## What Good Looks Like

After Day 4, your folder structure should look like this:

```
my-onemillion-build/
├── .onemillion/
│   ├── project.json
│   ├── prd.md
│   └── state.json
├── app/
│   ├── layout.tsx
│   ├── page.tsx               ← your homepage
│   └── globals.css
├── public/
├── .env.local                 ← your secrets (gitignored)
├── .gitignore
├── next.config.js
├── package.json
└── README.md
```

And visiting `https://[your-app].vercel.app` should show: "Hello from [your name]'s OneMillion build" or whatever you customized the homepage to say.

---

## Common Mistakes (Today)

1. **Skipping npm install errors.** When `npm install` produces warnings, builders panic. **Warnings are normal.** Errors (red text, "ERR!") need to be fixed. Yellow warnings = ignore.

2. **Pushing without committing first.** `git push` only sends *committed* changes. If you forgot `git commit`, the push does nothing. Always: `git add . && git commit -m "..." && git push`.

3. **Forgetting environment variables on Vercel.** You don't need any yet (no Supabase or Anthropic key on Day 4 — those come later). But on Day 5+ when you add env vars to your local `.env.local`, you MUST also add them to Vercel's dashboard. Builders forget this and wonder why their deployed app breaks.

4. **Editing the wrong file.** `app/page.tsx` is your homepage. `pages/page.tsx` (note: `pages/` plural) is the old Next.js router and doesn't exist in modern Next.js. Make sure you're editing the right file.

5. **Closing the terminal before `npm run dev` finishes.** When you start the local dev server, you have to leave the terminal running. Close it = server stops = `localhost:3000` doesn't work. Open a SECOND terminal for git commands.

---

## What Should Be True After Day 4

- [ ] A Next.js project exists in `my-onemillion-build/` with the standard folder structure
- [ ] `npm run dev` starts a local server at `http://localhost:3000`
- [ ] You can see your homepage at `http://localhost:3000`
- [ ] The code is pushed to a GitHub repo (you can see it at github.com/[your-username]/[repo-name])
- [ ] The app is deployed at a Vercel URL (you can see it at `[something].vercel.app`)
- [ ] You've made at least one change to the homepage, pushed it, and watched Vercel redeploy
- [ ] Verification ran and passed ✅

---

## Verify Your Day 4

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.
- Check the project structure exists
- Verify `package.json` has Next.js + correct dependencies
- Confirm `app/page.tsx` exists
- Check that you have a git remote (GitHub) configured
- Try to fetch your deployed Vercel URL and confirm it returns 200
- Report pass / needs revision

---

## Share It

```
✅ Day 4 done: Live at [your-app].vercel.app 🚀
🎯 Tomorrow: Auth + database
#BuildingWithOneMillion
```

(Optional: include the URL — your network sees you shipping)

---

## Go Deeper

- **[Next.js Learn](https://nextjs.org/learn)** — official tutorial, deep dive
- **[Vercel Docs](https://vercel.com/docs)** — what else you can do
- **[Git basics](https://www.atlassian.com/git/tutorials)** — if git feels foreign

---

→ **Next:** [Day 5 — Auth + Database](../day-05-auth-db/learn.md)
