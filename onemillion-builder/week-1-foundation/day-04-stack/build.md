# Day 4 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1–2.5 hours. The first real building day.**

Today you set up a Next.js project, push it to GitHub, and deploy to Vercel. Follow every step. Every command has an expected output.

---

## Before You Start

- [ ] Day 3 verified (PRD locked)
- [ ] GitHub, Vercel accounts ready (from getting-started.md)
- [ ] Opened [Account Setup Playbook: Day 4](../../docs/account-setup.md#day-4-github-app-repo--vercel-deploy)
- [ ] Terminal open, in `teach-one-million/my-onemillion-build`
- [ ] Editor ready to open

> 💡 **Pro tip:** Have TWO terminal windows open today. One for running the dev server (it stays open). One for running git commands.

---

## Step 1: Initialize Next.js Project (10 min)

In your terminal, in `my-onemillion-build` (this folder should already exist from Day 1):

```bash
npx create-next-app@latest .
```

The `.` (dot) means "create the Next.js project IN this current folder."

You'll be asked several questions. Answer like this:

| Question | Answer |
|----------|--------|
| Would you like to use TypeScript? | **Yes** |
| Would you like to use ESLint? | **Yes** |
| Would you like to use Tailwind CSS? | **Yes** |
| Would you like your code inside a `src/` directory? | **No** |
| Would you like to use App Router? | **Yes** (recommended) |
| Would you like to use Turbopack? | **No** (for compatibility) |
| Would you like to customize the import alias? | **No** |

**You should see:** A lot of output, ending with `Success! Created [your-folder] at [path]`. Takes 1-3 minutes.

> 🆘 **If you see "directory not empty" error:** That's because your `.onemillion/` folder is already there. Run `npx create-next-app@latest . --force` to proceed.

---

## Step 2: Run It Locally (2 min)

```bash
npm run dev
```

**You should see:**
```
   ▲ Next.js 15.x.x
   - Local:        http://localhost:3000
   - Network:      http://192.168.x.x:3000

 ✓ Starting...
 ✓ Ready in 1.5s
```

Open your browser to `http://localhost:3000`. You should see the default Next.js welcome page.

🎉 **That's the dining room running on your laptop.** Leave this terminal running.

---

## Step 3: Customize The Homepage (5 min)

Open a SECOND terminal window. (Keep the first running.) In the new terminal:

```bash
cd /path/to/teach-one-million/my-onemillion-build
claude
```

Once your coding harness is ready, ask it:

```
Edit app/page.tsx so the homepage says:
"Hello from [Your Name]'s OneMillion build. Day 4 — deployed live."

Keep it simple. One heading, one paragraph. Use Tailwind for centering.
```

Claude will edit `app/page.tsx`. Watch what it changes.

Save the file. Look at `http://localhost:3000` in your browser — it should hot-reload to show your new text within 1-2 seconds.

> 💡 **First magic moment.** You just used AI to write code and saw it run on your laptop. This is the whole game.

---

## Step 4: Set Up Git + GitHub (15 min)

**⚠️ DO THIS BEFORE TRYING TO PUSH:** GitHub no longer accepts passwords for authentication. You need either GitHub CLI or a Personal Access Token. Set this up FIRST or your push will fail with confusing errors.

### Step 4a: Authenticate with GitHub (CHOOSE ONE)

**Option A — GitHub CLI (easiest, RECOMMENDED):**

Open: https://cli.github.com/

```bash
# Mac
brew install gh

# Windows (in Git Bash)
winget install --id GitHub.cli
# Or download from cli.github.com
```

Then:
```bash
gh auth login
```

Answer the prompts:
- GitHub.com (not Enterprise)
- HTTPS
- Yes, authenticate Git
- Login with web browser
- Press Enter, paste the code into the browser window that opens
- Authorize

**You should see:** `✓ Logged in as your-username`.

**Option B — Personal Access Token (manual):**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token** → **Generate new token (classic)**
3. Note: `onemillion-course` | Expiration: 90 days | Scopes: check `repo`
4. Click **Generate token** → copy the token (starts with `ghp_`) — save it like a password
5. When git asks for your password later, paste this token instead

### Step 4b: Initialize Git + First Commit

In your second terminal:

```bash
git init
git add .
git commit -m "Day 4: Next.js project initialized"
```

**You should see:** Output ending with something like `[main (root-commit) abc1234] Day 4: Next.js project initialized`.

### Step 4c: Create The Remote GitHub Repo

Go to [github.com/new](https://github.com/new):

- Repository name: `my-onemillion-build` (or whatever you named your folder)
- **Public** or **Private** — your choice
- **Do NOT** check "Add a README" or any of the initial files
- Click **Create repository**

GitHub shows you commands. Use the block starting with `git remote add origin`:

```bash
git remote add origin https://github.com/YOUR-USERNAME/my-onemillion-build.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

**You should see:** Output ending with `Branch 'main' set up to track 'origin/main'.`

Refresh github.com/YOUR-USERNAME/my-onemillion-build — your code is there.

---

## Step 5: Deploy To Vercel (10 min)

Go to [vercel.com/new](https://vercel.com/new).

1. Sign in if you haven't (Continue with GitHub)
2. You'll see your repos. Find `my-onemillion-build` and click **Import**
3. Project name: leave default
4. Framework Preset: should auto-detect Next.js
5. Environment Variables: leave empty for today (you'll add some on Day 5)
6. Click **Deploy**

If Vercel does not show your repo, check the GitHub integration permissions. For a personal repo, you usually need to be the repo owner. See the setup playbook and Vercel Git docs: https://vercel.com/docs/deployments/git

**You should see:** A progress screen with "Building..." then "Deploying..." Takes 1-3 minutes.

When done, Vercel shows you fireworks and your deployed URL — something like `https://my-onemillion-build-username.vercel.app`.

Click the URL. **Your app is live on the internet.** 🚀

Send the URL to a friend or your group chat. This is your first deploy.

---

## Step 6: The Deploy Loop In Action (5 min)

Let's prove the loop works. In your editor, edit `app/page.tsx`:

Change the text to something different. Like: "Hello from [Your Name]'s OneMillion build — first deploy was magical."

Save the file.

In your second terminal:

```bash
git add .
git commit -m "Update homepage text"
git push
```

Now go to Vercel's dashboard for your project. You'll see a new deployment building. Wait 30 seconds.

Refresh your Vercel URL. **The text changed.** That's the deploy loop. You'll do this 50+ times over the next 14 days.

---

## Step 7: Run Day 4 Verification

```bash
claude
```

Paste the contents of [`ai-instructions-day-04.md`](./ai-instructions-day-04.md). Claude will:
- Check `package.json` for Next.js
- Verify `app/page.tsx` exists and isn't the default Next.js template
- Check that git remote is set
- Try to fetch your Vercel URL and confirm it returns HTTP 200

If pass: you're done with Day 4. If revision needed: fix and re-run.

---

## What Should Be True After Day 4

- [ ] `npm run dev` starts a working app at `http://localhost:3000`
- [ ] Your homepage shows YOUR text, not the default Next.js welcome
- [ ] Code is pushed to a GitHub repo
- [ ] Your app is live at a Vercel URL
- [ ] You made a change, pushed it, and saw Vercel redeploy
- [ ] Account setup QA passed from [Account Setup Playbook: Day 4](../../docs/account-setup.md#day-4-github-app-repo--vercel-deploy)
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 4 complete
- **Last verified day:** Day 4
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 5.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 04.

Here is the step I was trying to complete:
[paste the step heading or instructions]

Here is what happened:
[paste the error, terminal output, or describe what I see]

Diagnose the likely cause and give me the next smallest action.
Do not rewrite unrelated code.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `npx: command not found` | Node.js isn't installed correctly. Re-do Step 1 of [getting-started.md](../../docs/getting-started.md). |
| `npm install` takes forever (>5 min) | Slow connection. Wait it out. If it fails: `npm install --legacy-peer-deps`. |
| Port 3000 already in use | Something else is running on 3000. Either close it, or run `npm run dev -- -p 3001` to use port 3001. |
| `localhost:3000` shows "This site can't be reached" | Your dev server isn't running. Check the first terminal — `npm run dev` should still be running there. If not, restart it. |
| `git push` says "authentication required" | GitHub needs a Personal Access Token. Use `gh auth login` (install GitHub CLI: `brew install gh`) or follow [GitHub auth docs](https://docs.github.com/en/authentication). |
| Vercel deployment fails | Click the failed deployment → view logs. Most common: a TypeScript error. Your coding harness can fix it: paste the error into the harness. |
| Vercel shows "404 Not Found" after deploy | Wait 60 seconds and refresh. Build is still propagating. If still 404 after 5 min: check Vercel build logs for errors. |
| Made changes locally but Vercel still shows old version | You forgot to `git add` and `git commit` before `git push`. Run all three. |
| `app/page.tsx` looks weird (lots of imports and JSX) | That's normal. Just replace the contents with what Claude generated. |

If you're stuck for 30 min because your local machine is fighting you, switch to Codespaces ([browser setup path](../../docs/codespaces.md)) and try the day there.

---

→ **Done with Day 4?** Move to [Day 5 — Auth + Database](../day-05-auth/learn.md).
