# System Flow — Price-Aggregator Webscraper

```
seeds ─▶ FRONTIER ◀───────────────── new links ◀──┐
            │                                       │
            ▼                                       │
        SCHEDULER (politeness delay)                │
            │                                       │
            ▼                                       │
         FETCHER ── ok? ──no──▶ retry/backoff ──▶ drop+log
            │ yes                                   │
            ▼                                       │
         PARSER ──▶ links ───────────────────────-─┘
            │
            ▼ records
        NORMALIZER ── valid? ──no──▶ reject+log
            │ yes
            ▼
          STORE (idempotent upsert)

   stop when: FRONTIER empty  OR  pages_fetched ≥ CRAWL_BUDGET
```
