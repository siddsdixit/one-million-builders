---
title: Agent Requirements Document
app: [agent-name]
product_type: agent
agent_type: [chatbot / task_automation / multi_agent / mcp_server / scheduled_autonomous]
created: [ISO date]
version: 1
status: draft | refined | approved
---

# [Agent Name] — Agent Requirements Document

## Executive Summary

**Agent Vision:** [1-2 sentences — what this agent does and why it matters]
**Core Purpose:** [What task does it automate or assist with?]
**Target Users:** [Who interacts with or benefits from this agent?]
**Agent Type:** [Chatbot / Task automation / Multi-agent / MCP server / Scheduled autonomous]
**MVP Hypothesis:** The core hypothesis can be validated by shipping [capabilities]. All other capabilities are staged post-MVP.
**Core Capabilities:**

- [Capability 1]
- [Capability 2]
- [Capability 3]

**MVP Success Metrics:**

- Agent handles top 3 use cases correctly
- Tools are called correctly (not hallucinated)
- Agent refuses out-of-scope requests
- Token usage is within acceptable bounds

## 1. MARKET RESEARCH

**Competitors:**

| Competitor | Strengths | Gaps |
| --- | --- | --- |
| [Competitor 1] | [What they do well] | [Where they fall short] |
| [Competitor 2] | [What they do well] | [Where they fall short] |
| [Competitor 3] | [What they do well] | [Where they fall short] |

**Market Sizing:**

- **TAM:** [Total addressable market — with stated assumptions]
- **SAM:** [Serviceable addressable market]
- **SOM:** [Serviceable obtainable market — realistic 1-year target]

**Unique Value Proposition:** [One sentence — why this agent wins against the competitors above]

**Go-to-Market Channels:**

- [Channel 1]
- [Channel 2]

**Evidence of User Pain:** [Concrete evidence — forum posts, survey data, personal experience, etc.]

## 2. USERS & INTERACTION MODEL

**Primary User:**

> Example: "Jake is a DevOps engineer on a 4-person platform team. Every morning he spends 45 minutes checking 12 different monitoring dashboards, Slack channels, and email threads to piece together what happened overnight. He's missed two P1 incidents because the alert was buried in a noisy channel. His goal is to start every day with a single, prioritized summary of what needs his attention. Help Jake get a prioritized overnight ops summary in 30 seconds so he can respond to critical issues before standup."

[Replace this block with a narrative paragraph following the example above. Include: name and role, specific context about when/why they use the agent, a concrete frustration with real numbers, their primary goal, and a JTBD sentence.]

**Human-in-the-loop Requirements:**

- [Which actions require human approval]
- [When the agent should escalate to a human]
- [How the human provides feedback]

## 3. AGENT BEHAVIOR SPECIFICATION

### 3.1 Core Capabilities (what the agent CAN do)

- [Capability 1: description]
- [Capability 2: description]
- [Capability 3: description]

### 3.2 Boundaries (what the agent MUST NOT do)

- [Boundary 1]
- [Boundary 2]
- [Boundary 3]

### 3.3 Personality & Tone (if conversational)

- **Tone:** [Professional / Friendly / Casual / Formal]
- **Communication style:** [Concise / Detailed / Adaptive]
- **How it introduces itself:** [Opening message]
- **How it handles unknown questions:** [Fallback response]

### 3.4 Decision-Making Rules

- When to act immediately vs. ask for clarification
- When to use which tool
- When to escalate to a human

### 3.5 Conversation Simulations

**Simulation 1: Happy Path**

- **Context:** [Setup]
- **User:** "[Common request]"
- **Agent:** "[Expected response]"
- [Continue 4-6 exchanges]

**Simulation 2: Ambiguity Handling**

- **Context:** [Unclear input]
- **User:** "[Ambiguous request]"
- **Agent:** "[Clarification response with options]"

**Simulation 3: Boundary / Refusal**

- **Context:** [Out-of-scope request]
- **User:** "[Request outside agent's scope]"
- **Agent:** "[Polite refusal with explanation]"

## 4. TOOL DEFINITIONS

**Tool 1: [Tool Name]**

- **Purpose:** [What it does]
- **Inputs:** [Parameters with types]
- **Outputs:** [Return format]
- **Error handling:** [What happens when it fails]

**Tool 2: [Tool Name]**

- [Same structure]

**MCP Server Connections:** [If applicable]
**External API Integrations:** [If applicable]

## 5. API CONTRACT

- **Endpoint:** [e.g., `POST /api/ai/chat` or the FastAPI endpoint selected by architecture]
- **Request format:**
    ```json
    {
    	"message": "string",
    	"conversation_id": "string (optional)",
    	"stream": "boolean (optional, default false)"
    }
    ```
- **Response format (non-streaming):**
    ```json
    {
    	"response": "string",
    	"conversation_id": "string",
    	"tool_calls": ["list of tools invoked"],
    	"token_usage": { "input": 0, "output": 0 }
    }
    ```
- **Response format (streaming):** SSE with `data: {chunk}` per token, `data: [DONE]` on completion
- **Auth:** [Supabase user session / API key header / internal only, depending on architecture]
- **Rate limits:** [Requests per minute per user]

## 6. MEMORY & CONTEXT

- **Session memory:** [What the agent remembers within a conversation]
- **Persistent memory:** [What it remembers across conversations]
- **Context requirements:** [What context it needs per interaction]
- **Context window management:** [How to handle long conversations]

## 7. GUARDRAILS & SAFETY

- **Content the agent must never generate:** [List]
- **Actions requiring human approval:** [List]
- **Cost controls:** [Max API calls per conversation, token limits, daily budget]
- **Data privacy rules:** [What data the agent can/cannot access or store]
- **Fallback behavior:** [What the agent does when uncertain or when tools fail]
- **Prompt injection defense:** [How system prompt is protected]

## 8. DATA REQUIREMENTS

- **Conversation logs:** [Storage, retention, privacy]
- **Agent state:** [What persistent state the agent maintains]
- **Tool results:** [How tool outputs are stored/cached]
- **User preferences:** [Per-user settings the agent respects]

## 9. MVP SCOPE & DEFERRED CAPABILITIES

### 9.1 In Scope for MVP

- [Capability 1, Capability 2, etc.]

### 9.2 Deferred Capabilities

**DC-001: [Deferred Capability]**

- **Description:** [What it is]
- **Reason for Deferral:** [Why]

## 10. EVALUATION CRITERIA

**Test Cases:**

- Input: "[Example input]" → Expected: "[Expected behavior + output]"
- Input: "[Edge case]" → Expected: "[Expected handling]"
- Input: "[Adversarial input]" → Expected: "[Expected refusal]"

**Success Definition:**

- [How we know the agent is working correctly]
- [Acceptable response quality threshold]
- [Acceptable latency]

## 11. ASSUMPTIONS & DECISIONS

- **LLM Provider:** [Choose best available model for the task]
- **Deployment Target:** [API endpoint / MCP server / Embedded in web app]
- **Key Assumptions:** [Assumption 1 + reasoning]

---

Agent PRD Complete — Ready for Spec
