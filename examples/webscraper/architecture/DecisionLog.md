---
artifact: DecisionLog
status: complete
order: 99
fills: "architectural memory — decisions, alternatives, reasons, dates"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Price-Aggregator Webscraper

### D-001 — Single fetcher owns all network I/O
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** Only the Fetcher touches the network; Parser/Store never do.
- **Alternatives:** Let parsers fetch sub-resources directly.
- **Reason:** Politeness (G1) and robots.txt are only enforceable if there's a
  single choke point for outbound requests.
- **Affects:** Architecture, Dependencies, Contracts (G1).

### D-002 — Normalizer is the trust gate before storage
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** No record reaches the Store without passing the Normalizer.
- **Alternatives:** Store raw and clean later.
- **Reason:** Guarantees G4/I3 and keeps the datastore free of garbage that
  breaks downstream price aggregation.
- **Affects:** Flows, Contracts (G4), Interfaces.

### D-003 — Bounded crawl via CRAWL_BUDGET + seen-set
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** A crawl stops at an empty Frontier or `CRAWL_BUDGET` pages, and
  never fetches a URL twice.
- **Alternatives:** Crawl until "done" (unbounded).
- **Reason:** Termination must be a guarantee (G2/I1/I2), not a hope — the web
  is effectively infinite.
- **Affects:** Flows, Contracts (G2), Types.
