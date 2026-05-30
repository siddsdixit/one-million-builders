# Account Setup Playbook

Use this page whenever a day asks you to create an account, connect a service, create a key, set permissions, or verify a dashboard setting.

The rule is simple:

```text
Open the exact link. Do the smallest setup. Verify it immediately. Save only the non-secret proof.
```

Never paste secrets into chat, screenshots, GitHub, Slack, Loom, or committed files.

This playbook supports the `AGENTS.md` Preflight Gate and `course-manifest.json` provider setup links.

---

## Day 0: GitHub Course Fork

### Links

- Create GitHub account: https://github.com/signup
- Course repo: https://github.com/siddsdixit/teach-one-million
- Fork course repo: https://github.com/siddsdixit/teach-one-million/fork
- Install GitHub CLI: https://cli.github.com/
- GitHub Git setup docs: https://docs.github.com/en/get-started/git-basics/set-up-git

### Steps

1. Create or open your GitHub account.
2. Open the course repo and click **Star**.
3. Open the fork link and create a fork under your own GitHub account.
4. Clone your fork, not Sid's repo:

```bash
git clone https://github.com/YOUR-USERNAME/teach-one-million.git
cd teach-one-million
./onemillion-builder/install-agents.sh
```

### Permissions

- Fork owner: your personal GitHub account.
- Visibility: public is recommended for proof, private is acceptable if needed.
- `origin`: must point to your fork.
- `upstream`: must point to `https://github.com/siddsdixit/teach-one-million.git`.

### QA

Run:

```bash
git remote -v
git rev-parse --show-toplevel
test -f AGENTS.md
test -f onemillion-builder/course-manifest.json
```

Pass criteria:

- `origin` contains your GitHub username.
- `upstream` contains `siddsdixit/teach-one-million`.
- Both required files exist.

---

## Day 4: GitHub App Repo + Vercel Deploy

### Links

- Create new GitHub repo: https://github.com/new
- Vercel signup/login: https://vercel.com/signup
- Import Vercel project: https://vercel.com/new
- Vercel Git deployment docs: https://vercel.com/docs/deployments/git
- Vercel import docs: https://vercel.com/docs/getting-started-with-vercel/import

### Steps

1. Create a separate GitHub repo for your product app.
2. Push `my-onemillion-build` to that repo.
3. Sign in to Vercel with GitHub.
4. Import the product app repo.
5. Keep Framework Preset as Next.js.
6. Deploy.

### Permissions

- Vercel must have access to the product app repo.
- If the repo is under your personal GitHub account, you must be the owner.
- If the repo is under an organization, you need org/repo access that lets Vercel install its GitHub integration.

### QA

Pass criteria:

- Product repo opens at `https://github.com/YOUR-USERNAME/YOUR-APP-REPO`.
- Vercel deployment returns HTTP 200.
- Pushing a new commit triggers a new Vercel deployment.

---

## Day 5: Supabase Auth + Database

### Links

- Supabase signup/login: https://supabase.com/dashboard
- Create Supabase project shortcut: https://database.new
- Supabase Next.js Auth quickstart: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Supabase API keys docs: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls
- Supabase RLS docs: https://supabase.com/docs/guides/database/postgres/row-level-security
- Vercel env vars docs: https://vercel.com/docs/projects/environment-variables

### Steps

1. Create a Supabase project at `https://database.new`.
2. Copy the Project URL and publishable/anon key.
3. Put public browser-safe values in `.env.local`.
4. Add the same values to Vercel Project -> Settings -> Environment Variables.
5. Create your first table with RLS enabled.
6. Add a policy that uses `auth.uid() = user_id`.
7. Configure Supabase Auth URL settings for your live Vercel URL when auth redirects are introduced.

### Permissions

- Use the publishable key or legacy anon key in browser-facing env vars.
- Never put a secret key or service role key in client code.
- RLS must be enabled for tables exposed through the API.

### QA

Pass criteria:

- `.env.local` exists and is not staged by git.
- Vercel has the same env var names.
- Signup works locally.
- Signup works on the live Vercel URL.
- Supabase Authentication -> Users shows the test user.
- Table Editor shows RLS enabled.
- Policies include `auth.uid()`.

---

## Day 8: Anthropic API Key

### Links

- Anthropic Console: https://console.anthropic.com/
- Anthropic API overview: https://docs.anthropic.com/en/api/overview
- Vercel env vars: https://vercel.com/docs/projects/environment-variables

### Steps

1. Open Anthropic Console.
2. Create or open a workspace for this app.
3. Create an API key.
4. Save it as `ANTHROPIC_API_KEY` in `.env.local`.
5. Add `ANTHROPIC_API_KEY` to Vercel Project -> Settings -> Environment Variables.
6. Redeploy after adding the env var.

### Permissions

- `ANTHROPIC_API_KEY` is server-only.
- Never prefix it with `NEXT_PUBLIC_`.
- Never paste the value into chat or commit it.

### QA

Pass criteria:

- `ANTHROPIC_API_KEY` appears in `.env.local`.
- `ANTHROPIC_API_KEY` appears in Vercel env vars.
- `rg "NEXT_PUBLIC_ANTHROPIC|sk-ant" .` finds no client leak.
- Live AI route works on Vercel.

---

## Day 15: Monitoring

### Links

- Sentry signup/login: https://sentry.io/signup/
- Sentry Next.js setup: https://docs.sentry.io/platforms/javascript/guides/nextjs/
- Vercel Analytics docs: https://vercel.com/docs/analytics
- UptimeRobot signup/login: https://uptimerobot.com/signUp
- UptimeRobot first monitor guide: https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor

### Steps

1. Create a Sentry project for Next.js.
2. Install the Sentry SDK and add the DSN to local and Vercel env vars.
3. Trigger one test error and confirm it appears in Sentry.
4. Enable Vercel Analytics for the project.
5. Create an UptimeRobot HTTP monitor for the live URL.
6. Confirm alert email is active.

### Permissions

- Sentry DSN may be public, but do not paste auth tokens.
- UptimeRobot monitor should hit the public live URL, not localhost.
- Alert email must be an inbox you actually read.

### QA

Pass criteria:

- Sentry receives a test error.
- Vercel Analytics page shows visits after a short delay.
- UptimeRobot monitor is up.
- A temporary broken URL test sends an alert, then you restore the real URL.

---

## Day 18: Loom + Builder Claim

### Links

- Loom signup/login: https://www.loom.com/
- Loom sharing help: https://loomhelp.zendesk.com/hc/en-us/articles/360002208157-How-to-share-your-recording
- Builder Claim issue: https://github.com/siddsdixit/teach-one-million/issues/new/choose
- Builder Wall: https://github.com/siddsdixit/teach-one-million/tree/main/builders

### Steps

1. Record a 5-minute Loom demo.
2. Set sharing to public or "Anyone with the link can view."
3. Test the Loom link in an incognito window.
4. Save the live app URL, Loom URL, and proof summary in `.onemillion/demo.md`.
5. Submit the Builder Claim issue.

### Permissions

- Loom link must be viewable by reviewers without a login.
- App URL must be public.
- GitHub repo may be private if needed, but public is better proof.

### QA

Pass criteria:

- Incognito browser can view the Loom.
- Incognito browser can open the live app.
- Builder Claim issue includes live URL, Loom URL, and verification summary.
