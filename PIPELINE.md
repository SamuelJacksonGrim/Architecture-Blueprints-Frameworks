# PIPELINE — how to build

Default construction order:

```
Architecture → Flows → Contracts → Types → Schemas
         → Interfaces → Modules → Dependencies → implementation → verification
         → README

DecisionLog ── continuous + selective, any time ──
```

Follow that order. It is how the work is built, not a series of permission slips.

If later work shows an earlier artifact is wrong, revise it and continue.
That is construction. It is not a failed pipeline.

Do not stop after Architecture to ask if you may write Flows.
Do not stop after Contracts to ask if you may implement.
Finish the pass. Then expose the result and its evidence.

**Intent → autonomous construction → inspection / evidence → human decision.**

Not: intent → proposal → approval → next file → approval.

---

Human authority is persistent. It is not turn-by-turn supervision.
Freedom to execute the pass does not move final authority to you.

`depends_on` (SCHEMA) is when an artifact may be marked `complete`.
QUALITY-BAR is rigor of the result. Evidence supports claims and consequential
decisions. None of these are authorization to keep building.

README at `thin` depth depends only on Architecture, Flows, Contracts.
Load list for *reading this repo*: [`SELECTOR.md`](SELECTOR.md) Step D.
DecisionLog scope: [`SCHEMA.md`](SCHEMA.md).

---

## Done (once, at the end of the pass)

- Intent Card: class, depth, reasons.
- Structurally valid.
- Depth-complete.
- Consequential decisions in DecisionLog.
- Stack, if you chose one, logged and shown.
- Smoke test ran, or inability stated.

Do not emit this after each artifact.
