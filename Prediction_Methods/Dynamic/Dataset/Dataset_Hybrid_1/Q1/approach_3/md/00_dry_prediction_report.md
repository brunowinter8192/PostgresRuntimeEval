# Dry Prediction Report: Q1

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 307
- **Patterns Used:** 2
- **Reduction:** 99.3%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `2724c08067c0...` Aggregate -> Gather Merge (Outer)

## Query Trees

### Plan 1 (Example: Q1_100_seed_812199069)

```
Node 1 (Aggregate) [PATTERN ROOT] - ROOT
  Node 2 (Gather Merge) [consumed]
    Node 3 (Sort) [PATTERN ROOT]
      Node 4 (Aggregate) [consumed]
        Node 5 (Seq Scan)
```
