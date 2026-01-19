# Dry Prediction Report: Q3

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 71
- **Patterns Used:** 2
- **Reduction:** 97.2%

## Used Patterns

- `b3a450934720...` Sort -> Aggregate -> Gather (Outer) (Outer)
- `f4cb205adfd1...` Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q3_100_seed_812199069)

```
Node 4351 (Limit) - ROOT
  Node 4352 (Sort) [PATTERN ROOT]
    Node 4353 (Aggregate) [consumed]
      Node 4354 (Gather) [consumed]
        Node 4355 (Nested Loop)
          Node 4356 (Hash Join) [PATTERN ROOT]
            Node 4357 (Seq Scan) [consumed]
            Node 4358 (Hash) [consumed]
              Node 4359 (Seq Scan) [consumed]
          Node 4360 (Index Scan)
```
