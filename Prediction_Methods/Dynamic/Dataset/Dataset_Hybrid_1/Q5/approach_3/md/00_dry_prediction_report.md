# Dry Prediction Report: Q5

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 266
- **Patterns Used:** 5
- **Reduction:** 98.1%

## Used Patterns

- `2724c08067c0...` Aggregate -> Gather Merge (Outer)
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `3cfa90d7df3c...` Nested Loop -> [Hash Join (Outer), Index Scan (Inner)]
- `3e2d5a00246f...` Sort -> Hash Join (Outer)
- `895c6e8c1a30...` Hash Join -> [Seq Scan (Outer), Hash (Inner)]

## Query Trees

### Plan 1 (Example: Q5_100_seed_812199069)

```
Node 6901 (Sort) - ROOT
  Node 6902 (Aggregate) [PATTERN ROOT]
    Node 6903 (Gather Merge) [consumed]
      Node 6904 (Aggregate)
        Node 6905 (Sort) [PATTERN ROOT]
          Node 6906 (Hash Join) [consumed]
            Node 6907 (Nested Loop) [PATTERN ROOT]
              Node 6908 (Hash Join) [consumed]
                Node 6909 (Seq Scan)
                Node 6910 (Hash)
                  Node 6911 (Hash Join) [PATTERN ROOT]
                    Node 6912 (Seq Scan) [consumed]
                    Node 6913 (Hash) [consumed]
                      Node 6914 (Hash Join) [PATTERN ROOT]
                        Node 6915 (Seq Scan) [consumed]
                        Node 6916 (Hash) [consumed]
                          Node 6917 (Seq Scan)
              Node 6918 (Index Scan) [consumed]
            Node 6919 (Hash) [PATTERN ROOT]
              Node 6920 (Seq Scan) [consumed]
```
