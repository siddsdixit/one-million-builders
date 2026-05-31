# Day 17 — First 10 Users

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 13-18 | ~45-90 min | The day "I built a thing" becomes "real people are using my thing"**

---

## Learning Frame

- **Mental model:** A product becomes real when a target user reacts to it.
- **What can go wrong:** You ask for praise or wait for perfect polish before outreach.
- **What to ignore today:** Ignore broad launches; get specific feedback from a few people.

## What You'll Have After Today

- **At least 1 real user** (someone who's not you) has signed up + tried it
- **At least 1 piece of real feedback** (what they did, what they thought, what broke)
- A short list of **iteration candidates** for after Day 18
- The feeling of having shipped something to the world

This is one of the most underrated days. Most courses end at "deployed." OneMillion ends at "users." The difference is huge.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why First Users Matter (~5 min read)

A product without users is a Github project. A product with users — even one — is real.

Real users do things you didn't predict:
- They use the AI feature in a way you didn't design for
- They sign up with an email format that breaks your validation
- They love a feature you thought was throwaway
- They hate a feature you thought was the killer one

You can't learn any of this without putting it in front of humans. **Today you put it in front of humans.**

This is the human review loop pillar (#5) at the product level. AI proposes. Humans dispose. You proposed a product. Now humans dispose.

---

## Part 2: Who To Reach Out To (~10 min read)

You're going to reach out to 10 people. Some will sign up. Some won't. Aim for 1-3 actual users.

### Tier 1 (start here — highest response rate)
- The people you interviewed in Day 2's Mom Test conversations
- Friends/colleagues you've told about the project during the build
- Coworkers if your product is work-related

These people are pre-warmed. They know you've been building. They'll respond.

### Tier 2 (next — broader reach)
- Friends of friends who match your target user
- Your LinkedIn network (post about it — see Day 0 commitment)
- Reddit communities related to the problem (be respectful — read rules first)

### Tier 3 (cold — lowest response, but valuable signal)
- Cold DMs to strangers who match your target user profile
- Hacker News "Show HN" post (only if you feel ready — once you post, it's done)
- Product Hunt (for later, not Day 17)

**For Cohort 0 / Day 17: focus on Tier 1.** Aim for 1-3 real users by end of day. Don't try to launch broadly today. That's after Day 18.

---

## Part 3: How To Reach Out (~10 min read)

Use the same skills from Day 2's Mom Test — but inverted. Now you're asking for feedback on a product, not validating a problem.

### The template (for Tier 1 — people you know)

```
Hey [name],

Remember [X — your conversation, the problem you discussed]? I built it.

It's live at [URL]. Takes 2 minutes to sign up + try.

I'm looking for 1-3 people to try it this week and tell me what's confusing,
what's missing, what works. Especially you because [specific reason — they
had the exact problem, etc.]

Would you mind giving it a shot? Even 10 minutes of honest feedback would
help massively.

Thanks,
[you]
```

### The template (for Tier 2 — LinkedIn / broader)

```
Just shipped Day 17 of #OneMillion. Built [one-sentence description].

Live at [URL].

Looking for 5 people to try it this week + give honest feedback. If you'd
match the target user (specifically: [user type]), please DM me — I'll
send you direct access.

What worked, what's broken, what's missing — all feedback welcome.
```

### What NOT To Do

- ❌ Don't ask for "support" or "encouragement" — ask for FEEDBACK
- ❌ Don't promise free products forever as a gimmick
- ❌ Don't be apologetic ("sorry to bother you, just wanted to ask...")
- ❌ Don't mass-DM 50 strangers in one day (you'll get reported)

---

## Part 4: Capturing Feedback (~5 min read)

When someone tries it and tells you what they think, write it down. Today. Fresh.

Ask the orchestrator to record feedback notes in `.onemillion/state.json`:

```markdown
## Feedback Log

### [Name] — Tried [date]
**What they did:**
[Signed up. Created 3 deliverables. Tried AI feature once.]

**What worked:**
- "Loved how fast the dashboard loaded"
- "AI follow-up draft was useful — I'd use this regularly"

**What didn't:**
- "Got confused signing up — wasn't clear what 'tenant' meant"
- "AI feature didn't notice I had a deliverable due tomorrow — should have flagged"

**What's missing:**
- "Need a way to mark a deliverable as 'sent' — only 'in-progress' and 'done'"

**Quote of the conversation:**
- "This would save me 90 min every Sunday if it worked for multi-client emails"

**My take:**
- Validates the AI value
- Confirms the dashboard works
- Bug: "tenant" terminology — replace with friendlier word
- Feature gap: "sent" status — worth adding in v2
```

Capture 1-3 of these. They're gold.

---

## Today's Assignment

1. Make a list of 10 people to reach out to (mostly Tier 1)
2. Send DMs / emails / texts
3. Walk anyone who responds through signup (over a call or messaging)
4. Watch them use it (if possible — screenshare reveals tons)
5. Capture their feedback in `.onemillion/state.json`
6. Run Day 17 verification

---

## What Good Looks Like

By end of Day 17:
- 10 outreach messages sent
- 1-3 responded
- 1+ actually signed up and tried it
- 1+ feedback entry in `.onemillion/state.json` with specific quotes

You might get 0 actual users today. That's OK — your outreach list buys you 1-2 users over the next week. Demo Day (Day 18) can include the feedback you collected, not just users.

---

## Common Mistakes (Today)

1. **Asking for praise, not feedback.** "Tell me what you think!" → people say "looks great!" → useless. Ask: "What confused you? What's missing?"

2. **Not watching them use it.** If you can do a 10-min screenshare, do it. Watching someone use your product reveals more in 5 minutes than 5 written feedback notes.

3. **Defending against criticism.** When someone says "this confused me," don't explain why it shouldn't have. Just listen. They're right.

4. **Reaching out to too-friendly people only.** Your mom will love it. Your best friend will love it. Their feedback isn't useful. Reach out to actual target users.

5. **Trying to make changes mid-feedback.** Capture all the feedback first. Iterate after Day 18. Don't break the product trying to fix things mid-conversation.

---

## What Should Be True After Day 17

- [ ] You sent 10 outreach messages
- [ ] At least 1 response received
- [ ] At least 1 person actually used the product
- [ ] `.onemillion/state.json` records at least 1 feedback entry or pending-feedback status
- [ ] You did NOT iterate during feedback collection (resist the urge)
- [ ] Verification passed ✅

---

## Verify Your Day 17

Ask your harness to run the OneMillion verifier for this day.
- Check `.onemillion/state.json` records outreach and feedback status
- Ask about your outreach count + response count
- Help you categorize the feedback (now, v2, ignore)
- Report pass / needs revision

---

## Share It

```
✅ Day 17 done: real users + real feedback. The product is alive.
🎯 Tomorrow: Demo Day → Builder #N
#BuildingWith1M
```

---

## Go Deeper

- **[YC: Talk to your users](https://www.ycombinator.com/library/4f-talking-to-users)** — Eric Migicovsky's classic talk
- **[Lean Customer Development](https://www.amazon.com/Lean-Customer-Development-Building-Customers/dp/1492023744)** by Cindy Alvarez — playbook for ongoing user conversations
- **[The Mom Test](https://www.momtestbook.com/)** (same book as Day 2) — also great for product feedback conversations

---

→ **Next:** [Day 18 — Demo Day → Builder #N](../day-18-demo/learn.md)
