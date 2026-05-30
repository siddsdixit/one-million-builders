# Day 14 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 30-60 min. Buy domain, connect to Vercel, wait for DNS.**

---

## Step 1: Buy A Domain (5 min)

Recommended registrars (in order):
1. **[Cloudflare](https://www.cloudflare.com/products/registrar/)** — at-cost pricing, no upsells. Need a Cloudflare account.
2. **[Porkbun](https://porkbun.com)** — cheap, no upsells, clean UI.
3. **[Namecheap](https://www.namecheap.com)** — popular, occasional sales.

Avoid: GoDaddy (overpriced + aggressive upsells), Google Domains (shutting down).

Pick a domain:
- `.com` if available ($10-12/year)
- `.app`, `.io`, `.dev` if `.com` is taken ($15-50/year)
- Short, memorable, no hyphens, lowercase

Buy it. ~$10-30 total.

---

## Step 2: Connect To Vercel (3 min)

1. vercel.com → your project → **Settings** → **Domains**
2. Click **Add** → type `yourapp.com` → Add
3. Vercel shows you DNS instructions. Note them.

Vercel typically says either:
- "Add an A record pointing to 76.76.21.21" OR
- "Add a CNAME record pointing to cname.vercel-dns.com"

---

## Step 3: Configure DNS At Your Registrar (5 min)

Log in to your domain registrar. Find DNS settings for your domain.

Add the records Vercel told you. Example for Cloudflare:
- Type: A
- Name: @ (means root domain)
- Value: 76.76.21.21
- TTL: Auto

Also add www variant:
- Type: CNAME
- Name: www
- Value: cname.vercel-dns.com

Save.

---

## Step 4: Wait For DNS (5-30 min)

Go make a coffee. Don't troubleshoot for 30 minutes. Propagation takes time.

Check status periodically:
```bash
dig yourapp.com
# Should eventually show your A record
```

Or use [dnschecker.org](https://dnschecker.org) — paste your domain, see propagation across the globe.

---

## Step 5: Verify Domain + SSL

Visit `https://yourapp.com` in your browser.

**You should see:** your app + the lock icon in the address bar.

If you get a security warning: SSL hasn't issued yet. Wait 5 more min. Refresh.

---

## Step 6: Update Hardcoded URLs (5 min)

Some places in your code might reference your Vercel URL. Update them.

```bash
claude
```

```
Search my codebase for any hardcoded references to my old Vercel URL
(e.g., my-app-name.vercel.app or similar). Update them to use the new
domain (yourapp.com).

Specifically check:
- app/layout.tsx (metadata)
- Any redirect URLs in Supabase config
- NEXT_PUBLIC_SITE_URL env var if you have one
- Any emails/copy that mentions the URL
```

Update Supabase auth callback URL too:
- Supabase → Authentication → URL Configuration
- Add `https://yourapp.com/auth/callback` to allowed redirect URLs

---

## Step 7: Commit + Push + Verify

```bash
git add .
git commit -m "Day 14: Custom domain live"
git push
```

```bash
claude
```

Paste contents of [`ai-instructions-day-14.md`](./ai-instructions-day-14.md).

---

## What Should Be True After Day 14

- [ ] Custom domain purchased
- [ ] DNS records configured at registrar
- [ ] Domain connected to Vercel
- [ ] `https://yourapp.com` shows your app with SSL
- [ ] Hardcoded URLs updated to new domain
- [ ] Supabase auth callback URL updated
- [ ] Verification passed ✅

OR: you intentionally skipped (staying on .vercel.app — also fine).

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 14 complete
- **Last verified day:** Day 14
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 15.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 14.

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
| Domain "Invalid Configuration" in Vercel | DNS records not added or wrong values. Re-check registrar. |
| Site loads but SSL warning | Wait 10 more min. SSL takes longer than DNS. |
| Site doesn't load at all after 30 min | DNS records wrong. Check dig output vs Vercel's instructions. |
| Auth callback fails after domain change | Supabase redirect URLs not updated. Add the new domain. |
| Some pages show old domain URLs | You forgot to update some hardcoded references. Grep again. |

---

→ **Done with Day 14?** Move to [Day 15 — Monitoring](../day-15-monitoring/learn.md).
