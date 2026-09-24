# SELECTOR — classify, then build only what this system needs

> Read this **before** `GENERATOR.md`.
> The ten artifacts are the language. This file decides *which dialect* and
> *how much of it* to speak.

Two independent axes. Do not collapse them into a complexity score.

| Axis | Question | Not a question it answers |
|---|---|---|
| **Class** | What *kind* of thing is this? | How hard is it? How big is it? |
| **Depth** | How much structure must be made explicit? | What genre is it? |

A 30-line script with an irreversible external action can be `cli` + `standard`.
A 500-line single-purpose transform can be `pipeline` + `thin`.
Never score files, endpoints, or "complexity / 10."

---

## Step A — Intent Card

Copy `templates/INTENT.md` into the new project as `INTENT.md`.
If the human left lines blank, fill them from the conversation and show once.
Cap: **three** blocking questions. Otherwise assume and log `D-XXX`.

Do not invent a stack the human did not name.

---

## Step B — Class (what kind)

Pick one. If two apply, pick the one that owns the *main loop*.

| Class | The thing is… | Default skeleton |
|---|---|---|
| `agent-loop` | think → act → observe, tools, memory | `skeletons/agents/` (ReAct unless a failure mode demands a variant) |
| `cognitive-cycle` | continuous self-governing loop, bounded state | `skeletons/cognitive-cycle/` |
| `pipeline` | ingest → transform → emit | `templates/` |
| `service` | request/response, long-lived process | `templates/` |
| `cli` | invoked, does a job, exits | `templates/` |
| `library` | imported by other code | `templates/` |
| `ui` | humans click or type as the primary loop | `templates/` |
| `unknown` | none of the above | `templates/` — you are forging a skeleton |

Read only the skeleton you picked.

---

## Step C — Depth (how much structure)

**Governing test:** choose the thinnest depth that can express every decision
the system cannot safely leave implicit.

If a decision would otherwise be made silently in code — a boundary, a secret,
a forbidden import, an irreversible action — escalate until that decision has
a home in an artifact. That is the test. "When in doubt, go thinner" is not.

Do not add a fourth depth. If `standard` is too broad later, add a *conditional
requirement* to an existing depth before inventing `full-lite`.

| Depth | Must reach `complete` | May stay `stub` / `partial` |
|---|---|---|
| **thin** | Architecture, Flows, Contracts, DecisionLog, README | Types, Schemas, Interfaces, Dependencies, Modules |
| **standard** | thin + Types + Interfaces + Modules | Schemas, Dependencies |
| **full** | all ten | none |

Escalate when any of these become true — these are structural consequences,
not size:

- more than one process or more than one network boundary
- secrets, money, private data, or irreversible actions
- two modules that must not import each other
- you intend this design to be copied as a skeleton

All ten files still exist from minute zero (**structurally valid**).
A build is done at **depth-complete**. A reusable skeleton is **fully complete**.
See `SCHEMA.md`.

Record the choice in the Intent Card's decision block so a later entity does
not have to re-derive it.

---

## Step D — Minimum context

This is a property of the framework, not etiquette.

Load only the artifacts, skeletons, and instructions required by the selected
class and depth. Unselected material is not assumed relevant.

Read, in this order, and stop:

1. This file
2. The Intent Card
3. `PIPELINE.md` non-negotiables
4. `QUALITY-BAR.md` — always. Thin is not permission to be vague.
5. Only the skeleton or templates you selected
6. `GENERATOR.md` from Step 1 onward

---

## Step E — Hand off

Tell the human: class, depth, the structural reasons, assumptions, what "done"
means at this depth. Then build.
