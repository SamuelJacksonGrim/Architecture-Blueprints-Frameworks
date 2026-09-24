# ⚙️ PIPELINE — The Architecture Generation Build Order

> Every system built from this repo is created by walking the **same
> deterministic sequence**. An intelligent entity handed a skeleton + a goal
> follows this order step by step.

---

## 🚫 NON-NEGOTIABLE RULES (read first, every time)

Compressing or reordering the process is a failure. Filling every artifact to
`complete` when SELECTOR picked `thin` is also a failure.

0. **Read `SELECTOR.md` first.** Class and depth are independent axes. Fill the
   Intent Card, including the selector decision block. (`DecisionLog` D-002, D-004.)
1. **Create all 10 artifact files as stubs BEFORE writing any content**, plus
   `INTENT.md`. That is **structurally valid** (`SCHEMA.md`).
2. **Follow the exact order below for whatever you fill. Never reorder.**
   Stop filling when the chosen depth is satisfied. Jumping ahead of a `stub`
   dependency is not allowed. Starting the next artifact while a dependency is
   `partial` is allowed. See the **Dependency rule** in `SCHEMA.md` — do not
   invent a second meaning here.
3. **Log every non-obvious decision** in `DecisionLog.md` with a `D-XXX` id.
4. **Never write code you can't trace to a design note this depth required.**
5. **Run the self-audit before declaring the build done.** Depth-allowed stubs
   do not fail the build.

---

## The Build Order

```
0. Select                    ← class + depth + Intent Card (independent axes)
        ↓
1. Instantiate Artifact Set ← structurally valid: all 10 stubs exist
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
7. Interfaces
        ↓
8. Dependencies
        ↓
9. Modules
        ↓
10. README

   DecisionLog ── maintained continuously ──
```

---

## Why this order

Contracts come after Flows because a contract about undescribed behavior is a
slogan. `DecisionLog` D-001.

---

## Status progression

Each artifact: `stub → partial → complete`.

System-level states are defined in `SCHEMA.md`. Restated only so this file
cannot drift:

- **structurally valid** — all ten files exist
- **depth-complete** — every artifact this depth requires is `complete` (a *build* is done)
- **fully complete** — all ten `complete` (a *reusable skeleton*)

---

## Practical loop

1. Find the lowest-`order` artifact this depth still requires whose `status` is
   not `complete` and whose `depends_on` targets are at least `partial`.
2. Fill it. You may mark it `complete` only when those targets are themselves
   `complete` (SCHEMA dependency rule).
3. Log non-obvious choices.
4. Repeat until the build is depth-complete — or the human corrects you.

---

## Step 10 — Self-audit

- [ ] Intent Card exists. Class, depth, and structural reasons are recorded.
- [ ] Structurally valid: all 10 artifact files exist, valid frontmatter.
- [ ] Depth-complete: every artifact this depth requires is `complete`.
- [ ] Remaining artifacts are honestly `stub` or `partial`.
- [ ] No artifact is `complete` while a required `depends_on` target is `stub`.
- [ ] `depends_on` summary for each completed artifact.
- [ ] Non-obvious decisions have `D-XXX` entries.
- [ ] No untraceable code.
- [ ] Smoke test passed, or inability to run is stated plainly.
