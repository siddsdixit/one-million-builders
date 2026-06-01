---
title: Product Requirements Document
app: [app-name]
product_type: web_app
created: [ISO date]
version: 1
status: draft | refined | approved
build_timeline: [X weeks]
---

# [App Name] — Product Requirements Document

## Executive Summary

**Product Vision:** [1-2 sentences — what this product will be]
**Core Purpose:** [What problem does this solve?]
**Target Users:** [Who will use this product?]
**MVP Hypothesis:** The core hypothesis can be validated by shipping [FR-X, FR-X]. All other features are staged post-MVP.
**Key Features:**

- [Feature 1 — with entity type]
- [Feature 2 — with entity type]
- [Feature 3 — with entity type]

**MVP Success Metrics:**

- Users can complete core workflow end-to-end
- All entity lifecycles function correctly
- Core features work without errors

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

- [Channel 1 — e.g., Product Hunt launch]
- [Channel 2 — e.g., Reddit communities]
- [Channel 3 — e.g., Direct outreach]

**Evidence of User Pain:** [Concrete evidence — forum posts, survey data, personal experience, etc.]

## 2. USERS & PERSONAS

**Primary Persona:**

> Example: "Priya is a freelance graphic designer who juggles 8-12 client projects at a time. She tracks deadlines in a mix of sticky notes, iCal, and a Google Sheet that's three tabs deep. Every Monday she spends 45 minutes just figuring out what's due this week, and she's missed two client deadlines in the past quarter because a task slipped through the cracks. Her goal is to see everything she owes every client in one glance. Help Priya track all client deliverables in one place so she can hit every deadline without the Monday morning scramble."

[Replace this block with a narrative paragraph following the example above. Include: name and role, specific situational context, a concrete daily frustration with real numbers, their primary goal, and a JTBD sentence.]

**Secondary Personas:** [If applicable, same narrative paragraph format]

## 3. FUNCTIONAL REQUIREMENTS

### 3.1 User-Requested Features (All Priority 0)

**FR-001: [Core Feature Name]**

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
    - **Additional:** [Archive, Share, Export, Bulk ops if applicable]
- **Acceptance Criteria:**
    - [ ] Given [context], when user creates [entity], then [expected result]
    - [ ] Given [entity exists], when user views it, then [what they see]
    - [ ] Given [entity exists], when user edits it, then [what happens]
    - [ ] Given [entity exists], when user deletes it, then [what happens]
    - [ ] Users can search/filter their [entities] by [criteria]

### 3.2 Essential Market Features

> Include User Authentication below if the product requires user accounts. Omit this section entirely if the product is public-facing with no per-user data.

**FR-XXX: User Authentication**

- **Description:** Secure user login and session management
- **Entity Type:** Configuration/System
- **User Benefit:** Protects user data and personalizes experience
- **Primary User:** All personas
- **Lifecycle Operations:**
    - **Create:** Register new account
    - **View:** View profile information
    - **Edit:** Update profile and preferences
    - **Delete:** Account deletion option (with data export)
    - **Additional:** Password reset, session management
- **Acceptance Criteria:**
    - [ ] Given valid credentials, when user logs in, then access is granted
    - [ ] Given invalid credentials, when user attempts login, then access is denied with clear error
    - [ ] Users can reset forgotten passwords
    - [ ] Users can update their profile information
    - [ ] Users can delete their account (with confirmation and data export option)

## 4. USER WORKFLOWS

### 4.1 Primary Workflow: [Main User Journey]

- **Trigger:** [What starts this workflow]
- **Outcome:** [What user achieves]
- **Steps:**
    1. User [does something]
    2. System [responds with]
    3. User sees [result]
    4. [Continue through completion]
- **Alternative Paths:**
    - If [condition], then [alternative flow]

### 4.2 Entity Management Workflows

[For each major entity, include Create, Edit, Delete, Search flows]

## 5. BUSINESS RULES

**Entity Lifecycle Rules:** [For each entity type]

- **Who can create:** [Role/condition]
- **Who can view:** [Owner only / Team / Public]
- **Who can edit:** [Owner / Admin / Specific roles]
- **Who can delete:** [Owner / Admin] or [No one — archive only]
- **What happens on deletion:** [Hard delete / Soft delete / Archive]
- **Related data handling:** [Cascade / Restrict / Archive]

**Access Control:**

- [Who can see what]
- [Who can do what]

**Data Rules:**

- [Validation rules]
- [Required vs optional fields]
- [Constraints and limits]
- [Relationships between entities]

## 6. DATA REQUIREMENTS

**Core Entities:**

**User**

- **Type:** System/Configuration
- **Attributes:** identifier, email, name, created_date, last_modified_date, role
- **Relationships:** [has many X, belongs to Y]
- **Lifecycle:** Full CRUD with account deletion option
- **Retention:** User-initiated deletion with data export

**[Entity 2]**

- **Type:** [User-Generated Content / Financial / Communication / etc.]
- **Attributes:** identifier, name, description, owner, created_date, last_modified_date, status
- **Relationships:** [belongs to User, has many Z]
- **Lifecycle:** [Based on entity type]
- **Retention:** [Deletion rules or archive requirements]

## 7. INTEGRATION REQUIREMENTS

**External Systems:** [System Name] OR [None for MVP]

## 8. FUNCTIONAL VIEWS/AREAS

**Primary Views:**

- **[Main View]:** [Core functionality]
- **[List/Browse View]:** [Where users see all their entities]
- **[Detail View]:** [Where users see individual entity details]
- **[Create/Edit Forms]:** [Where users input data]
- **[Settings Area]:** [Configuration and preferences]

**Navigation Structure:**

- **Persistent access to:** [Key areas always available]
- **Default landing:** [Where users start after login]
- **Entity management:** [How users navigate list → detail → edit → back]

## 9. MVP SCOPE & DEFERRED FEATURES

### 9.1 MVP Success Definition

- Core workflow functions end-to-end
- All features in Section 3.1 are fully functional
- Basic auth and data persistence work reliably

### 9.2 In Scope for MVP

- [FR-001, FR-002, etc.]

### 9.3 Deferred Features (Post-MVP)

**DF-001: [Deferred Feature Name]**

- **Description:** [What it is]
- **Reason for Deferral:** [Why it's not in MVP]

### 9.4 Technical Constraints

- **Expected concurrent users:** [Number]
- **Data volume limits:** [Reasonable for MVP]

## 10. EVALUATION CRITERIA

**Acceptance Test Cases:**

- Given [precondition], when [action], then [expected result]
- Given [precondition], when [edge case action], then [expected handling]
- Given [error condition], when [action], then [user-friendly error shown]

**Success Definition:**

- [How we know the app is working correctly]
- [Minimum quality bar for handoff to Test mode]

## 11. ASSUMPTIONS & DECISIONS

**Business Model:** [How value is exchanged]
**Access Model:** [Individual / Team / Multi-tenant]
**Entity Lifecycle Decisions:**

- **[Entity 1]:** [Full CRUD + archiving because reason]
- **Key Assumptions:** [Assumption 1 + reasoning]

---

PRD Complete — Ready for Spec
