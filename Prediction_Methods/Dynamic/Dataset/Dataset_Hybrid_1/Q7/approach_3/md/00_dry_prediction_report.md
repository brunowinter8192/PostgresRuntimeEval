# Dry Prediction Report: Q7

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 289
- **Patterns Used:** 4
- **Reduction:** 98.6%

## Used Patterns

- `2724c08067c0...` Aggregate -> Gather Merge (Outer)
- `3cfa90d7df3c...` Nested Loop -> [Hash Join (Outer), Index Scan (Inner)]
- `3e2d5a00246f...` Sort -> Hash Join (Outer)
- `895c6e8c1a30...` Hash Join -> [Seq Scan (Outer), Hash (Inner)]

## Query Trees

### Plan 1 (Example: Q7_100_seed_812199069)

```
Node 10501 (Aggregate) [PATTERN ROOT] - ROOT
  Node 10502 (Gather Merge) [consumed]
    Node 10503 (Sort) [PATTERN ROOT]
      Node 10504 (Hash Join) [consumed]
        Node 10505 (Nested Loop) [PATTERN ROOT]
          Node 10506 (Hash Join) [consumed]
            Node 10507 (Seq Scan)
            Node 10508 (Hash)
              Node 10509 (Hash Join) [PATTERN ROOT]
                Node 10510 (Seq Scan) [consumed]
                Node 10511 (Hash) [consumed]
                  Node 10512 (Seq Scan)
          Node 10513 (Index Scan) [consumed]
        Node 10514 (Hash)
          Node 10515 (Hash Join) [PATTERN ROOT]
            Node 10516 (Seq Scan) [consumed]
            Node 10517 (Hash) [consumed]
              Node 10518 (Seq Scan)
```
