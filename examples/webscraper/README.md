# 🕷️ Price-Aggregator Webscraper — a generated schematic

> **This folder is a worked example of [`../../GENERATOR.md`](../../GENERATOR.md)
> run on a real idea:** *"a webscraper that aggregates product prices."*
>
> It's what a human receives after saying that one sentence to an intelligent
> entity. Nothing here was hand-filled by the human — the entity walked the
> pipeline and produced the whole thing. Read it as the reference for what
> "give me the repo schematic" actually delivers.

## What you get
1. **The design** — all ten artifacts in [`architecture/`](architecture/),
   filled specifically for a webscraper (not generic stubs).
2. **The source tree** — [`ProjectStructure.md`](ProjectStructure.md) plus a
   [`src/`](src/) layout, one folder per module.

> This example stops at the design + structure layers to keep it readable. In a
> live build the AI then **writes the actual code** into each `src/` folder
> (Step 4 of [`../../GENERATOR.md`](../../GENERATOR.md)) — the human never touches it.

## Suggested reading order
1. [`architecture/README.md`](architecture/README.md) — what & why
2. [`architecture/Architecture.md`](architecture/Architecture.md) — the subsystems
3. [`architecture/diagrams/system_flow.md`](architecture/diagrams/system_flow.md) — the loop, as a picture
4. [`architecture/Flows.md`](architecture/Flows.md) — the crawl loop in detail
5. the rest of `architecture/` — Contracts, Types, Schemas, Interfaces, Dependencies, Modules, DecisionLog
6. [`ProjectStructure.md`](ProjectStructure.md) — where the code goes

## The point
Same ten artifacts as the agent skeletons. Different system entirely. That
sameness is the thesis: **one structure, any system, built consistently by any
intelligence from a human's idea.**
