# Dry Prediction Report: Q10

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 294
- **Patterns Used:** 3
- **Reduction:** 99.0%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `c53c43965386...` Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q10_100_seed_812199069)

```
Node 19370 (Limit) - ROOT
  Node 19371 (Sort) [PATTERN ROOT]
    Node 19372 (Aggregate) [consumed]
      Node 19373 (Gather)
        Node 19374 (Hash Join)
          Node 19375 (Hash Join)
            Node 19376 (Nested Loop) [PATTERN ROOT]
              Node 19377 (Seq Scan) [consumed]
              Node 19378 (Index Scan) [consumed]
            Node 19379 (Hash) [PATTERN ROOT]
              Node 19380 (Seq Scan) [consumed]
          Node 19381 (Hash) [PATTERN ROOT]
            Node 19382 (Seq Scan) [consumed]
```
