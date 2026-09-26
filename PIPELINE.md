# PIPELINE — completeness graph, not a thinking order

The filename is historical. This file is **not** a procedure the intelligence
must walk. It is the graph that says when an artifact may be marked `complete`.

Load order for *reading this repo* lives only in [`SELECTOR.md`](SELECTOR.md).
`depends_on` meaning lives only in [`SCHEMA.md`](SCHEMA.md).

The blueprint describes the space in which intelligence can reason.
It does not dictate the path intelligence must take through that space.

---

## Distinctions (do not collapse them)

| This | is not this |
|---|---|
| documentation | procedure |
| evidence | permission |
| validation | authorization |
| traceability | step-by-step supervision |
| inspectability | serialized cognition |
| structured reasoning | constrained reasoning |
| reproducibility | forced intermediate emissions |
| cognitive work | observable output |

One reasoning pass may touch every artifact. That is not a workflow violation.
Revising an earlier artifact because later work exposed a better model is reasoning.
Skipping an artifact this depth does not require is correct, not incomplete.
Emitting a receipt after every thought is a token tax. Do not pay it.

---

## What still binds

- Class and depth (SELECTOR). Depth decides which artifacts must end `complete`.
- `depends_on` is a **completeness predicate**: an artifact may not be marked
  `complete` while a required dependency is still `stub`. It does not require
  you to think, draft, or emit in that order.
- Consequential decisions are logged when they happen (SCHEMA scope). Git for the rest.
- Behaviorally significant decisions at this depth must be traceable in the
  *persisted* design — not narrated turn-by-turn.
- Attempt a smoke test, or say you could not. That is output, not a mid-thought gate.

---

## The graph

Useful default for *settling* completeness — not a required traversal:

```
Architecture ↔ Flows ↔ Contracts ↔ Types ↔ Schemas
         ↔ Interfaces ↔ Modules ↔ Dependencies ↔ README

DecisionLog ── continuous + selective, any time ──
```

`order` in frontmatter is a reading hint. It is not a queue.

You may draft Dependencies while naming Modules. You may discover the
architecture from a flow. You may hold competing architectures. You may
change your mind. You may not mark Dependencies `complete` while Modules
is still `stub` — the names have to exist for the edges to be real.

README at `thin` depth depends only on Architecture, Flows, Contracts.

---

## Done (output, once)

- Intent Card: class, depth, reasons.
- Structurally valid (the ten files exist as handles).
- Depth-complete: required artifacts `complete`; unused ones honestly stub/partial.
- Consequential decisions in DecisionLog. Not a diary.
- Stack, if you chose one, logged and shown.
- Smoke test ran, or inability stated. No implied success.

Do not emit this checklist after each artifact. Emit the result.
