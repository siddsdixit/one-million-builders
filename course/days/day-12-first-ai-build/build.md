# Day 12 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

## Before You Start

- [ ] Previous day is verified in `.onemillion/state.json`.
- [ ] You are in the correct product/course workspace.
- [ ] You have read [learn.md](./learn.md).

## Step 1: Ask The Harness To Teach The Day

Paste this:

```text
I am on OneMillion Day 12: First AI Build.

Act as the `build` agent for this day.
First teach me the concept in plain language:
- how the app calls an LLM from server-side code
- why AI API keys must stay server-side
- how to create/get the selected provider key
- how to store it in .env.local
- how to store it in Vercel env vars
- how to update .env.example with placeholders only
- how to build a Next.js route handler or server action for the AI call
- how to pass product data into the prompt safely
- how to show AI output in the UI
- how to test locally and live
- how to detect key leaks
- how to handle missing key, invalid key, rate limit, timeout, and bad response errors

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Read the AI feature section in .onemillion/refined-prd.md before changing code.
Use Anthropic/Claude by default unless Day 11 selected OpenAI or Google Gemini.
Do not use an AI framework unless Day 11 explicitly justified it.
Do not add tool calling unless Day 11 explicitly said this MVP needs tools.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Copy-Paste AI Build Prompts

### Prompt 1: Provider Key Setup

```text
Help me set up the selected AI provider key for Day 12.

Read the AI feature section in .onemillion/refined-prd.md.
Use Anthropic/Claude by default unless the spec selected another provider.

Give me exact steps and links:
- Anthropic Console: https://console.anthropic.com/
- Anthropic API overview: https://docs.anthropic.com/en/api/overview
- OpenAI API keys: https://platform.openai.com/api-keys
- OpenAI quickstart: https://platform.openai.com/docs/quickstart
- Google AI Studio API keys: https://aistudio.google.com/app/apikey
- Google Gemini API key docs: https://ai.google.dev/gemini-api/docs/api-key
- Vercel env vars: https://vercel.com/docs/projects/environment-variables

Tell me the exact env var name to use.
Tell me how to put it in .env.local.
Tell me how to put it in Vercel.
Tell me how to confirm .env.local is gitignored.
Do not ask me to paste the secret value into chat.
```

### Prompt 2: Build Server-Side AI Call

```text
Build the first server-side AI call for the selected Day 11 AI feature.

Use the existing app architecture.
Prefer a Next.js route handler or server action.
Use the selected provider key from server-side env vars only.
Do not expose the AI key to client code.
Do not add an AI framework unless Day 11 explicitly required it.
Do not add tool calling unless Day 11 explicitly required it.

Implement:
- request validation
- prompt construction from safe product data
- model/provider call
- user-safe response shape
- missing key error
- provider error handling
- timeout/rate-limit friendly error
- no secret leakage in responses/logs
```

### Prompt 3: Add UI Trigger

```text
Add the UI trigger for the Day 12 AI feature.

Use the existing MUI design system.
The UI should include:
- button or form action
- loading state
- success state showing AI output
- error state with user-friendly copy
- clear indication that AI output should be reviewed before trust/action if needed

Keep it simple. Day 13 will improve AI UX and safety.
```

### Prompt 4: Local Verification

```text
Verify the AI feature locally.

Check:
- app builds
- local env var exists but is not committed
- AI route/server action works locally
- UI trigger shows AI output
- missing key error is handled
- invalid input is handled
- no API key appears in browser code or response

Record exact commands and results.
```

### Prompt 5: Live Verification

```text
Verify the AI feature on the live Vercel deployment.

Check:
- selected AI env var is set in Vercel
- app redeployed after env var was added
- live AI path works
- live UI shows AI output
- live error state is acceptable
- source/build markers or visible feature text match current code

Record live URL, test time, result, and failures.
```

### Prompt 6: Secret Leak Scan

```text
Run a secret leak scan for AI keys.

Check for:
- NEXT_PUBLIC_ANTHROPIC
- NEXT_PUBLIC_OPENAI
- NEXT_PUBLIC_GEMINI
- sk-ant
- sk-proj
- AIza
- real provider keys in committed files

Confirm .env.local is ignored by git.
Confirm .env.example contains placeholders only.
Fix any leak before Day 12 is marked done.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- prompt behavior
- sample inputs
- first output quality
- selected provider and env var name
- what product data is safe to send
- whether output is displayed only, saved, reviewed, edited, or acted on
- user-facing error copy

## Step 3: Produce The Day Output

Expected output today:

- selected provider key stored safely
- `.env.example` updated with placeholder only
- server-side AI route or server action
- UI trigger for the AI feature
- AI output displayed in the app
- local AI verification
- live AI verification after Vercel env var is set
- secret leak scan result

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: External Tools

- Anthropic Console: https://console.anthropic.com/
- Anthropic API docs: https://docs.anthropic.com/en/api/overview
- OpenAI API keys: https://platform.openai.com/api-keys
- OpenAI quickstart: https://platform.openai.com/docs/quickstart
- Google AI Studio API keys: https://aistudio.google.com/app/apikey
- Google Gemini API key docs: https://ai.google.dev/gemini-api/docs/api-key
- Vercel env vars: https://vercel.com/docs/projects/environment-variables
- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git docs: https://vercel.com/docs/deployments/git
- Vercel domains docs: https://vercel.com/docs/domains
- Vercel Analytics: https://vercel.com/docs/analytics

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 5: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 12.
Inspect the AI feature section in refined PRD, app code, env var placeholders, deployment links, local/live AI verification, secret leak scan, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 12 complete
- **Last verified day:** Day 12
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 13.

## What Should Be True After Day 12

- [ ] AI route or server action exists
- [ ] AI output appears in app
- [ ] selected provider key is stored in `.env.local`
- [ ] selected provider key is stored in Vercel env vars
- [ ] `.env.example` has placeholders only
- [ ] API key is not exposed to client code
- [ ] local app AI path works
- [ ] live app AI path works
- [ ] common error states are handled

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 12: First AI Build.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 13 — Product Polish + UX Finish](../day-13-product-polish/learn.md)
