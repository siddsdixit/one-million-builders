---
title: Hybrid Product Requirements Document
app: [app-name]
product_type: hybrid
created: [ISO date]
version: 1
status: draft | refined | approved
build_timeline: [X weeks]
---

# [App Name] — Hybrid Product Requirements Document

> **Hybrid Product:** A web application with an embedded AI agent feature.
> The agent is a functional component of the app, not a standalone product.

## Executive Summary

**Product Vision:** [1-2 sentences — what this product will be]
**Core Purpose:** [What problem does this solve?]
**Target Users:** [Who will use this product?]
**MVP Hypothesis:** The core hypothesis can be validated by shipping [FR-X, AG-X]. All other features are staged post-MVP.

**Key Features (Web App):**

- [Feature 1 — with entity type]
- [Feature 2 — with entity type]

**AI Agent Capabilities:**

- [Capability 1]
- [Capability 2]

**MVP Success Metrics:**

- Users can complete core web app workflow end-to-end
- Agent handles top 3 use cases correctly
- Agent tools are called correctly (not hallucinated)
- All entity lifecycles function correctly

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

**Unique Value Proposition:** [One sentence — why this product wins against the competitors above]

**Go-to-Market Channels:**

- [Channel 1]
- [Channel 2]

**Evidence of User Pain:** [Concrete evidence — forum posts, survey data, personal experience, etc.]

## 2. USERS & PERSONAS

**Primary Persona:**

> Example: "Lena manages customer support for a 50-person SaaS company. She spends 2 hours every day manually reading and tagging 150+ support tickets by category, priority, and product area before her team can even start working them. Last month she mis-routed 12 tickets to the wrong team, adding 2 days of resolution time each. Her goal is to have tickets auto-triaged so her team starts on the right work immediately. Help Lena auto-classify and route support tickets so her team can resolve issues faster without manual triage."

[Replace this block with a narrative paragraph following the example above. Include: name and role, specific situational context, a concrete daily frustration with real numbers, their primary goal, and a JTBD sentence.]

**Human-in-the-loop Requirements:**

- [Which agent actions require human approval]
- [When the agent should escalate to a human]

## 3. FUNCTIONAL REQUIREMENTS

### 3.1 Web App Features (All Priority 0)

**FR-001: [Core Web Feature Name]**

- **Description:** [What it does functionally, including full lifecycle]
- **Entity Type:** [User-Generated Content / Financial / Communication / Configuration / System]
- **User Benefit:** [Why user wants this]
- **Primary User:** [Which persona]
- **Lifecycle Operations:**
    - **Create:** [How users create]
    - **View:** [How users view/access]
    - **Edit:** [How users modify] OR [Not allowed — reason]
    - **Delete:** [How users remove] OR [Archive only — reason]
    - **List/Search:** [How users find and browse]
- **Acceptance Criteria:**
    - [ ] Given [context], when user creates [entity], then [expected result]
    - [ ] Given [entity exists], when user views it, then [what they see]
    - [ ] Given [entity exists], when user edits it, then [what happens]
    - [ ] Given [entity exists], when user deletes it, then [what happens]

### 3.2 Agent Behavior Specification

**AG-001: Core Agent Capabilities (what the agent CAN do)**

- [Capability 1: description]
- [Capability 2: description]

**AG-002: Agent Boundaries (what the agent MUST NOT do)**

- [Boundary 1]
- [Boundary 2]

**AG-003: Personality & Tone**

- **Tone:** [Professional / Friendly / Casual / Formal]
- **Communication style:** [Concise / Detailed / Adaptive]
- **Fallback behavior:** [What agent does when uncertain]

**AG-004: Decision-Making Rules**

- When to act immediately vs. ask for clarification
- When to escalate to a human

**AG-005: Conversation Simulations**

_Simulation 1: Happy Path_

- **User:** "[Common request]"
- **Agent:** "[Expected response]"

