# 🤝 Contributing

This repo is meant to grow — new skeletons, new examples, a richer schema. Here's
how to add to it without breaking the consistency that makes it valuable.

## Adding a new skeleton

A skeleton is a reusable *pattern* (an agent loop, an event bus, an ETL job…).

1. Create `skeletons/<your-pattern>/`.
2. Instantiate **all 10 artifacts** from `templates/` (the Instantiation Rule
   applies to skeletons too — see `SCHEMA.md`).
3. Walk `PIPELINE.md` to fill them. At minimum, ship the baseline `complete`.
4. Add a `DecisionLog` entry for the load-bearing choices that *define* the
   pattern — that's what a future reader needs most.
5. Register it in the catalog table in the root `README.md`.

## Adding a variant (the delta/inheritance pattern)

When a new pattern is *mostly* an existing skeleton with one key difference,
don't copy all 10 artifacts. Follow the model in `skeletons/agents/`:

- Pick a **base** skeleton that is fully worked (e.g. `agents/react/`).
- Create the variant folder with **only the artifacts that change** — usually
  `README.md`, `Flows.md`, one `DecisionLog.md` entry, and a diagram.
- In the variant's frontmatter, point `depends_on` at the base's artifacts.
- State clearly in the variant README: *"variant + base = one complete
  10-artifact system."*

Rationale: the *difference* is the lesson. Four near-identical full copies bury
it; a focused delta makes it legible. (See `skeletons/agents/README.md`.)

## Adding an example

An example is a *generated build* for one concrete idea (not a reusable pattern).
Put it in `examples/<idea>/`, following the layout of `examples/webscraper/`:
filled `architecture/` (all 10), a `ProjectStructure.md`, and the code.

## Extending the schema

The 10 artifact names are **closed** — resist adding an 11th. If something seems
to need a new artifact, it almost always belongs *inside* an existing one. If you
genuinely believe the ontology must change, that itself is a `D-XXX` decision:
propose it, log the reasoning, and update `SCHEMA.md` (the single source of
truth) plus every template in lockstep.

## The one rule above all

**Keep the ten artifacts consistent across everything.** A `Contracts.md` here
must mean the same thing as a `Contracts.md` there. That sameness is the entire
value of the repo — guard it.
