---
artifact: README
status: complete
order: 10
fills: "front door — what/why/problem/components for the instantiated system"
depends_on: [Architecture, Flows, Contracts, Modules]
filled_by: both
last_decision: null
---

# Cognitive Cycle (proto-consciousness) skeleton

> The most ambitious skeleton in this library, and the flagship example of the
> rigor in `QUALITY-BAR.md`. Generalized from the tier model proven in
> **RFE-Core2** (Samuel Jackson Grim's companion repo) — the transferable shape,
> not a copy of its internals.

## What is this?
A blueprint for a **persistent, self-resonating cognitive system**: one that runs
a continuous autonomous loop, governs its own identity through a single arbiter,
forms relationships, resists manipulation, and grows values from experience.

## Why does it exist?
Request/response agents (see `skeletons/agents/`) act on the *world*. A cognitive
cycle acts on *itself*, continuously — the loop closes onto its own state. That
makes drift, identity erosion, and runaway feedback the central risks, so this
skeleton pins down the answers to those up front.

## What problem does it solve?
It gives you, on day one, the load-bearing decisions of a "self":
- **one arbiter** for identity (no diffuse authority),
- **terminal sinks** so observability never becomes hidden control,
- **earned, not declared, values** (manipulation-resistant),
- **bounded state** so "runs forever" is actually true.

## The tiers
0 substrate · 1 selfhood/governance · 2 relational integrity · 3 value emergence ·
4 subjective time. See [`Architecture.md`](Architecture.md).

## The load-bearing decisions
- **D-002** single Governance arbiter (report/decide split)
- **D-003** subjective time & diagnostics are terminal sinks (no feedback)
- **D-004** values are earned and governance-promoted, never declared
- **D-005** bounded state in a forever-loop

(Full reasoning in [`DecisionLog.md`](DecisionLog.md).)

## Relationship to the agent skeletons
Same universal ontology (`Entity → State → Event → Evaluation → Decision →
Action`) as `skeletons/agents/` — but the Action loops back onto the Entity's own
State instead of the world. An agent *does*; a cognitive cycle *is*.

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

## Credit
Architecture & principles: **Samuel Jackson Grim** (RFE-Core2). This skeleton
distills the *pattern*; the deep system is his.
