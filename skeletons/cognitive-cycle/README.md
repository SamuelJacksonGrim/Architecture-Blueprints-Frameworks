---
artifact: README
status: complete
order: 10
fills: "front door — what/why/problem/components for the instantiated system"
depends_on: [Architecture, Flows, Contracts, Modules]
filled_by: both
last_decision: null
---

# Autonomous Cognitive Loop skeleton

> A complete reference skeleton for a **persistent, self-governing system** — one
> that runs continuously, protects its own identity through a single arbiter,
> handles external sources safely, and grows preferences from experience.
> Copy it, then fill the bracketed parts in for your system.

## What is this?
A blueprint for a system that runs a continuous loop and acts on **its own
state** rather than only on the world — the difference between a *self* and a
*tool*.

## Why does it exist?
Request/response agents (see `skeletons/agents/`) act on the world on demand. A
continuous, self-governing loop has a different failure surface — drift, identity
erosion, runaway feedback — so this skeleton pins the answers to those down front.

## What problem does it solve?
It gives you, on day one, the load-bearing decisions of a "self":
- **one arbiter** for identity (no diffuse authority),
- **terminal sinks** so observability never becomes hidden control,
- **earned, not declared, preferences** (manipulation-resistant),
- **bounded state** so "runs forever" is actually true.

## The tiers
0 substrate · 1 governance · 2 source integrity · 3 preference learning ·
4 internal clock. See [`Architecture.md`](Architecture.md).

## The load-bearing decisions
- **D-002** single Governor (report/decide split)
- **D-003** clock & metrics are terminal sinks (no feedback)
- **D-004** preferences are earned and promotion-gated, never declared
- **D-005** bounded state in a forever-loop

(Full reasoning in [`DecisionLog.md`](DecisionLog.md).)

## Relationship to the agent skeletons
Same universal ontology (`Entity → State → Event → Evaluation → Decision →
Action`) as `skeletons/agents/` — but the Action loops back onto the Entity's own
State instead of the world. An agent *does*; an autonomous loop *is*.

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
