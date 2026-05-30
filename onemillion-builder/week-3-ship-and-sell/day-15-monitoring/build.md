# Day 15 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 30-60 min. Three services, ~15-20 min each.**

---

## Before You Start

- [ ] Day 14 verified
- [ ] Live app URL works
- [ ] Opened [Account Setup Playbook: Day 15](../../docs/account-setup.md#day-15-monitoring)

---

## Step 1: Sentry (15-20 min)

1. Sign up at [sentry.io/signup](https://sentry.io/signup/). Free plan.
2. Create new project → Platform: Next.js
3. Sentry shows you a **DSN** (looks like `https://xxx@xxx.ingest.sentry.io/xxx`). Copy.
4. Keep Sentry's Next.js docs open: https://docs.sentry.io/platforms/javascript/guides/nextjs/

In your terminal:
```bash
npx @sentry/wizard@latest -i nextjs
```

The wizard installs the SDK + creates config files + asks for your DSN. Paste it.

It modifies your `next.config.js` and creates `sentry.client.config.js` + `sentry.server.config.js` + `sentry.edge.config.js`.

Add the env vars to Vercel:
- `NEXT_PUBLIC_SENTRY_DSN` (your DSN)
- `SENTRY_AUTH_TOKEN` (the wizard provides this)

Test it:
```bash
git add . && git commit -m "Day 15: Sentry" && git push
```

After Vercel redeploys, trigger a test error. Easiest: add this line temporarily to a server component:
```typescript
throw new Error('Sentry test error — Day 15');
```

Push, visit that page on your live URL. The error should fire. Check Sentry dashboard within 60 sec — the error should appear.

Then revert the test error.

---

## Step 2: Vercel Analytics (5 min)

1. vercel.com → your project → **Analytics** tab → enable
   - Docs: https://vercel.com/docs/analytics
2. Install the package:
   ```bash
   npm install @vercel/analytics
   ```
3. Add to `app/layout.tsx`:
   ```typescript
   import { Analytics } from '@vercel/analytics/react';
   // ... inside <body>
   <Analytics />
   ```
4. Commit + push.

After your next visit (and ~10 min of data accumulation), Vercel dashboard shows visitor counts.

---

## Step 3: UptimeRobot (10 min)

1. Sign up at [uptimerobot.com/signUp](https://uptimerobot.com/signUp). Free plan.
   - First monitor guide: https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor
2. Dashboard → **+ New Monitor**
3. Type: HTTP(s)
4. Friendly name: "OneMillion build — [your-app-name]"
5. URL: `https://yourapp.com` (or your .vercel.app URL)
6. Monitoring Interval: 5 minutes (free tier minimum)
7. **Save Changes**

8. **Settings** → **My Settings** → **Alert Contacts**
9. Add your email (probably already there from signup)
10. Make sure the new monitor uses this alert contact.

Test it: temporarily change your monitor URL to a domain that doesn't exist (`https://broken123.example`). Wait 5-10 min. You should get an email saying it's down.

Restore to your real URL.

---

## Step 4: Verify

```bash
claude
```

Paste contents of [`ai-instructions-day-15.md`](./ai-instructions-day-15.md).

---

## What Should Be True After Day 15

- [ ] `@sentry/nextjs` in package.json
- [ ] Sentry config files exist (client, server, edge)
- [ ] `NEXT_PUBLIC_SENTRY_DSN` in `.env.local` AND Vercel
- [ ] Sentry test error appeared in dashboard
- [ ] `@vercel/analytics` in package.json
- [ ] `<Analytics />` component in app/layout.tsx
- [ ] UptimeRobot monitoring your live URL
- [ ] Confirmed email alerts work
- [ ] Account setup QA passed from [Account Setup Playbook: Day 15](../../docs/account-setup.md#day-15-monitoring)
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 15 complete
- **Last verified day:** Day 15
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 16.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 15.

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
| Sentry test error doesn't appear | DSN wrong OR error doesn't actually fire OR ad blocker blocking Sentry. Check Sentry dashboard "Configure SDK". |
| Vercel Analytics shows no data | Wait 10-15 min. Also confirm `<Analytics />` is inside `<body>`. |
| UptimeRobot can't reach my site | Some CDNs block their IPs. Add UptimeRobot IPs to allowed list (Cloudflare). |
| Too many Sentry events | Add `beforeSend` filter to ignore non-critical errors (bots, transient). |
| Sentry SDK breaking build | Wizard may have created bad config. Re-run wizard OR ask Claude to fix `sentry.*.config.js` files. |

---

→ **Done with Day 15?** Move to [Day 16 — Landing Page](../day-16-landing/learn.md).
