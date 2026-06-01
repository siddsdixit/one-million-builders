# Builder Claim Submission

This is the final submission packet for OneMillion.

At the end of Day 18, your harness generates the verified data below. Submit it through the official Builder Claim form for your cohort. If no form link has been announced yet, use the public GitHub Builder Claim issue path.

## Official Submission Paths

| Path | Use when |
|---|---|
| **Builder Claim Form** | Your cohort, live session, or Sid gives you the Google Form link. Submit the packet below there first. |
| **GitHub Builder Claim issue** | You are self-paced or no form link has been announced yet. |

Current public fallback:

```text
https://github.com/siddsdixit/one-million-builders/issues/new/choose
```

## What The Form Should Ask

Use these fields for the Google Form or GitHub issue. Do not ask learners to invent new proof at the end; this should come from the app, the PRD, the live URL, the Loom URL, and `.onemillion/state.json`.

| Field | Required | Source |
|---|---:|---|
| Builder display name | Yes | `.onemillion/state.json` or learner |
| Email | Yes for form | Learner |
| GitHub username | Yes | Learner |
| Course fork URL | Yes | Day 0 preflight |
| Product name | Yes | `.onemillion/project.json` |
| Product one-liner | Yes | `.onemillion/project.json` or demo summary |
| Live app URL | Yes | Day 6+ deployment |
| Public Loom demo URL | Yes | Day 18 |
| Public product repo URL | Optional | Learner product repo |
| OneMillion fork URL | Yes | Learner course fork |
| Last verified day | Yes | `.onemillion/state.json` |
| Verification summary | Yes | `.onemillion/state.json` |
| Cohort | Optional | Cohort name, live session, or self-paced |
| Consent to list on Builder Wall | Yes | Learner |
| LinkedIn/X profile | Optional | Learner |
| Notes for reviewer | Optional | Learner |

## Claim Packet Template

Copy this into the form or GitHub issue:

```markdown
# OneMillion Builder Claim

**Builder display name:**
**Email:**
**GitHub username:**
**OneMillion course fork URL:**
**Product name:**
**Product one-liner:**
**Live app URL:**
**Public Loom demo URL:**
**Product repo URL:**
**Cohort:** self-paced / cohort name
**Consent to be listed on Builder Wall:** yes/no
**LinkedIn/X profile:**

## Verification Summary

- Day 0:
- Day 1:
- Day 2:
- Day 3:
- Day 4:
- Day 5:
- Day 6:
- Day 7:
- Day 8:
- Day 9:
- Day 10:
- Day 11:
- Day 12:
- Day 13:
- Day 14:
- Day 15:
- Day 16:
- Day 17:
- Day 18:

## Reviewer Notes

[Anything the reviewer should know.]
```

## Reviewer QA

The reviewer should check:

- Course fork exists and has Day 0 setup evidence.
- Product live URL opens in an incognito browser.
- Loom opens without login.
- Loom shows the live product, not slides only.
- Demo behavior matches the product claim.
- Verification reports exist for all required days.
- Deployment evidence matches local code where automated checks support it.
- Duplicate submissions are not using the same product URL/Loom/repo without explanation.

Accepted claim = official Builder #N.
