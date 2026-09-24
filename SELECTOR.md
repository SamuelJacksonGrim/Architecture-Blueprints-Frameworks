# SELECTOR — classify, then build only what this system needs

> Read this **before** anything else except this sentence.
> Load order lives **only here**. AGENTS, GENERATOR, and PIPELINE point here.
> They do not restate a second list.

Two independent axes. Do not collapse them into a complexity score.

| Axis | Question |
|---|---|
| **Class** | What *kind* of thing is this? |
| **Depth** | How much structure must be made explicit? |

---

## Step A — Intent Card

Copy `templates/INTENT.md` to the project as `INTENT.md`.
Blank lines: fill from the conversation, show once. Cap: three questions.
Otherwise assume and log `D-XXX`.

**Stack rule:** do not *silently* impose a stack. If implementation needs a
technology the human did not name, choose the smallest stack that can pass a
smoke test, record it in `DecisionLog`, and show it to the human. You may
decide. You may not hide the decision.

---

## Step B — Class

Pick the class that owns the main loop.

| Class | Default skeleton |
|---|---|
| `agent-loop` | `skeletons/agents/` (ReAct unless a named failure mode needs a variant) |
| `cognitive-cycle` | `skeletons/cognitive-cycle/` |
| `pipeline` `service` `cli` `library` `ui` `unknown` | `templates/` |

Read only the skeleton you picked.

---

## Step C — Depth

**Governing test:** the thinnest depth that can express every decision the
system cannot safely leave implicit. No fourth depth. No complexity score.

| Depth | Must be `complete` | May stay `stub` / `partial` |
|---|---|---|
| **thin** | Architecture, Flows, Contracts, DecisionLog, README | Types, Schemas, Interfaces, Modules, Dependencies |
| **standard** | thin + Types + Interfaces + Modules | Schemas, Dependencies |
| **full** | all ten | none |

Escalate when: extra process or network boundary; secrets / money / private
data / irreversible action; modules that must not import each other; this
design will be reused as a skeleton.

States: structurally valid → depth-complete → fully complete (`SCHEMA.md`).

Record class, depth, reasons, escalate_if on the Intent Card.

---

## Step D — Load list (authoritative)

Load only what the selected class and depth require. Unselected material is
not relevant.

1. This file
2. Intent Card
3. `PIPELINE.md` non-negotiables + fill order
4. `QUALITY-BAR.md`
5. The one selected skeleton or `templates/`
6. `GENERATOR.md` from Step 1 onward

Stop.

---

## Step E — Hand off

Class, depth, reasons, stack if you chose one, assumptions, what done means.
Then build.
