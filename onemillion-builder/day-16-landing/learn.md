# Day 16 — Landing Page

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 13-18 | ~1-2 hours | The page that explains what you built**

---

## Learning Frame

- **Mental model:** A landing page explains who the product is for and why they should try it.
- **What can go wrong:** You write generic hype instead of a specific promise.
- **What to ignore today:** Ignore brand perfection; make the offer clear.

## What You'll Have After Today

- A **landing page** at your root URL (yourapp.com)
- The page follows the **5-section anatomy** that converts visitors to users
- Working CTA (Call To Action) — a clear button that leads to signup
- Optional: signup flow that lets visitors try the product in <2 min
- The page someone would send a friend to explain what you built

This is the marketing equivalent of Day 3's PRD. Specific. Locked. Not perfect.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why Landing Pages Matter (~5 min read)

Your app exists. You have users. But when someone hears about it, they need a way to **understand it in 10 seconds**.

If you tell a friend "I built [thing]" and they ask "what is it?" — you need somewhere to send them. The Vercel root URL of your app showing a login screen isn't enough. They land, see a login form, think "I'm not signing up to figure out what this even is," and leave.

The landing page solves this. It's the **first thing** every potential user sees. It either earns 60 seconds of their attention OR they bounce.

---

## Part 2: The 5-Section Landing Page Anatomy (~15 min read)

Every effective landing page has these five sections. Same template that Stripe, Linear, Notion, and 90% of SaaS products use. Tested for decades.

### Section 1: HERO (above the fold)
What appears when someone lands. Three elements:

**Headline (the promise):**
- Specific, outcome-focused, addresses your target user
- Bad: "An AI-powered productivity tool"
- Good: "Never miss a freelance deliverable again."

**Subhead (the proof + scope):**
- Brief context for the headline
- Bad: "Use AI to be more productive!"
- Good: "DeliverableDash tracks all your client deliverables in one place. AI drafts your follow-ups. Save 90 minutes every Sunday."

**Primary CTA (the action):**
- One button. Specific verb.
- Bad: "Learn More"
- Good: "Start Free →"

Plus: a visual. Screenshot of the product OR a 30-sec demo video. Whatever shows "this is real."

### Section 2: PROBLEM
Name the pain.

- "Right now you spend Sunday cross-referencing Notion, email, and Slack to figure out what you owe whom."
- "You've lost clients because something fell through the cracks."

Use the user's language from your Day 2 conversations. Quote them if you have permission.

### Section 3: SOLUTION
Three specific things the product does.

Not features. **Outcomes.**

Bad: "✅ Dashboard ✅ AI features ✅ Email integration"
Good:
- ✅ See every deliverable across every client in one place
- ✅ AI drafts your status emails — review + send in 30 seconds
- ✅ Clients sign off on deliverables — no more "I never approved that"

### Section 4: PROOF
Why should they believe you?

Options (use 1-3):
- **Screenshot of the actual product** working
- **A quote from a real user** ("I dropped my Sunday review from 90 min to 10")
- **Numbers if you have them** ("Used by 50 freelancers across 12 industries")
- **Logos of companies your users work at** (with permission)
- **Founder credibility** ("Built by Sid Dixit — 8 years freelancing.")

For Cohort 0 builders: you may not have proof yet. That's OK. Use:
- A demo screenshot
- A quote from yourself ("I'm Sarah's first user. Saved me 4 hours last week.")
- "Launching publicly [date]" if it sounds like momentum

### Section 5: SECOND CTA
Same button as Hero. Same verb. End of page.

People who scroll all the way down are highly interested. Give them one more chance to click.

---

## Part 3: What NOT To Include (~5 min read)

The 5 sections are it. Don't add:

- ❌ Long product feature list (lives in app docs, not landing page)
- ❌ Multiple competing CTAs ("Sign up" + "Learn more" + "Book a demo")
- ❌ Generic startup-speak ("revolutionize", "synergy", "next-gen")
- ❌ Pricing page links (Cohort 0: keep it simple — free for now)
- ❌ About Us section (irrelevant on day 1)
- ❌ Team page
- ❌ Blog (you don't have one yet)

Less = better. Aim for ~500-800 words total on the landing page.

---

## Today's Assignment

1. Write copy for all 5 sections (you can write it raw or have Claude draft)
2. Build the page at `app/page.tsx` (replaces your current homepage)
3. Make sure auth redirects work — logged-in users go to dashboard, logged-out see landing
4. Test the CTA flow end-to-end
5. Run Day 16 verification

---

## What Good Looks Like

After Day 16, visiting yourapp.com (logged out) should:
1. Load in <1 second
2. Show a clear headline in the hero
3. Have a single prominent CTA button
4. Show the problem you solve
5. Show 3 specific outcomes (with checkmarks)
6. Show some form of proof (screenshot, quote, etc.)
7. End with another CTA matching the first

A logged-in user visiting yourapp.com should be redirected to their dashboard (not see the landing page).

---

## Common Mistakes (Today)

1. **Vague headline.** "Productivity reimagined" tells me nothing. "Never miss a freelance deliverable again" tells me everything.

2. **Multiple CTAs.** "Start Free" + "Watch Demo" + "Learn More" + "Book a Call" splits attention. Pick ONE.

3. **Listing features instead of outcomes.** People don't buy features. They buy what features let them do.

4. **No proof at all.** If you have nothing, write "Launching publicly [date]" — that creates urgency. Avoid the empty proof section.

5. **Page is too long.** 500-800 words. If it's a scroll, you've added too much. Cut.

---

## What Should Be True After Day 16

- [ ] `app/page.tsx` is the new landing page (not the default Next.js page)
- [ ] All 5 sections present (Hero, Problem, Solution, Proof, CTA)
- [ ] Single primary CTA in Hero AND at bottom
- [ ] Logged-in users redirect to dashboard
- [ ] Mobile-responsive (test on phone — Tailwind handles this if used properly)
- [ ] Live URL shows the new landing page
- [ ] Verification passed ✅

---

## Verify Your Day 16

Ask your harness to run the OneMillion verifier for this day.
- Check all 5 sections exist in the page
- Verify only one primary CTA
- Test that logged-out users see the landing
- Confirm logged-in users redirect
- Report pass / needs revision

---

## Share It

```
✅ Day 16 done: real landing page at yourapp.com. Time to get users.
🎯 Tomorrow: first 10 users
#BuildingWith1M
```

---

## Go Deeper

- **[Stripe's Landing Pages](https://stripe.com)** — the canonical example of a great SaaS landing
- **[Linear's Marketing Site](https://linear.app)** — modern, minimal, effective
- **[GoodPages.dev](https://goodpages.dev)** — curated gallery of landing pages
- **[Marketing Examples](https://marketingexamples.com)** — concrete patterns that work

---

→ **Next:** [Day 17 — First 10 Users](../day-17-first-users/learn.md)
