# Pattern Selection Report

**Strategy:** size
**Generated:** 2025-12-17 19:26:42

## Summary

**Total Patterns:** 6
**Selected:** 2
**Rejected:** 2
**Skipped (Low Error):** 2
**Skipped (No FFS):** 0
**Skipped (Low Template Count):** 0

**Initial MRE:** 22.97%
**Final MRE:** 20.68%
**Improvement:** 2.29%

## Operator Baseline MRE

| Operator | Mean MRE (%) | Count |
|----------|--------------|-------|
| Hash | 16958.0 | 556 |
| Seq Scan | 9870.8 | 868 |
| Hash Join | 4268.8 | 556 |
| Sort | 114.1 | 336 |
| Index Scan | 104.8 | 284 |
| Nested Loop | 60.3 | 260 |
| Limit | 55.9 | 72 |
| Aggregate | 15.1 | 576 |
| Gather Merge | 15.0 | 168 |
| Gather | 13.1 | 144 |
| Index Only Scan | 3.0 | 24 |
| Incremental Sort | 0.6 | 24 |
| Merge Join | 0.6 | 24 |

## Iteration Log

### Iteration 0: Hash -> Seq Scan (Outer)

**Pattern Hash:** `3aab37bea1a884da206eb32f2c1ae5ba`
**Operator Count:** 2
**Occurrences:** 336

**Root Operator:** Hash
**Operator MRE:** 26213.6%
**Check:** 26213.6% > 10% threshold -> EVALUATE

**MRE Before:** 22.97%
**MRE After:** 21.18%
**Delta:** -1.79%
**Status:** SELECTED

### Iteration 1: Sort -> Aggregate (Outer)

**Pattern Hash:** `1d35fb978b379d4a820897907e56ab7b`
**Operator Count:** 2
**Occurrences:** 192

**Root Operator:** Sort
**Operator MRE:** 15.5%
**Check:** 15.5% > 10% threshold -> EVALUATE

**MRE Before:** 21.18%
**MRE After:** 20.68%
**Delta:** -0.49%
**Status:** SELECTED

### Iteration 2: Hash -> Hash Join (Outer)

**Pattern Hash:** `7df893ad48ca148008fc536ad76ff48a`
**Operator Count:** 2
**Occurrences:** 172

**Root Operator:** Hash
**Operator MRE:** 3573.9%
**Check:** 3573.9% > 10% threshold -> EVALUATE

**MRE Before:** 20.68%
**MRE After:** 20.68%
**Delta:** +0.00%
**Status:** REJECTED

### Iteration 3: Aggregate -> Gather Merge (Outer)

**Pattern Hash:** `2724c08067c017e6455632f46231780c`
**Operator Count:** 2
**Occurrences:** 168

**Root Operator:** Aggregate
**Operator MRE:** 8.7%
**Check:** 8.7% < 10% threshold
**Status:** SKIPPED_LOW_ERROR

### Iteration 4: Aggregate -> Gather (Outer)

**Pattern Hash:** `4fc84c77ced18a46514c982f23f12deb`
**Operator Count:** 2
**Occurrences:** 144

**Root Operator:** Aggregate
**Operator MRE:** 18.0%
**Check:** 18.0% > 10% threshold -> EVALUATE

**MRE Before:** 20.68%
**MRE After:** 21.55%
**Delta:** +0.87%
**Status:** REJECTED

### Iteration 5: Gather Merge -> Sort (Outer)

**Pattern Hash:** `1691f6f0dbbde049f7f6b5d065d62f74`
**Operator Count:** 2
**Occurrences:** 96

**Root Operator:** Gather Merge
**Operator MRE:** 8.8%
**Check:** 8.8% < 10% threshold
**Status:** SKIPPED_LOW_ERROR

## Collision Log

No collisions detected.
