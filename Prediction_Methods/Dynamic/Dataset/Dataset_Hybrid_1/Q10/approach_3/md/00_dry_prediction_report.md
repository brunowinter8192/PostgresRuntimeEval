# Dry Prediction Report: Q10

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 294
- **Patterns Used:** 2
- **Reduction:** 99.3%

## Used Patterns

- `25df29b5b698...` Limit -> Sort -> Aggregate -> Gather (Outer) (Outer) (Outer)
- `7a51ce50a8f4...` Hash Join -> [Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q10_100_seed_812199069)

```
Node 19370 (Limit) [PATTERN ROOT] - ROOT
  Node 19371 (Sort) [consumed]
    Node 19372 (Aggregate) [consumed]
      Node 19373 (Gather) [consumed]
        Node 19374 (Hash Join) [PATTERN ROOT]
          Node 19375 (Hash Join) [consumed]
            Node 19376 (Nested Loop) [consumed]
              Node 19377 (Seq Scan) [consumed]
              Node 19378 (Index Scan) [consumed]
            Node 19379 (Hash) [consumed]
              Node 19380 (Seq Scan) [consumed]
          Node 19381 (Hash) [consumed]
            Node 19382 (Seq Scan) [consumed]
```
