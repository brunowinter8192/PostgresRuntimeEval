# Dry Prediction Report: Q6

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 71
- **Patterns Used:** 1
- **Reduction:** 98.6%

## Used Patterns

- `a5f39f08c510...` Aggregate -> Gather -> Aggregate (Outer) (Outer)

## Query Trees

### Plan 1 (Example: Q6_100_seed_812199069)

```
Node 9901 (Aggregate) [PATTERN ROOT] - ROOT
  Node 9902 (Gather) [consumed]
    Node 9903 (Aggregate) [consumed]
      Node 9904 (Seq Scan)
```
