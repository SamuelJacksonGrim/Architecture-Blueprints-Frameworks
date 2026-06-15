---
artifact: README
status: complete
order: 10
fills: "front door — what/why/problem/components for the instantiated system"
depends_on: [Architecture, Flows, Contracts, Modules]
filled_by: both
last_decision: null
---

# Price-Aggregator Webscraper

> The design front door. (The project-level README is one level up.)

## What is this?
A polite, bounded webscraper that crawls product pages, extracts and normalizes
prices, and stores them for downstream aggregation.

## Why does it exist?
To keep a fresh, deduplicated view of product prices across sites without
hammering them or storing garbage.

## What problem does it solve?
Manual price checking doesn't scale; naive scrapers get blocked, loop forever,
or fill the DB with malformed data. This design bakes in politeness,
termination, idempotent storage, and a validation gate from day one.

## Major components
Frontier · Scheduler · Fetcher · Parser · Normalizer · Store · Pipeline ·
Observability. See [`Architecture.md`](Architecture.md) and [`Modules.md`](Modules.md).

## Artifact status
| Artifact | Status |
|----------|--------|
| Architecture | complete |
| Flows | complete |
| Contracts | complete |
| Types | complete |
| Schemas | complete |
| Interfaces | complete |
| Dependencies | complete |
| Modules | complete |
| DecisionLog | complete |
| README | complete |
