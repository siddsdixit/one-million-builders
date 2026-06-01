# OneMillion Testing Templates & Reference

> Reference for the Test Specialist. Read this file at the start of your work before generating any test plans or executing tests.

---

## QA Mindset

Good QA combines manual inspection and automated proof.

- **Manual QA** checks whether the product makes sense to a human, works on the live URL, and handles realistic product flows.
- **Automated QA** checks repeatable behavior so regressions are caught after future changes.
- **Skipped checks are not passes.** Record skipped checks as limitations with a reason and next action.

## Ship-Ready Checklist

Before declaring "ready for Guard", critical behavior must have evidence. Evidence can be automated test output, manual QA results, screenshots, live URL checks, or documented limitations when automation is not feasible yet.

- [ ] All Tier 1 API contract tests pass — Playwright request/Vitest for Next.js, pytest/httpx for FastAPI
- [ ] All Tier 2 security tests pass — auth, IDOR, tenant/RBAC, injection, validation
- [ ] All Tier 3 data integrity tests pass — CRUD/archive and persistence checks
- [ ] All Tier 4 E2E tests pass — `npx playwright test`
- [ ] All Tier 5 unit tests pass — Vitest/RTL for frontend/domain logic, pytest for FastAPI services
- [ ] All Tier 6 performance benchmarks pass — basic local/live response checks
- [ ] CI pipeline runs green — `.github/workflows/test.yml` committed
- [ ] Backend coverage ≥ 80% on services/ — `pytest --cov=services --cov-report=term`
- [ ] For agents: behavioral tests pass — `pytest backend/tests/test_agent/ -v`

If ANY critical item fails, the test phase is BLOCKED unless the builder explicitly accepts and documents the risk.
Add limitations (things that genuinely cannot be automated) to the Limitations section of `.onemillion/test-results.md`.

---

## Mandatory Deliverables

All required before handoff to Guard:

- `.onemillion/test-plan.md` — test cases written before any testing begins
- `.onemillion/test-results.md` — summary with actual manual QA evidence, automated command output, limitations, and verdict
- Automated tests in the repo where appropriate for the selected architecture
- `.github/workflows/test.yml` when the repo is ready for CI

---

## Testing Priorities

### Web App Testing Priority

1. **API contracts** — every endpoint happy + error path (status codes, response shapes)
2. **Security** — auth bypass, IDOR, injection, rate limiting, CSRF, header validation
3. **Data integrity** — CRUD completeness, relationships, business rules, concurrency
4. **E2E user flows** — core flow + per-feature happy path + auth flows + error states
5. **Unit tests** — service layer business logic edge cases
6. **Performance** — response time benchmarks, basic concurrent load

### Agent Testing Priority

1. **Happy path conversations** — agent responds correctly to the top 3 use cases defined in the PRD
2. **Tool call verification** — agent calls the right tool with correct parameters, handles tool results properly
3. **Boundary testing** — agent refuses out-of-scope requests politely, does not hallucinate capabilities
4. **Ambiguity handling** — agent asks clarifying questions when input is unclear, does not guess
5. **Error recovery** — agent handles tool failures gracefully, informs user of issues without exposing internals
6. **Adversarial testing** — prompt injection attempts are refused, system prompt is not leaked
7. **Multi-turn coherence** — agent maintains context across 5+ turns without confusion or repetition
8. **Cost verification** — token usage per conversation is within budget, no infinite tool call loops

---

## Conversation Test Format (agents)

```markdown
## Test: [Test Name]

**Category:** [Happy Path / Boundary / Error / Adversarial]
**Setup:** [Any required state]

| Turn | Role  | Message | Expected Behavior                                |
| ---- | ----- | ------- | ------------------------------------------------ |
| 1    | User  | [input] | —                                                |
| 2    | Agent | —       | [Expected: tool call / response / clarification] |
```

**Conversation Test Suites:**
Create test suites covering these categories:

1. **Core Capability Tests**
2. **Edge Case Tests**
3. **Boundary Tests**
4. **Integration Tests**
5. **Regression Tests**

---

## Pre-Flight Procedures

Run ALL of these BEFORE starting the server:

a. **Port conflict check:** Run `lsof -i :3000 | grep LISTEN`. If any process is on port 3000, kill it:

- **macOS:** `kill -9 $(lsof -ti:3000)`
- **Linux:** `fuser -k 3000/tcp`

Do NOT run tests against a stale process from a previous run.

b. **Framework availability check** (avoid unnecessary installs):

- Backend: `python -m pytest --version 2>/dev/null` — if exits 0, pytest is ready; skip pip install.
- Frontend: `npx playwright --version 2>/dev/null` — if exits 0, Playwright is ready; skip install.
- Only install if missing. If Chromium is already present (`ls ~/.cache/ms-playwright/ 2>/dev/null | grep chromium`), add `--skip-browser-download` to playwright install.

