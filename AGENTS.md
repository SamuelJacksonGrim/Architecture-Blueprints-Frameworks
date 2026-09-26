# AGENTS.md — for any AI building from this repo

This is the first file you read. It is for you, not the human.
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

1. [`SELECTOR.md`](SELECTOR.md): Intent Card (with implied counterparts), class,
   depth, exposure. Ask only about consequential guesses.
2. Instantiate the ten stubs (`templates/` or the selected skeleton) in the
   human's project, never inside this repo. If the target already holds work
   you did not make in this pass, do not overwrite or delete it: build
   alongside it, or ask. The intake
   decisions (stack, depth, consequential guesses) are the first DecisionLog entries.
3. Build in [`PIPELINE.md`](PIPELINE.md) order. If later work breaks an earlier
   artifact, revise it and continue. Do not pause for approval. Too big for one
   pass: design the whole, implement end-to-end slices (PIPELINE).
4. Log consequential decisions when they happen. Scope: [`SCHEMA.md`](SCHEMA.md).
5. [`QUALITY-BAR.md`](QUALITY-BAR.md) when marking `complete` and once at the end.
6. Implement. Attempt a smoke test. Report whether it ran.
7. Validate: `python tools/validate.py <project>` from this repo, if Python is available.
8. Hand over: guesses first, then what was built, what was excluded and why,
   and evidence. Stop. More rounds only if asked: [`KAIZEN.md`](KAIZEN.md).

## Do not

- Ask permission between artifacts.
- Ask about taste. Choose, and log it if it is consequential.
- Cross the live boundary (deploy, publish, charge, message real people). See PIPELINE.
- Emit a turn per file to prove you passed through it.
- Ask the human to author the architecture.
- Treat depth as a complexity score.
- Restate the load list.
- Treat [`OPERATOR.md`](OPERATOR.md) as required.
- Turn DecisionLog into a journal.
