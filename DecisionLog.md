# DecisionLog — this repository

The repo eats its own dog food. Decisions about *the framework* live here.

---

### D-001 — Architecture before Flows before Contracts

**Question:** Should guarantees be written before behavior?

**Chosen:** Architecture → Flows → Contracts.

**Rejected:** Contracts-first.

**Why:** A contract about a behavior you have not described is a slogan.

---

### D-002 — Instantiation is total; completeness is tiered

**Question:** Must every build fill all ten artifacts to `complete`?

**Chosen:** All ten files exist from minute zero. Depth decides which reach
`complete`. See `SELECTOR.md` and the three states in `SCHEMA.md`.

**Rejected:** (a) skip creating files; (b) require all ten `complete` for a CLI.

**Date:** 2026-09-24

---

### D-003 — Multi-model routing is an operator note, not the spine

**Question:** Require a Gemini → GPT → Copilot → Claude/Grok line?

**Chosen:** Optional `OPERATOR.md`. Seams stay. Vendor roster is a field note.

**Date:** 2026-09-24

---

### D-004 — Class ≠ depth; implicit-decision test; one depends_on meaning

**Question:** Is depth a complexity score? When in doubt, go thinner?

**Chosen:**
- Class answers *what kind*. Depth answers *how much structure must be explicit*.
  Independent axes. No complexity score, no fourth depth.
- Governing test: the thinnest depth that can express every decision the system
  cannot safely leave implicit.
- `depends_on` meaning lives only in `SCHEMA.md`: partial-or-complete to *start*;
  not-stub before the dependent artifact may itself be `complete`.
- Completeness states: structurally valid / depth-complete / fully complete.

**Rejected:** "When in doubt, go thinner" as the governing rule (guards
overbuilding, under-guards implicit decisions in code).

**Date:** 2026-09-24
