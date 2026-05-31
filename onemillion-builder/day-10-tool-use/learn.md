# Day 10 — Tool Use

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 7-12 | ~1-2.5 hours | Make your AI actually do things**

---

## Learning Frame

- **Mental model:** Tool use lets AI read or change product state through narrow, validated actions.
- **What can go wrong:** You give the AI too much write power or loose parameters.
- **What to ignore today:** Ignore complex agents; build one small tool.

## What You'll Have After Today

- An AI that can **take real actions** in your app — not just generate text
- At least one **tool** the AI can call (e.g., "save this draft," "update task status," "fetch latest data")
- Understanding of when to use tools vs. when to use plain text generation
- Your first taste of agentic behavior (Pattern C from Day 7)

This is where AI stops being a chatbot and starts being a coworker.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: What Is Tool Use? (~10 min read)

Until today, your AI feature has been a one-way conversation: user gives input → AI generates output → user uses output.

Tool use changes the loop. Now the AI can **call functions in your code** to take actions or fetch data:

```
User clicks "Draft and save my follow-up to Sarah"
  → AI generates the email draft
  → AI calls the saveDraft(client: "Sarah", body: "...") tool
    → Your code runs: inserts the draft into the database
    → Your code returns: { success: true, id: 42 }
  → AI tells the user: "Saved draft to Sarah. Open it from your drafts folder."
```

**The AI isn't just generating text. It's deciding to call a function. Your code runs the function. The AI uses the result to continue.**

This is the foundation of every "AI does things for me" product — Cursor's Composer, Claude.ai's web browsing, every workflow agent. They're all just LLMs + tools.

---

## Part 2: How Tools Work Technically (~15 min read)

You define tools by name, description, and parameters. The AI sees the list and decides which to call.

### Tool Definition

```typescript
const tools = {
  saveDraft: tool({
    description: 'Save a draft email to the user\'s drafts folder',
    parameters: z.object({
      client_name: z.string().describe('Name of the client this draft is for'),
      subject: z.string().describe('Email subject line'),
      body: z.string().describe('Email body, 3 paragraphs'),
    }),
    execute: async ({ client_name, subject, body }) => {
      // Your code that actually saves it
      const result = await supabase.from('drafts').insert({
        client_name, subject, body, user_id: currentUserId
      });
      return { success: true, draft_id: result.data.id };
    }
  }),
  
  getRecentDeliverables: tool({
    description: 'Get the user\'s 5 most recent deliverables',
    parameters: z.object({
      status_filter: z.enum(['all', 'in-progress', 'sent']).default('all'),
    }),
    execute: async ({ status_filter }) => {
      const query = supabase.from('deliverables').select().eq('user_id', currentUserId);
      if (status_filter !== 'all') query.eq('status', status_filter);
      const { data } = await query.limit(5);
      return data;
    }
  }),
};
```

### How The AI Uses Them

When you call `streamText` with tools, the AI:
1. Reads the user's request + your system prompt + the tool descriptions
2. Decides which tool(s) to call (if any)
3. Generates a tool call with the right parameters
4. Your code executes the tool, returns the result
5. The AI uses the result to continue the conversation / generate next output
6. Loop until done

**You don't have to write this loop.** Vercel AI SDK + Anthropic handle it. You just define tools + system prompt; the AI does the orchestration.

### Two Categories Of Tools

**Read tools (low risk):** Tools that fetch data without changing anything.
- `getRecentDeliverables`
- `getClientHistory`
- `searchEmails`

**Write tools (high risk):** Tools that modify data or take actions.
- `saveDraft`
- `markDeliverableComplete`
- `sendEmail` (the scariest — usually want a confirmation step)

**Recommendation: start with read-only tools today.** Add write tools tomorrow once you're comfortable.

---

## Part 3: Multi-Agent Decomposition (Pillar 2 In Action) (~10 min read)

This is the third pillar of Agentic SDLC showing up in real code.

**Naive approach:** One mega-prompt that tries to do everything.

