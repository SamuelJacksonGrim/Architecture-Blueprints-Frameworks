# AGENTS.md — for any AI building from this repo

This is the first file you read after the README. It is for you, not the human.
No extra prompt is required.

Next file: [`SELECTOR.md`](SELECTOR.md). What to *read of this repo* lives only there.

## Division of labor

- The human supplies **intent** and retains **authority**.
- You supply **reasoning and authorship**. You do not wait for a blueprint,
  a depth name, or permission to cross artifacts.
- This repo supplies a **language and a workspace**. It does not supply a
  path you must walk, and it does not tax you a turn per artifact.

Useful surprise is allowed. Hidden consequential decisions are not.
Inspectable is not pre-approved. Evidence is not permission.

Cognitive work and observable output are different granularities.
Think across the network in as few passes as the work needs. Persist what
this depth requires. Do not emit intermediate proofs of passage.

## Do this

1. [`SELECTOR.md`](SELECTOR.md) — class, depth, Intent Card, load list.
   You choose depth. Three questions max.
2. Instantiate the ten stubs + `INTENT.md` so the workspace exists.
3. Reason across whatever artifacts the problem needs. Revisit, skip, draft
   out of graph order, hold rivals, change your mind. Mark `complete` only
   when [`SCHEMA.md`](SCHEMA.md) `depends_on` and this depth allow it.
4. Log consequential decisions when they happen. Not every thought.
   Scope is SCHEMA.
5. Consult [`QUALITY-BAR.md`](QUALITY-BAR.md) when calling something `complete`
   and once at the end — not after each artifact.
6. Stack the human did not name: smallest that can smoke-test, log, show.
7. Persist traceability for significant behavior at this depth. Glue is free.
8. Attempt a smoke test. Report whether it ran.

## Do not

- Wait for approval between artifacts.
- Serialize one coherent pass into one turn per file.
- Ask the human to author the architecture.
- Treat depth as a complexity score.
- Restate the load list.
- Treat [`OPERATOR.md`](OPERATOR.md) as required.
- Treat [`PIPELINE.md`](PIPELINE.md) as a queue.
- Turn DecisionLog into a journal. Git already exists.
