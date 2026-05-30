# AI Acceptance Criteria

## Test Case 1 — Normal Weekly Update

**Given** a client has three deliverables with statuses `done`, `in-progress`, and `blocked`  
**When** the user clicks "Draft weekly update"  
**Then** the output mentions all three statuses accurately and does not invent extra work.

## Test Case 2 — Sparse Data

**Given** a client has one deliverable with no notes  
**When** the user generates an update  
**Then** the output is short and asks the designer to add context before sending.

## Test Case 3 — Cost Budget

Each generation should cost less than $0.05 for typical input size. If average cost exceeds $0.10, switch to Haiku or shorten context.

