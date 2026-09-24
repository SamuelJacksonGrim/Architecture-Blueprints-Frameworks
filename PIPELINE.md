# ⚙️ PIPELINE — The Architecture Generation Build Order

> Walk this sequence. Loading order (what to read first) lives only in
> [`SELECTOR.md`](SELECTOR.md) Step D. This file is fill order, not load order.

---

## 🚫 NON-NEGOTIABLE RULES

0. **Read `SELECTOR.md` first** — including its load list. Class and depth are
   independent. Fill the Intent Card. (`DecisionLog` D-002, D-004, D-005.)
1. **Instantiate all 10 stubs + `INTENT.md`.** Structurally valid (`SCHEMA.md`).
2. **Fill in the order below. Never reorder.** Stop when depth is satisfied.
   Dependency meaning is only in `SCHEMA.md`.
3. **Log non-obvious decisions**, including any stack the human did not name.
4. **No code you cannot trace** to a note this depth required.
5. **Self-audit before "done."** Depth-allowed stubs do not fail the build.

---

## The Build Order

```
0. Select                    ← class + depth + Intent Card
        ↓
1. Instantiate               ← structurally valid
        ↓
2. Architecture
        ↓
3. Flows
        ↓
4. Contracts
        ↓
5. Types
        ↓
6. Schemas
        ↓
7. Interfaces                ← plug points
        ↓
8. Modules                   ← named pieces that implement those plugs
        ↓
9. Dependencies              ← allowed/forbidden edges *between those modules*
        ↓
10. README

   DecisionLog ── continuous ──
```

You cannot forbid an import between modules you have not named. That is D-005.

---

## Status progression

Defined in `SCHEMA.md`: structurally valid → depth-complete → fully complete.

---

## Practical loop

1. Lowest-`order` artifact this depth still requires, whose `depends_on` targets
   are at least `partial`.
2. Mark it `complete` only when those targets are themselves `complete`.
3. Log choices, including implementation stack if you had to pick one.
4. Stop at depth-complete.

---

## Step 10 — Self-audit

- [ ] Intent Card: class, depth, structural reasons.
- [ ] Structurally valid.
- [ ] Depth-complete.
- [ ] Remaining artifacts honestly `stub`/`partial`.
- [ ] No `complete` artifact while a required `depends_on` is `stub`.
- [ ] Any chosen stack is in DecisionLog and was shown to the human.
- [ ] Smoke test passed, or inability to run is stated plainly.
