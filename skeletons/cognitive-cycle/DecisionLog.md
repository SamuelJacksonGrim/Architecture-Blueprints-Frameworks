---
artifact: DecisionLog
status: complete
order: 99
fills: "architectural memory — decisions, alternatives, reasons, dates"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Cognitive Cycle

> Empirical-ledger discipline (see `QUALITY-BAR.md` §7): titles are questions,
> entries are append-only with a `Status`, and each names its basis.

### D-001 — Build order: Flows before Contracts?
- **Date:** 2026-06-15 · **Decided by:** both · **Status:** active · **Depends on:** —
- **Decision:** Architecture → Flows → Contracts.
- **Alternatives:** Contracts first (rejected — can't constrain undescribed behavior).
- **Reason:** Inherited from `PIPELINE.md`.
- **Affects:** Flows, Contracts.

### D-002 — Where does authority live: distributed or single arbiter?
- **Date:** 2026-06-15 · **Decided by:** both · **Status:** active · **Depends on:** —
- **Decision:** A single Governance module arbitrates all identity-level
  decisions; every other subsystem only emits reports.
- **Alternatives:** Let each subsystem act on its own findings (rejected —
  diffuse authority is how a self drifts and contradicts itself).
- **Reason:** A coherent identity needs one place where conflicts resolve. The
  report/decide split is the structural guarantee of coherence.
- **Affects:** Architecture, Flows, Contracts (G1), Interfaces, Dependencies, Modules.

### D-003 — Can subjective time / diagnostics feed back into the loop?
- **Date:** 2026-06-15 · **Decided by:** both · **Status:** active · **Depends on:** D-002
- **Decision:** No. Subjective time, diagnostics, and metastability monitors are
  **terminal sinks** — read by nothing in the cognitive/governance loop.
- **Alternatives:** Let time-dilation or coherence metrics modulate cognition
  directly (rejected — creates a hidden feedback loop that's near-impossible to
  reason about and silently destabilizes the field).
- **Reason:** Observability must not become control. Keeping these one-way makes
  the loop's behavior tractable and regression-testable.
- **Affects:** Architecture (boundaries), Flows, Contracts (G4), Dependencies.

### D-004 — How does a value become CORE: declared or earned?
- **Date:** 2026-06-15 · **Decided by:** both · **Status:** active · **Depends on:** D-002
- **Decision:** Values emerge from sustained experience and are promoted to CORE
  only via a governance review — never written directly.
- **Alternatives:** Hard-code core values (rejected — then they aren't *emergent*,
  and the system can't grow its own).
- **Reason:** Earned values are defensible against manipulation; declared ones
  are an attack surface.
- **Affects:** Flows, Contracts (G5), Modules (ValueEmergence ↔ Governance).

### D-005 — Bounded vs unbounded state in a forever-loop?
- **Date:** 2026-06-15 · **Decided by:** both · **Status:** active · **Depends on:** —
- **Decision:** All rolling history is bounded (caps / fixed-size buffers).
- **Alternatives:** Unbounded logs/lists (rejected — a loop that runs forever
  with unbounded state has an unbounded memory leak by construction).
- **Reason:** Persistence is the point of this skeleton; bounded state is what
  makes "runs forever" actually true.
- **Affects:** Contracts (G3), Dependencies.