_Simulation 2: Ambiguity Handling_

- **User:** "[Ambiguous request]"
- **Agent:** "[Clarification response with options]"

_Simulation 3: Boundary / Refusal_

- **User:** "[Request outside agent's scope]"
- **Agent:** "[Polite refusal with explanation]"

### 3.3 Web App vs. Agent Responsibility Boundary

| Responsibility                      | Handled By | Rationale                           |
| ----------------------------------- | ---------- | ----------------------------------- |
| [e.g., CRUD operations on entities] | Web App    | [Direct user action, no AI needed]  |
| [e.g., Natural language search]     | Agent      | [Requires NLP interpretation]       |
| [e.g., Data validation]             | Web App    | [Deterministic rules, no AI needed] |
| [e.g., Content generation]          | Agent      | [Requires generative capability]    |

**Handoff rules:**

- Agent results that modify app state must go through the same validation as direct user actions
- Agent cannot bypass authorization rules — it acts with the permissions of the invoking user

### 3.4 Essential Market Features

> Include User Authentication below if the product requires user accounts. Omit this section entirely if the product is public-facing with no per-user data.

**FR-XXX: User Authentication**

- **Description:** Secure user login and session management
- **Acceptance Criteria:**
    - [ ] Given valid credentials, when user logs in, then access is granted
    - [ ] Given invalid credentials, access is denied with clear error
    - [ ] Users can reset forgotten passwords
    - [ ] Users can delete their account (with confirmation)

## 4. AGENT TOOL DEFINITIONS

**Tool 1: [Tool Name]**

- **Purpose:** [What it does]
- **Inputs:** [Parameters with types]
- **Outputs:** [Return format]
- **Error handling:** [What happens when it fails]

## 5. API CONTRACT (Agent Endpoint)

- **Endpoint:** [server-side AI route or action, e.g., `POST /api/ai/chat`]
- **Auth:** Inherits the current Supabase-authenticated user session from the web app
- **Rate limits:** [Requests per minute per user]

## 6. MEMORY & CONTEXT

- **Session memory:** [What the agent remembers within a conversation]
- **Persistent memory:** [What it remembers across conversations]

## 7. GUARDRAILS & SAFETY

- **Content the agent must never generate:** [List]
- **Actions requiring human approval:** [List]
- **Cost controls:** [Max API calls per conversation, token limits, daily budget]
- **Prompt injection defense:** [How system prompt is protected]

## 8. USER WORKFLOWS

### 8.1 Primary Web App Workflow

- **Trigger:** [What starts this workflow]
- **Outcome:** [What user achieves]

### 8.2 Agent Interaction Workflow

- **Entry point:** [How user invokes the agent]
- **Happy path:** [Step-by-step expected interaction]
- **Handoff:** [How agent result feeds back into the web app]

## 9. BUSINESS RULES

**Entity Lifecycle Rules:** [For each entity type]
**Agent data access:** [What the agent can read/write in the app's data]

## 10. DATA REQUIREMENTS

**Core Entities:** [User, Entity 2, etc.]
**Agent Data:** [Conversation logs, agent state]

## 11. FUNCTIONAL VIEWS/AREAS

- **[Agent Interface]:** [Where users interact with the AI agent]

## 12. MVP SCOPE & DEFERRED FEATURES

### 12.1 In Scope for MVP

- [FR-001, AG-001, etc.]

### 12.2 Deferred Features (Post-MVP)

**DF-001: [Deferred Feature Name]**

## 13. EVALUATION CRITERIA (Agent)

- Input: "[Example input]" → Expected: "[Expected behavior + output]"
- Input: "[Adversarial input]" → Expected: "[Expected refusal]"

## 14. ASSUMPTIONS & DECISIONS

- **LLM Provider:** [Choose best available model for the task]
- **Deployment Target:** [Embedded in web app]

---

Hybrid PRD Complete — Ready for Spec
