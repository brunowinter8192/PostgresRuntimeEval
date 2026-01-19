# Dry Prediction Report: Q12

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 67
- **Patterns Used:** 2
- **Reduction:** 97.0%

## Used Patterns

- `2724c08067c0...` Aggregate -> Gather Merge (Outer)
- `c53c43965386...` Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q12_100_seed_812199069)

```
Node 24320 (Aggregate) [PATTERN ROOT] - ROOT
  Node 24321 (Gather Merge) [consumed]
    Node 24322 (Aggregate)
      Node 24323 (Sort)
        Node 24324 (Nested Loop) [PATTERN ROOT]
          Node 24325 (Seq Scan) [consumed]
          Node 24326 (Index Scan) [consumed]
```
