# Day 15 — Monitoring

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 13-18 | ~30-60 min | Know when things break before users tell you**

---

## Learning Frame

- **Mental model:** Monitoring lets you find problems before users have to explain them.
- **What can go wrong:** You install tools but never confirm they receive real events.
- **What to ignore today:** Ignore complex dashboards; capture errors, analytics, and uptime.

## What You'll Have After Today

- **Sentry** — catches every error in your app, emails you when something breaks
- **Vercel Analytics** — shows real visitor traffic, page views, top pages
- **UptimeRobot** — pings your site every 5 minutes; alerts you if it goes down
- **Email alerts configured** — you find out about problems before users do

All three are free for your usage level. Total setup time: ~30-60 min.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why Monitor? (~5 min read)

You're about to put real users on this. Things will break. The question isn't *if*, it's *how fast you find out*.

Without monitoring:
- A user hits an error → they leave silently → you never know
- Your app goes down → you discover it 12 hours later when you check Vercel
- Your AI feature returns gibberish for some users → you find out in week 4 when someone DMs you

With monitoring:
- Sentry emails you the SECOND an error fires, with the full stack trace + user context
- UptimeRobot pings you 5 min after your site goes down
- Vercel Analytics shows you who's using what — and patterns you didn't expect

Monitoring is the difference between "I think it's working" and "I know what's working."

---

## Part 2: Three Tools, Three Concerns (~10 min read)

This is multi-agent decomposition (Pillar 2) applied to observability. Don't try to do all of monitoring in one tool. Three small focused tools each doing one thing.

### Sentry — Errors
**Concern:** "Did something break?"
**What it catches:** Unhandled exceptions, runtime errors, failed promises, React render errors.
**Free tier:** 5,000 events/month — plenty for Cohort 0 scale.
**Setup:** Add SDK, drop in your DSN (a key), errors auto-report.

### Vercel Analytics — Traffic
**Concern:** "Is anyone using this?"
**What it shows:** Page views, unique visitors, top pages, referrers, device breakdown.
**Free tier:** 2,500 events/month on Hobby plan — plenty for first cohort.
**Setup:** One environment variable + one `<Analytics />` component.

### UptimeRobot — Uptime
**Concern:** "Is the site up?"
**What it does:** Pings your URL every 5 min. Alerts if down.
**Free tier:** 50 monitors, 5-min check interval — way more than you need.
**Setup:** Add your URL in their dashboard. Add your email.

You could swap any of these for alternatives (LogRocket, PostHog, Pingdom, etc.) — but for Cohort 0 these three are free, fast, and proven.

---

## Part 3: The Alert Discipline (~5 min read)

Two failure modes for monitoring:

### 1. No alerts → you miss real problems
Setup all three but don't configure email. Errors fire silently. UptimeRobot pings but you never see. Wasted setup.

### 2. Too many alerts → alert fatigue
Every error from a bot. Every 404 from someone testing your URLs. Every transient blip in Vercel. Your inbox fills up. You stop reading the emails. You miss the one that mattered.

**The discipline:**
- Sentry: only alert on **new** error types (not repeats of known errors)
- UptimeRobot: only alert if **down for 5+ minutes** (transient blips don't matter)
- Both: route to email you actually check (or set up a separate `alerts@` inbox)

Cohort 0 scale: ~5-10 alerts per month is healthy. More = signal of real bugs. Fewer = you're not catching enough.

---

## Today's Assignment

1. Set up Sentry — open https://sentry.io/signup/, install SDK, add DSN, deploy
2. Set up Vercel Analytics — open https://vercel.com/dashboard, enable Analytics, add component
3. Set up UptimeRobot — open https://uptimerobot.com/signUp, add monitor, configure email
4. Trigger a test error to confirm Sentry catches it
5. Run Day 15 verification

---

## Common Mistakes (Today)

1. **Forgetting to add Sentry to production.** Sentry SDK installed locally, but not configured to send events in production. Easy mistake — confirm by triggering a prod error.

2. **Notification email goes to a dead inbox.** Use an email you actually check daily.

3. **Vercel Analytics not visible because it's hidden behind a paywall.** Hobby plan gets 2,500 events. Beyond that, you need Pro. Stay under, or skip Analytics (Sentry covers most of what matters).

4. **Setting up but not testing.** "Sentry is installed" doesn't mean "Sentry works." Throw a test error.

5. **Adding bot traffic to UptimeRobot.** Sometimes UptimeRobot's pings get blocked by Cloudflare/firewall. Allow their IPs OR use a different keyword check.

---

## What Should Be True After Day 15

- [ ] Sentry installed and capturing errors
- [ ] Sentry test error appeared in dashboard
- [ ] Vercel Analytics enabled and showing data (after a few visits)
- [ ] UptimeRobot monitoring your live URL
- [ ] Alert emails confirmed (test by triggering)
- [ ] Verification passed ✅

---

## Verify Your Day 15

Ask your harness to run the OneMillion verifier for this day.

---

## Share It

```
✅ Day 15 done: monitoring on. Will know within 5 min if something breaks.
🎯 Tomorrow: landing page that explains what I built
#BuildingWith1M
```

---

## Go Deeper

- **[Sentry Docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/)** — official Next.js setup
- **[Vercel Analytics Docs](https://vercel.com/docs/analytics)** — official
- **[UptimeRobot Docs](https://uptimerobot.com/help/)** — official

---

→ **Next:** [Day 16 — Landing Page](../day-16-landing/learn.md)
