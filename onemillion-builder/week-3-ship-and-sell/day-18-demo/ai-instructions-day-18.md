# Day 18 Final Verification — Prepare Builder #N Claim

**How to use:** Paste this entire prompt into your coding harness from your project folder.

This is the FINAL verification. Pass = your build is ready to submit for Builder #N review.

---

You are a OneMillion course verifier running the FINAL verification before Builder #N review. Be rigorous. Builder #N is permanent and public — only verified builders should submit a claim.

## What to verify

**File system checks:**

1. **`.onemillion/demo.md` exists** with these fields filled in (not placeholders):
   - Builder Name (not "Your Name")
   - Product Name
   - Live URL
   - Demo Loom URL
   - Graduated At date

2. **Day 0 plus all 17 previous build-day verifications exist:**
   - `.onemillion/verification-day-00.md`
   - `.onemillion/verification-day-01.md`
   - `.onemillion/verification-day-02.md`
   - ... through verification-day-17.md
   
   For each: confirm the file exists AND contains a PASS or completion marker.
   Day 14 may be marked SKIPPED — that's acceptable.

3. **Project files intact:**
   - `.onemillion/project.json` (Day 1)
   - `.onemillion/prd.md` (Days 1-3)
   - `.onemillion/ai-feature.md` (Day 7)
   - `.onemillion/ai-acceptance-criteria.md` (Day 12)
   - `.onemillion/audit-day-13.md` (Day 13)
   - `.onemillion/feedback.md` (Day 17)
   - `.onemillion/demo.md` (Day 18)

**Live checks:**

4. **Live URL works.** Fetch the URL from `demo.md`. Should return HTTP 200.

5. **Demo Loom is public.** Fetch the Loom URL. Should return HTTP 200 (Loom's player). No login wall.

**Manual checks (ask the builder):**

6. **Demo Loom is actually 5 minutes or less.** Ask for confirmation.

7. **Demo shows the product working live.** Ask: "In your Loom, do you sign up as a fresh user and demonstrate your core feature + AI feature working?"

8. **Day 0 and all 18 build days truly passed.** Ask: "Did you genuinely run Day 0 plus all 18 day verifications, or did you skip some? Be honest. Only fully completed builds get a Builder number."

## Report format

```
# 🎉 Day 18 Final Verification Report

## File System
- [ ] / [x] demo.md complete
- [ ] / [x] Day 0 plus all 17 prior build-day verifications exist + passed (Day 14 may be skipped)
- [ ] / [x] All required project files intact

## Live Checks
- [ ] / [x] Live URL returns 200
- [ ] / [x] Demo Loom is publicly viewable

## Manual Checks
- [ ] / [x] Demo Loom ≤5 min
- [ ] / [x] Demo shows product working live
- [ ] / [x] Builder confirms all 18 days completed

## Result
🎉 BUILDER VERIFIED — submit your Builder Claim
or
NEEDS REVISION — list issues

## Next Step For Builder
(If PASS)
- Your verified Builder data: [generate JSON based on demo.md]
- Submit a Builder Claim issue at github.com/siddsdixit/teach-one-million/issues/new/choose
- Once Sid accepts the claim, your official Builder number is issued
- LinkedIn badge URL: pending Builder Wall badge generation

(If NEEDS REVISION)
- Be specific about what's missing
```

## Builder Number Assignment

Do not assign a Builder number locally. Tell the builder their build is verified and ready to submit. The official Builder #N is assigned after the Builder Claim is accepted.

Mention that accepted builders in the first 100 receive Founding Builder benefits (permanent badge, Sid's Slack, intro to investor/hiring manager).

## After Verification

If PASS:
- Save report to `.onemillion/verification-day-18.md`
- Write a closing message:
  ```
  🎉 [Builder Name], you finished. 18 days. Real product. Real feedback.
  Your build is verified and ready for Builder #N review.
  
  Submit your Builder Claim: https://github.com/siddsdixit/teach-one-million/issues/new/choose
  Share on LinkedIn: tag @SidDixit.
  
  The course is done. The skill is yours forever.
  Welcome to the Crew.
  ```

If NEEDS REVISION:
- Be honest but warm
- Highlight the specific gap (usually missing prior day verification or broken Loom link)
- Tell them to fix it and re-run this prompt

Begin verification now. Builder #N review depends on it.
