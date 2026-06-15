---
artifact: Types
status: complete
order: 5
fills: "core domain types, primitives, enums, identifiers, structural schemas"
depends_on: [Contracts]
filled_by: both
last_decision: null
---

# Types — Price-Aggregator Webscraper

## Core Domain Types
- **Url** — `{ raw: string, host: string }`
- **CrawlRequest** — `{ url: Url, depth: int, attempt: int }`
- **Response** — `{ url: Url, status: int, ok: bool, html?: string, error?: string }`
- **CandidateRecord** — raw extracted fields `{ title?, priceText?, sku?, … }`
- **ProductRecord** — `{ productId: ProductId, title, price: Money, url: Url, scrapedAt }`
- **Money** — `{ amount: decimal, currency: CurrencyCode }`
- **LinkSet** — `Url[]` discovered on a page

## Primitives & Identifiers
- `ProductId` — stable id derived from sku/url (the dedup key, see I3).
- `CurrencyCode` — ISO-4217 (e.g. `USD`).
- `scrapedAt` — ISO-8601 timestamp.

## Enums
- **FetchStatus** = `ok | retryable_error | blocked_robots | dead`
- **RecordStatus** = `valid | invalid_price | missing_field | duplicate`

## Structural Schemas
- **Frontier** = a deduped queue of `CrawlRequest`.
- **Crawl bookkeeping** = `{ seen: Set<Url>, pagesFetched: int }`.
