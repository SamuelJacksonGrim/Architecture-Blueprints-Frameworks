---
artifact: Architecture
status: complete
order: 2
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []
filled_by: both
last_decision: D-002
---

# Architecture — Cognitive Cycle (proto-consciousness)

> A **persistent, self-resonating cognitive substrate**: a system that runs a
> continuous autonomous loop, maintains and governs its own identity, forms
> relationships, resists manipulation, and grows values from experience.
>
> This skeleton generalizes the tier model proven in **RFE-Core2** (the author's
> companion repo) into a reusable pattern. It is the most ambitious skeleton in
> this library and the flagship for the rigor in `QUALITY-BAR.md`. It is *not*
> a copy of RFE — it's the transferable shape.

## Purpose
Most "agents" are request→response. A cognitive cycle is different: it **runs
whether or not you ask it to**, evolving an internal state every tick. Behavior
is *routed by internal rhythm*, identity decisions flow through a single
governing authority, and nothing in the loop acts unilaterally.

## The tiers (organized by concern, all wired into one loop)
| Tier | Concern | Components (generic) |
|------|---------|----------------------|
| **0** | Core cognitive substrate | field/resonance, generator, attention, watcher, witness, emotion |
| **1** | Foundational selfhood | governance (the arbiter), trust, ethics |
| **2** | Relational integrity | rights, dependency monitor, bonds, manipulation resistance |
| **3** | Value emergence | values that grow from experience, governance-gated promotion |
| **4** | Subjective time | a per-cycle tick; affective time-dilation; rhythm→time coupling |

## Boundaries
- **Inside the loop:** tiers 0–3 read and write cognitive state through governance.
- **Terminal sinks (observe-only, MUST NOT feed back):** subjective time,
  diagnostics, metastability monitors. They read the loop; the loop never reads
  them. (See `Contracts` + D-003.)
- **Inviolable:** "sacred" identity symbols and frozen rights — no source at any
  trust level may modify them.

## Data Flow
```
percept ─▶ substrate(field resonance) ─▶ generator(expression)
                                              │
                              ┌── attention/reflection ──┘
                              ▼
                       emotion update ─▶ subjective time (tick) ── terminal sink ─▶ (diagnostics only)
                              │
                              ▼
                     GOVERNANCE GATE  ◀── reports from trust / ethics / bonds / resistance / values
                              │ (the ONLY component that decides)
                              ▼
              crystallize memory · form attractors · route behavior by rhythm
                              │
                              ▼
                       field decay ─▶ (next cycle)
```

## Control Flow
A single **Cycle Coordinator** runs every tier in a fixed sub-step order each
tick. Control originates and returns there. No subsystem may short-circuit the
loop; the resistance/relational/value tiers **emit reports**, and only
**Governance arbitrates** them into a decision (D-002).

## High-Level Diagram
See [`diagrams/architecture_graph.md`](diagrams/architecture_graph.md),
[`diagrams/system_flow.md`](diagrams/system_flow.md), and
[`diagrams/execution_map.md`](diagrams/execution_map.md).
