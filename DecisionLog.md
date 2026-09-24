# DecisionLog — this repository

The repo eats its own dog food. Decisions about *the framework* live here.

---

### D-001 — Architecture before Flows before Contracts

**Question:** Should guarantees be written before behavior?

**Chosen:** Architecture → Flows → Contracts.

**Rejected:** Contracts-first (“define the laws, then the movie”).

**Why:** A contract about a behavior you have not described is a slogan.
Recorded in `PIPELINE.md`. Kept.

---

### D-002 — Instantiation is total; completeness is tiered

**Question:** Must every build fill all ten artifacts to `complete`?

**Chosen:** All ten files exist from minute zero. Depth (`thin` / `standard` /
`full`) decides which ones must reach `complete`. See `SELECTOR.md`.

**Rejected:** (a) skip creating files; (b) require all ten `complete` for a CLI.

**Why:** Auto-propagating a full cathedral for every application was the
original impulse and the original failure. Systems differ. The language stays
universal. The *volume* does not. Leaving Types `stub` at `thin` depth is
obedience to SELECTOR, not a skipped pipeline.

**Date:** 2026-09-24

---

### D-003 — Multi-model routing is an operator note, not the spine

**Question:** Should the repo require a Gemini → GPT → Copilot → Claude/Grok
assembly line?

**Chosen:** Optional `OPERATOR.md`. Seams (Intent, Shape, Invariants, Wiring)
are named. Vendor roster is a field note.

**Rejected:** Baking current model personalities into `PIPELINE.md`.

**Why:** Model strengths rot. The seams are the ten artifacts in work-order
clothes. A single model must still be able to finish a build.

**Date:** 2026-09-24
