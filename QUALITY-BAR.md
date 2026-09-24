# 🎯 QUALITY-BAR — rigor when you call something complete

Consult this when marking an artifact `complete` and at self-audit.
It is **not** part of the SELECTOR upfront load list.

---

## 1. Specificity over boilerplate
A `complete` artifact describes *this* system — real names, numbers, thresholds.

- ❌ "The system validates input and handles errors."
- ✅ "A request over 10 MB is rejected with 413 before parsing; a malformed body returns 400 and is never written to the queue."

If an artifact would read the same for a different system, it isn't done.

## 2. Name the invariants that look optional but aren't
Subtle breakage, not loud errors. Each with *why* and the failure it prevents.

- ✅ "The cache key must include the tenant id. Omit it and tenant A silently serves tenant B's data."
- ✅ "Retry backoff must be capped. Without a ceiling, a downstream outage becomes a retry storm."

## 3. Guardrails name the prohibition and the legitimate alternative

- ✅ "Don't write to the orders table from a handler — emit `OrderPlaced`; the projector owns that table."

## 4. One authority per kind of decision
Everyone else produces input. Diffuse authority is how systems drift.

## 5. Constants carry provenance
Record the number once. If derived, name the source and how to re-derive. A validator must not depend on the system it certifies.

## 6. Observe-only paths stay one-way
A dashboard number must not become a control signal.

## 7. DecisionLog records why, titled as the question
Append-only. Supersede, never rewrite. Continuous and selective — scope in `SCHEMA.md`.
A log of every edit is a failed log.

## 8. Docs match reality in the same change
A drifted artifact lies with authority.

## 9. Prove the main path, or disclose that you could not
"Wrote it" and "it ran" are different claims.

---

Behaviorally significant decisions belong here. Glue does not need a paragraph.
