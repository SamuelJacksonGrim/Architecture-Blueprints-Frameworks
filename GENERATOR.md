# 🏗️ GENERATOR — From a human's idea to a complete repo schematic

> This is the procedure an **intelligent entity** follows when a human shows up
> with an idea. It turns one sentence — *"I want to build a webscraper for X"* —
> into a full repo schematic: the **folder/file tree** plus all **ten filled
> artifacts** (`Architecture`, `Flows`, `Types`, `Schemas`, `Contracts`,
> `Interfaces`, `Dependencies`, `Modules`, `DecisionLog`, `README`).
>
> The human brings the idea. The entity runs this. The repo guarantees the
> result is consistent. (See the README's "division of labor".)

---

## Inputs & outputs

**Input:** a human idea in plain language. Optionally: constraints (language,
scale, deadline), or "ask me questions first."

**Output, two layers:**
1. **The design** — the ten artifacts from `SCHEMA.md`, *filled for this idea*.
2. **The source tree** — the actual folders/files the design implies
   (`ProjectStructure.md` + a real directory layout), so the human can start
   coding immediately.

---

## The procedure

### Step 0 — Classify the idea
Decide what *kind* of system this is, because that picks the starting point:

| If the idea is… | Start from… |
|---|---|
| an autonomous, tool-using, looping system | a skeleton in `skeletons/agents/` |
| a known pattern we already have a skeleton for | that skeleton |
| anything else (webscraper, API, ETL, CLI, service…) | the blank `templates/` |

> If no skeleton fits, you are **creating a new one** as you go — fill the
> templates, and the result becomes a reusable skeleton for the next person.

### Step 1 — Instantiate
Copy the chosen starting point. All ten artifact stubs now exist. *Nothing is
optional at the structural level* (the Instantiation Rule from `SCHEMA.md`).

### Step 2 — Walk the pipeline
Fill the artifacts **in `PIPELINE.md` order**, because each depends on the one
before:

```
Architecture → Flows → Contracts → Types → Schemas
            → Interfaces → Dependencies → Modules → README
            (DecisionLog maintained throughout)
```

At each artifact: read its frontmatter (`depends_on`, `order`), fill it for the
*specific* idea, set `status: complete`. Log any non-obvious choice in
`DecisionLog`.

### Step 3 — Derive the source tree
From `Modules.md` + `Dependencies.md`, emit `ProjectStructure.md`: the real
folder/file layout. One module → roughly one folder/package. The artifacts are
the *design*; this is the *scaffold* the design maps onto.

### Step 4 — Hand back the schematic
Present both layers. The human reviews, catches the little things, and steers.
Then they (or the entity) scaffold the actual code into the tree.

---

## What "done" looks like

A folder like this (see [`examples/webscraper/`](examples/webscraper/) for a
real, complete one):

```
<project>/
├── README.md              ← what & why, for this specific system
├── architecture/          ← the 10 design artifacts, all filled
│   ├── Architecture.md  Flows.md  Contracts.md  Types.md  Schemas.md
│   ├── Interfaces.md  Dependencies.md  Modules.md  DecisionLog.md
│   └── diagrams/
├── ProjectStructure.md    ← the source tree the design implies
└── src/ (…)               ← stubbed folders/files ready to code into
```

---

## See it work

[`examples/webscraper/`](examples/webscraper/) is this exact procedure run on the
idea *"a webscraper that aggregates product prices."* Read it as the reference
for what a generated schematic looks like.
