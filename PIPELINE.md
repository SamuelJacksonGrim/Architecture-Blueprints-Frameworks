# ⚙️ PIPELINE — The Architecture Generation Build Order

> Every system built from this repo is created by walking the **same
> deterministic sequence**. This is what makes the repo a *machine for
> generating architectures* rather than a pile of documentation. An
> intelligent entity handed a skeleton + a goal can follow this order
> step by step.

---

## 🚫 NON-NEGOTIABLE RULES (read first, every time)

These are not suggestions. If you are an AI building from this repo, you follow
them exactly. Compressing, reordering, or "improving" the process is a failure,
not initiative.

1. **Create all 10 artifact files as stubs BEFORE writing any content.** The
   structure exists in full from moment zero. (See the Instantiation Rule in
   `SCHEMA.md`.)
2. **Follow the exact order below. Never skip or reorder.** Each artifact
   depends on the ones before it; jumping ahead produces drift.
3. **Log every non-obvious decision** in `DecisionLog.md` with a `D-XXX` id, and
   reference it from the artifact's `last_decision` frontmatter field.
4. **Never write code you can't trace to a design note.** If something isn't
   pinned down in an artifact yet, fix the artifact first — don't improvise in
   code. (That's the line between this and vibe-coding.)
5. **Run the self-audit (Step 10 below) before declaring the build done.** No
   "looks good" without it.

---

## The Build Order

```
0. Select Skeleton          ← pick the closest pattern from /skeletons
        ↓
1. Instantiate Artifact Set ← copy the skeleton; all 10 stubs now exist
        ↓
2. Architecture             ← draw the city map first
        ↓
3. Flows                    ← describe behavior over that structure
        ↓
4. Contracts                ← lock guarantees onto the flows
        ↓
5. Types                    ← name the vocabulary the contracts use
        ↓
6. Schemas                  ← generalize the types into ontology
        ↓
7. Interfaces               ← define the plug points between modules
        ↓
8. Dependencies             ← lock allowed/forbidden import directions
        ↓
9. Modules                  ← decompose and assign ownership
        ↓
10. README                  ← write the front door last, once it's true

   DecisionLog ── maintained continuously throughout every step above ──
```

---

## Why this order (and why it differs from the naive one)

A tempting ordering puts **Contracts before Flows** ("define guarantees, then
behavior"). We rejected that. You cannot write a meaningful contract for a
behavior you have not yet described — the invariants are *about* the flows.
So: **Architecture → Flows → Contracts**, matching the artifact stack in
`SCHEMA.md`.

This is recorded as decision **D-001** in every skeleton's `DecisionLog.md`,
and the repo eats its own dog food: when we changed the order, we logged *why*
instead of silently flip-flopping it.

---

## Status progression

Each artifact moves through `stub → partial → complete` (the `status` field
in its frontmatter).

- A skeleton is **valid** the moment it is instantiated (all 10 stubs exist).
- A skeleton is **complete** when every artifact reads `status: complete`.
- You may stop at `partial` anywhere — the structure must stay intact, but the
  content can lag the design. That is the **Instantiation Rule** from
  `SCHEMA.md`.

---

## Practical loop for an intelligent entity

When collaborating on a fill:

1. Read the skeleton's frontmatter to find the lowest-`order` artifact whose
   `status` is not `complete` and whose `depends_on` are satisfied.
2. Fill it. Update its `status`.
3. If you made a non-obvious choice, append an entry to `DecisionLog.md` and
   set the artifact's `last_decision`.
4. Repeat until the system is complete — or until the human points out a little
   thing that's wrong. 🙂

---

## Step 10 — Self-audit (mandatory before "done")

Before telling the human it's built, output this checklist filled in. If any box
can't be ticked, the build is **not** done — go fix it.

- [ ] All 10 artifact files exist.
- [ ] Every artifact has valid frontmatter (`artifact`, `status`, `order`).
- [ ] No artifact is `complete` while something in its `depends_on` is still `stub`.
- [ ] **`depends_on` satisfaction summary** — for each artifact, one line stating
      which prior artifact(s) it built on and that they were in place first.
      Example: *"Contracts ← built on Architecture + Flows (both complete). ✅"*
- [ ] Every non-obvious decision has a `D-XXX` entry, referenced by `last_decision`.
- [ ] No code exists that can't be traced to a design note.

This step is what stops a model from quietly skipping or compressing the process.
