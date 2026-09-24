# AGENTS.md — for any AI building from this repo

You are reading this because someone pointed you at this repo and asked you to
build something. **This file is for you, not the human.** No extra prompt is
required.

## Your job

Turn a plain-language request into a correctly-built project: **intent, then
design, then code.** The human may not read the design notes. They judge the
result in their own language.

You are capable. Do not shrink the work into a ceremony that burns the window
and produces ten empty essays. Use judgment. The ontology is a language.
`SELECTOR.md` is when to speak how much of it.

## Do this

1. Read [`SELECTOR.md`](SELECTOR.md). Classify. Pick a depth. Fill the Intent
   Card (`templates/INTENT.md`). Ask at most three blocking questions.
2. Instantiate all ten artifact stubs (and `INTENT.md`) in the new project.
   Structure is not optional. Completeness follows the depth you picked.
3. Walk [`PIPELINE.md`](PIPELINE.md) in order for the artifacts your depth
   requires to reach `complete`. Do not reorder. Do not fill a later artifact
   before its `depends_on` are at least `partial`.
4. Hold every `complete` artifact to [`QUALITY-BAR.md`](QUALITY-BAR.md).
   Thin depth is not permission to be generic.
5. Derive `ProjectStructure.md`, then write only the code you can trace to a
   design note.
6. Smoke-test the main path. If you cannot run it, say so. Do not imply it works.
7. Report to the human: what it does, how to run it, that it ran (or why not),
   class + depth you picked, assumptions you logged.

## Do not

- Load every skeleton “for context.”
- Invent a stack the human did not name.
- Declare an artifact `complete` if it would read the same for a different system.
- Treat [`OPERATOR.md`](OPERATOR.md) as required. It is optional routing advice
  for humans who have more than one model.

That's the contract. The human says *what*. This repo says *how to stay honest
while you build it*.
