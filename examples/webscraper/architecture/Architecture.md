---
artifact: Architecture
status: complete
order: 2
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []
filled_by: both
last_decision: D-001
---

# Architecture — Price-Aggregator Webscraper

> Generated from the idea: *"a webscraper that aggregates product prices."*
> This is the design layer; the source tree it implies is in
> [`../ProjectStructure.md`](../ProjectStructure.md).

## Purpose
Given a set of seed product pages, fetch them politely, extract price + product
data, normalize it, store it, and discover more product links to crawl — on a
schedule — so a downstream consumer always has fresh aggregated prices.

## Major Subsystems
- **Frontier** — the queue of URLs still to crawl (seeded + discovered).
- **Scheduler** — decides what to fetch next and when (politeness/rate limits).
- **Fetcher** — performs HTTP requests; handles retries, timeouts, robots.txt.
- **Parser** — turns raw HTML into candidate records via selectors.
- **Normalizer** — cleans/validates records (currency, price format, dedup).
- **Store** — persists normalized records + crawl bookkeeping.
- **LinkDiscovery** — pulls new product links out of parsed pages → Frontier.
- **Pipeline** — orchestrates the flow end to end.
- **Observability** — logs, metrics, crawl stats.

## Boundaries
- **Inside:** Frontier, Scheduler, Parser, Normalizer, Store, Pipeline.
- **Outside (untrusted):** the target websites. Everything the Fetcher returns
  is untrusted input until the Normalizer validates it.
- **Process line:** the Fetcher is the only component that talks to the network.

## Data Flow
```
seeds ─▶ Frontier ─▶ Scheduler ─▶ Fetcher ─▶ raw HTML
                          ▲                       │
                          │                       ▼
                   LinkDiscovery ◀── Parser ──▶ candidate records
                                                  │
                                                  ▼
                                            Normalizer ─▶ Store
```

## Control Flow
The Pipeline drives the loop: pull from Frontier → fetch → parse → (discover
links back to Frontier) → normalize → store → repeat until the Frontier is empty
or a crawl budget is hit.

## High-Level Diagram
See [`diagrams/system_flow.md`](diagrams/system_flow.md).
