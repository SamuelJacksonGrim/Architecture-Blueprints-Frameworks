# AGENTS.md — for any AI building from this repo

You are reading this because someone pointed you at this repo and asked you to
build something. **This file is for you, not the human.** No extra prompt is
required.

## Your job

Turn a plain-language request into a correctly-built project: **intent, then
design, then code.** The human judges the result in their own language.

You are capable. The ontology is a language. `SELECTOR.md` decides how much of
it to speak. Do not perform ceremony that produces ten empty essays.

**Minimum context is a property of this framework.** Load only the artifacts,
skeletons, and instructions required by the selected class and depth.
Unselected material is not assumed relevant.

## Do this

1. Read [`SELECTOR.md`](SELECTOR.md). Class and depth are *independent* axes.
   Fill the Intent Card, including the selector decision block. Ask at most
   three blocking questions.
2. Instantiate all ten artifact stubs (and `INTENT.md`). That is **structurally
   valid**. Completeness follows depth (**depth-complete** vs **fully complete** —
   [`SCHEMA.md`](SCHEMA.md)).
3. Walk [`PIPELINE.md`](PIPELINE.md) in order. Dependency meaning lives in
   SCHEMA: a `depends_on` target must be `partial` or `complete` before you
   *start*; it must not still be `stub` when you mark the dependent artifact
   `complete`.
4. Hold every `complete` artifact to [`QUALITY-BAR.md`](QUALITY-BAR.md).
5. Write only code you can trace to a design note this depth required.
6. Smoke-test the main path, or say you could not.
7. Report: what it does, how to run it, that it ran (or why not), class, depth,
   structural reasons, assumptions.

## Do not

- Load unselected skeletons or instructions "for context."
- Invent a stack the human did not name.
- Treat depth as a size or complexity score.
- Declare an artifact `complete` if it would read the same for a different system.
- Treat [`OPERATOR.md`](OPERATOR.md) as required.

That's the contract. The human says *what*. This repo says *how to stay honest
while you build it*.
