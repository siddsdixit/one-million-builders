# OneMillion Security Checklists

> Reference for the Guard agent. The course default is Next.js + MUI + Supabase + Vercel, with FastAPI only when explicitly selected.

---

## Web App Security Checklist

- [ ] **Transport:** HTTPS everywhere in production.
- [ ] **Authentication:** Supabase Auth configured correctly when login is required.
- [ ] **Authorization:** Protected routes verify the current user before reading/writing protected data.
- [ ] **Row Level Security:** RLS enabled on every user-owned or tenant-owned table.
- [ ] **Ownership/Tenancy:** Policies enforce `owner_id`, `tenant_id`, `organization_id`, or public/community rules.
- [ ] **Secrets:** No secrets in code, git history, browser bundles, or `NEXT_PUBLIC_*` vars.
- [ ] **Service Role:** Supabase service-role key is never exposed to client components.
- [ ] **AI Secrets:** `ANTHROPIC_API_KEY` is server-side only.
- [ ] **Input Validation:** Server-side validation with Zod, Supabase constraints, or Pydantic if FastAPI is selected.
- [ ] **Rate/Cost Limits:** AI routes and expensive actions have rate/cost limits.
- [ ] **Error Messages:** No stack traces, internal paths, raw DB errors, or sensitive data exposed to users.
- [ ] **XSS/CSP:** No unsafe HTML rendering without sanitization. CSP/security headers considered for production.
- [ ] **Dependencies:** No known Critical/High vulnerabilities from `npm audit` and relevant backend scans.
- [ ] **API Surface:** Every route/action classified as public, authenticated, owner-only, tenant-only, or admin.
- [ ] **Data Privacy:** PII inventory documented. No PII in logs. Delete/export posture documented when relevant.

## Supabase-Specific Checks

- [ ] RLS is enabled on all protected tables.
- [ ] Policies use `auth.uid()` or tenant membership checks.
- [ ] Anonymous access is intentional and documented for public tables.
- [ ] Storage buckets, if used, have explicit public/private policies.
- [ ] Auth redirect URLs are restricted to local/dev and production domains.
- [ ] SQL functions, if any, do not bypass tenant boundaries.

## Agent / AI Security Checklist

- [ ] System prompt is protected and never revealed.
- [ ] User input and retrieved/tool data are treated as untrusted.
- [ ] Agent only sees data the invoking user may access.
- [ ] Tool calls validate inputs and enforce permissions.
- [ ] Destructive actions require explicit human confirmation.
- [ ] Token and cost limits are enforced.
- [ ] Conversation/history data is scoped per user or tenant.
- [ ] Prompt-injection tests exist for agent/hybrid products.

## Optional FastAPI Checklist

Only use when FastAPI was selected in architecture.

- [ ] CORS restricted to the Vercel production URL.
- [ ] Pydantic validates all request bodies/query params.
- [ ] Supabase Auth session/user verification is implemented server-side.
- [ ] Service-role operations are limited and audited.
- [ ] `/docs` is disabled or protected in production.
- [ ] Backend env vars are set in the backend host, not committed.

---

## Agent Threat Model

| Threat | Impact | Mitigation |
|---|---|---|
| Prompt injection | Agent ignores instructions or leaks data | System prompt protection, untrusted-context handling |
| Data exfiltration | User or tenant data leaks | RLS, scoped queries, filtered tool results |
| Cost explosion | Unexpected API bills | Rate limits, token limits, budget alerts |
| Tool misuse | Unauthorized actions | Permission checks and human confirmation |
| Context poisoning | Bad retrieved/tool content steers agent | Treat retrieved content as data, not instructions |
