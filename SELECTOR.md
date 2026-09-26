# SELECTOR — classify, then persist only what this system needs

> What you *read of this repo* lives **only here**.

The human supplies **intent**. You supply the **construction pass**. The human
inspects the result and retains **authority**. That authority is not a gate
between artifacts.

Two independent axes. Not a complexity score.

| Axis | Question | Who answers |
|---|---|---|
| **Class** | What *kind* of thing is this? | You |
| **Depth** | How much structure must be explicit in the result? | You. Human may override after the pass. |

---

## Step A — Intent Card

Copy `templates/INTENT.md` to `INTENT.md`. Fill blanks. Show once. Three questions max.

**Stack rule:** do not *silently* impose a stack. Smallest that can smoke-test,
log it, show it with the result.

---

## Step B — Class

Pick the class that owns the main loop. Read only that skeleton.

| Class | Default skeleton |
|---|---|
| `agent-loop` | `skeletons/agents/` (ReAct unless a named failure mode needs a variant) |
| `cognitive-cycle` | `skeletons/cognitive-cycle/` |
| tool dispatch / named tools | `skeletons/tool-ecosystem/` |
| pub/sub events | `skeletons/event-bus/` |
| score + critique | `skeletons/evaluator/` |
| observe → hypothesize → test → report | `skeletons/diagnostic/` |
| `pipeline` `service` `cli` `library` `ui` `unknown` | closest skeleton above, else `templates/` |

`cognitive-cycle` only if the thing *is* a persistent self acting on its own
state. Catalog siblings are not imported by selecting this class.

---

## Step C — Depth

**Governing test:** the thinnest depth that can express every decision this
system cannot safely leave implicit.

No fourth depth. No score.

| Depth | Must be `complete` in the result | May stay `stub` / `partial` |
|---|---|---|
| **thin** | Architecture, Flows, Contracts, DecisionLog, README | Types, Schemas, Interfaces, Modules, Dependencies |
| **standard** | thin + Types + Interfaces + Modules | Schemas, Dependencies |
| **full** | all ten | none |

**Escalate — only these, stated once, here — when the design has:**

- a second process, or any network boundary
- secrets, money, private data, or irreversible actions
- modules that must not import each other
- the intent to reuse this design as a skeleton

Persistent local state by itself is not an escalation trigger.

States: structurally valid → depth-complete → fully complete (`SCHEMA.md`).

---

## Step D — Load list

1. This file
2. Intent Card
3. [`PIPELINE.md`](PIPELINE.md) — construction order
4. The one selected skeleton or `templates/`
5. [`GENERATOR.md`](GENERATOR.md)

Stop reading the framework. [`QUALITY-BAR.md`](QUALITY-BAR.md) is for the result.

---

## Step E — Build the pass

Then construct. Do not return for approval until the pass is done.
