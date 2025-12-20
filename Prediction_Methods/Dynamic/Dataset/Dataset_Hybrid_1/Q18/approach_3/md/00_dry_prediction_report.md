# Dry Prediction Report: Q18

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 250
- **Patterns Used:** 3
- **Reduction:** 98.8%

## Used Patterns

- `2724c08067c0...` Aggregate -> Gather Merge (Outer)
- `895c6e8c1a30...` Hash Join -> [Seq Scan (Outer), Hash (Inner)]
- `e296a71f8301...` Limit -> Sort (Outer)

## Query Trees

### Plan 1 (Example: Q18_100_seed_812199069)

```
Node 28820 (Limit) [PATTERN ROOT] - ROOT
  Node 28821 (Sort) [consumed]
    Node 28822 (Aggregate) [PATTERN ROOT]
      Node 28823 (Gather Merge) [consumed]
        Node 28824 (Incremental Sort)
          Node 28825 (Nested Loop)
            Node 28826 (Merge Join)
              Node 28827 (Sort)
                Node 28828 (Hash Join) [PATTERN ROOT]
                  Node 28829 (Seq Scan) [consumed]
                  Node 28830 (Hash) [consumed]
                    Node 28831 (Aggregate)
                      Node 28832 (Index Scan)
              Node 28833 (Sort)
                Node 28834 (Seq Scan)
            Node 28835 (Index Scan)
```
