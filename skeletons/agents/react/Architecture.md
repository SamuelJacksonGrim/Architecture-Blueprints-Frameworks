---
artifact: Architecture
status: complete
order: 2
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []
filled_by: both
last_decision: D-002
---

# Architecture — ReAct Agent

> The **simplest, most common** agent shape (2026). An LLM that alternates
> **Reasoning** and **Acting** in one loop until it decides it's done.
> This is the baseline every other agent variant in this family builds on.

## Purpose
Turn a goal into an answer by repeatedly: thinking about what to do next, doing
one thing (usually a tool call), looking at the result, and thinking again.
The model itself decides when it has enough to answer.

## Major Subsystems
- **Reasoner** — the LLM. Reads the goal + scratchpad, emits either a *Thought+Action* or a *Final Answer*.
- **Tool Registry** — the catalog of actions the agent is allowed to take.
- **Executor** — runs the chosen action, returns an Observation.
- **Scratchpad** — the running transcript of `(Thought, Action, Observation)` triples. This is the agent's working memory.
- **Output** — emits the final answer when the Reasoner signals it's done.

## Boundaries
- **Inside:** Reasoner, Scratchpad, loop control.
- **Outside (untrusted):** anything the Executor touches (tools, network, files) and the result it returns.
- **Process line:** the Executor is the only place that affects the outside world.

## Data Flow
```
Goal ─▶ Reasoner ─▶ Thought + Action ─▶ Executor ─▶ Observation
          ▲                                              │
          └────────────── Scratchpad ◀──────────────────┘
                              (append each triple, feed back in)
   ... until Reasoner emits "Final Answer" ─▶ Output
```

## Control Flow
Control lives in the loop: Reasoner → Executor → back to Reasoner. The Reasoner
owns termination by emitting a Final Answer; a `MAX_STEPS` budget is the safety
backstop so the loop can't run forever.

## High-Level Diagram
See [`diagrams/system_flow.md`](diagrams/system_flow.md).
