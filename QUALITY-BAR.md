# 🎯 QUALITY-BAR — the standard a generated build should reach

> A 10-artifact skeleton can be filled with shallow boilerplate or with real
> rigor. This file defines the **rigor** — so "complete" means *good*, not just
> *present*. It's the bar to aim every build at, and the thing to point the
> system prompt's "standard of quality" slot at.

---

## 1. Specificity over boilerplate
A `complete` artifact describes *this* system, with real names, real numbers,
real thresholds — never generic filler.

- ❌ "The system validates input and handles errors."
- ✅ "A request over 10 MB is rejected with 413 before parsing; a malformed body
  returns 400 and is never written to the queue."

If an artifact would read the same for a different system, it isn't done.

## 2. Name the invariants that "look optional but aren't"
The most dangerous rules are the ones whose violation causes **subtle breakage,
not a loud error**. `Contracts.md` should call these out explicitly, each with
*why* it matters — and, where possible, **the failure mode it prevents**. An
invariant justified by a demonstrated failure is far stronger than a bare
"don't change this."

- ✅ "The cache key must include the tenant id. Omit it and tenant A silently
  serves tenant B's data — no error, just a leak."
- ✅ "Retry backoff must be capped. Without a ceiling, a downstream outage turns
  every client into a retry storm that prevents recovery."

## 3. Guardrails as explicit "do not" — with the legitimate alternative
For each easy-to-make mistake, state the prohibition **and** where the urge
should actually go. A guardrail without an alternative just gets violated.

- ✅ "Don't write to the orders table directly from a handler — emit an
  `OrderPlaced` event; the projector owns that table."

## 4. Single source of truth / authority hierarchy
For every kind of decision, exactly one component decides; everything else only
*produces input*. Write down who decides and who merely advises. Diffuse
authority is how systems drift.

- ✅ "Pricing is computed in one place (`PricingService`). Callers may *request*
  a quote; none compute their own — duplicated pricing logic always diverges."

## 5. Constants carry an audit obligation — and provenance
A magic number is a contract with everything downstream of it. Record it once,
and state: *"do not change without auditing every consumer"* — and ideally list
them. (Weights that must sum to 1.0; bounds that gate safety; timeouts that
must stay below an upstream deadline.)

For a constant that was **derived rather than chosen**, go further:
- **Record where it came from** — "computed by X, not picked." A derived value
  with no provenance is indistinguishable from a guess.
- **Name one authoritative source** and make downstream consumers explicitly
  subordinate: *"if a running value drifts from the source, the source is correct."*
- **Give a re-derivation protocol** — the checklist to re-validate when an input
  changes, *before* propagating the new value.
- **Keep the validator independent.** A tool that certifies a system shouldn't
  depend on that system, or it can't stay an honest check.

## 6. Boundaries: terminal sinks and no hidden feedback
Be explicit about what is **observe-only** and must never feed back into the
core path. Many subtle failures are a metric or diagnostic value quietly
becoming a control input. Name the one-way streets.

- ✅ "The metrics exporter reads state; nothing in the request path reads the
  exporter. Don't let a dashboard number become a control signal."

## 7. The DecisionLog is an empirical ledger, not a changelog
- **Every claim names its basis.** A verdict with no reasoning is a guess.
- **Pre-declare what success *and* failure look like** before committing to a
  choice — a clean confirming result is the alarm, not the trophy.
- **Append-only. Supersede, never rewrite.** When a later decision overturns an
  earlier one, add an entry and mark the old one `superseded`/`invalidated`.
- **Negative results count.** "We tried X; it didn't work because Y" saves the
  next person from re-deriving it.
- **Title the question, not the verdict.** "Auth: sessions vs tokens?" survives
  a reversal; "Use tokens" becomes a lie the moment you switch.
- **Separate observation from interpretation.** Facts survive; explanations age.
- **Rigor per unit friction.** A ledger nobody maintains is worthless. Keep only
  the fields that prevent self-deception; reject ceremony.

## 8. Keep the docs in sync with reality
If an artifact claims a structure, that structure must exist. The cheapest
enforcement is discipline: when behavior changes, the artifact changes in the
same commit. A drifted artifact is worse than none — it lies with authority.

---

## How to use this file
- **Building?** Skim this before declaring an artifact `complete`. The Step 10
  self-audit in `PIPELINE.md` checks structure; this checks *depth*.
- **Reviewing?** These eight are the rubric.
- **Setting the bar for a model?** Point the "standard of quality" line in
  `prompts/system-prompt.md` here.