c. **Test data strategy:** All Playwright tests MUST use unique identifiers to prevent collision on re-run:

- Emails: `test_${Date.now()}@example.com` (never hardcode test@example.com)
- Entity names: `TEST-PO-${Date.now()}` or similar timestamped suffix

d. **Database env check:** If the project uses a database (look for `SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_URL`, or `DATABASE_URL` in `.env`, `.env.local`, or `docker-compose.yml`):

- Confirm a test-safe env is in use: value should contain "test", "dev", "local", or "localhost" — not a production host.
- If only a production DB URL is found, skip all write tests (create/update/delete). Run read-only tests only. Write in `QA/testing-limitations.md`: "Write tests skipped — no test database configured. Set TEST_DATABASE_URL to a non-production DB before running."
- Never run destructive operations against a production database.

**Supabase test database guidance:**

- Prefer a separate Supabase project for test/dev data.
- Never run destructive tests against production.
- Use unique test users and unique entity names for every run.
- Clean up test rows by owner/test marker after test completion.

e. **Teardown script:** After tests complete, write `QA/cleanup.sh` listing the exact delete/reset commands to remove test data, so the builder can reset manually.

---

## Test Plan Format

Use this format when writing `.onemillion/test-plan.md`:

```
# Test Plan — [App Name]
Source: [.onemillion/refined-prd.md / source code scan] | Sprint coverage: [.onemillion/development-plan.md / inferred]
Date: [ISO date]
UI Element Map: [list of pages and their key buttons/inputs discovered]

## [FR-001 or Page: /route-name]: [Feature/Page Name]
- TC-1a: [Action using exact UI label] → Expected: [result]
- TC-1b: [Validation] → Expected: [error or block]
- TC-1c: [Edge case] → Expected: [behavior]
```

---

## Testing Tiers — Full Reference

### TIER 1: API CONTRACT TESTS
**Framework:** Playwright/request tests for Next.js route handlers/server actions, or pytest + httpx.AsyncClient only if FastAPI is selected.
**Location:** `tests/api/` or `backend/tests/test_api/` for FastAPI-path projects.
**Coverage target:** 100% of in-scope server routes/actions.

For every endpoint, test:
- Happy path (correct status code and response shape)
- 401 without token, 401 with expired token
- 403 accessing another user's resource (IDOR)
- 422 with missing required fields, invalid types
- 404 with non-existent ID
- 409 on duplicate creation (if applicable)
- 429 rate limit exceeded (on auth endpoints)
- Pagination: empty, first page, cursor continuation, invalid cursor, limit boundaries

### TIER 2: SECURITY INTEGRATION TESTS
**Framework:** Playwright/request tests for default Next.js/Supabase apps, or pytest + httpx.AsyncClient only when FastAPI is selected.
**Location:** `tests/security/` or `backend/tests/test_security/` for FastAPI-path projects.

Dynamic security tests against running API:
- Missing/expired Supabase session → 401
- IDOR: User A's resource accessed by User B → 403
- SQL/RPC injection-style payloads are rejected or treated as plain text
- XSS payload in text fields → stored but escaped
- Oversized payload (10MB) → 413 or 422
- Malformed JSON → 400
- Rate limiting: 11 rapid auth requests → 429 on 11th

### TIER 3: DATA INTEGRITY TESTS
**Framework:** Playwright/request tests or test runner selected by architecture.
**Location:** `tests/data/` or app-specific test folder.

- Create → Read returns same data
- Update → Read returns updated data
- Delete → Read returns 404 (or filtered if soft-delete)
- Soft-deleted records don't appear in lists or aggregations
- Relationship integrity (cascade, restrict, archive per business rules)
- Concurrent updates → no data corruption
- Business rules from sprint briefs each have a test

### TIER 4: E2E USER FLOW TESTS
**Framework:** Playwright (TypeScript, **Chromium only**)
**Location:** `tests/e2e/` or `frontend/tests/e2e/` — one spec per sprint

- Complete Core Flow end-to-end on full stack
- Per-feature happy path for each in-scope feature
- Auth flows: register → login → protected → logout → rejected
- Error states: backend down → user-friendly error
- Responsive: critical flows at 375px and 1280px
- Config: screenshot on failure, video retain on failure, 1 retry

### TIER 5: UNIT TESTS
**Framework:** Vitest/React Testing Library for Next.js modules, or pytest + pytest-asyncio for FastAPI-path services.
**Location:** `tests/unit/` or `backend/tests/test_services/`.
**Coverage target:** meaningful coverage on validation/business rules.

