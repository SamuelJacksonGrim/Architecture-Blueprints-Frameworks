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

> A plain record of the choices that shaped the build, so nobody re-litigates
> them later. Maintained as you go, not in one pass. Reference entries by id
> (e.g. `D-002`) from an artifact's `last_decision` field.

## A couple of habits that keep it useful
- **Append-only. Supersede, never rewrite.** If a later choice overturns an
  earlier one, add a new entry and mark the old one's `Status`. The change of
  mind is part of the record.
- **Title the question, not the verdict.** "Auth: sessions vs tokens?" still
  makes sense after a reversal; "Use tokens" becomes a lie the moment you switch.

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
