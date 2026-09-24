---
artifact: DecisionLog
status: stub
order: 99
fills: "architectural memory — consequential decisions, not every change"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — *the architectural memory*

> Why the architecture became what it is. Git records what changed.
> Scope is [`SCHEMA.md`](../SCHEMA.md): continuous and selective.

## Habits
- **Append-only. Supersede, never rewrite.**
- **Title the question, not the verdict.**
- **Skip ordinary work.** A rename, a null check, a typo, a local refactor — no entry.

## Status values
`active` · `superseded by D-NNN` · `reversed by D-NNN`

## Entry format

```
### D-NNN — <title phrased as the question>
- **Date:** YYYY-MM-DD
- **Decided by:** <human / AI / both>
- **Status:** active | superseded by D-NNN | reversed by D-NNN
- **Decision:** <what was chosen>
- **Alternatives:** <what was rejected, and the trade-off>
- **Reason:** <why>
- **Affects:** <artifacts/modules>
```

---

### D-001 — Build order: Flows before Contracts?
- **Date:** <fill on instantiation>
- **Decided by:** both
- **Status:** active
- **Decision:** Build order is Architecture → Flows → Contracts.
- **Alternatives:** Contracts before Flows (rejected).
- **Reason:** A contract constrains a behavior; you can't write a meaningful
  guarantee for a flow you haven't described yet. Inherited from `PIPELINE.md`.
- **Affects:** Flows, Contracts, build pipeline.
