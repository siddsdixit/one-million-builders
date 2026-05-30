# Getting Your API Keys

You need exactly **two API keys** to take this course:

1. **Anthropic** — powers your product's AI features if you choose Claude as the model provider
2. **Supabase** — your database and auth (you'll get this on Day 5, but you can do it now)

Each takes about 5 minutes. Total cost over 18 days: $5–15.

---

## What's An API Key?

An API key is a password that lets your code talk to an external service. It's how your app calls an AI provider. It's how your app reads from Supabase. Without it, your code can't do anything beyond what's on your own machine.

**Treat API keys like passwords:**
- Never paste them in public (GitHub, Slack, screenshots, screen-share)
- Never commit them to git (the course shows you how to use `.env` files)
- If a key leaks, regenerate it immediately (every dashboard has a "regenerate" button)

---

## 1. Anthropic API Key (For AI Features)

### Step-by-Step

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Click **Sign Up** (top right). Use Google or email.
3. Verify your email if asked
4. Once you're logged in, look at the left sidebar. Click **Settings**.
5. Click **API Keys** (under Settings)
6. Click the **Create Key** button (top right of the page)
7. Name it: `onemillion-course`
8. **CRITICAL: Copy the key NOW.** It starts with `sk-ant-` and is about 100 characters long. You won't see it again — once you close the page, it's gone forever. (You can always create a new one, but you can't see the old one.)

Save it somewhere safe now: ideally your password manager. When the course asks you to use it, put it only in `.env.local` and the required deployment environment variable screen. Never paste it into chat, screenshots, GitHub, Slack, or committed files.

### Add Credits

Anthropic gives you $5 free to start. That's enough for the first few days. To finish the course, add $20 to your account:

1. Settings → **Billing** (left sidebar)
2. Click **Add Funds**
3. Add $20

Total spend over 18 days for most builders: **$5–15**. You'll have credit left over.

> 💡 **Don't have a credit card?** Some banks issue virtual cards (Privacy.com in the US, Revolut, Wise). You can also use a prepaid Visa.

### What If My Key Doesn't Work?

| Problem | Fix |
|---------|-----|
| `Invalid API key` error | Check you copied the full key including `sk-ant-` prefix. No spaces, no quotes. |
| `Insufficient credits` error | Add credits in Billing. Free $5 used up. |
| `Rate limit exceeded` | You hit the limit for your tier. Wait 60 sec or upgrade billing tier. |
| Lost the key | Create a new one. Delete the old one. |

---

## 2. Supabase Project (For Database + Auth)

You'll do this on **Day 5**, not today. But if you want to get it out of the way:

1. Go to [supabase.com](https://supabase.com)
2. Click **Start your project** (top right). Sign in with GitHub.
3. Click **New Project**
4. Choose your org (created automatically)
5. **Project Name:** something memorable, like `my-onemillion-app`
6. **Database Password:** generate a strong one — write it down! You won't need it often but you do need it.
7. **Region:** pick one near you (US East, EU West, etc.)
8. Click **Create Project**. Wait ~2 minutes for setup.

Once it's ready, you'll get:
- **Project URL** (looks like `https://abcdefgh.supabase.co`)
- **anon key** (a long string starting with `eyJ...`)

You'll need both on Day 5. Copy them somewhere safe.

### Free Tier Limits

| Limit | Free Tier | Enough For Course? |
|-------|-----------|--------------------|
| Database size | 500 MB | Yes (your app uses ~1 MB) |
| Bandwidth | 5 GB/month | Yes |
| Auth users | 50,000 | Yes |
| Edge functions | 500K invocations | Yes |

You will not pay Supabase anything during the course.

---

## 3. Optional: Other Services

These have free tiers and you sign up *when you get to that day*, not now:

| Service | When you need it | Free tier |
|---------|-----------------|-----------|
| **Vercel** | Day 4 (deploy your app) | Generous |
| **GitHub** | Day 4 (host your code) | Forever free |
| **Sentry** | Day 15 (error monitoring) | 5,000 events/month |
| **UptimeRobot** | Day 15 (uptime monitoring) | 50 monitors |

You'll see step-by-step signup for each one on the day you need it.

---

## Total Cost Of API Keys Over 18 Days

| Service | Cost |
|---------|------|
| Anthropic API (Claude calls) | $5–15 |
| Supabase | $0 |
| Vercel | $0 |
| GitHub | $0 |
| Sentry | $0 |
| Domain (optional, Day 14) | ~$10/year |

**Realistic total: $5–25 for the entire 18 days.**

This page is the current cost breakdown for the course.

---

→ **Back to:** [Getting Started](./getting-started.md) · [Day 1](../week-1-foundation/day-01-vision/learn.md)
