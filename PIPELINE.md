# ⚙️ PIPELINE — fill order

Load order lives only in [`SELECTOR.md`](SELECTOR.md) Step D.

**Construction is sequential. Decision capture is continuous and selective.**
Scope is defined only in [`SCHEMA.md`](SCHEMA.md). DecisionLog is not a late
pipeline step and not an activity journal.

---

## Rules

0. SELECTOR first. You choose class and depth. Human may override later.
1. Instantiate all 10 stubs + `INTENT.md`.
2. Fill sequential artifacts in the order below. Never reorder. Stop at depth.
3. When a decision is consequential, log it as it happens. Git handles the rest.
4. Behaviorally significant decisions and non-trivial behavior must be traceable
   to a note this depth required. Ordinary glue does not.
5. Self-audit. Attempt a smoke test. State whether it ran.

`depends_on` meaning is only in `SCHEMA.md`.

---

## Sequential fill order

```
Architecture → Flows → Contracts → Types → Schemas
         → Interfaces → Modules → Dependencies → README

DecisionLog ── continuous + selective ──
```

README at `thin` depth depends only on Architecture, Flows, Contracts.

---

## Self-audit

- [ ] Intent Card: class, depth, reasons (your judgment).
- [ ] Structurally valid.
- [ ] Depth-complete. No required artifact still blocked by a stub it depends on.
- [ ] Consequential decisions made during the work are in DecisionLog. The log is not a diary of edits.
- [ ] Chosen stack, if any, is logged and was shown.
- [ ] Smoke test ran, or inability to run is stated. No implied success.
