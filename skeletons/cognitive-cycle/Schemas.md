---
artifact: Schemas
status: complete
order: 6
fills: "conceptual ontology — Entity→State→Event→Evaluation→Decision→Action"
depends_on: [Types]
filled_by: both
last_decision: null
---

# Schemas — Autonomous Cognitive Loop

## Core Transformation Chain
This loop is the universal ontology made *recursive* — the Action feeds back
into the Entity's own State, which is what makes it a *self*:

```
Entity      = the system itself (a persistent identity, not a session)
   ↓
State       = working state + consolidated memory + identity
   ↓
Event       = an input (external) or an action (internal, self-generated)
   ↓
Evaluation  = subsystem reports → governor.decide()   (advice → ruling)
   ↓
Decision    = a ruling (allow / limit / sandbox / reject)
   ↓
Action      = commit to state · consolidate memory · route next behavior
   ↺ (the new state is the next cycle's State — the loop closes on itself)
```

The closing of the loop **onto its own state** is the difference between an agent
(acts on the world) and an autonomous cognitive loop (acts on itself, continuously).

## Cognitive Schemas
- **Identity** — the protected core + continuity record; the invariant self.
- **Belief** — consolidated memories that survived the thresholds.
- **Preferences** — values grown from experience; core ones are protected.

## Information Schemas
Input/action → committed to state (governed) → metric reading → consolidation (if
thresholds met) → durable memory. Trust transitions happen only at the Governor.

## Transformation Schemas
- `state → behavior`: routing.
- `reports → decision`: governance (the one-way authority step).
