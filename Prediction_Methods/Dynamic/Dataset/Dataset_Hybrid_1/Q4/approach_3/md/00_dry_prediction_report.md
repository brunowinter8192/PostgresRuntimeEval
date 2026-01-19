# Dry Prediction Report: Q4

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 69
- **Patterns Used:** 2
- **Reduction:** 97.1%

## Used Patterns

- `29ee00dbeea6...` Aggregate -> Gather Merge -> Sort (Outer) (Outer)
- `c53c43965386...` Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q4_100_seed_812199069)

```
Node 5851 (Aggregate) [PATTERN ROOT] - ROOT
  Node 5852 (Gather Merge) [consumed]
    Node 5853 (Sort) [consumed]
      Node 5854 (Aggregate)
        Node 5855 (Nested Loop) [PATTERN ROOT]
          Node 5856 (Seq Scan) [consumed]
          Node 5857 (Index Scan) [consumed]
```
