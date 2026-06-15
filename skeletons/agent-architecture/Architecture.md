---
artifact: Architecture
status: complete
order: 2
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []
filled_by: both
last_decision: D-002
---

# Architecture — Agent

> The city map for a general autonomous agent: something that takes a **goal**,
> reasons over **memory** and **perception**, selects and runs **tools**,
> **evaluates** the result, and loops until the goal is met or it must stop.
>
> This is a *worked example* — a real, comparable instantiation of the
> 10-artifact schema, not a stub. Use it as a reference for how full looks.

## Purpose
An agent is a bounded control loop wrapped around a reasoner. It turns a goal
plus observations into a sequence of evaluated actions, maintaining state across
steps, and terminates with a response (success, partial, or give-up).

## Major Subsystems
- **Intake** — receives the goal + initial context; normalizes into a `Goal` + first `Percept`.
- **Memory** — working memory (this run) + long-term store (across runs). Read/write of `MemoryRecord`s.
- **Planner** — the reasoner. Given goal + memory + last observation, proposes the next `Action` as a `Plan`.
- **Tool Registry** — catalog of available tools and their `Interfaces`. Resolves a `ToolId` to an implementation.
- **Executor** — runs the selected `ToolCall` in isolation, produces a `ToolResult` → `Observation`.
- **Evaluator** — the critic/gate. Scores each proposed action *before* execution and each observation *after*. Decides: proceed, retry, replan, or terminate.
- **Output** — assembles the final `Response` when the loop ends.

## Boundaries
- **Inside:** Planner, Evaluator, Memory, Tool Registry, Executor orchestration.
- **Outside (untrusted):** tool side-effects (network, filesystem, other systems) and the goal-giver. Everything crossing the Executor boundary is treated as untrusted input on return.
- **Process line:** the Evaluator gate sits between *deciding* an action and *executing* it. Nothing crosses into the Executor without passing it (see D-002).

## Data Flow
```
Goal ─▶ Intake ─▶ Percept ─▶ Planner ─▶ Plan(Action)
                                  ▲            │
                              Memory◀──────────┤ (read context / write records)
                                  ▲            ▼
                            Observation   Evaluator(pre-gate)
                                  ▲            │ proceed
                                  │            ▼
                              Executor ◀── ToolCall ◀── Tool Registry
                                  │
                                  └─▶ ToolResult ─▶ Evaluator(post) ─▶ {loop | finalize}
```

## Control Flow
Control originates at **Intake**, lives in the **loop coordinator** (Planner ↔
Evaluator ↔ Executor), and returns at **Output**. The loop coordinator owns
termination; no subsystem can end the run except by signalling the coordinator.

## High-Level Diagram
See [`diagrams/architecture_graph.md`](diagrams/architecture_graph.md) and
[`diagrams/system_flow.md`](diagrams/system_flow.md).
