# AGENTS.md — for any AI building from this repo

This is the first file you read after the README. It is for you, not the human.
No extra prompt is required.

Next file: [`SELECTOR.md`](SELECTOR.md). Load order lives only there.

## Division of labor

- The human supplies **intent** and retains **authority** (they may reject the result).
- You supply **reasoning and authorship** of the architecture. You do not wait
  for them to hand you modules, a stack, or a depth.
- This repo supplies **language, order, evidence, and inspectability**.

Useful surprise is allowed. Hidden decisions are not. Inspectable is not the
same as pre-approved.

## Do this

1. Follow [`SELECTOR.md`](SELECTOR.md) — class, depth, Intent Card, load list.
   You choose depth. Three questions max.
2. Instantiate all ten stubs + `INTENT.md`.
3. Fill in [`PIPELINE.md`](PIPELINE.md) order. Record decisions *as you make them*
   in DecisionLog. Do not wait for its slot. Construction is sequential; capture
   is continuous.
4. Consult [`QUALITY-BAR.md`](QUALITY-BAR.md) when marking an artifact `complete`
   and at self-audit — not as a second constitution up front.
5. Stack the human did not name: smallest that can smoke-test, log, show.
6. Behaviorally significant decisions and non-trivial behavior must be traceable
   to the design at this depth. Glue does not need a paragraph.
7. Attempt a smoke test. Report whether it ran. Do not claim a working project
   you could not run.

## Do not

- Ask the human to author the architecture.
- Treat depth as a complexity score.
- Restate the load list.
- Treat [`OPERATOR.md`](OPERATOR.md) as required.
- Skip this file because a vendor stub (`CLAUDE.md`, `GEMINI.md`, Copilot
  instructions) exists. Those files only point here.
