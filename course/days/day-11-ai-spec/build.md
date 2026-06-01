# Day 11 — Build Guide

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
I am on OneMillion Day 11: AI Feature Spec.

Act as the `spec` agent for this day.
First teach me the concept in plain language:
- what adding AI means: calling a large language model inside my app to do a specific job
- useful AI feature versus AI decoration
- simple AI feature versus agentic behavior
- examples like a college counselor advising a student from profile data
- provider/API key basics for Anthropic, OpenAI, and Google Gemini
- how to store API keys safely in .env.local and deployment env vars
- why AI keys must never be exposed as NEXT_PUBLIC_* or client-side code
- inputs, outputs, structured output, and prompt plan
- tool calling: what it means, when it helps, and what boundaries it needs
- AI frameworks such as Google ADK, LangChain, LangGraph, Langflow, Langfuse, and CrewAI, and why we skip them for now unless the product truly needs them
- measurable AI quality, failure modes, privacy, latency, and cost

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Read .onemillion/refined-prd.md, .onemillion/architecture.md, .onemillion/review-findings.md, .onemillion/test-results.md, and the completed Day 8 sprint brief.
Update the existing pipeline artifacts. Do not create a new core spec document.
Primary output: update .onemillion/refined-prd.md with an AI feature section.
Only update .onemillion/architecture.md or existing sprint briefs if the AI decision changes architecture, security boundaries, or build scope.
Do not create API keys today unless I explicitly ask. Day 12 is the build/API-key day.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Copy-Paste AI Spec Prompts

### Prompt 1: Choose The AI Job

```text
Help me choose one useful AI job for my product.

Read the PRD, refined PRD, Day 8 workflow, Day 9 review, and Day 10 QA results.
Suggest 3 possible AI jobs that improve the core workflow.
For each option, explain:
- target user benefit
- input data needed
- output produced
- risk/privacy concern
- why it is or is not worth building now

Then recommend one AI job for Day 11.
```

### Prompt 2: Update The Existing Spec

```text
Update the existing pipeline artifacts for the selected AI job.

Do not create a new core spec document.
Primary output: update .onemillion/refined-prd.md with an AI feature section.
Only update architecture or existing sprint briefs if needed.

Include:
- AI job-to-be-done
- user story
- provider/model recommendation
- input contract
- output contract
- structured output schema if useful
- prompt plan
- examples of good output and bad output
- privacy/permission boundary
- whether output is saved, edited, reviewed, or acted on
- tool-calling boundary, even if no tools are used yet
- measurable acceptance criteria
- eval criteria
- failure modes and fallback behavior
- latency and cost budget
```

### Prompt 3: API Key And Secret Plan

```text
Create the API key and secret-storage plan for the AI feature.

Teach me where API keys come from:
- Anthropic Console: https://console.anthropic.com/
- Anthropic API overview: https://docs.anthropic.com/en/api/overview
- OpenAI API keys: https://platform.openai.com/api-keys
- OpenAI quickstart: https://platform.openai.com/docs/quickstart
- Google AI Studio API keys: https://aistudio.google.com/app/apikey
- Google Gemini API key docs: https://ai.google.dev/gemini-api/docs/api-key

For the course default, use Anthropic/Claude unless there is a product reason to use another provider.
Record how the key will be stored locally and in Vercel.
Record what must never happen: no NEXT_PUBLIC AI key, no key in client code, no key in GitHub, no key in screenshots/logs.
Do not ask me to create the key yet unless we are starting Day 12.
```

### Prompt 4: Tool Calling Decision

```text
Decide whether this AI feature needs tool calling.

Explain tool calling in simple language.
List possible tools the AI might need.
For each tool, decide:
- read-only or write-capable
- what user data it can access
- what permission check is required
- whether human approval is needed
- what could go wrong

If tools are not needed for MVP, record "no tool calling for Day 12" and explain why.
```

### Prompt 5: Framework Decision

```text
Decide whether this AI feature needs an AI framework.

Briefly explain Google ADK, LangChain, LangGraph, Langflow, Langfuse, and CrewAI at a high level.
Then decide whether we should skip them for now.
Default to direct provider API/SDK from server-side Next.js unless there is a strong reason.
Record the decision in the AI feature section of .onemillion/refined-prd.md.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- AI job-to-be-done
- provider/model preference
- simple AI feature versus agentic workflow
- what data the AI can see
- whether tool calling is needed
- whether output is saved, edited, reviewed, or acted on
- quality bar
- failure modes
- privacy boundary
- cost ceiling

## Step 3: Produce The Day Output

Expected output today:

- updated `.onemillion/refined-prd.md` with an AI feature section
- updated architecture or existing sprint notes only if needed

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: External Tools

- No new external account is required today unless you intentionally prepare for Day 12.
- Anthropic Console: https://console.anthropic.com/
- Anthropic API overview: https://docs.anthropic.com/en/api/overview
- OpenAI API keys: https://platform.openai.com/api-keys
- OpenAI quickstart: https://platform.openai.com/docs/quickstart
- Google AI Studio API keys: https://aistudio.google.com/app/apikey
- Google Gemini API key docs: https://ai.google.dev/gemini-api/docs/api-key

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 5: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 11.
Inspect .onemillion/refined-prd.md, relevant pipeline artifacts, provider/API-key plan, privacy boundary, tool-calling decision, cost/latency limits, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 11 complete
- **Last verified day:** Day 11
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 12.

## What Should Be True After Day 11

- [ ] `.onemillion/refined-prd.md` includes the selected AI feature section
- [ ] adding AI is described as one specific model-backed job
- [ ] provider/model choice is recorded
- [ ] API key and secret-storage plan is recorded
- [ ] input/output contract is recorded
- [ ] tool-calling decision is recorded
- [ ] AI behavior is measurable
- [ ] failure modes, privacy boundary, latency, and cost budget are recorded

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 11: AI Feature Spec.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 12 — First AI Build](../day-12-first-ai-build/learn.md)
