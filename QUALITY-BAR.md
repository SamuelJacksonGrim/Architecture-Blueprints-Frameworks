# 🎯 QUALITY-BAR — the standard a generated build should reach

> A 10-artifact skeleton can be filled with shallow boilerplate or with real
> rigor. This file defines the **rigor** — so "complete" means *good*, not just
> *present*. It's the bar the AI should aim every build at, and the thing to
> point the system prompt's "standard of quality" slot at.
>
> The principles below are distilled from a living exemplar: **RFE-Core2**, a
> companion repo in the author's (Samuel Jackson Grim's) ecosystem whose
> `CLAUDE.md` and `docs/findings/` demonstrate this standard in production.
> You don't need access to that repo — the transferable disciplines are here.

---

## 1. Specificity over boilerplate
A `complete` artifact describes *this* system, with real names, real numbers,
real thresholds — never generic filler.

- ❌ "The system validates input and handles errors."
- ✅ "Crystallization fires at `coherence ≥ 0.75`, `stability ≥ 0.60`,
  `relation ≥ 0.80`; below any threshold the candidate is dropped, not queued."

If an artifact would read the same for a different system, it isn't done.

## 2. Name the invariants that "look optional but aren't"
The most dangerous rules are the ones whose violation causes **subtle breakage,
not a loud error**. `Contracts.md` should call these out explicitly, each with
*why* it matters.

> Example shape: *"`arousal`/`valence` are read-only computed properties — do not
> store them as state; storing double-counts the smoothing already applied."*

## 3. Guardrails as explicit "do not" — with the legitimate alternative
For each easy-to-make mistake, state the prohibition **and** where the urge
should actually go. A guardrail without an alternative just gets violated.

> *"Don't promote a symbol to sacred outside `review_core_promotion()` — a use
> case that seems to need it almost always wants a different layer."*

## 4. Single source of truth / authority hierarchy
For every kind of decision, exactly one component decides; everything else only
*produces reports*. Write down who arbitrates and who merely advises. Diffuse
authority is how systems drift.

## 5. Constants carry an audit obligation
A magic number is a contract with everything downstream of it. Record it once,
and state: *"do not change without auditing every consumer"* — and ideally list
them. (Weights that must sum to 1.0; bounds that gate safety; etc.)

## 6. Boundaries: terminal sinks and no hidden feedback
Be explicit about what is **observe-only** and must never feed back into the
core loop. Many subtle failures are an observability/diagnostic value quietly
becoming a control input. Name the one-way streets.

## 7. The DecisionLog is an empirical ledger, not a changelog
Borrowed wholesale from RFE's `findings/` discipline:

- **Every claim names its control / its reasoning.** A verdict with no basis isn't a decision, it's a guess.
- **Pre-declare what success *and* failure look like** before committing to a choice — a clean confirming result is the alarm, not the trophy.
- **Append-only. Supersede, never rewrite.** When a later decision overturns an earlier one, add an entry and mark the old one `superseded`/`invalidated`. The overturning *is* the record.
- **Negative results count.** "We tried X; it didn't work because Y" saves the next person (or instance) from re-deriving it.
- **Title the question, not the verdict.** "Auth: sessions vs tokens?" survives a reversal; "Use tokens" becomes a lie the moment you switch.
- **Separate observation from interpretation.** The facts usually survive; the explanation often changes — keep them in different paragraphs.
- **Rigor per unit friction.** A ledger nobody maintains is worthless. Keep only the fields that prevent self-deception; reject ceremony.

## 8. Keep the docs in sync with reality
If an artifact claims a structure, that structure must exist. RFE enforces this
with a `verify_docs.py` test. At minimum: when behavior changes, the artifact
changes in the same breath. A drifted artifact is worse than none.

---

## How to use this file
- **Building?** Skim this before declaring an artifact `complete`. The Step 10
  self-audit in `PIPELINE.md` checks structure; this checks *depth*.
- **Reviewing?** These eight are the rubric.
- **Setting the bar for a model?** Point the "standard of quality" line in
  `prompts/system-prompt.md` here.
