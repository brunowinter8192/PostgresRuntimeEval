# Dry Prediction Report: Q1

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 69
- **Patterns Used:** 1
- **Reduction:** 98.6%

## Used Patterns

- `29ee00dbeea6...` Aggregate -> Gather Merge -> Sort (Outer) (Outer)

## Query Trees

### Plan 1 (Example: Q1_100_seed_812199069)

```
Node 1 (Aggregate) [PATTERN ROOT] - ROOT
  Node 2 (Gather Merge) [consumed]
    Node 3 (Sort) [consumed]
      Node 4 (Aggregate)
        Node 5 (Seq Scan)
```
