---
artifact: Dependencies
status: complete
order: 8
fills: "allowed/forbidden dependency directions, hierarchy, import rules"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: null
---

# Dependencies — Price-Aggregator Webscraper

## Module Hierarchy (top = depended-upon)
```
Types / Schemas                       (pure vocabulary)
        ▲
Interfaces                            (depend only on Types/Schemas)
        ▲
Fetcher · Parser · Normalizer · Store · Frontier · Scheduler   (implementations)
        ▲
Pipeline                              (orchestrates via Interfaces only)
        ▲
Observability (cross-cutting; may read all, write none)
```

## Allowed Directions
- Any module → Types/Schemas.
- Implementations → the Interface they implement.
- Pipeline → Interfaces (never concrete implementations).

## Forbidden Directions
- **Parser ⇏ Fetcher.** The Parser receives a Response; it must not fetch on its
  own (keeps all network I/O in one place — enforces G1).
- **Store ⇏ Fetcher/Parser.** Storage is a leaf; it can't trigger crawling.
- **No cycles.**

## Import Rules
- Depend on interfaces, not implementations, so the Fetcher (HTTP vs headless
  browser), Parser (per site), and Store (file vs DB) are all swappable.
