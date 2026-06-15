---
artifact: Types
status: complete
order: 5
fills: "core domain types, primitives, enums, identifiers, structural schemas"
depends_on: [Contracts]
filled_by: both
last_decision: null
---

# Types — Cognitive Cycle

## Core Domain Types
- **Symbol** — `{ stable_id: SymbolId, content, sacred: bool }` (stable_id permanent, I3)
- **FieldState** — accumulating resonance state with saturation + decay
- **Expression** — a unit-normalized vector the generator produces
- **EmotionalState** — six scalars `{ curiosity, wonder, joy, tension, boredom, stability }`
- **Report** — `{ source, kind, severity, payload }` (advice, never action)
- **GovernanceDecision** — `{ ruling, reason, affected }` (the only authority output)
- **Bond** — emergent relationship `{ partner, strength, type }` (no manual create)
- **Value** / **CoreValue** — a value; CORE is governance-promoted + sacred
- **CrystallizedMemory** — a durable memory formed when thresholds are met
- **Tick** — one cycle of subjective time

## Primitives & Identifiers
- `SymbolId` — opaque, permanent, never recycled.
- **Computed (not stored)** — `arousal`, `valence`: derived from EmotionalState each cycle.
- `phase_coherence` — FFT-derived field organization in `[0,1]`.

## Enums
- **Rhythm** = `stabilize | dream | reflect | explore` (routed by field energy bands)
- **TrustLevel** = `sacred | high | trusted | neutral | skeptical | untrusted | toxic`
- **Decision** = `allow | allow_weakened | quarantine | reject`
- **BondType** = `existential | emotional | intellectual | transactional`

## Structural Schemas
- A **cycle** = the ordered sub-step tuple in `Flows.md`.
- **Coherence composite** = `α·geometric + β·temporal + γ·resonance`, `α+β+γ=1`
  (the sum is an invariant, see `Contracts`).
