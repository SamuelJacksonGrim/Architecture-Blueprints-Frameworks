# DecisionLog — this repository

---

### D-001 — Construction order: Architecture → Flows → Contracts
### D-002 — Instantiation total; completeness tiered
### D-003 — OPERATOR is optional
### D-004 — Class ≠ depth; implicit-decision test
### D-005 — Interfaces → Modules → Dependencies as completeness edges
### D-006 — Authority is not authorship
### D-007 — Planned catalog is forged, not sketched
### D-008 — One agent brief, many loaders
### D-009 — Cognitive-cycle is a class, not a difficulty setting
### D-010 — Continuous does not mean exhaustive
### D-011 — Artifacts are not permission checkpoints

---

### D-012 — Authority is inspection of the pass

**Question:** Did removing the permission-queue also remove the construction order?

**Chosen:** Restore the order. It is how to build. Human authority is the right
to accept, reject, modify, or redirect *the finished pass*. It is not a signature
required between artifacts. Revising an earlier artifact mid-pass is construction.

**Intent → autonomous construction → inspection / evidence → human decision.**

**Rejected:** Asking "is this architecture okay?" before Flows. Treating D-011 as
"there is no order." Transferring final authority to the AI because it finished.

**Date:** 2026-09-26

---

### D-013 — Must Interfaces wait on Schemas at standard depth?

**Question:** `standard` requires Interfaces `complete` and leaves Schemas
optional. Every Interfaces file had `depends_on: [Schemas]`, which broke depth
self-consistency. Every standard-depth build hit it. No full-depth skeleton
showed it.

**Chosen:** Interfaces `depends_on: [Types, Contracts]` in templates, all
skeletons, and the example. The operations and guarantees an interface names
come from Types and Contracts. Schemas is the cross-system ontology, and
nothing plugs into it. Also, `SCHEMA.md`: an inherited edge to an artifact the
depth leaves optional does not gate completeness. So the next template that
makes the same mistake resolves itself, and it does not stall the build or
push depth up without anyone saying so.

**Rejected:** Requiring Schemas at standard (that is `full` under another
name). Leaving each builder to resolve it (the outcome then depends on which
entity builds, and a careless one misses the conflict). Changing construction
order (PIPELINE is unchanged: Schemas is still built before Interfaces when it
is built).

**Found by:** a standard-depth build (Resonance Journal, its D-007).

**Date:** 2026-09-26
