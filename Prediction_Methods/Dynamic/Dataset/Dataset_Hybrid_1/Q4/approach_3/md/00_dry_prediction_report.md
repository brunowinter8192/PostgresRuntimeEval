# Dry Prediction Report: Q4

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 302
- **Patterns Used:** 3
- **Reduction:** 99.0%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `2724c08067c0...` Aggregate -> Gather Merge (Outer)
- `c53c43965386...` Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q4_100_seed_812199069)

```
Node 5851 (Aggregate) [PATTERN ROOT] - ROOT
  Node 5852 (Gather Merge) [consumed]
    Node 5853 (Sort) [PATTERN ROOT]
      Node 5854 (Aggregate) [consumed]
        Node 5855 (Nested Loop) [PATTERN ROOT]
          Node 5856 (Seq Scan) [consumed]
          Node 5857 (Index Scan) [consumed]
```
