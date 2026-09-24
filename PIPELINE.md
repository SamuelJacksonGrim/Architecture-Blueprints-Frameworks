# ⚙️ PIPELINE — The Architecture Generation Build Order

> Every system built from this repo is created by walking the **same
> deterministic sequence**. This is what makes the repo a *machine for
> generating architectures* rather than a pile of documentation. An
> intelligent entity handed a skeleton + a goal can follow this order
> step by step.

---

## 🚫 NON-NEGOTIABLE RULES (read first, every time)

These are not suggestions. If you are an AI building from this repo, you follow
them exactly. Compressing or reordering the process is a failure, not initiative.
Filling every artifact to `complete` when SELECTOR picked `thin` is also a failure.

0. **Read `SELECTOR.md` first.** Classify the request, pick a depth
   (`thin` / `standard` / `full`), fill the Intent Card. That decision is
   logged (`D-002` in this repo's `DecisionLog.md`).
1. **Create all 10 artifact files as stubs BEFORE writing any content**, plus
   `INTENT.md`. The structure exists in full from moment zero. (See the
   Instantiation Rule in `SCHEMA.md`.)
2. **Follow the exact order below for whatever you fill. Never reorder.**
   You may stop filling when the chosen depth says stop — leaving later
   artifacts `stub` at `thin` or `standard` depth is correct. Jumping *ahead*
   of an unfilled dependency is not.
3. **Log every non-obvious decision** in `DecisionLog.md` with a `D-XXX` id, and
   reference it from the artifact's `last_decision` frontmatter field.
4. **Never write code you can't trace to a design note.** If something isn't
   pinned down in an artifact your depth requires, fix the artifact first —
   don't improvise in code.
5. **Run the self-audit (Step 10 below) before declaring the build done.** No
   "looks good" without it. The audit is depth-aware: stubs allowed by
   SELECTOR do not fail the build.

---

## The Build Order

```
0. Select                    ← SELECTOR.md: class + depth + Intent Card
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

This is recorded as decision **D-001** in this repo's `DecisionLog.md`.

---

## Status progression

Each artifact moves through `stub → partial → complete` (the `status` field
in its frontmatter).

- A skeleton is **valid** the moment it is instantiated (all 10 stubs exist).
- A *reusable skeleton* is **complete** when every artifact reads `status: complete` (full depth).
- A *build* is **done** when every artifact required by its SELECTOR depth is `complete`,
  and the rest are honestly still `stub` or `partial`.
- You may stop at `partial` anywhere the depth allows — the structure must stay intact.
  That is the Instantiation Rule from `SCHEMA.md`, plus D-002.

---

## Practical loop for an intelligent entity

When collaborating on a fill:

1. Read the skeleton's frontmatter to find the lowest-`order` artifact whose
   `status` is not `complete`, whose `depends_on` are satisfied, and that this
   depth still requires.
2. Fill it. Update its `status`.
3. If you made a non-obvious choice, append an entry to `DecisionLog.md` and
   set the artifact's `last_decision`.
4. Repeat until the depth is satisfied — or until the human points out a little
   thing that's wrong.

---

## Step 10 — Self-audit (mandatory before "done")

Before telling the human it's built, output this checklist filled in. If any box
can't be ticked, the build is **not** done — go fix it.

- [ ] Intent Card exists (`INTENT.md`). Class and depth are named.
- [ ] All 10 artifact files exist (stubs count).
- [ ] Every artifact has valid frontmatter (`artifact`, `status`, `order`).
- [ ] Every artifact required by the chosen depth is `complete`.
- [ ] Artifacts allowed to remain `stub`/`partial` at this depth are marked honestly.
- [ ] No artifact is `complete` while something in its `depends_on` that *this depth requires* is still `stub`.
- [ ] **`depends_on` satisfaction summary** — for each *completed* artifact, one line stating which prior artifact(s) it built on.
- [ ] Every non-obvious decision has a `D-XXX` entry, referenced by `last_decision`.
- [ ] No code exists that can't be traced to a design note this depth required.
- [ ] **It runs.** A smoke test of the main path passed — or, if the environment can't run it, that's stated plainly. (QUALITY-BAR §9.)

This step is what stops a model from quietly skipping the process *or* padding it.
