# one-million-builders

*Teaching 1,000,000 people to build real products with AI. Free. Forever.*

*By [Sid Dixit](https://www.linkedin.com/in/siddharthdixit/)*

[![one-million-builders](course/diagrams/hero-animated.gif)](course/README.md)

## Start The Course

The canonical learner page is:

**[course →](course/README.md)**

That folder contains the course, agents, install script, docs, verification tools, and examples. Start there.

Learners should star, fork, clone, and install from their own fork:

```bash
git clone https://github.com/YOUR-USERNAME/one-million-builders.git
cd one-million-builders
./course/install-agents.sh
```

Then paste this into Claude Code, Codex, Cursor, Gemini, Copilot, Antigravity, or another coding harness:

```text
I am starting the OneMillion course from my fork.

Read AGENTS.md and course/course-manifest.json.
Read course/docs/teaching-protocol.md.
Read course/days/single.md.
Become my OneMillion learning orchestrator.
First enforce the Preflight Gate.
Then start Day 0.
```

## Repository Map

| Path | Purpose |
|---|---|
| [course](course/README.md) | The full 18-day learner course and canonical landing page |
| [course/days](course/days/single.md) | Day 0-18 course content |
| [course/agents](course/agents/README.md) | Portable OneMillion agents and skills |
| [AGENTS.md](AGENTS.md) | Universal bootstrap that tells coding harnesses how to teach the course |
| [onemillion-plugin](onemillion-plugin/README.md) | Optional native extension path |
| [MANIFESTO.md](MANIFESTO.md) | The OneMillion manifesto |
| [builders](builders/README.md) | Builder wall |
| [cohort](cohort/README.md) | Cohort information |

Generated harness adapters such as `.claude/`, `.cursor/`, `.gemini/`, `.agents/`, and Copilot instruction files are not committed at the repository root. The installer creates them locally from `course/agents`.

*MIT licensed. Free for learners, forever.*
*→ [onemillion.build](https://onemillion.build)*
