---
artifact: Types
status: complete
order: 5
fills: "core domain types, primitives, enums, identifiers, structural schemas"
depends_on: [Contracts]
filled_by: both
last_decision: null
---

# Types — Autonomous Cognitive Loop

## Core Domain Types
- **Identifier** — `{ id: StableId, protected: bool }` (protected ids are immutable, I3)
- **WorkingState** — the per-cycle internal state (accumulates + ages)
- **Action** — a candidate the generator proposes
- **Report** — `{ source, kind, severity, payload }` (advice, never action)
- **Decision** — `{ ruling: Ruling, reason, affected }` (the only authority output)
- **MemoryRecord** — a durable record created on consolidation
- **Preference** / **CorePreference** — a learned preference; core = promoted + protected
- **Metric** — an observe-only health/coherence reading
- **Tick** — one cycle of the internal clock

## Primitives & Identifiers
- `StableId` — opaque, permanent, never recycled.
- **Computed (not stored)** — any value derived from others each cycle.

## Enums
- **Ruling** = `allow | allow_limited | sandbox | reject`
- **TrustLevel** = `core | high | trusted | neutral | low | untrusted | blocked`
- **Behavior** = `[ define the behavior modes your system routes between ]`

## Structural Schemas
- A **cycle** = the ordered sub-step tuple in `Flows.md`.
- A **composite metric** = a weighted blend whose weights sum to 1 (the sum is
  an invariant, see `Contracts`).
