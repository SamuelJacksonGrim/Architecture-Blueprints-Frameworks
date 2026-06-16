---
artifact: Architecture
status: complete
order: 2
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []
filled_by: both
last_decision: D-002
---

# Architecture — Autonomous Cognitive Loop

> A blueprint for a **persistent, self-governing system**: one that runs a
> continuous loop, maintains and protects its own identity through a single
> governing authority, handles external sources, and grows preferences from
> experience.
>
> Different from a request/response agent (`skeletons/agents/`): that acts on the
> *world* on demand. This runs **continuously**, and its actions loop back onto
> its **own state** — which is what makes it a *self* rather than a tool.
> Fill the bracketed parts in for your system.

## Purpose
Give a system a stable identity that survives across time: it perceives, updates
internal state every tick, decides through one arbiter (so it never contradicts
itself), consolidates lasting memory, and routes its own behavior — without any
subsystem acting unilaterally.

## The tiers (organized by concern, all wired into one loop)
| Tier | Concern | Components (generic) |
|------|---------|----------------------|
| **0** | Core substrate | working state, perception, action generator, self-monitor |
| **1** | Governance | the **Governor** (single arbiter), policy, source trust |
| **2** | Source integrity | input validation, dependency/over-reliance checks, abuse resistance |
| **3** | Preference learning | preferences that grow from experience, promotion-gated |
| **4** | Internal clock & metrics | a per-cycle tick and self-health metrics — **observe-only** |

## Boundaries
- **Inside the loop:** tiers 0–3 read and write internal state *through the Governor*.
- **Terminal sinks (observe-only, MUST NOT feed back):** the internal clock,
  health metrics, and any diagnostics. They read the loop; the loop never reads
  them. (See `Contracts` + D-003.)
- **Protected core:** a set of identity invariants that no source, at any trust
  level, may modify (e.g. the system's purpose, its safety limits).

## Data Flow
```
input ─▶ working state ─▶ action generator ─▶ candidate action
                                                   │
                            ┌── self-monitor ──────┘
                            ▼
                     update metrics ─▶ internal clock (tick) ── terminal sink ─▶ (diagnostics only)
                            │
                            ▼
                       GOVERNOR  ◀── advice from: source-trust / validation / abuse-resistance / preferences
                            │ (the ONLY component that decides)
                            ▼
              commit action · consolidate memory · route next behavior
                            │
                            ▼
                       state decay/aging ─▶ (next cycle)
```

## Control Flow
A single **Loop Coordinator** runs every tier in a fixed sub-step order each
tick. Control originates and returns there. The advisory subsystems **produce
reports**; only the **Governor decides** (D-002). No subsystem may short-circuit
the loop.

## High-Level Diagram
See [`diagrams/architecture_graph.md`](diagrams/architecture_graph.md),
[`diagrams/system_flow.md`](diagrams/system_flow.md), and
[`diagrams/execution_map.md`](diagrams/execution_map.md).
