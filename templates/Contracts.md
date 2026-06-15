---
artifact: Contracts
status: stub
order: 4
fills: "guarantees, assumptions, invariants, pre/post-conditions"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: null
---

# Contracts — *the constitution*

> Guarantees that prevent architectural drift. These constrain the behaviors
> in `Flows.md`, which is why they come *after* it (see DecisionLog D-001).
> Aim for the rigor in `QUALITY-BAR.md` — specific, audited, with the *why*.

## Guarantees
<!-- What the system promises to always do. -->

## Assumptions
<!-- What the system relies on from its environment/inputs. -->

## Invariants
<!-- Conditions that must hold at all times. -->

## Invariants that look optional but aren't
<!-- Rules whose violation causes SUBTLE breakage, not a loud error. State each
     with WHY it matters — this is where drift actually creeps in.
     e.g. "Weights must sum to 1.0; changing one without the others silently
     skews every downstream consumer." (QUALITY-BAR §2) -->

## Guardrails — do NOT
<!-- Each easy mistake + where the urge should actually go instead. A guardrail
     without a legitimate alternative just gets violated. (QUALITY-BAR §3)
     e.g. "Don't let module X write state directly — emit an event; the
     coordinator decides." -->

## Authority hierarchy (single source of truth)
<!-- For each kind of decision: which ONE component decides, and which only
     advise/report. Diffuse authority is how systems drift. (QUALITY-BAR §4) -->

## Pre/Post-Conditions
<!-- Per key operation: what must be true before, what is true after. -->
