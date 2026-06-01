# Day 11 — AI Feature Spec

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `spec`
**Supporting agents:** validate-spec

Day 11 is where the product becomes AI-native on purpose. You do **not** build the AI feature yet. Today you decide what AI should do, why it matters, what data it can see, what output it should produce, and how you will know whether it worked.

Adding AI means calling a large language model inside your application to do a specific job. The AI is not magic dust. It is a server-side capability your product uses for a defined user outcome.

## Learning Frame

- **Mental model:** AI is a worker inside the product. It receives inputs, follows instructions, may use tools, produces output, and must stay inside privacy, cost, and safety boundaries.
- **Input:** PRD, refined PRD, architecture, Day 8 workflow, Day 9 review, Day 10 QA results, and current app behavior.
- **Output:** updated pipeline artifacts, primarily `.onemillion/refined-prd.md`, with one useful AI job, input/output contract, model/provider decision, prompt plan, tool boundary, eval criteria, failure modes, cost limits, and privacy rules.
- **What can go wrong:** the learner says "add AI" without naming a job, sends private data unnecessarily, exposes API keys in client code, saves low-quality AI output without review, or adds an agent that can act outside user permissions.
- **What to ignore today:** do not create API keys or write AI code unless the course explicitly moves to Day 12. Today is the spec.

## What You Learn

- what adding AI means in an application
- define useful AI behavior
- avoid AI decoration
- choose model/provider: Claude, OpenAI, or Google Gemini
- understand where API keys come from
- understand API key and secret-storage best practices
- choose inputs and outputs
- decide whether the AI is a simple feature or an agent that makes decisions
- understand tool calling at a high level
- understand AI frameworks at a high level and why to skip them for now
- write measurable AI acceptance criteria
- define failure modes, privacy boundaries, latency, and cost budget

## Core Concepts

### What Adding AI Means

Adding AI means your application calls a large language model, usually from server-side code, to do a specific job for the user.

Examples:

- a college counseling app reviews a student's profile and suggests colleges, essay themes, and next steps
- a teacher workflow app drafts parent update messages from classroom notes
- a sales app summarizes customer calls and recommends follow-up actions
- a legal intake app extracts key facts from a client narrative

The AI feature should improve the core workflow from Day 8. It should not be decoration.

### Feature, Agent, Or Tool User

An AI feature may be simple: user clicks a button, the model returns a recommendation.

An AI feature may also behave like an agent: it reads context, decides the next step, calls tools, and produces a result. Agents are more powerful, but they need stronger boundaries:

- what tools can it call?
- what data can it read?
- can it write to the database?
- does a human need to approve actions?
- what is the maximum number of steps?

For this course, start with one useful AI job. Add agentic behavior only if the product truly needs it.

### API Keys And Providers

To call an AI model, your app needs an API key from a model provider.

Common provider links:

- Anthropic Console: https://console.anthropic.com/
- Anthropic API overview: https://docs.anthropic.com/en/api/overview
- OpenAI API keys: https://platform.openai.com/api-keys
- OpenAI quickstart: https://platform.openai.com/docs/quickstart
- Google AI Studio API keys: https://aistudio.google.com/app/apikey
- Google Gemini API key docs: https://ai.google.dev/gemini-api/docs/api-key

The course default is Claude through Anthropic, but the learner should understand the pattern is the same: get a provider key, store it safely, call the model from server-side code, and never expose the key to the browser.

### Secret Storage

API keys are secrets. Treat them like passwords.

Good practices:

- store local keys in `.env.local`
- add `.env.local` to `.gitignore`
- store production keys in Vercel environment variables
- never use `NEXT_PUBLIC_` for AI provider keys
- never paste keys into chat, screenshots, GitHub, or logs
- rotate the key immediately if it leaks
- keep separate dev/test/prod keys when the product gets serious

### Inputs And Outputs

Every AI spec needs an input/output contract.

Inputs answer: what information does the model receive?

Outputs answer: what should come back?

For example:

```text
Input: student GPA, interests, constraints, preferred location, budget, activities
Output: 5 college recommendations with rationale, risk level, next action, and missing information
```

Structured outputs are often better than free text when the app needs to display, save, sort, or validate the result.

### Tool Calling

Tool calling means the model can ask your application to run a function, such as:

- search a database
- fetch a user profile
- create a draft task
- calculate a score
- call an external API

Tool calling is useful when the model needs fresh data or needs to take a bounded action. It is risky when tools can write data, send messages, spend money, or expose private records. Tool actions should respect the current user's permissions.

### AI Frameworks

There are many AI frameworks and platforms: Google ADK, LangChain, LangGraph, Langflow, Langfuse, CrewAI, and others.

They can help with advanced agent workflows, tracing, evaluation, orchestration, and multi-agent systems. For now, skip them unless the architecture truly needs them. A beginner-friendly MVP can usually call the provider SDK or API directly from a Next.js route/server action.

### AI Quality

AI quality needs examples, failure modes, and measurable acceptance criteria.

Ask:

- What should a good answer include?
- What should it refuse or avoid?
- What data must never be used?
- Should the user review/edit the output before saving or sending?
- How much latency is acceptable?
- How much can each run cost?

## What You Produce

- updated `.onemillion/refined-prd.md` with an AI feature section
- updated `.onemillion/architecture.md` or sprint brief notes only if the AI decision changes architecture or build scope
- one selected AI job
- provider/model recommendation
- input/output contract
- prompt plan
- structured output shape when useful
- tool-calling boundary if tools are needed
- privacy and permission boundary
- failure modes and fallback behavior
- measurable acceptance/eval criteria
- cost and latency budget

## Human Decisions

- AI job-to-be-done
- provider/model preference: Anthropic Claude by default, or OpenAI/Google if there is a reason
- whether this is a simple AI feature or an agentic workflow
- what user/product data the AI can see
- whether AI output is saved, reviewed, edited, or acted on
- whether tool calling is needed
- quality bar
- failure modes
- privacy boundary
- cost ceiling

## Done Checklist

- [ ] `.onemillion/refined-prd.md` includes the selected AI feature
- [ ] adding AI is described as one specific model-backed job
- [ ] provider/model choice is recorded
- [ ] API key handling and secret-storage rules are recorded
- [ ] input/output contract is recorded
- [ ] tool-calling boundary is recorded, even if the answer is "no tools yet"
- [ ] AI behavior is measurable
- [ ] failure modes, privacy boundary, latency, and cost budget are recorded

## Verify Your Day 11

When the checklist is true, ask your harness to run the OneMillion verifier for Day 11. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 12 — First AI Build](../day-12-first-ai-build/learn.md)
