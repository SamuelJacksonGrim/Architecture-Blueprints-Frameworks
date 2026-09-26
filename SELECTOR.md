# SELECTOR — classify, then persist only what this system needs

> The reading order for this repo lives only here (Step D).

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

Copy `templates/INTENT.md` to `INTENT.md`. Fill it from the request.

**Consequential fields:** who uses it (roles), where it runs and what it is
exposed to, money, private data or secrets, irreversible actions.

A field is **implied** when any competent reader of the request would fill it
the same way. It is a **guess** when two plausible readings lead to different
designs. Done-when is derived from the named features and is not a reason to
ask.

1. The human says one-shot / don't ask → **go.** This overrides rule 3. Pick
   the reading with the fewest escalation triggers. Build it so the other
   reading can be added without a rewrite, and name that other reading first in
   the handover.
2. Every consequential field stated or implied → **go.** Do not ask.
3. Otherwise ask **only about the guessed fields**, three questions max. Or run
   a short pre-plan if the human says they want to talk it through.

Stack and taste (names, colors, layout, wording) are never a reason to ask.
If the human named no stack, pick the smallest that can smoke-test.
Consequential guesses and the stack go in DecisionLog (scope: `SCHEMA.md`,
Capture) and first in the handover. Taste goes in neither.

**Definitions used by the triggers in Step C:**
- *Private data*: records whose subject is someone other than the operator
  (their contact details, accounts, orders, messages, health, money), or the
  operator's data leaving their machine. What the operator writes about their
  own life or work is theirs, even when it names other people. Their own data
  on their own machine is not a trigger.
- *Irreversible action*: the system acting outside its own store: moving money,
  sending messages, publishing, deleting what it does not own. A user deleting
  their own records behind a guard (confirmation, or archive first) is an
  ordinary feature, not a trigger.

**Implied counterparts.** People name the verbs they are thinking of, not the
ones they expect. For each thing named, list what a user of *this kind* of
system would expect without saying it, then mark each `include` or `exclude`
with a reason:

- each verb's counterpart: create↔delete, export↔import, add↔remove,
  publish↔unpublish, connect↔disconnect/traverse, edit↔recover the previous
  value (bounded)
- the category's norms: what every competent example of this kind of thing has
  (dated records → filter by date; linked items → follow links more than one
  step; data out → comes back in, with its links still working; uploads → strip
  hidden metadata)
- norms outside software (tax, licensing, terms, privacy policy, consent):
  never build or decide these. Always list them for the human.

Include by default when it is small, reversible, adds no new escalation
trigger, and adds no new *kind* of irreversible action. Otherwise exclude, with
a reason. Excluded items are handover notes, not silent gaps.

---

## Step B — Class

Pick the class that owns the main loop. `class:` is one token from this table.
Settle `app` vs `cli` once the stack is chosen. Use a skeleton only if its main
loop *is* your main loop. The skeletons are AI-system patterns. Ordinary apps,
sites, services, and tools use `templates/`.

| Class | Default skeleton |
|---|---|
| `agent-loop` | `skeletons/agents/` (ReAct unless a named failure mode needs a variant) |
| `cognitive-cycle` | `skeletons/cognitive-cycle/` |
| `tool-ecosystem` (an AI dispatching named tools) | `skeletons/tool-ecosystem/` |
| `event-bus` (pub/sub is the core) | `skeletons/event-bus/` |
| `evaluator` (score + critique) | `skeletons/evaluator/` |
| `diagnostic` (observe → hypothesize → test → report) | `skeletons/diagnostic/` |
| `app` `service` `cli` `library` `pipeline` `unknown` | `templates/` |

`cognitive-cycle` only if the thing *is* a persistent self acting on its own
state. Catalog siblings are not imported by selecting this class.

---

## Step C — Depth and exposure

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
- modules that must not import each other, because a Contract depends on it
  (only one module may touch money, secrets, or another tenant's data). Ordinary
  layering does not count.
- the intent to reuse this design as a skeleton

Persistent local state by itself is not an escalation trigger. Private data and
irreversible action are defined in Step A.

**Where triggers take you:** none → `thin`. Any → at least `standard`. `full`
when a network boundary comes with money, secrets, or private data, or when
the design will be reused as a skeleton. The governing test may raise the
depth further (log why). It never lowers it.

In the Intent Card, triggers that hold now go in `reasons`. Triggers that do
not hold yet go in `escalate_if`.

**Exposure profile.** Choose the stack first, because the stack decides the
exposure. Pick one:
- `local-single`: one OS user, no listener
- `local-shared`: several OS users or a shared folder, still no listener
- `networked`: any listener, even localhost. One user's local UI on 127.0.0.1
  behind a per-launch token takes SECURITY's networked row, but it is **not** a
  network boundary for depth.
- `multi-tenant`: accounts whose data must be invisible to each other

Put the SECURITY controls that apply (Step D) into Contracts.

States: structurally valid → depth-complete → fully complete (`SCHEMA.md`).

---

## Step D — Reading order

Read now:
1. This file
2. `templates/INTENT.md`
3. [`PIPELINE.md`](PIPELINE.md): construction order, slices, the live boundary
4. The one selected skeleton, or `templates/`
5. [`SECURITY.md`](SECURITY.md): its `always` row whenever the system stores
   data, and the rest when Step C says so

Consult when that step arrives:
- [`SCHEMA.md`](SCHEMA.md): artifact states and what goes in DecisionLog
- [`QUALITY-BAR.md`](QUALITY-BAR.md): when marking `complete`, and at the end
- [`KAIZEN.md`](KAIZEN.md): after handover, only if the human asks for more rounds

Nothing else in this repo is needed to build.

---

## Step E — Build the pass

Then construct. Do not return for approval until the pass is done.
