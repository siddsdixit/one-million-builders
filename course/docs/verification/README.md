# Verification System — How Builder #N Is Earned

OneMillion's credential is not earned by clicking through videos. It's earned by passing **Day 0 preflight verification plus 18 daily verification checks** through one verifier. Each check inspects the product directory, the active OneMillion pipeline outputs, deployed URLs when relevant, and manual confirmations when the work happens outside the repo.

This is what makes Builder #N credible: every Builder on the wall genuinely shipped what the course promised.

---

## How It Works

### One Verifier

The verifier is [`agent/verify.md`](agent/verify.md). The primary path is to say `day done`; your harness then reads the manifest completion gate and verifies the day.

1. Reads your product files, app directories, and active pipeline outputs
2. Checks structural requirements (files exist, JSON is valid, code patterns present)
3. Fetches deployed URLs when the day has a deployment gate
4. Confirms the live deployment contains meaningful text markers from the local source where possible
5. Reviews quality (PRD specific enough, prompts well-formed, etc.)
6. Reports pass / needs-revision with specifics
7. Updates `.onemillion/state.json`

You run this at the end of each day. Pass it, move on. Fail it, fix the issues and re-run.

### Final Verification (Day 18)

On Day 18, you run a final pass that:
1. Confirms Day 0 preflight and all 18 daily verifications are recorded in `.onemillion/state.json`
2. Checks your deployed URL is still live
3. Confirms anti-cheating signals (deployed URL is unique, commit history shows organic build, demo Loom features the builder)
4. Generates the [Builder Claim packet](../builder-claim.md) for form/GitHub submission

Your official Builder #N is issued after the Builder Claim is accepted.

---

## Two Layers Of Verification

### Layer 1: Structural Checks
File exists. JSON is valid. URL returns 200. The live page contains text from the local source. API endpoint behavior matches expectations. RLS is enabled. These are binary — either they're true or they're not.

Deployment verification is not just "the URL loaded." For deploy days, the verifier should fetch the live URL and compare what it sees against local code or expected artifacts. Example: Day 6 checks that the live homepage contains meaningful text from `app/page.tsx`; later deploy gates should compare the live product against local source markers or inspectable product evidence.

### Layer 2: Quality Checks (AI-Graded)
Is the PRD actually specific enough? Is the prompt well-designed? Does the landing page communicate clearly? These require judgment. Claude reviews and reports.

---

## Current Verification Path

### Harness-Native Verification

This is the supported path for the current version of the course. After each day:

1. Say `day done`.
2. Your harness reads `.onemillion/state.json`.
3. It reads the current day in `course-manifest.json`.
4. It checks the completion gate.
5. It updates `.onemillion/state.json`.
6. If the day passes, it advances your state to the next day.

### CLI Verification

Engineers can also run the schema-backed verifier directly for schema-backed days:

```bash
python course/docs/verification/scripts/verify.py 4 \
  --project-dir my-onemillion-build \
  --deployment-url https://your-app.vercel.app \
  --write-report
```

The CLI verifies local artifacts, runs schema checks, fetches deployment URLs, and updates `.onemillion/state.json` when `--write-report` is provided.

Today the CLI has machine schemas for Days 1-6. Days 7-18 use the same verifier with manifest gates plus harness inspection and human confirmation. Do not create extra proof files just to satisfy verification.

---

## Future Automation

### Submission Form
The course is designed for a final Google Form or web form where builders paste their verified claim packet. The form should collect:

- Builder name and email
- GitHub username
- OneMillion course fork URL
- Product name and one-liner
- Live app URL
- Public Loom demo URL
- Product repo URL if public
- Verification summary from `.onemillion/state.json`
- Builder Wall consent

See [Builder Claim Submission](../builder-claim.md) for the exact field list.

### Web Verifier
The future web verifier will let builders:
- Paste your GitHub repo URL
- Paste your deployed app URL
- Click "Verify Day X"
- Backend clones, runs checks, reports back

### GitHub Action
The future GitHub Action will run verification automatically on every push and sync daily progress to the Builder Wall.

---

## The Schemas

For builders who want to know exactly what's checked: see `verify/schema/day-XX.json` files. Today, schema files exist for Days 1-6. Days 7-18 use the unified verifier, manifest gates, app inspection, deployment checks, and final Builder Claim review.

Engineers: feel free to read the schemas. They're machine-readable specifications of what "pass" means for the schema-backed days.

---

## Anti-Cheating

Builders can theoretically fork someone else's repo and pass verification. To prevent this:
- Day 18 requires a live URL and public Loom demo
- Duplicate or suspicious submissions are flagged for manual review
- Day 2 validation evidence lives inside the PRD and may be spot-checked manually
- Demo Loom (Day 18) must show the builder using the product live

It's not bulletproof. It's good enough. The Builder Wall is a reputation system — fakes get noticed.

---

## What Happens After All 18 Days Pass

```
1. Your harness generates your verified Builder Claim packet
2. You submit the official form if available, or the GitHub Builder Claim issue fallback
3. Sid reviews the claim
4. Accepted claim receives the next official Builder #N
5. Builder profile / badge assets are added when Builder Wall automation is live
```

You receive:
- **Verified submission data** — generated by Day 18 verification
- **Builder #N after review** — your permanent, sequential number once accepted
- **Public profile / badge assets** — added when Builder Wall automation is live

---

→ Back to: [README](../../README.md) · [Getting Started](../getting-started.md)