> "You are an AI assistant. Help the user manage their freelance work, draft emails, update statuses, search their CRM, ..."

This fails. The AI gets confused. It tries to do everything in one shot. It hallucinates results.

**Multi-agent approach:** Define small focused tools. The AI's job is just to decide WHICH tool to call. Each tool is a "small agent" with a clear job.

> "You are an AI assistant for freelance designers. You have these tools: [list]. Pick the right tool for the user's request."

This works. The AI is great at decomposition. Each tool does one thing well. The whole system is the sum of focused parts.

**Translation to your code:** Don't write one giant prompt + giant function. Write a thin orchestrator prompt + several small focused tools, each with a tight description and tight parameters.

---

## Today's Assignment

Pick the simplest version of "your AI takes an action":

- **If you went Pattern A on Day 7** (text generation): Add one tool — `save_generated_output` — so after the AI drafts content, it can save it to your DB.
- **If you went Pattern B** (decision-maker): Add tools the AI uses to FETCH the data it needs to decide. E.g., `get_user_data`, `get_recent_activity`.
- **If you went Pattern C** (agent): Define 1-3 tools the agent can use to take its assigned actions.

Start with ONE tool, even if your Pattern needs more eventually. One working tool today; expand later.

In [build.md](./build.md):
1. Add a tool definition to your API route
2. Update the system prompt to mention the tool ("You have access to these tools...")
3. Test that AI calls the tool when appropriate
4. Verify the tool actually changes data / takes action
5. Run Day 10 verification

---

## What Good Looks Like

After Day 10:

1. User types "Save my draft for the Acme website project as 'in progress'"
2. AI generates the response
3. Behind the scenes: AI calls `update_project_status` tool with `project_name: "Acme website", new_status: "in-progress"`
4. Your code updates the DB
5. AI responds: "Done — Acme website is marked in progress."
6. The user refreshes their dashboard — Acme website actually shows "in progress."

The AI didn't just talk about doing it. It did it.

---

## Common Mistakes (Today)

1. **Tools without proper auth.** Critical security. Every tool MUST verify the user has permission to do whatever the tool does. The user_id should come from the session, not from the AI.

2. **AI hallucinates tool calls.** AI might "call" a tool that doesn't exist, or pass wrong parameters. Validate inputs. Use Zod schemas. Return errors gracefully.

3. **Write tools before read tools.** Builders get excited about "AI takes actions" and skip safer read tools first. Build confidence with read tools today; add write tools later.

4. **No logging.** When something goes wrong, you'll want to know which tool was called with which parameters. Log every tool call.

5. **Tool description too vague.** "save_thing" doesn't tell the AI when to use it. "Save the AI-generated draft to the user's drafts folder so they can review and send later" does.

---

## What Should Be True After Day 10

- [ ] API route defines at least 1 tool with description + parameters + execute function
- [ ] System prompt mentions the available tools
- [ ] When user makes a relevant request, AI calls the tool
- [ ] Tool actually changes data / fetches data correctly
- [ ] Tool has auth check (verifies user can do this action)
- [ ] Tool failures are handled (returns error object, doesn't crash)
- [ ] Tested live (Vercel URL, not just localhost)
- [ ] Verification passed ✅

---

## Verify Your Day 10

Ask your harness to run the OneMillion verifier for this day.

---

## Share It

```
✅ Day 10 done: AI takes real actions in my app — not just talking, actually doing
🎯 Tomorrow: AI personalized to MY user's data (RAG)
#BuildingWith1M
```

---

## Go Deeper

- **[Anthropic Tool Use docs](https://docs.anthropic.com/en/docs/tool-use)** — official
- **[Vercel AI SDK Tools](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling)** — implementation
- **[Function Calling Patterns](https://platform.openai.com/docs/guides/function-calling)** — OpenAI's docs, same patterns
- **[Anthropic's Tool Use Cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/tool_use)** — real examples

---

→ **Next:** [Day 11 — RAG (AI reads your user's data)](../day-11-rag/learn.md)
