# Dry Prediction Report: Q12

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 302
- **Patterns Used:** 2
- **Reduction:** 99.3%

## Used Patterns

- `460af52cdecd...` Aggregate -> Gather Merge -> Aggregate -> Sort (Outer) (Outer) (Outer)
- `c53c43965386...` Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q12_100_seed_812199069)

```
Node 24320 (Aggregate) [PATTERN ROOT] - ROOT
  Node 24321 (Gather Merge) [consumed]
    Node 24322 (Aggregate) [consumed]
      Node 24323 (Sort) [consumed]
        Node 24324 (Nested Loop) [PATTERN ROOT]
          Node 24325 (Seq Scan) [consumed]
          Node 24326 (Index Scan) [consumed]
```
