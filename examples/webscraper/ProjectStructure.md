# Project Structure — Price-Aggregator Webscraper

> The **source tree** the design implies, derived from `Modules.md` +
> `Dependencies.md` (Step 3 of `GENERATOR.md`). One module → one package. This
> is the scaffold a human starts coding into; the stub files exist in `src/`.

```
webscraper/
├── README.md                  # project overview (what/why/how to run)
├── ProjectStructure.md        # this file
├── architecture/              # the 10 design artifacts (the schematic)
│   ├── Architecture.md
│   ├── Flows.md
│   ├── Contracts.md
│   ├── Types.md
│   ├── Schemas.md
│   ├── Interfaces.md
│   ├── Dependencies.md
│   ├── Modules.md
│   ├── DecisionLog.md
│   ├── README.md
│   └── diagrams/
│       └── system_flow.md
└── src/                       # one folder per module (see Modules.md)
    ├── types/                 # Types.md  → domain types
    ├── interfaces/            # Interfaces.md → the swap points
    ├── frontier/              # FrontierInterface impl (queue + dedup)
    ├── scheduler/             # politeness / rate limiting
    ├── fetcher/               # FetcherInterface impl (HTTP, retries, robots)
    ├── parser/                # ParserInterface impls (per-site selectors)
    ├── normalizer/            # NormalizerInterface impl (the trust gate)
    ├── store/                 # StoreInterface impl (persistence)
    ├── pipeline/              # the crawl loop (orchestration)
    └── observability/         # logs / metrics / crawl stats
```

## Module → folder → interface map
| Folder | Module | Implements |
|--------|--------|------------|
| `src/frontier/` | frontier | FrontierInterface |
| `src/scheduler/` | scheduler | — |
| `src/fetcher/` | fetcher | FetcherInterface |
| `src/parser/` | parser | ParserInterface |
| `src/normalizer/` | normalizer | NormalizerInterface |
| `src/store/` | store | StoreInterface |
| `src/pipeline/` | pipeline | — (orchestrator) |
| `src/observability/` | observability | — (cross-cutting) |

> Language-agnostic on purpose: each `src/*` folder maps to a package/module in
> whatever language the human chooses. The `.keep` files mark the intended tree.
