---
artifact: Modules
status: complete
order: 9
fills: "module list, ownership, responsibilities, boundaries"
depends_on: [Interfaces]
filled_by: both
last_decision: null
---

# Modules — Price-Aggregator Webscraper

> One module ≈ one source folder. This table drives `../ProjectStructure.md`.

| Module | Responsibility | Owns (boundary) | Implements interface |
|--------|----------------|-----------------|----------------------|
| frontier | Deduped URL queue | seen-set, queue | FrontierInterface |
| scheduler | Pick next URL; enforce politeness delay | rate-limit state | — |
| fetcher | HTTP GET, retries, robots.txt | all network I/O | FetcherInterface |
| parser | HTML → candidate records + links | site selectors | ParserInterface |
| normalizer | Clean/validate/dedup records | price/currency rules | NormalizerInterface |
| store | Persist records idempotently | the datastore | StoreInterface |
| pipeline | Drive the crawl loop end to end | control flow, budget | — |
| observability | Logs, metrics, crawl stats | telemetry | — |
