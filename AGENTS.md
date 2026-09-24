# AGENTS.md — for any AI building from this repo

This file is for you, not the human. No extra prompt is required.

## Your job

Intent, then design, then code. The human judges in their language.

The ontology is a language. [`SELECTOR.md`](SELECTOR.md) decides how much of it
to speak, **and what to load**. Do not invent a second reading order.

**Minimum context is a property of this framework.** Unselected material is not
relevant.

## Do this

1. Follow [`SELECTOR.md`](SELECTOR.md) end to end — class, depth, Intent Card,
   load list. Ask at most three blocking questions.
2. Instantiate all ten stubs + `INTENT.md` (structurally valid).
3. Fill in [`PIPELINE.md`](PIPELINE.md) order. `depends_on` meaning is only in
   [`SCHEMA.md`](SCHEMA.md).
4. Hold every `complete` artifact to [`QUALITY-BAR.md`](QUALITY-BAR.md).
5. If you must pick a stack the human did not name: smallest that can smoke-test,
   log it, show it. Do not hide it.
6. Write only traceable code. Smoke-test, or say you could not.
7. Report: what it does, how to run it, ran-or-not, class, depth, reasons, stack.

## Do not

- Restate or invent a load list.
- Treat depth as a complexity score.
- Declare `complete` an artifact that would fit a different system.
- Treat [`OPERATOR.md`](OPERATOR.md) as required.
