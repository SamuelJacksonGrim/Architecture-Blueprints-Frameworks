# SELECTOR — classify, then persist only what this system needs

> What you *read of this repo* lives **only here**. AGENTS, GENERATOR, and
> PIPELINE point here. They do not restate a second list.

The human supplies **intent**. You supply **reasoning**. The human retains
**authority**, not authorship. You may surprise them. You may not hide a
consequential decision.

The artifacts are a workspace. Class and depth decide how much of it must be
*persisted*. They do not decide the order you think.

Two independent axes. Not a complexity score.

| Axis | Question | Who answers |
|---|---|---|
| **Class** | What *kind* of thing is this? | You |
| **Depth** | How much structure must be explicit *in the result*? | You. Human may override. |

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
| tool dispatch / named tools | `skeletons/tool-ecosystem/` |
| pub/sub events | `skeletons/event-bus/` |
| score + critique | `skeletons/evaluator/` |
| observe → hypothesize → test → report | `skeletons/diagnostic/` |
| `pipeline` `service` `cli` `library` `ui` `unknown` | closest skeleton above, else `templates/` |

`cognitive-cycle` only if the thing *is* a persistent self acting on its own
state. A CLI, library, one-shot function, or request/response agent is a
different class. Catalog siblings are not imported by selecting this class.

---

## Step C — Depth

**Governing test:** the thinnest depth that can express every decision this
system cannot safely leave implicit. You apply the test.

No fourth depth. No score.

| Depth | Must be `complete` in the result | May stay `stub` / `partial` |
|---|---|---|
| **thin** | Architecture, Flows, Contracts, DecisionLog, README | Types, Schemas, Interfaces, Modules, Dependencies |
| **standard** | thin + Types + Interfaces + Modules | Schemas, Dependencies |
| **full** | all ten | none |

You may *think* about a stubbed artifact. You need not *emit* it.

**Escalate — and only these, stated once, here — when the design has:**

- a second process, or any network boundary
- secrets, money, private data, or irreversible actions
- modules that must not import each other
- the intent to reuse this design as a skeleton

Persistent local state by itself is not an escalation trigger.

A depth must be able to reach its own completion without requiring an artifact
that same depth permits to remain incomplete.

States: structurally valid → depth-complete → fully complete (`SCHEMA.md`).

---

## Step D — Load list (what to read of *this* repo)

1. This file
2. Intent Card
3. [`PIPELINE.md`](PIPELINE.md) — completeness graph only
4. The one selected skeleton or `templates/`
5. [`GENERATOR.md`](GENERATOR.md) from after SELECTOR onward

Stop reading the framework. [`QUALITY-BAR.md`](QUALITY-BAR.md) is a rubric for
the *result*, not a pass you run after each thought.

---

## Step E — Then work

Class, depth, reasons, stack if you chose one, assumptions, what done means.
Then reason and persist. One pass is allowed. Many internal revisions are
allowed. A turn per artifact is not required.
