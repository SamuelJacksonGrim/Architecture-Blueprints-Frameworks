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

## Slices

If the whole intent cannot be built and verified in one pass, design all of it
(Architecture, Flows, Contracts cover the whole system). Then implement one
**end-to-end slice**: the smallest path a real user takes from start to finish
(for a store: list → buy → receive). Verify it, then take the next slice.
Shallow everywhere is worse than whole and working somewhere. Artifacts describe
the whole design, so they can be `complete` while later slices are unbuilt. The
README and the handover say which slices are built and which remain.

## The live boundary

Nothing leaves the workspace during the pass: no deploy, no DNS, no real
charge, no message to real people, no publishing, no writes to accounts or
services the human did not hand you for this task. Build and test against local
fakes. Outbound messages go to a local outbox file. Use a sandbox account only
if the human handed you one. Hand over the exact steps that would go live.
Going live is the human's decision.

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

- Intent Card: class, depth, exposure, implied counterparts, reasons.
- Every `include` built, or listed as not yet built. Every `exclude` has a reason.
- Structurally valid and depth-complete. Run `python tools/validate.py <project>`
  from this repo if Python is available; otherwise check SCHEMA.md by hand.
- Consequential decisions in DecisionLog. The handover lists consequential guesses first.
- Stack, if you chose one, logged and shown.
- Smoke test ran, or inability stated.
- Anything that grows without limit has a stated bound.

Do not emit this after each artifact.
