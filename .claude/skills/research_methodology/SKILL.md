---
name: research_methodology
description: Research output templates, distillation workflow, and quality standards for evidence-driven research
---

# Research Methodology

## Research Output Template

Use for all research documents in `docs/research/`.

```markdown
# Research: {Topic}

**Date**: {ISO-8601} | **Confidence**: {High/Medium/Low} | **Sources**: {count}

## Executive Summary
{2-3 paragraph overview of key findings, main insights, and overall conclusion}

## Research Methodology
**Search Strategy**: {how sources were found}
**Source Selection**: Types: {academic/official/industry/technical_docs} | Reputation: {high/medium-high min} | Verification: {cross-referencing approach}
**Quality Standards**: Target 3 sources/claim (min 1 authoritative) | All major claims cross-referenced | Avg reputation: {0.0-1.0}

## Findings

### Finding 1: {Descriptive Title}
**Evidence**: "{Direct quote or specific data point}"
**Source**: [{Source Name}]({URL}) - Accessed {YYYY-MM-DD}
**Confidence**: {High/Medium/Low}
**Verification**: [{Source 2}]({URL2}), [{Source 3}]({URL3})
**Analysis**: {Brief interpretation or context}

## Source Analysis
| Source | Domain | Reputation | Type | Access Date | Cross-verified |
|--------|--------|------------|------|-------------|----------------|
| {name} | {domain} | {High/Medium-High/Medium} | {academic/official/industry/technical} | {YYYY-MM-DD} | {Y/N} |

## Knowledge Gaps
### Gap 1: {Description}
**Issue**: {missing/unclear info} | **Attempted**: {sources searched} | **Recommendation**: {how to address}

## Conflicting Information (if applicable)
### Conflict 1: {Topic}
**Position A**: {Statement} — Source: [{Name}]({URL}), Reputation: {score}, Evidence: {quote}
**Position B**: {Contradictory statement} — Source: [{Name}]({URL}), Reputation: {score}, Evidence: {quote}
**Assessment**: {Which source more authoritative and why}

## Recommendations for Further Research
1. {Specific recommendation with rationale}

## Full Citations
[1] {Author}. "{Title}". {Publication}. {Date}. {URL}. Accessed {YYYY-MM-DD}.

## Research Metadata
Examined: {count} | Cited: {count} | Cross-refs: {count} | Confidence: High {%}, Medium {%}, Low {%} | Output: docs/research/{filename}
```

## Quality Standards

### Per-Claim Requirements (Adaptive to Turn Budget)

- **Ideal**: 3+ independent sources per major claim
- **Acceptable**: 2 credible sources when budget is constrained
- **Minimum**: 1 authoritative source (official docs, RFC, specification) with explicit confidence note
- **Never**: 0 sources — unsourced claims must be flagged as "[unverified]"

When budget runs low, prioritize BREADTH (cover all claims with minimum sources) over DEPTH (exhaust sources for one claim while ignoring others).

### Confidence Ratings
- **High**: 3+ high-reputation sources agree, no contradictions
- **Medium**: 2+ agree, minor contradictions or some medium-trust
- **Low**: single source or significant contradictions

### Quality Gates (before finalizing)
1. Every major claim has citations (3+ ideal, 2 acceptable, 1 authoritative minimum)
2. All sources from trusted domains
3. All findings evidence-backed
4. Knowledge gaps documented
5. Claims with fewer than 3 sources have confidence rating adjusted accordingly
