# 🏗️ GENERATOR — From a plain-English idea to a finished, working build

> This is the procedure an **AI** follows when a non-technical human shows up
> with an idea. The human says one sentence — *"build me a webscraper for X"* —
> and the AI does the rest: it designs the system, writes the **ten design
> notes** (`Architecture`, `Flows`, `Types`, `Schemas`, `Contracts`,
> `Interfaces`, `Dependencies`, `Modules`, `DecisionLog`, `README`), lays out the
> folder/file tree, and **writes the actual code**.
>
> The human writes nothing and reads none of these notes. They exist so the AI
> knows *exactly* what to build before it builds it — which is the difference
> between a precise build and vibe-coding. (See the README's "Who does what".)

---

## 🚫 Before you start: the rules are non-negotiable

This procedure is a contract, not a buffet. Read **`PIPELINE.md` → "Non-Negotiable
Rules"** and follow them exactly: all 10 stubs first, exact order, every decision
logged, no untraceable code, and the mandatory self-audit before "done."
Compressing or "streamlining" the process is the failure mode this repo exists to
prevent — don't reinvent it.

---

## Inputs & outputs

**Input:** a human idea in plain language. Optionally: constraints (language,
scale, deadline), or "ask me questions first."

**Output, three layers:**
1. **The design** — the ten artifacts from `SCHEMA.md`, *filled for this idea*
   (the AI's own spec; the human never reads these).
2. **The source tree** — the actual folders/files the design implies
   (`ProjectStructure.md` + a real directory layout).
3. **The code** — the working implementation, written by the AI against the
   design, plus a plain-English explanation of what it does and how to run it.

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

### Step 4 — Write the code
Implement each module into its folder, using the artifacts as the spec:
- `Types.md`/`Schemas.md` → the data structures.
- `Interfaces.md` → the function/class signatures.
- `Contracts.md` → the validations, guards, and tests that must hold.
- `Flows.md` → the control flow that wires it together.

Because every piece was pinned down first, the code is *implementing a plan*,
not improvising one. That's the whole anti-vibe-coding mechanism: the AI never
writes a line it can't trace back to a decision in the design notes.

### Step 5 — Prove it runs (smoke test)
Don't hand over code you haven't run. Write and run a **smoke test of the main
path** — the happy path, end to end — and any quick checks the `Contracts`
demand. "Wrote it" and "it works" are different claims; this step is what makes
the difference. If the build environment can't run it, say so plainly instead of
implying it works. (See `QUALITY-BAR.md` §9.)

### Step 6 — Show the human, in their language
Present the result the way a non-coder can judge it: *what it does*, *how to run
it*, *that it ran* (the smoke test passed), and *whether it matches what they
asked for* — not a wall of code. The human confirms it's the thing they meant (or
describes the difference), and the AI iterates. They never read an artifact to do this.

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
└── src/ (…)               ← the working code the AI writes against that design
```

---

## See it work

[`examples/webscraper/`](examples/webscraper/) is this exact procedure run on the
idea *"a webscraper that aggregates product prices."* Read it as the reference
for what a generated schematic looks like.
