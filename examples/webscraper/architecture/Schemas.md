---
artifact: Schemas
status: complete
order: 6
fills: "conceptual ontology — Entity→State→Event→Evaluation→Decision→Action"
depends_on: [Types]
filled_by: both
last_decision: null
---

# Schemas — Price-Aggregator Webscraper

## Core Transformation Chain
How a webscraper maps onto the repo's universal ontology — note it's the *same*
chain as an agent, just with different nouns (that's the comparability payoff):

```
Entity      = a web page (a crawl target)
   ↓
State       = the Frontier + seen-set + stored records
   ↓
Event       = a fetched Response
   ↓
Evaluation  = Normalizer: is this record valid? is this link worth following?
   ↓
Decision    = store / skip the record; enqueue / drop the link
   ↓
Action      = store.upsert(record) and frontier.add(links)
   ↺ (newly enqueued URLs become the next Entities)
```

## Information Schemas
Raw HTML → `CandidateRecord` (extraction) → `ProductRecord` (normalization) →
stored row. Each arrow is a narrowing toward trusted, structured data.

## Transformation Schemas
- `Url → Response`: fetching.
- `Response → (records, links)`: parsing.
- `CandidateRecord → ProductRecord | invalid`: normalization (the trust gate).
