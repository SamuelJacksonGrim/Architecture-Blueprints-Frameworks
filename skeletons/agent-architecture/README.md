---
artifact: README
status: complete
order: 10
fills: "front door — what/why/problem/components for the instantiated system"
depends_on: [Architecture, Flows, Contracts, Modules]
filled_by: both
last_decision: null
---

# Agent Architecture Skeleton

> A fully-worked instantiation of the repo's 10-artifact schema. Use it as the
> reference for what a *complete* skeleton looks like, or copy it as the
> starting point for a real agent.

## What is this?
A blueprint for a **general autonomous agent**: a bounded control loop that
turns a goal into a sequence of evaluated, tool-executed actions over memory.

## Why does it exist?
Agents are the most on-theme pattern for *collaboration with intelligent
entities* — and the one most prone to drift (runaway loops, ungated actions,
polluted memory). This skeleton pins the load-bearing decisions down front.

## What problem does it solve?
It gives you, on day one: guaranteed termination, an evaluation gate before
every action, memory integrity, and a bounded blast radius — as **contracts**,
not afterthoughts.

## Major components
Intake · Memory · Planner · Evaluator · Tool Registry · Executor ·
Loop Coordinator · Output. See [`Modules.md`](Modules.md) and
[`Architecture.md`](Architecture.md).

## The three load-bearing decisions
- **D-001** Flows before Contracts
- **D-002** Evaluator gate before every action
- **D-003** Bounded loop for guaranteed termination

(Full reasoning in [`DecisionLog.md`](DecisionLog.md).)

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
