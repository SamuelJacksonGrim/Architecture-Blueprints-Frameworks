---
artifact: README
status: complete
order: 10
fills: "front door — what/why/problem/components for the instantiated system"
depends_on: [Architecture, Flows, Contracts, Modules]
filled_by: both
last_decision: null
---

# ReAct Agent (baseline)

> The simplest, most common agent loop in 2026 — and the one to read first.
> Every other variant in `skeletons/agents/` is described as a change *to this*.

## What is this?
An agent that alternates **Reasoning** and **Acting**: think about what to do,
do one thing (usually call a tool), look at the result, think again — until it
decides it has the answer.

## Why does it exist?
It's the default for a reason: the full reasoning trace is visible, so it's the
easiest agent to build, inspect, and debug. Start here; add complexity only when
a real problem forces you to.

## What problem does it solve?
Lets an LLM tackle tasks it can't answer in one shot, by giving it tools and
letting it work step by step.

## Major components
Reasoner (the LLM) · Tool Registry · Executor · Scratchpad · Loop Control ·
Output. See [`Architecture.md`](Architecture.md) and [`Flows.md`](Flows.md) —
the loop itself is the code block in `Flows.md`.

## Artifact status
| Artifact | Status |
|----------|--------|
| Architecture | complete |
| Flows | complete |
| Contracts | complete |
| Types | complete |
| Schemas | complete |
| Interfaces | complete |
| Dependencies | complete |
| Modules | complete |
| DecisionLog | complete |
| README | complete |
