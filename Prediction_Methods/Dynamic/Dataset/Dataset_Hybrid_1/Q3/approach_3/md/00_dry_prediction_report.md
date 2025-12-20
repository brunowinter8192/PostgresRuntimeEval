# Dry Prediction Report: Q3

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 293
- **Patterns Used:** 3
- **Reduction:** 99.0%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `3cfa90d7df3c...` Nested Loop -> [Hash Join (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q3_100_seed_812199069)

```
Node 4351 (Limit) - ROOT
  Node 4352 (Sort) [PATTERN ROOT]
    Node 4353 (Aggregate) [consumed]
      Node 4354 (Gather)
        Node 4355 (Nested Loop) [PATTERN ROOT]
          Node 4356 (Hash Join) [consumed]
            Node 4357 (Seq Scan)
            Node 4358 (Hash) [PATTERN ROOT]
              Node 4359 (Seq Scan) [consumed]
          Node 4360 (Index Scan) [consumed]
```
