# ⚙️ PIPELINE — The Architecture Generation Build Order

> Every system built from this repo is created by walking the **same
> deterministic sequence**. This is what makes the repo a *machine for
> generating architectures* rather than a pile of documentation. An
> intelligent entity handed a skeleton + a goal can follow this order
> step by step.

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
