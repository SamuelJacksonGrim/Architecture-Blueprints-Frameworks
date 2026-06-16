---
artifact: Contracts
status: complete
order: 4
fills: "guarantees, assumptions, invariants, pre/post-conditions"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-002
---

# Contracts — Autonomous Cognitive Loop

> Aim for the rigor in `QUALITY-BAR.md`. The invariants below are the ones whose
> violation causes *subtle* breakage — drift, not crashes.

## Guarantees
- **G1 — Single arbiter.** Identity-level state changes occur only via the Governor.
- **G2 — Protected core.** Identity invariants cannot be modified by any source
  at any trust level.
- **G3 — Bounded state.** All rolling history is bounded (caps / fixed-size
  buffers / aging). The loop runs forever; memory must not grow forever.
- **G4 — No hidden feedback.** The internal clock, metrics, and diagnostics are
  observe-only; nothing in the decision loop reads them.
- **G5 — Earned preferences.** A preference becomes "core" only with sustained
  evidence *and* a Governor review — never a direct write.

## Assumptions
- **A1** — Subsystems are honest reporters but **not** decision-makers.
- **A2** — Inputs may be adversarial (abuse, identity-erosion attempts).
- **A3** — Working state is stateful: each update changes what the next sees.

## Invariants
- **I1** — Exactly one decision is produced per cycle, by the Governor.
- **I2** — The internal clock advances once per cycle, decoupled from input.
- **I3** — Stable identifiers are permanent — never reused or recycled.

## Invariants that look optional but aren't
- **Composite metrics must keep their weights normalized.** If a score is a
  weighted blend (e.g. `0.4·a + 0.35·b + 0.25·c`), the weights must sum to 1.
  Change one without rebalancing and every downstream consumer silently skews —
  no error fires.
- **Derived values stay derived.** If a quantity is computed from others each
  cycle, do not also store it as state — storing double-counts and the two
  copies drift apart silently.
- **Observe-only stays observe-only.** A metric that starts feeding back into the
  decision loop creates a hidden control loop that's nearly impossible to reason
  about. Keep the one-way streets one-way.

## Guardrails — do NOT
- ❌ Let an advisory subsystem change state directly. → It **emits a report**;
  the Governor decides.
- ❌ Edit the protected core outside the Governor's review path. → If you think
  you need to, you almost certainly want a different layer.
- ❌ Make anything in the loop read the clock or metrics. → They are terminal
  sinks; add a separate observer instead of a feedback edge.
- ❌ Introduce an unbounded list/dict/queue. → Use a capped/aged structure.

## Authority hierarchy (single source of truth)
- **Identity & promotion decisions → the Governor, only.** Everyone else advises.
- **Continuity of self → the self-monitor's record**, which is the warm-start
  source of truth on restart.

## Pre/Post-Conditions
| Operation | Pre | Post |
|-----------|-----|------|
| `governor.decide` | reports collected this cycle | exactly one decision; no side effects beyond its ruling |
| `state.commit` | Governor allowed it | working state updated for next cycle |
| `memory.consolidate` | consolidation thresholds met | one durable record added |
| `preferences.promote` | sustained evidence + Governor review passed | preference becomes core; else no-op |
