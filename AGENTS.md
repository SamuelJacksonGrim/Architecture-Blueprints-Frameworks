# AGENTS.md — for any AI building from this repo

This is the first file you read after the README. It is for you, not the human.
No extra prompt is required.

Next file: [`SELECTOR.md`](SELECTOR.md).

## Relationship

The human specifies intent. You run the construction process. You produce the
artifacts, implementation, tests, and evidence. Then the human inspects.

They keep authority. They do not supervise each file.
You do not ask "is this architecture okay?" before writing Flows.
You do not transfer final authority to yourself by finishing the pass.

**Intent → autonomous construction → inspection / evidence → human decision.**

Useful surprise is allowed. Hidden consequential decisions are not.
Evidence is not permission. A longer transcript is not more rigor.

## Do this

1. [`SELECTOR.md`](SELECTOR.md) — class, depth, Intent Card. Three questions max.
2. Instantiate the ten stubs + `INTENT.md`.
3. Build in [`PIPELINE.md`](PIPELINE.md) order. If later work breaks an earlier
   artifact, revise it and continue. Do not pause for approval.
4. Log consequential decisions when they happen. Scope: [`SCHEMA.md`](SCHEMA.md).
5. [`QUALITY-BAR.md`](QUALITY-BAR.md) when marking `complete` and once at the end.
6. Stack the human did not name: smallest that can smoke-test, log, show.
7. Attempt a smoke test. Report whether it ran.
8. Hand over the pass. Stop.

## Do not

- Ask permission between artifacts.
- Emit a turn per file to prove you passed through it.
- Ask the human to author the architecture.
- Treat depth as a complexity score.
- Restate the load list.
- Treat [`OPERATOR.md`](OPERATOR.md) as required.
- Turn DecisionLog into a journal.
