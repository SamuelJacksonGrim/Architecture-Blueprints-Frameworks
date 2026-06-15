---
artifact: Interfaces
status: complete
order: 7
fills: "plug points — the contracts between modules that make them swappable"
depends_on: [Schemas]
filled_by: both
last_decision: null
---

# Interfaces — Price-Aggregator Webscraper

> Each interface is a swap point. Want a headless-browser fetcher instead of
> plain HTTP? Implement `FetcherInterface` and nothing else changes.

### FetcherInterface
- **Purpose:** fetch a URL politely.
- **Inputs:** `get(request: CrawlRequest)`
- **Outputs:** `Response` (never throws)
- **Upholds:** G1 (politeness), A3 (returns untrusted data).
- **Implemented by:** Fetcher · **Consumed by:** Pipeline

### ParserInterface
- **Purpose:** extract records + links from HTML.
- **Inputs:** `parse(response: Response)`
- **Outputs:** `(CandidateRecord[], LinkSet)` — `([], [])` on layout miss
- **Upholds:** A2 (fails soft).
- **Implemented by:** site-specific parsers · **Consumed by:** Pipeline

### NormalizerInterface
- **Purpose:** clean + validate a candidate into a ProductRecord.
- **Inputs:** `normalize(candidate: CandidateRecord)`
- **Outputs:** `ProductRecord | invalid`
- **Upholds:** G4, I3 (the trust gate).
- **Implemented by:** Normalizer · **Consumed by:** Pipeline

### StoreInterface
- **Purpose:** persist records idempotently.
- **Inputs:** `upsert(record: ProductRecord)`, `get(productId)`
- **Outputs:** ack / record
- **Upholds:** G3 (idempotent), I2/I3.
- **Implemented by:** Store (DB/file) · **Consumed by:** Pipeline

### FrontierInterface
- **Purpose:** the crawl queue with dedup.
- **Inputs:** `seed(urls)`, `add(urls)`, `next()`
- **Outputs:** `CrawlRequest`
- **Upholds:** I2.
- **Implemented by:** Frontier · **Consumed by:** Scheduler, Pipeline
