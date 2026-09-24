# DecisionLog — this repository

---

### D-001 — Architecture before Flows before Contracts

**Chosen:** Architecture → Flows → Contracts.

---

### D-002 — Instantiation is total; completeness is tiered

**Chosen:** All ten files exist from minute zero. Depth decides which reach `complete`.

**Date:** 2026-09-24

---

### D-003 — Multi-model routing is an operator note, not the spine

**Chosen:** Optional `OPERATOR.md`.

**Date:** 2026-09-24

---

### D-004 — Class ≠ depth; implicit-decision test; one depends_on meaning

**Chosen:** Independent axes. Thinnest depth that makes unsafe-to-leave-implicit decisions explicit. `depends_on` defined only in SCHEMA. Three completeness states.

**Date:** 2026-09-24

---

### D-005 — Plug points, then modules, then edges; stacks may be chosen but not hidden

**Question:** Can Dependencies complete before Modules? Must the AI refuse to pick a stack?

**Chosen:** Fill order is Interfaces → Modules → Dependencies. You cannot forbid an import between modules you have not named. Templates and PIPELINE now match that graph.

Stack rule: if the human named none, pick the smallest that can smoke-test, log it, show it. Decide. Do not hide.

Load order lives only in SELECTOR Step D.

**Rejected:** PIPELINE saying Dependencies before Modules while `depends_on` required Modules first (full-depth builds were formally impossible). "Do not invent a stack" (collides with one-sentence generation).

**Date:** 2026-09-24
