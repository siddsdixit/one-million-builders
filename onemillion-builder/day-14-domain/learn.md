# Day 14 — Custom Domain

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 13-18 | ~30-60 min | The 15-minute upgrade from "student project" to "real product"**

---

## Learning Frame

- **Mental model:** A domain is a credibility layer, not a requirement for learning.
- **What can go wrong:** DNS or auth callback settings break the live app.
- **What to ignore today:** Ignore expensive names; use a simple domain or intentionally stay on Vercel.

## What You'll Have After Today

- A **custom domain** for your app — `yourapp.com` (or `.io`, `.app`, `.dev`, whatever)
- **SSL working** automatically (https://, the lock icon)
- Your product **looks like a real product** the moment someone reads the URL
- DNS knowledge — the 5-min version of "how the internet finds your app"

This is optional. You can finish OneMillion and submit for Builder review on `your-app.vercel.app`. But for ~$10/year, you make your product look 10x more serious.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why A Custom Domain Matters (~5 min read)

A URL is a signal. People judge professionalism in 200 milliseconds.

- `my-app-v3-final-real.vercel.app` — looks like a hobby project
- `deliverabledash.com` — looks like a real product

Same code. Same features. Same product. The URL changes who takes it seriously.

For Demo Day (Day 18), for first users (Day 17), for your LinkedIn post — a custom domain matters. The $10/year cost pays back in 5 minutes of credibility.

---

## Part 2: DNS In 60 Seconds (~3 min read)

DNS = Domain Name System. The phone book of the internet.

When someone types `yourapp.com` in their browser:
```
Browser asks: "What IP address is yourapp.com?"
DNS responds: "It's 76.76.x.x (a Vercel server)"
Browser connects to that IP
Vercel server says: "Here's the website for that domain"
Browser displays your app
```

To make this work, you tell your domain registrar (where you bought the domain) where to point. For Vercel, the answer is: "point CNAME to cname.vercel-dns.com" or "point A record to 76.76.21.21".

That's it. Then wait 5-30 minutes for DNS to propagate globally.

---

## Part 3: SSL / HTTPS (~2 min read)

SSL (now called TLS) is the lock icon in the browser. It means traffic between user and server is encrypted.

**Vercel does SSL automatically.** Once you connect your domain, Vercel issues a free SSL certificate via Let's Encrypt. The lock icon appears within 5-30 min of connecting.

You don't configure anything. You don't pay anything. SSL just works because Vercel handles it.

(If you remember when SSL cost $200/year and took a sysadmin a day to set up — that's gone. Free + automatic now.)

---

## Today's Assignment

1. Buy a domain — $10/year on any registrar (Cloudflare, Namecheap, Porkbun, etc.)
2. Connect domain to your Vercel project
3. Wait for DNS to propagate
4. Update your app's references to use the new domain
5. Confirm SSL works (lock icon)

---

## Common Mistakes (Today)

1. **Buying a domain that's hard to spell.** "DelliveraballDashbord.com" → people will misspell it. Pick something short, memorable, lowercase, no hyphens.

2. **Not waiting long enough for DNS.** Propagation can take up to 24 hours. If it doesn't work after 5 minutes, wait. Don't troubleshoot until at least 30 min has passed.

3. **Adding the domain in Vercel but forgetting to update the registrar's DNS records.** Both sides need to know about each other. Both sides need to be configured.

4. **Buying `.io` or `.dev` without realizing they cost more.** `.com` is $10-12/year. `.io` is $30-50. `.dev` is $15. Pick based on budget, not vibes.

5. **Forgetting to update env vars / config that reference your Vercel URL.** Some places in your code might hardcode the URL — update them to use the new domain.

---

## What Should Be True After Day 14

- [ ] You bought a domain (or decided to stay on .vercel.app — that's also fine)
- [ ] Domain connected to your Vercel project (Settings → Domains)
- [ ] DNS records configured at your registrar (per Vercel's instructions)
- [ ] Visiting `yourapp.com` shows your app
- [ ] SSL works (https:// + lock icon)
- [ ] Any hardcoded URL references in your code updated
- [ ] Verification passed ✅

> 💡 **If you skip this day (stay on .vercel.app):** that's OK. Mark Day 14 as "skipped intentionally" in your verification. You can still earn Builder #N. The Builder Wall shows your Vercel URL.

---

## Verify Your Day 14

Ask your harness to run the OneMillion verifier for this day.
- Confirm your domain resolves (fetches the URL)
- Verify SSL is active
- Check for hardcoded URLs in code
- Report pass / needs revision (or "skipped" if you chose not to)

---

## Share It

```
✅ Day 14 done: live at yourapp.com 🎉
🎯 Tomorrow: monitoring (so I know when something breaks)
#BuildingWith1M
```

---

## Go Deeper

- **[Vercel Domain Docs](https://vercel.com/docs/projects/domains)** — official
- **[DNS Explained](https://www.cloudflare.com/learning/dns/what-is-dns/)** — Cloudflare's primer
- **[Let's Encrypt](https://letsencrypt.org/)** — the free SSL service Vercel uses

---

→ **Next:** [Day 15 — Monitoring](../day-15-monitoring/learn.md)
