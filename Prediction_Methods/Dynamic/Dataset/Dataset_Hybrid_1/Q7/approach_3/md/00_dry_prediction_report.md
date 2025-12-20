# Dry Prediction Report: Q7

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 289
- **Patterns Used:** 3
- **Reduction:** 99.0%

## Used Patterns

- `9d0e407c0aa5...` Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)]
- `a54055cece1a...` Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer)
- `b149ff282ebc...` Aggregate -> Gather Merge -> Sort -> Hash Join (Outer) (Outer) (Outer)

## Query Trees

### Plan 1 (Example: Q7_100_seed_812199069)

```
Node 10501 (Aggregate) [PATTERN ROOT] - ROOT
  Node 10502 (Gather Merge) [consumed]
    Node 10503 (Sort) [consumed]
      Node 10504 (Hash Join) [consumed]
        Node 10505 (Nested Loop) [PATTERN ROOT]
          Node 10506 (Hash Join) [consumed]
            Node 10507 (Seq Scan) [consumed]
            Node 10508 (Hash) [consumed]
              Node 10509 (Hash Join) [consumed]
                Node 10510 (Seq Scan) [consumed]
                Node 10511 (Hash) [consumed]
                  Node 10512 (Seq Scan)
          Node 10513 (Index Scan) [consumed]
        Node 10514 (Hash) [PATTERN ROOT]
          Node 10515 (Hash Join) [consumed]
            Node 10516 (Seq Scan) [consumed]
            Node 10517 (Hash) [consumed]
              Node 10518 (Seq Scan) [consumed]
```
