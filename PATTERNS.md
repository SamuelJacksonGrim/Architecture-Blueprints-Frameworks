# 🧭 PATTERNS — the reference bank

> A living log of patterns and anti-patterns spotted while studying companion
> repos, captured **as we go** so the learnings survive context resets and
> hand-offs. This is reference material that *feeds* the skeletons and the
> `QUALITY-BAR`; it is not itself a build artifact.

---

## Operating principle: **Capture forward, refine before merge**

Jot ideas as forward movement — write the observation down the moment it's seen,
even if it's rough or might be wrong. Keep open eyes on editability: every entry
here is **provisional and revisable**, dated, and may be corrected, refined, or
superseded before merge (same discipline as the empirical-ledger `DecisionLog`).
A half-formed note captured beats a sharp insight forgotten.

- **Capture** > polish. Get it on the page.
- **Date and source** every entry so it's traceable.
- **Refine in place** when a closer look changes the picture — mark what changed.
- **Negative findings count** — "this looked useful but isn't" saves the next pass.

---

## Skeleton candidates emerging
- **Observer / read-model** — background compute loop → cached snapshot →
  non-blocking read-only API. (source: unified-observer-architecture) — *strong*
- **Event Bus** — planned; do **not** source from unified-observer (stub). Wait
  for sovereign_manifold / ProjectSynapse instances.
- **Gateway / I-O adapter** — `sensory_input → encoder → translator → expression`
  boundary pipeline. (source: unified-observer-architecture) — *maybe*

---

## Repo entries

### unified-observer-architecture
- **Studied:** 2026-06-15 · **Status:** active
- **Role in its stack:** identity-observation layer; exposes a self-model over a
  read-only HTTP API (`/identity`) that sovereign_manifold polls.

**Patterns worth lifting**
- 🎯 **Observer / read-model server.** Background thread runs the system at a
  fixed rate, mirrors computed state into a lock-protected snapshot; API returns
  the cached snapshot and **never blocks on computation**. Genuinely reusable
  (telemetry, dashboards, CQRS read models, "expose live state" needs).
- **Adaptive-neutral via bounded history.** The emotional engine keeps a
  `deque(maxlen=1000)` and EMA-updates a baseline — a clean bounded-state idiom.
- **Cross-system contract with caps.** Consumers center each field at 0.5 and
  cap perturbation at `±0.05`/cycle — a tidy "bound before you inject" contract.

**Anti-patterns (great teaching material for QUALITY-BAR §8)**
- **Doc/code drift:** docs say the loop is 1 Hz (×3 places); code is `hz=10.0`.
- **Dead fields:** `memory_depth` and `biological_health` are documented in
  detail but **never written** by the loop — they sit at defaults forever.
- **Health check that lies:** the background loop has no error handling; if
  `step()` throws, the thread dies, `/identity` serves stale state, and
  `/health` still returns `ok`. Liveness is never verified.
- **Clamp at the edge only:** state can leave `[0,1]` internally; it's clamped
  only at the API boundary, not in the core.
- **Computed-then-discarded:** the emotional engine's output goes into
  `state.metadata`, which the `/identity` endpoint never returns.
- **Config not wired:** `system_config.yaml` thresholds aren't read by the code.

**Lessons → QUALITY-BAR**
- A health endpoint must reflect **loop liveness**, not just "HTTP is up."
- Don't document a field the system doesn't populate (drift is worse than a gap).
- Normalize/clamp **internally**, not only at the boundary.
- New principle candidate: **"bound before you inject; normalize before you
  compare"** (raw counts through a centering formula explode or collapse).

> **Revision note (eat our own dog food):** the first pass of this entry was
> written from the README/CLAUDE.md alone and was too generous — it called the
> EventBus a usable reference and repeated the "1 Hz" / live-biology claims. A
> second pass reading the *source* corrected all of that. Captured forward,
> refined before merge — exactly the principle above.

### relational_system_mc
- **Studied:** 2026-06-15 · **Status:** active
- **Role in its stack:** standalone mathematical certifier — derives the
  constants (e.g. `K_SCALE = 0.1418`) and proves the relational system is
  globally stable (single attractor, GAS). Not a service, not an architecture.

**Skeleton value:** none. Pure research/numerics — nothing to turn into a skeleton.

**Methodology worth lifting (this is why the repo isn't a zero)**
- 🎯 **Derived-constant provenance + re-derivation protocol.** Constants are
  *computed and certified*, not chosen; one repo is the authoritative source;
  downstream consumers are explicitly subordinate ("if they drift, this is
  correct"); and there's a checklist to re-validate before propagating. →
  folded into `QUALITY-BAR §5`.
- **Invariants justified by named failure modes.** FM1/FM2/FM3 are documented
  failure regimes, and each motivates a specific invariant (FM2 erosion → why
  `_MAX_DELTA = 0.05` exists). → strengthened `QUALITY-BAR §2`.
- **Independent validator.** The certifier has *zero* dependencies on the
  systems it certifies, by design — so it stays an honest check. → `QUALITY-BAR §5`.

**Lesson:** a repo can contribute real rigor without contributing a pattern.
Negative-on-skeletons is not negative-on-value. (Our own "negative findings
count" rule, applied.)