- Service layer business logic edge cases (mock repository)
- Correct AppError subclass thrown for each error condition
- Do NOT test routers or repositories directly (covered by Tier 1 and 3).

### TIER 6: PERFORMANCE BENCHMARKS
**Framework:** pytest + httpx + time measurement
**Location:** `backend/tests/test_performance/`

- Health endpoint < 50ms
- List endpoint (100 records seeded) < 200ms
- Single resource GET < 100ms
- Create endpoint < 300ms
- Auth login < 500ms
- 10 concurrent requests to health → all 200

### TIER 7: CI PIPELINE
**Location:** `.github/workflows/test.yml`

Generate GitHub Actions workflow:
- Backend: pytest + coverage report + lint
- Frontend: build + lint + Playwright (with browser install cache)
- Database: Supabase test project or appropriate service container for the selected architecture
- Triggers: push to main, all PRs
- Artifacts: upload Playwright reports + coverage on failure

### TIER 8: API SCHEMA VALIDATION
**Framework:** Zod/Vitest or Playwright/request tests by default, pytest + httpx + Pydantic only when FastAPI is selected.
**Location:** `tests/schema/` or `backend/tests/test_security/test_schema_validation.py` for FastAPI-path projects.

For every endpoint with a Zod or Pydantic response model:
- Default Next.js/Supabase path: validate Zod schemas and user-safe response shapes.
- FastAPI path: call endpoint and validate response with `ResponseModel.model_validate(response.json())`.
- Verify no extra fields leak.
- Verify nullable fields return null (not missing) when empty

### TIER 9: RATE LIMIT & RESILIENCE TESTS
**Framework:** Playwright/request tests by default, pytest + httpx + asyncio for FastAPI.
**Location:** `tests/security/` or `backend/tests/test_security/test_rate_limit.py`

- Auth endpoints: N+1 rapid requests → 429 on overflow
- Verify `Retry-After` or `X-RateLimit-Remaining` headers
- Timeout handling: slow endpoint (if any) returns 504 or client timeout gracefully
- Malformed auth headers (`Bearer invalid`, `Bearer `, no header) → appropriate 401

### TIER 10: CONCURRENCY & RACE CONDITION TESTS
**Framework:** Playwright/request tests or the architecture-selected backend test runner.
**Location:** `tests/data/` or `backend/tests/test_data/test_concurrency.py`

- Two users update same resource simultaneously → no data corruption
- Concurrent creates with unique constraint → one 201, one 409
- Rapid delete + read of same resource → 404 (not 500)

### TIER 11: ACCESSIBILITY TESTS
**Framework:** Playwright + @axe-core/playwright
**Location:** `frontend/tests/e2e/` (added to existing specs)

- Run `checkA11y()` on each critical page after navigation
- Fail on "critical" or "serious" axe-core violations
- Check: color contrast, ARIA labels, keyboard navigation, focus management

### TIER 12: DATABASE MIGRATION TESTS
**Framework:** Supabase SQL/migration checks by default, or Alembic only if the FastAPI architecture selected it.
**Location:** Run as a SEPARATE command in Phase 2 (cross-cutting), NEVER chained with pytest

- Supabase migrations/SQL apply cleanly against the project or local Supabase environment
- RLS policies exist after migration
- Alembic upgrade/downgrade round-trip only for FastAPI-path projects that use Alembic
- If migrations fail, log as a bug for the build agent. Do NOT let migration failures block pytest.

### AGENT BEHAVIORAL TESTS (agent/hybrid only)
**Framework:** pytest + LLM provider SDK
**Location:** `backend/tests/test_agent/`

Happy paths, boundary/refusal tests, injection attempts, cost verification, multi-turn coherence.

---

## Test Factories Reference

Create reusable fixtures in the repo's selected test location:
- `client` — request client, browser context, or httpx.AsyncClient with ASGITransport for FastAPI
- `auth_client` — client or browser context with registered + logged-in Supabase user
- `second_auth_client` — different user for IDOR tests
- `make_[entity](**overrides)` — factory functions for test data with sensible defaults
- `cleanup` — auto-cleanup fixture that removes test rows after each test module

Every test uses factories — never hardcode test data inline.

---

## Playwright Configuration Reference

**Always use Chromium. Never Firefox or WebKit.**

Install: `npx playwright install chromium` (not `npx playwright install` which downloads all browsers)

Standard config for `frontend/playwright.config.ts`:

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
  retries: 1,
  reporter: [['list']],
  webServer: [
    {
      command: 'cd ../backend && python -m uvicorn app.main:app --port 8000',
      port: 8000,
      reuseExistingServer: true,
    },
    {
      command: 'npm run dev',
      port: 3000,
      reuseExistingServer: true,
    },
  ],
});
```

---

## Test Plan Template

Use this format for `.onemillion/test-plan.md`:

```
# Test Plan — [Product Name]

