# OneMillion Deployment Guide & Checklists

> Reference for the Ship agent. Read the relevant deployment target section, then execute the 9-phase deployment process.

---

## Deployment Targets by Product Type

### Web App

- **Frontend:** Vercel — connect GitHub repo, set env vars, auto-deploy on push to `main`
- **Backend:** Railway or Fly.io — connect GitHub repo, set env vars, configure start command
- **Database:** MongoDB Atlas — confirm cluster, indexes, and connection string

### Agent (API Endpoint)

- **Deploy:** FastAPI backend to Railway or Fly.io
- **Endpoint:** `POST /api/v1/chat` (supports request/response and streaming)
- **Auth:** API key header (`X-API-Key`) — generate and store in env vars
- **Docs:** Auto-generated at `/docs` (FastAPI Swagger) — disable in production or add auth

### Agent (MCP Server)

- **Deploy:** MCP-compatible server to Railway or Fly.io
- **Register:** Add server URL to MCP client configuration
- **Document:** List all available tools and their schemas in README
- **Verify:** Test each tool individually before announcing live

### Hybrid (Web App + Embedded Agent)

- **Agent:** Runs as a FastAPI route within the backend (`/api/v1/chat`)
- **Frontend:** Calls agent endpoint from Next.js
- **Deploy:** Both frontend (Vercel) and backend (Railway) deployed together
- **Env vars:** LLM API key and all secrets in backend env only — never in frontend

### Scheduled/Triggered Agent (Autonomous)

- **Deploy:** Railway cron job or Fly.io scheduled machine
- **Monitoring:** Required — autonomous agents must have alerting configured

---

## Pre-Deployment Checklist

### Code & Tests
- [ ] All backend tests pass: `cd backend && python -m pytest tests/ -x -q`
- [ ] Frontend builds: `cd frontend && npm run build`
- [ ] No open Critical/High security findings in security-audit.md
- [ ] No hardcoded secrets in codebase (grep verified)
- [ ] `.env` is in `.gitignore` and NOT committed (including git history)
- [ ] `.env.example` committed with all required keys and placeholder values
- [ ] CI pipeline (`.github/workflows/test.yml`) runs green

### Environment Variables
- [ ] Every variable in `.env.example` has a corresponding value set in the deployment platform
- [ ] `CORS_ORIGINS` set to production frontend URL only (not `*`)
- [ ] `JWT_SECRET` is minimum 256-bit random value (not a dictionary word)
- [ ] `MONGODB_URL` uses `mongodb+srv://` (TLS by default)
- [ ] No secrets in `NEXT_PUBLIC_` variables (those are client-visible)
- [ ] `SENTRY_DSN` set in both backend and frontend

### Database
- [ ] MongoDB Atlas cluster reachable from deployment platform
- [ ] Network access: IP allowlist configured (or documented risk if using 0.0.0.0/0)
- [ ] Database user has readWrite permissions (not atlas admin)
- [ ] Indexes created for all frequently queried fields
- [ ] Automated backups enabled and verified in Atlas dashboard

**For agents additionally:**
- [ ] LLM API key stored as environment variable (backend only)
- [ ] Token usage monitoring and cost limits configured
- [ ] Rate limiting on agent endpoint
- [ ] Conversation logging enabled
- [ ] `/docs` endpoint disabled or auth-gated in production

---

## Deployment Steps

### 1. Database Preparation

1. Verify MongoDB Atlas cluster is running and reachable
2. Create indexes for frequently queried fields:
   ```
   db.users.create_index("email", unique=True)
   db.recipes.create_index("owner_id")
   db.recipes.create_index("created_at")
   db.recipes.create_index([("title", "text"), ("description", "text")])
   ```
   Adapt index list based on development plan entity schemas.
3. Verify automated daily backups are enabled

### 2. Backend Deploy (Railway / Fly.io)

1. Connect to GitHub repo, select `main` branch
2. Set ALL required environment variables
3. Configure start command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Set health check path: `/api/v1/health`
5. Deploy and monitor build logs
6. Verify:
   ```bash
   curl -s "$BACKEND_URL/api/v1/health"  # → {"status": "ok"}
   curl -sI "$BACKEND_URL/api/v1/health" | grep -iE "(x-content-type|x-frame|referrer)"  # security headers
   curl -sI -H "Origin: $FRONTEND_URL" "$BACKEND_URL/api/v1/health" | grep -i "access-control"  # CORS
   ```

### 3. Frontend Deploy (Vercel)

1. Set `NEXT_PUBLIC_API_URL` to live backend URL
2. Connect to GitHub repo, select `main` branch
3. Deploy and monitor build logs
4. Verify: `curl -s -o /dev/null -w "%{http_code}" "$FRONTEND_URL"` → 200

### 4. Domain & SSL (if custom domain)

1. Add custom domain in Vercel project settings
2. Add DNS records at registrar (CNAME to cname.vercel-dns.com)
3. Wait for DNS propagation: `dig +short your-domain.com`
4. Verify SSL: `curl -sI https://your-domain.com | grep "strict-transport"`
5. Update `CORS_ORIGINS` in backend to include custom domain, redeploy

---

## Post-Deployment Verification

### Automated Smoke Tests

Run the Complete Core Flow against the live URL using curl — not manual browser checks:

1. Register a test user → 201
2. Login → get access token
3. Create a resource with token → 201
4. Read it back → 200, data matches
5. Delete it (cleanup) → 204 or 200
6. Verify auth rejection: request without token → 401

Every step must succeed. Any failure = deployment is NOT verified.

### Monitoring Setup

- [ ] Sentry project receiving events (check dashboard)
- [ ] Uptime monitor configured (UptimeRobot or Betterstack, free tier)
- [ ] Builder has access to Railway/Fly.io logs
- [ ] Request IDs visible in log output

### Performance Baseline

Run response time checks against live URL:

| Endpoint | Target | Method |
|----------|--------|--------|
| GET /health | < 100ms | `curl -o /dev/null -s -w "%{time_total}" $URL/api/v1/health` |
| GET /[list] | < 500ms | Same method |
| POST /[create] | < 300ms | Same method with -X POST -d ... |
| Frontend load | < 3s | `curl -o /dev/null -s -w "%{time_total}" $FRONTEND_URL` |

Document actual numbers for future comparison.

---

## Rollback Procedure

1. **Railway:** Dashboard → Deployments → select previous → Redeploy
2. **Fly.io:** `fly releases` → `fly deploy --image <previous-image>`
3. **Vercel:** Dashboard → Deployments → select last working → Promote to Production
4. **MongoDB Atlas:** Backups → select most recent → Restore to new cluster (for safety)
5. **Verify rollback access:** Builder must confirm they can see previous deployments in each dashboard
6. **Expected rollback time:** < 5 minutes for Railway/Vercel, < 15 minutes for MongoDB restore
7. Investigate failure, fix, and redeploy — do not leave rollback as permanent state
