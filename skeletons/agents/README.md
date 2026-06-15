# 🤖 Agent Skeletons — the loop family

The four agent-loop patterns that dominate practice in 2026. They all share the
same bones (an LLM, tools, memory, a loop); they differ in **the shape of the
loop**. Learn the baseline, then read each variant as "what changes."

---

## Read this first: what an "agent loop" is

An agent doesn't answer in one shot. It works like a person at a desk:

> **think** ("I need the budget file") → **act** (open it) →
> **observe** ("the number is $4,000") → **think again** → … until done.

That **think → act → observe → repeat** cycle is *the loop*. Every pattern below
is a different way to organize it.

---

## The family at a glance

| Pattern | The loop in one line | Best for | Cost |
|---|---|---|---|
| **[ReAct](react/)** ⭐ baseline | think → act → observe, repeat | simple tool-use; the default starting point | low |
| **[Plan-Execute](plan-execute/)** | plan all steps up front → run them → replan if needed | long tasks with dependent steps (~3.6× faster) | low–med |
| **[Reflexion](reflexion/)** | attempt → critique the failure → retry smarter | tasks with a pass/fail signal to learn from | med |
| **[Tree-of-Thoughts](tree-of-thoughts/)** | branch into many thoughts → score → backtrack | puzzles/planning needing exploration | high |

**The golden rule (2026 consensus):** start with **ReAct**. Add a fancier
pattern *only* when a specific failure mode demands it. Over-engineering an agent
costs more than it pays back.

---

## How this folder is organized (and why)

- **`react/`** is a **complete** skeleton — all 10 artifacts filled. It's the one
  to read in full.
- **`plan-execute/`, `reflexion/`, `tree-of-thoughts/`** are **deltas**. Each
  carries only the artifacts that actually change — its `README`, its `Flows`
  (the new loop), one `DecisionLog` entry, and a diagram. Everything else
  (Types, Interfaces, Dependencies, the Schema chain) is **inherited from
  `react/`**.

Why deltas instead of four full copies? Because the *difference* between patterns
is the entire lesson. Four near-identical 10-artifact folders would bury the one
paragraph that matters. **A variant + the ReAct base = one complete 10-artifact
system** — which keeps the repo's Instantiation Rule satisfied without 40 files
of duplication.

---

## They all speak the same ontology

Every pattern maps onto the repo's universal chain
(`Entity → State → Event → Evaluation → Decision → Action`, see `../../SCHEMA.md`):

- **ReAct** — Evaluation is *implicit*, inside each Thought.
- **Reflexion** — Evaluation is *explicit and remembered* (the critique step).
- **Tree-of-Thoughts** — Evaluation *scores branches* to steer a search.
- **Plan-Execute** — Decision is *front-loaded* into one plan.

That shared ontology is what lets you compare an agent to any other skeleton in
this repo.

---

## Sources (current as of June 2026)
- [Agentic Loops: From ReAct to Loop Engineering (2026 Guide) — Data Science Dojo](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/)
- [Agentic Design Patterns: The 2026 Guide — SitePoint](https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/)
- [LLM Agent Architectures in 2026: Core Components and Patterns — Future AGI](https://futureagi.com/blog/llm-agent-architectures-core-components/)
- [What Is the AI Agent Loop? — Oracle Developers](https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems)
- [Architecting Resilient LLM Agents: Secure Plan-then-Execute — arXiv](https://arxiv.org/pdf/2509.08646)
