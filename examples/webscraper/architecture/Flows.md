---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — request, event, execution, error, state-update flows"
depends_on: [Architecture]
filled_by: both
last_decision: D-002
---

# Flows — Price-Aggregator Webscraper

## Crawl Flow (the core loop)
```
frontier.seed(seed_urls)
loop (until frontier empty OR pages_fetched >= CRAWL_BUDGET):
    url   = scheduler.next(frontier)          # respects per-host politeness delay
    if seen(url): continue                    # dedup
    resp  = fetcher.get(url)                   # retries, timeout, robots.txt check
    mark_seen(url)
    if not resp.ok: handle_error(url, resp); continue
    records, links = parser.parse(resp)
    frontier.add(filter_new(links))            # link discovery
    for r in records:
        clean = normalizer.normalize(r)
        if clean.valid: store.upsert(clean)    # idempotent write
```

## Request Flow (single URL)
resolve host → check robots.txt (cached) → wait for politeness slot →
GET with timeout → on 429/5xx retry with backoff → return Response.

## Event Flow
The recurring event is a fetched **Response**. It fans out into extracted
**records** (→ Normalizer → Store) and discovered **links** (→ Frontier).

## Error Flow
- **Network error / timeout:** retry up to `MAX_RETRIES` with exponential
  backoff; then drop the URL and log it.
- **Blocked by robots.txt:** skip the URL, record `skipped_robots`.
- **Parse failure (page layout changed):** emit zero records, log `parse_miss`;
  never crash the crawl.
- **Invalid record:** Normalizer rejects it; it is *not* written to the Store.

## State-Update Flow
- `seen` set + Frontier update every iteration.
- Store writes are **idempotent upserts** keyed by product id, so re-crawling
  the same page updates the price rather than duplicating it.
