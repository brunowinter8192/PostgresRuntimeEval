# Dry Prediction Report: Q1

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 307
- **Patterns Used:** 1
- **Reduction:** 99.7%

## Used Patterns

- `f8231c4dd4c5...` Aggregate -> Gather Merge -> Sort -> Aggregate (Outer) (Outer) (Outer)

## Query Trees

### Plan 1 (Example: Q1_100_seed_812199069)

```
Node 1 (Aggregate) [PATTERN ROOT] - ROOT
  Node 2 (Gather Merge) [consumed]
    Node 3 (Sort) [consumed]
      Node 4 (Aggregate) [consumed]
        Node 5 (Seq Scan)
```
