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
>
> Treat this as an **empirical ledger**, not a changelog — see `QUALITY-BAR.md`
> §7. The disciplines below are why it stays trustworthy across handoffs.

## Discipline (non-negotiable)
- **Append-only. Supersede, never rewrite.** When a later decision overturns an
  earlier one, add a new entry and set the old one's `Status` — the overturning
  *is* the record.
- **Title the question, not the verdict.** "Auth: sessions vs tokens?" survives
  a reversal; "Use tokens" becomes a lie the moment you switch.
- **Negative results count.** "Tried X, it failed because Y" is often the most
  time-saving entry there is.
- **Separate observation from interpretation** — facts survive, explanations age.

## Status values
`active` · `superseded by D-NNN` · `invalidated by D-NNN` · `partial / blocked`

## Entry format

```
### D-NNN — <title phrased as the question/investigation, not a conclusion>
- **Date:** YYYY-MM-DD
- **Decided by:** <human / entity / both>
- **Status:** active | superseded by D-NNN | invalidated by D-NNN | partial
- **Depends on:** <D-NNN, …>   (which earlier decisions this rests on)
- **Decision:** <what was chosen>
- **Alternatives:** <what was rejected, and the trade-off>
- **Reason:** <why — the basis, not just the verdict>
- **Affects:** <artifacts/modules>
```

---

### D-001 — Build order: Flows before Contracts?
- **Date:** <fill on instantiation>
- **Decided by:** both
- **Status:** active
- **Depends on:** —
- **Decision:** Build order is Architecture → Flows → Contracts.
- **Alternatives:** Contracts before Flows (rejected).
- **Reason:** A contract constrains a behavior; you cannot write a meaningful
  guarantee for a flow you have not yet described. Inherited from the repo's
  `PIPELINE.md`.
- **Affects:** Flows, Contracts, build pipeline.
