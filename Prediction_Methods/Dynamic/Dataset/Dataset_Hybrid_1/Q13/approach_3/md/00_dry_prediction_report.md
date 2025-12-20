# Dry Prediction Report: Q13

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 299
- **Patterns Used:** 2
- **Reduction:** 99.3%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `895c6e8c1a30...` Hash Join -> [Seq Scan (Outer), Hash (Inner)]

## Query Trees

### Plan 1 (Example: Q13_100_seed_812199069)

```
Node 25370 (Sort) [PATTERN ROOT] - ROOT
  Node 25371 (Aggregate) [consumed]
    Node 25372 (Aggregate)
      Node 25373 (Hash Join) [PATTERN ROOT]
        Node 25374 (Seq Scan) [consumed]
        Node 25375 (Hash) [consumed]
          Node 25376 (Index Only Scan)
```
