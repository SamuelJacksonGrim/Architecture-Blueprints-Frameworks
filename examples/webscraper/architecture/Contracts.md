---
artifact: Contracts
status: complete
order: 4
fills: "guarantees, assumptions, invariants, pre/post-conditions"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-002
---

# Contracts — Price-Aggregator Webscraper

## Guarantees
- **G1 — Politeness.** The Fetcher respects `robots.txt` and a per-host rate
  limit. No host is hit faster than its configured delay.
- **G2 — Termination.** A crawl ends when the Frontier empties or
  `CRAWL_BUDGET` pages are fetched — never an unbounded crawl.
- **G3 — Idempotent storage.** Crawling the same product page twice updates one
  record; it never creates duplicates.
- **G4 — No bad data.** Only records that pass the Normalizer reach the Store.

## Assumptions
- **A1** — Target pages expose price + product info extractable via selectors.
- **A2** — Page layouts may change without warning (so parsing must fail soft).
- **A3** — Everything the Fetcher returns is untrusted until normalized.

## Invariants
- **I1** — `pages_fetched ≤ CRAWL_BUDGET`.
- **I2** — A URL is fetched at most once per crawl (the `seen` set).
- **I3** — Every stored record has a non-null product id and a valid price.

## Pre/Post-Conditions
| Operation | Pre | Post |
|-----------|-----|------|
| `fetcher.get` | url allowed by robots, politeness slot available | returns Response (ok or error), never throws |
| `parser.parse` | response ok | returns `(records, links)`; `[]` on layout miss |
| `normalizer.normalize` | candidate record | returns valid record or marks invalid |
| `store.upsert` | record valid | exactly one record per product id |
