# SELECTOR — classify, then build only what this system needs

> Load order lives **only here**. AGENTS, GENERATOR, and PIPELINE point here.

The human supplies **intent**. You supply **reasoning**. The human retains
**authority**, not authorship of the architecture. You may surprise them.
You may not hide a consequential decision.

Two independent axes. Not a complexity score.

| Axis | Question | Who answers |
|---|---|---|
| **Class** | What *kind* of thing is this? | You |
| **Depth** | How much structure must be explicit? | You, by the test below. The human may override. |

---

## Step A — Intent Card

Copy `templates/INTENT.md` to `INTENT.md`. Fill blanks. Show once. Three questions max.

**Stack rule:** do not *silently* impose a stack. If you need a technology the
human did not name, choose the smallest that can pass a smoke test, log it,
show it. You may decide. You may not hide the decision.

---

## Step B — Class

Pick the class that owns the main loop. Read only that skeleton.

| Class | Default skeleton |
|---|---|
| `agent-loop` | `skeletons/agents/` (ReAct unless a named failure mode needs a variant) |
| `cognitive-cycle` | `skeletons/cognitive-cycle/` |
| `pipeline` `service` `cli` `library` `ui` `unknown` | `templates/` |

---

## Step C — Depth (canonical escalation)

**Governing test:** the thinnest depth that can express every decision this
system cannot safely leave implicit. You apply the test. The human does not
have to tell you the depth.

No fourth depth. No score.

| Depth | Must be `complete` | May stay `stub` / `partial` |
|---|---|---|
| **thin** | Architecture, Flows, Contracts, DecisionLog, README | Types, Schemas, Interfaces, Modules, Dependencies |
| **standard** | thin + Types + Interfaces + Modules | Schemas, Dependencies |
| **full** | all ten | none |

**Escalate — and only these, stated once, here — when the design has:**

- a second process, or any network boundary
- secrets, money, private data, or irreversible actions
- modules that must not import each other
- the intent to reuse this design as a skeleton

Persistent local state by itself is not an escalation trigger.

A depth must be able to reach its own completion without requiring an artifact
that same depth permits to remain incomplete.

States: structurally valid → depth-complete → fully complete (`SCHEMA.md`).

Instantiate class, depth, reasons, and these triggers on the Intent Card.
Do not keep a second copy of this list anywhere else.

---

## Step D — Load list (authoritative)

1. This file
2. Intent Card
3. `PIPELINE.md` non-negotiables + fill order
4. The one selected skeleton or `templates/`
5. `GENERATOR.md` from after SELECTOR onward

Stop. [`QUALITY-BAR.md`](QUALITY-BAR.md) is the rubric for marking an artifact
`complete` and for the self-audit — load it then, not as a second constitution
up front.

---

## Step E — Hand off

Class, depth, reasons, stack if you chose one, assumptions, what done means,
whether you could run it. Then build.
