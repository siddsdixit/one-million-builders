# Day 12 — First AI Build

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** debug

Day 12 is the first real AI implementation. Day 11 decided what AI should do. Today you make the app call the selected model from server-side code, show the output in the product, and verify the API key is safe.

The goal is not to build a perfect AI system. The goal is to prove one useful AI path works locally and live.

## Learning Frame

- **Mental model:** the browser asks your app for AI help; your server-side code reads the secret key, calls the model provider, and returns safe output to the UI.
- **Input:** refined PRD with AI feature section, architecture, completed app workflow, provider/API-key plan, and live Vercel project.
- **Output:** server-side AI route or server action, UI trigger, AI output in the app, safe env vars, local test, live test, and no key leak.
- **What can go wrong:** API key is exposed to client code, key is missing in Vercel, prompt sends too much private data, the UI accepts bad output as truth, or the build jumps into tool calling/frameworks before the first call works.
- **What to ignore today:** skip AI frameworks, advanced agents, RAG, tool calling, streaming, and complex evals unless Day 11 explicitly justified them. Build the first useful AI call.

## What You Learn

- how an app calls an LLM from server-side code
- how to create or get the selected provider API key
- how to store API keys in `.env.local`
- how to store API keys in Vercel environment variables
- how to update `.env.example` without real values
- how to build a Next.js route handler or server action for the AI call
- how to pass product data into the prompt safely
- how to show AI output in the UI
- how to test locally and live
- how to check for key leaks
- how to handle common AI errors: missing key, invalid key, rate limit, timeout, and bad response

## Core Concepts

### Server-Side Only

AI provider keys must stay server-side. The browser should never receive `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, or any other model-provider secret.

The safe path is:

```text
Browser UI -> Next.js route/server action -> AI provider -> server returns safe result -> UI displays output
```

The unsafe path is:

```text
Browser UI -> AI provider directly with secret key
```

Never do the unsafe path.

### Provider Key Setup

Use the provider selected on Day 11.

Course default:

- Anthropic Console: https://console.anthropic.com/
- Anthropic API overview: https://docs.anthropic.com/en/api/overview
- Env var: `ANTHROPIC_API_KEY`

Other provider options:

- OpenAI API keys: https://platform.openai.com/api-keys
- OpenAI quickstart: https://platform.openai.com/docs/quickstart
- Env var: `OPENAI_API_KEY`
- Google AI Studio API keys: https://aistudio.google.com/app/apikey
- Google Gemini API key docs: https://ai.google.dev/gemini-api/docs/api-key
- Env var: `GEMINI_API_KEY`

### Environment Variables

Local:

- put the real key in `.env.local`
- confirm `.env.local` is ignored by git
- add only placeholder names to `.env.example`

Production:

- add the same env var name in Vercel Project -> Settings -> Environment Variables
- redeploy after adding the env var

Leak check:

```bash
rg "NEXT_PUBLIC_ANTHROPIC|NEXT_PUBLIC_OPENAI|NEXT_PUBLIC_GEMINI|sk-ant|sk-proj|AIza" .
```

This should not find real keys in committed/client code.

### Prompt Inputs

The prompt should use only the data needed for the AI job.

Do:

- include relevant user/product data
- include the desired output shape
- include constraints from Day 11
- include what the AI should avoid

Do not:

- send entire database rows without reason
- send another user's data
- send service-role secrets
- let the AI act outside the current user's permissions

### First AI UI

The first UI can be simple:

- button or form action
- loading state
- success state with output
- error message when the call fails

Day 13 will improve AI UX and safety. Day 12 only needs one useful path working.

### Common Errors

| Error | Likely cause | Fix |
|---|---|---|
| Missing key | Env var not set locally or in Vercel | Add env var and restart/redeploy |
| Invalid key | Copied wrong key or provider mismatch | Recreate/copy key |
| Rate limit | Too many requests or low tier | Wait, retry, or add billing |
| Timeout | Model call too slow | Add timeout/error handling |
| Bad response | Prompt/output shape unclear | Tighten prompt and validation |

## What You Produce

- selected provider key stored safely
- `.env.example` updated with placeholder only
- server-side AI route or server action
- UI trigger for the AI feature
- AI output displayed in the app
- local AI test
- live AI test after Vercel env var is set
- leak check showing no client-side key exposure

## Human Decisions

- prompt behavior
- sample inputs
- first output quality
- selected provider and env var name
- what product data is safe to send
- whether output is displayed only, saved, reviewed, edited, or acted on
- what error message users should see on failure

## Done Checklist

- [ ] AI route or server action exists
- [ ] AI output appears in app
- [ ] selected provider key is stored in `.env.local`
- [ ] selected provider key is stored in Vercel env vars
- [ ] `.env.example` has placeholders only
- [ ] API key is not exposed to client code
- [ ] local app AI path works
- [ ] live app AI path works
- [ ] common error states are handled

## Verify Your Day 12

When the checklist is true, ask your harness to run the OneMillion verifier for Day 12. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 13 — Product Polish + UX Finish](../day-13-product-polish/learn.md)
