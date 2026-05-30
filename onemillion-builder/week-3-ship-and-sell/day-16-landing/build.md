# Day 16 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1-2 hours. Build the landing page.**

---

## Step 1: Draft The Copy (30 min)

Open your coding harness:

```bash
claude
```

Paste:

```
I'm on Day 16 of OneMillion. Help me write copy for my landing page.

Here's my PRD:
[paste contents of .onemillion/prd.md]

Here's my AI feature spec:
[paste contents of .onemillion/ai-feature.md]

Write copy for the 5-section landing page anatomy:

1. HERO: headline (specific, outcome-focused) + subhead + one CTA
2. PROBLEM: 2-3 sentences naming the pain (use the user's language)
3. SOLUTION: 3 outcome-focused bullets (NOT feature lists)
4. PROOF: a quote, screenshot description, or "launching publicly soon"
5. SECOND CTA: same button as Hero

Keep total length under 800 words. Be specific, not generic. Avoid startup-speak.

Draft a full version. Iterate with me until it sounds like the product.
```

Claude drafts. Iterate. The headline is the hardest part — spend 80% of the time getting it right.

---

## Step 2: Build The Page (30-45 min)

```
Now build the landing page at app/page.tsx using the copy above.

Use Tailwind. Make it:
- Mobile-responsive (works on iPhone Safari)
- Fast (single image max, no heavy assets)
- Single primary CTA in Hero and at bottom
- The button text should be specific (e.g., "Start Free" not "Click Here")
- The CTA should link to /signup

Also: add logic to redirect logged-in users to /dashboard so they don't
see the landing page after they've already signed up.

Use shadcn/ui components if any are already installed. Otherwise raw Tailwind.

Show me the file before saving.
```

Review. Push back if it looks generic — make Claude rewrite a section if it sounds like every other SaaS landing.

---

## Step 3: Add Auth Redirect Logic

In your landing page, add the redirect for logged-in users. Claude likely did this in Step 2 — verify:

```typescript
// app/page.tsx
import { createClient } from '@/lib/supabase/server';
import { redirect } from 'next/navigation';

export default async function LandingPage() {
  const supabase = createClient();
  const { data: { user } } = await supabase.auth.getUser();
  
  if (user) {
    redirect('/dashboard');
  }
  
  return (
    <main>
      {/* Hero, Problem, Solution, Proof, CTA */}
    </main>
  );
}
```

---

## Step 4: Test Locally (10 min)

```bash
npm run dev
```

Open `http://localhost:3000`:
- Logged out → see the landing page
- Click "Start Free" → goes to /signup
- Sign up → redirected to /dashboard
- Now visit `http://localhost:3000` again → redirects to /dashboard (because logged in)

Test on phone (use browser dev tools mobile view, or actually open on phone via local IP).

---

## Step 5: Deploy + Test Live (10 min)

```bash
git add .
git commit -m "Day 16: Landing page"
git push
```

After Vercel deploys, visit your live URL.

**Critical test:** open incognito and visit. See the landing? Click CTA → does it actually let you sign up?

---

## Step 6: Mobile Check (5 min)

Open the live URL on your phone. Does it look right?

Common issues:
- Text too big (Tailwind responsive classes like `text-2xl md:text-5xl` fix this)
- Buttons too small to tap (min 44px height)
- Hero image too wide / hidden on mobile

If broken on mobile: have Claude fix.

---

## Step 7: Verify

```bash
claude
```

Paste contents of [`ai-instructions-day-16.md`](./ai-instructions-day-16.md).

---

## What Should Be True After Day 16

- [ ] `app/page.tsx` is the landing page (not Next.js default)
- [ ] All 5 sections present
- [ ] One primary CTA in Hero + same CTA at bottom
- [ ] Logged-in users redirect to /dashboard
- [ ] Loads in <2 sec on live URL
- [ ] Looks reasonable on mobile
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 16 complete
- **Last verified day:** Day 16
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 17.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 16.

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
| Landing page redirects but I want to see it (logged in) | Sign out, OR add a query param like `?preview=true` to bypass the redirect during testing |
| Multiple CTAs look like they're competing | Make the primary CTA much bigger / bolder. Make any secondary actions ghosted/text-only |
| Headline is generic | Generic = bad. Use the EXACT phrase from a Day 2 conversation if possible |
| Mobile broken | Use Tailwind responsive utilities. `md:` prefix for desktop, default = mobile-first |
| Page is too long | Cut every word that doesn't earn its place. Aim for 500-800 words total |

---

→ **Done with Day 16?** Move to [Day 17 — First 10 Users](../day-17-first-users/learn.md).
