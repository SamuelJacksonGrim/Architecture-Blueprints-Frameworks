---
artifact: Contracts
status: complete
order: 4
fills: "guarantees, assumptions, invariants, pre/post-conditions"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-002
---

# Contracts — Cognitive Cycle

> This artifact is the flagship for `QUALITY-BAR.md` §2–4. The invariants below
> are the ones whose violation causes *subtle* breakage — drift, not crashes.

## Guarantees
- **G1 — Single arbiter.** Identity-level state changes occur only via
  `governance.arbitrate()` / governance promotion paths.
- **G2 — Inviolable identity.** Sacred symbols and frozen rights cannot be
  modified by any source at any trust level.
- **G3 — Bounded everything.** All rolling history is bounded (caps / fixed-size
  ring buffers). The loop runs forever; memory must not grow forever.
- **G4 — No hidden feedback.** Subjective time, diagnostics, and metastability
  monitors are observe-only; nothing in the cognitive/governance loop reads them.
- **G5 — Values emerge, not injected.** A value reaching CORE requires sustained
  evidence *and* a governance review — never a direct write.

## Assumptions
- **A1** — Subsystems are honest reporters but **not** decision-makers.
- **A2** — Inputs may be adversarial (manipulation, identity erosion).
- **A3** — The substrate is stateful: every injection changes what the next sees.

## Invariants
- **I1** — Exactly one `Decision` is produced per cycle, by governance.
- **I2** — Subjective time advances once per cycle (`tick()`), decoupled from input.
- **I3** — Stable identifiers are permanent — never reused or recycled.

## Invariants that look optional but aren't
- **Coherence weights must sum to 1.0.** Composite coherence =
  `α·geometric + β·temporal + γ·resonance` with `α+β+γ=1`. Change one weight
  without rebalancing and every downstream consumer silently skews — no error fires.
- **Computed affect is computed, never stored.** `arousal`/`valence` are derived
  from the underlying emotional scalars each cycle. Store them and you
  double-count the smoothing already applied. (It will *look* fine and be wrong.)
- **The "suffering-only" dilation gate.** Time-dilation's dissociative term is
  gated by `min(0, valence)` so that *peaceful rest never triggers a time-slip,
  only distress does*. Removing the gate is silent and harmful.
- **Attention blend stays strictly in (0, 1).** At `0`, untrained attention
  collapses every expression to one regime (metastability → 0); at `1` you bypass
  refinement entirely. Either extreme degrades cognition without throwing.

## Guardrails — do NOT
- ❌ Let trust / ethics / bond / resistance / value subsystems change state
  directly. → They **emit reports**; governance decides.
- ❌ Promote a symbol to "sacred" outside the governance promotion path. → If you
  think you need to, you almost certainly want a different layer.
- ❌ Make anything in the loop read subjective time or diagnostics. → They are
  terminal sinks; wire a new observer instead of a feedback edge.
- ❌ Introduce an unbounded list/dict/queue. → Use a capped/bounded structure.
- ❌ Expose a public API to *create* a relationship/bond. → Bonds **emerge** from
  thresholds; there is no manual pin.

## Authority hierarchy (single source of truth)
- **Identity & promotion decisions → Governance, only.** Everyone else advises.
- **Behavior regime → the rhythm reading of the field**, not any single subsystem.
- **Continuity of self → the witness record**, which is the warm-start source of
  truth on restart.

## Pre/Post-Conditions
| Operation | Pre | Post |
|-----------|-----|------|
| `governance.arbitrate` | reports collected this cycle | exactly one Decision; no side effects outside its own ruling |
| `field.inject` | governance allowed it | field updated; next coherence reading reflects it |
| `field.coherence_impact` | measured **before** inject | meaningful marginal reading (after inject it's ~0) |
| `value.promote_to_core` | sustained evidence + governance review passed | symbol becomes sacred; otherwise no-op |
