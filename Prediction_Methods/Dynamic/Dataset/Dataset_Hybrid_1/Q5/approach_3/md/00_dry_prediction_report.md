# Dry Prediction Report: Q5

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 266
- **Patterns Used:** 2
- **Reduction:** 99.2%

## Used Patterns

- `460af52cdecd...` Aggregate -> Gather Merge -> Aggregate -> Sort (Outer) (Outer) (Outer)
- `a95bee4e9ae5...` Hash Join -> [Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer) (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q5_100_seed_812199069)

```
Node 6901 (Sort) - ROOT
  Node 6902 (Aggregate) [PATTERN ROOT]
    Node 6903 (Gather Merge) [consumed]
      Node 6904 (Aggregate) [consumed]
        Node 6905 (Sort) [consumed]
          Node 6906 (Hash Join) [PATTERN ROOT]
            Node 6907 (Nested Loop) [consumed]
              Node 6908 (Hash Join) [consumed]
                Node 6909 (Seq Scan) [consumed]
                Node 6910 (Hash) [consumed]
                  Node 6911 (Hash Join) [consumed]
                    Node 6912 (Seq Scan) [consumed]
                    Node 6913 (Hash) [consumed]
                      Node 6914 (Hash Join) [consumed]
                        Node 6915 (Seq Scan) [consumed]
                        Node 6916 (Hash) [consumed]
                          Node 6917 (Seq Scan) [consumed]
              Node 6918 (Index Scan) [consumed]
            Node 6919 (Hash) [consumed]
              Node 6920 (Seq Scan) [consumed]
```