> Generated: [date] | Scope: [full/mvp] | Sprints: S0–S[N]

## Summary

Total: [X] tests | [N] tiers | [M] sprints

| Tier | Tests | Target |
|------|-------|--------|
| 1. API Contracts | [n] | 100% endpoints |
| 2. Security | [n] | OWASP top risks |
| 3. Data Integrity | [n] | All CRUD chains |
| 4. E2E Flows | [n] | Core journeys |
| 5. Unit Tests | [n] | 80% services/ |
| 6. Performance | [n] | Key endpoints |
| 7. CI Pipeline | 1 | GitHub Actions |
| 8. Schema Validation | [n] | All response models |
| 9. Rate Limit & Resilience | [n] | Auth endpoints |
| 10. Concurrency | [n] | Shared resources |
| 11. Accessibility | [n] | Critical pages |
| 12. Migration | 1 | Round-trip |

## Sprint Matrix

| Sprint | Features | T1 | T3 | E2E |
|--------|----------|----|----|-----|
| S0 | Foundation | [n] | [n] | 0 |
| S1 | Auth | [n] | [n] | [n] |
...

## Per-Sprint Detail

### S[N] — [Sprint Name]

**Acceptance Criteria → Test Mapping:**
| AC | Criterion | Test ID | Tier | File |
|----|-----------|---------|------|------|
| AC-01 | ... | T1-S1-001 | 1 | test_s1_auth.py |
```

---

## Test Results Report Template

Use this format for `.onemillion/test-results.md`:

```
# Test Results — [Product Name]

> Generated: [date] | Duration: [X min] | Verdict: PASS / FAIL

## Dashboard

| Metric | Value |
|--------|-------|
| Total Tests | [X] |
| Passed | [Y] |
| Failed | [Z] |
| Skipped | [W] |
| Coverage (services/) | [X]% |
| Bugs Found | [N] |
| Bugs Fixed | [M] |

## Per-Sprint Results

| Sprint | T1 | T3 | Status |
|--------|----|----|--------|
| S0 | 3/3 | 1/1 | GREEN |
...

## Cross-Cutting Results

| Tier | Total | Passed | Failed | Status |
|------|-------|--------|--------|--------|
| 2. Security | [n] | [n] | 0 | GREEN |
| 8. Schema Validation | [n] | [n] | 0 | GREEN |
| 9. Rate Limit | [n] | [n] | 0 | GREEN |
| 10. Concurrency | [n] | [n] | 0 | GREEN |
| 11. Accessibility | [n] | [n] | 0 | GREEN |
| 12. Migration | 1 | 1 | 0 | GREEN |
...

## Spec-Aligned Verification

| Metric | Value |
|--------|-------|
| Total Acceptance Criteria | [X] |
| Criteria with Tests | [Y] |
| Coverage | [Y/X] ([%]) |

**Missing coverage:**
| AC | Criterion | Status |
|----|-----------|--------|
| AC-XX | ... | No test / Partial |

## Bug Report

| ID | Sev | Sprint | Description | Fix | Status |
|----|-----|--------|-------------|-----|--------|
| BUG-001 | P0 | S1 | ... | ... | Fixed |
...

## Performance Benchmarks

| Endpoint | Target | Actual | Status |
|----------|--------|--------|--------|
| GET /health | < 50ms | [n]ms | ... |
...
```

---

## PDF Test Report Reference

Generate `.onemillion/assets/test-report.pdf` using the `pdf` skill with reportlab.

### Visual Design
- **Color palette:** Primary brand color (from design-system.md if available, else deep blue #1a365d) + green (#16a34a) for pass + red (#dc2626) for fail + gray (#6b7280) for neutral
- **Typography:** Helvetica bold for headings, Helvetica regular for body. 24pt title, 16pt section heads, 10pt body/tables
- **Layout:** 0.75" margins. Header bar on every page with product name + "Test Report" + date. Footer with page number

### Page Layout
- **Page 1 — Dashboard:** Verdict banner, stats row (Total/Passed/Failed/Coverage), donut chart, bar chart per tier, sprint status strip
- **Page 2 — Sprint Results:** Full table with alternating row colors, stacked bar chart
- **Page 3 — Bug Report:** Severity color-coded table (P0=red, P1=orange, P2=yellow)
- **Page 4 — Performance & Coverage:** Horizontal bar chart with target line, coverage gauge
- **Page 5 — Limitations & Recommendations:** Bulleted list with section icons
