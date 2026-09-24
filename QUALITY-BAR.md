# 🎯 QUALITY-BAR — rigor when you call something complete

Load this when marking an artifact `complete` and at self-audit. It is not part
of the SELECTOR upfront load list.

---

## 1. Specificity over boilerplate
A `complete` artifact describes *this* system. If it would read the same for a
different system, it isn't done.

## 2. Name the invariants that look optional but aren't
Subtle breakage, not loud errors. Each with the failure mode it prevents.

## 3. Guardrails name the prohibition *and* the legitimate alternative

## 4. One authority per kind of decision
Everyone else produces input.

## 5. Constants carry provenance
Derived values name their source and a re-derivation check. Validators stay independent.

## 6. Observe-only paths stay one-way
A metric must not become a control input.

## 7. DecisionLog records why, titled as the question
Append-only. Supersede, never rewrite.

## 8. Docs match reality in the same change

## 9. Prove the main path or disclose that you could not
"Wrote it" and "it ran" are different claims.

---

Glue code does not need a paragraph here. Behaviorally significant decisions do.
