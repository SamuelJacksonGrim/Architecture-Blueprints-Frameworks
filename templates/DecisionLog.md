---
artifact: DecisionLog
status: stub
order: 99
fills: "architectural memory — decisions, alternatives, reasons, dates"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — *the architectural memory*

> Maintained **continuously**, not in a single pass. This is the artifact that
> lets different intelligences across time avoid re-litigating settled choices.
> Append entries; never rewrite history. Reference entries by id (e.g. `D-002`)
> from an artifact's `last_decision` field.

## Entry format

```
### D-NNN — <short title>
- **Date:** YYYY-MM-DD
- **Decided by:** <human / entity / both>
- **Decision:** <what was chosen>
- **Alternatives:** <what was rejected>
- **Reason:** <why>
- **Affects:** <artifacts/modules>
```

---

### D-001 — Flows before Contracts
- **Date:** <fill on instantiation>
- **Decided by:** both
- **Decision:** Build order is Architecture → Flows → Contracts.
- **Alternatives:** Contracts before Flows.
- **Reason:** A contract constrains a behavior; you cannot write a meaningful
  guarantee for a flow you have not yet described. Inherited from the repo's
  `PIPELINE.md`.
- **Affects:** Flows, Contracts, build pipeline.
