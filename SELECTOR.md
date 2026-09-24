# SELECTOR — classify, then build only what this system needs

> Read this **before** `GENERATOR.md`.
> The ten artifacts are the language. This file is the judgment about how much
> of that language a given request actually needs.

Every application is built differently. That is not a bug in the ontology.
It is why this repo does **not** auto-spawn a full cathedral for a 40-line CLI.
Structure still appears (all ten files exist as stubs). Depth is chosen here.

---

## Step A — Intent Card

Fill `templates/INTENT.md` (copy it into the new project as `INTENT.md`).
Eight lines. If the human left them blank, you fill them from the conversation
and show them once before you start designing.

If two facts are missing **and** they would change the shape of the system,
ask. Cap: **three questions**. Otherwise assume, and log the assumption as a
`D-XXX` in `DecisionLog.md`.

Do not invent a stack the human did not name. If they said nothing about
language or host, pick the simplest thing that can pass a smoke test and log it.

---

## Step B — Classify

Pick one class. If two apply, pick the one that owns the *main loop*.

| Class | The thing is… | Default skeleton |
|---|---|---|
| `agent-loop` | think → act → observe, tools, memory | `skeletons/agents/` (ReAct unless a failure mode demands a variant) |
| `cognitive-cycle` | continuous self-governing loop, bounded state | `skeletons/cognitive-cycle/` |
| `pipeline` | ingest → transform → emit, batch or stream | `templates/` |
| `service` | request/response, API, long-lived process | `templates/` |
| `cli` | invoked, does a job, exits | `templates/` |
| `library` | imported by other code, no main loop of its own | `templates/` |
| `ui` | humans click or type as the primary loop | `templates/` |
| `unknown` | none of the above, or genuinely new | `templates/` — you are forging a skeleton as you go |

Do **not** read every skeleton. Read only the one you picked.

---

## Step C — Depth

Pick one. When in doubt, go **one step thinner**, not thicker.

| Depth | When | Must reach `complete` | May stay `stub` or `partial` |
|---|---|---|---|
| **thin** | spike, script, one-shot tool, “see if the idea works” | Architecture, Flows, Contracts, DecisionLog, README | Types, Schemas, Interfaces, Dependencies, Modules |
| **standard** | it will live more than a week | thin + Types + Interfaces + Modules | Schemas, Dependencies |
| **full** | multi-module, safety-sensitive, secrets in play, or you are writing a *reusable skeleton* | all ten | none |

**Instantiation still happens.** All ten artifact files exist from minute zero.
That is structure. Completeness is tiered. Leaving an artifact `stub` at `thin`
depth is obedience, not laziness.

Escalate depth the moment any of these become true:

- more than one process or more than one network boundary
- secrets, money, private data, or irreversible actions
- two modules that must not import each other
- you intend this design to be copied as a skeleton

---

## Step D — What you load

Read, in this order, and stop:

1. This file (you are here)
2. The Intent Card
3. `PIPELINE.md` non-negotiables (as amended for depth)
4. `QUALITY-BAR.md` — always. Thin depth is not permission to be vague.
5. Only the skeleton or templates you selected
6. `GENERATOR.md` from Step 1 onward

Do not ingest the rest of the repo “for context.”

---

## Step E — Hand off

Tell the human, in their language:

- class you picked, and why
- depth you picked, and why
- assumptions you logged
- what “done” will look like at this depth

Then build.
