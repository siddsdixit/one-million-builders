# OneMillion Security Checklists

> Reference for the Guard agent. Work through these checklists systematically.

---

## Web App Security Checklist

- [ ] **Transport:** HTTPS everywhere — enforce in production, redirect HTTP → HTTPS. HSTS header enabled.
- [ ] **Authentication:** Argon2 password hashing, JWT with short expiry (15-30 min access token), refresh token rotation
- [ ] **Input Validation:** Server-side validation with Pydantic on ALL incoming data — never trust the client
- [ ] **Authorization:** Ownership verification on every resource — user can only access their own data
- [ ] **Secrets Management:** No secrets in code or version control (including git history) — all credentials in environment variables
- [ ] **CORS:** Restrictive CORS policy — only allow the frontend origin, never `*` in production
- [ ] **Rate Limiting:** API rate limiting on auth endpoints (10/min) and general API (100/min)
- [ ] **Error Messages:** Never expose stack traces, internal paths, or DB error details to the client. Global error handler catches all exceptions.
- [ ] **Dependencies:** No known Critical/High vulnerabilities (`pip-audit`, `npm audit`). All licenses compatible.
- [ ] **XSS / CSP:** Content Security Policy header configured. No `dangerouslySetInnerHTML` without sanitization.
- [ ] **Cookie Security:** HttpOnly, Secure, SameSite=Strict on all auth cookies (if using cookies)
- [ ] **NoSQL Injection:** Pydantic models validate all query parameters — never pass raw user input to MongoDB query operators ($gt, $regex, $where, $expr)
- [ ] **API Surface:** Every endpoint classified (public/authenticated/admin). No unintentionally public endpoints.
- [ ] **Data Privacy:** PII inventory documented. No PII in logs. Account deletion removes PII. Data in transit over TLS.
- [ ] **Swagger/Docs:** `/docs` endpoint disabled or auth-protected in production config

---

## Agent Security Checklist

### 1. Prompt Injection Defense

- [ ] System prompt is in a separate, protected section
- [ ] User input is sanitized before being appended to context
- [ ] Agent tested with known injection payloads
- [ ] System prompt contents are never revealed in responses

### 2. Data Leakage Prevention

- [ ] Conversation history is scoped per-user
- [ ] Agent does not reveal internal implementation details
- [ ] Tool results are filtered — sensitive fields stripped
- [ ] PII in tool responses is masked unless explicitly required

### 3. Tool Misuse Prevention

- [ ] Destructive actions require explicit human confirmation
- [ ] Tool inputs are validated against expected types and ranges
- [ ] Tool access is limited to what the agent needs (least privilege)
- [ ] No arbitrary code execution tools unless sandboxed

### 4. Cost Controls

- [ ] Token limits enforced per conversation
- [ ] Max tool calls per conversation enforced
- [ ] Budget alerts configured (alert at 80% of daily budget)
- [ ] Usage logging enabled — every API call logged with cost estimate

### 5. Content Safety

- [ ] Output filtering for prohibited content categories
- [ ] Agent refuses requests outside its defined scope

### 6. Monitoring

- [ ] All tool calls logged with inputs, outputs, and latency
- [ ] Unusual pattern alerts configured (e.g., spike in tool calls per user)
- [ ] Usage/cost tracking per user and per conversation

---

## Agent Threat Model

| Threat             | Impact                                 | Mitigation                                   |
| ------------------ | -------------------------------------- | -------------------------------------------- |
| Prompt injection   | Agent ignores instructions, leaks data | System prompt protection, input sanitization |
| Data exfiltration  | User data leaked to other users        | Scoped history, output filtering             |
| Cost explosion     | Unexpected API bills                   | Token limits, max tool calls, budget alerts  |
| Tool misuse        | Unauthorized actions taken             | Human-in-the-loop for destructive tools      |
| Hallucinated tools | Agent calls non-existent functions     | Strict tool definitions, tool validation     |
| Context poisoning  | Corrupted conversation state           | History validation, session isolation        |
