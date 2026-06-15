# System Flow — Tree-of-Thoughts

Branch, score, keep the best, prune the rest, repeat.

```
Goal
 │
 ▼
ROOT ──┬──▶ thought A  (score 0.8)  ──┬──▶ A1 (0.9) ──▶ … ──▶ solution ✅
       │                              └──▶ A2 (0.3) ✗ pruned
       ├──▶ thought B  (score 0.6)  ──────▶ B1 (0.5) … (kept on frontier)
       └──▶ thought C  (score 0.2) ✗ pruned

  pick the best node on the frontier each round; drop dead ends (= backtrack);
  stop at a solution or when the search budget runs out.
```
