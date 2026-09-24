# 🏗️ GENERATOR — From a plain-English idea to a finished, working build

> This is the procedure an **AI** follows when a non-technical human shows up
> with an idea. The human says one sentence — *"build me a webscraper for X"* —
> and the AI does the rest: Intent Card, design notes at the right depth,
> folder tree, and **code that has been run** (or an honest "could not run").
>
> The human writes nothing and reads none of these notes unless they want to.

---

## 🚫 Before you start: the rules are non-negotiable

Read **`SELECTOR.md` first**, then **`PIPELINE.md` → "Non-Negotiable Rules"**:
Intent Card and depth, all 10 stubs first, exact fill order, every decision
logged, no untraceable code, and the mandatory self-audit before "done."

Compressing the *order* is a failure. Filling all ten artifacts to `complete`
for a thin CLI is also a failure — that is cargo cult, and SELECTOR exists to
stop it.

---

## Inputs & outputs

**Input:** a human idea in plain language. Optionally: constraints (language,
scale, deadline), or "ask me questions first."

**Output, three layers:**
1. **The design** — artifacts from `SCHEMA.md` filled to the chosen depth.
2. **The source tree** — `ProjectStructure.md` + a real directory layout.
3. **The code** — implementation against the design, plus a plain-English
   explanation of what it does and how to run it.

---

## The procedure

### Step 0 — Select (do not skip)
Follow **`SELECTOR.md`** end to end: Intent Card, class, depth, load list.
Do not read skeletons you did not pick.

| If the class is… | Start from… |
|---|---|
| `agent-loop` | a skeleton in `skeletons/agents/` (ReAct unless a named failure mode needs a variant) |
| `cognitive-cycle` | `skeletons/cognitive-cycle/` |
| anything else, or `unknown` | the blank `templates/` |

> If no skeleton fits, you are **creating a new one** as you go. Use **full**
> depth so the result can become a reusable skeleton.

### Step 1 — Instantiate
Copy the chosen starting point. All ten artifact stubs now exist, plus
`INTENT.md`. *Nothing is optional at the structural level.* Completeness
follows the depth from SELECTOR.

### Step 2 — Walk the pipeline
Fill the artifacts **in `PIPELINE.md` order**, because each depends on the one
before. At each artifact your depth requires: fill it for *this* idea, set
`status: complete`. Leave the rest `stub`. Log non-obvious choices.

### Step 3 — Derive the source tree
From `Modules.md` + `Dependencies.md` (or from Architecture + Flows at thin
depth), emit `ProjectStructure.md`.

### Step 4 — Write the code
Implement against the notes you actually filled:
- Types / Schemas → data structures (if those artifacts were completed)
- Interfaces → signatures (if completed)
- Contracts → validations, guards, tests
- Flows → control flow

No line you cannot trace to a design note this depth required.

### Step 5 — Prove it runs (smoke test)
Run the main path. If you cannot, say so. Do not imply it works.

### Step 6 — Show the human, in their language
What it does. How to run it. That it ran (or why not). Class and depth you
picked. Assumptions you logged. They confirm or correct. They never have to
read an artifact to do this.

---

## What "done" looks like

```
<project>/
├── INTENT.md
├── README.md
├── architecture/          ← 10 artifacts; only some may be complete
├── ProjectStructure.md
└── src/                   ← real code, not .keep files
```

[`examples/webscraper/`](examples/webscraper/) is a **design-only** schematic.
Its `src/` folders are placeholders. Do not treat it as a running build.
