# 🏗️ GENERATOR — idea to a working build

The human says one sentence. You design at the right depth, then write code
that has been run — or say you could not.

**Load order is [`SELECTOR.md`](SELECTOR.md) Step D. Do not restate it here.**

---

## Before you start

Follow SELECTOR end to end, then the fill order in [`PIPELINE.md`](PIPELINE.md).
Compressing fill *order* is a failure. Filling all ten to `complete` at `thin`
depth is also a failure.

If you need a stack the human did not name: smallest that can pass a smoke test,
`DecisionLog` entry, shown to the human. Allowed to decide. Not allowed to hide.

---

## Outputs

1. Design notes at the chosen depth
2. `ProjectStructure.md` + real folders
3. Code + plain-English how to run it

---

## After SELECTOR

1. Instantiate all ten stubs + `INTENT.md`.
2. Fill required artifacts in PIPELINE order.
3. Derive the tree (Modules, or Architecture + Flows at thin depth).
4. Write traceable code.
5. Smoke-test or disclose that you could not.
6. Report in the human's language, including any stack you chose.

---

## Done looks like

```
<project>/
├── INTENT.md
├── README.md
├── architecture/
├── ProjectStructure.md
└── src/          ← real code, not .keep files
```

[`examples/webscraper/`](examples/webscraper/) is design-only. Do not treat it
as a running build.
