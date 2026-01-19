# Dry Prediction Report: Q5

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 52
- **Patterns Used:** 5
- **Reduction:** 90.4%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `3e2d5a00246f...` Sort -> Hash Join (Outer)
- `9d0e407c0aa5...` Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)]
- `f4cb205adfd1...` Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q5_100_seed_812199069)

```
Node 6901 (Sort) [PATTERN ROOT] - ROOT
  Node 6902 (Aggregate) [consumed]
    Node 6903 (Gather Merge)
      Node 6904 (Aggregate)
        Node 6905 (Sort) [PATTERN ROOT]
          Node 6906 (Hash Join) [consumed]
            Node 6907 (Nested Loop) [PATTERN ROOT]
              Node 6908 (Hash Join) [consumed]
                Node 6909 (Seq Scan) [consumed]
                Node 6910 (Hash) [consumed]
                  Node 6911 (Hash Join) [consumed]
                    Node 6912 (Seq Scan) [consumed]
                    Node 6913 (Hash) [consumed]
                      Node 6914 (Hash Join) [PATTERN ROOT]
                        Node 6915 (Seq Scan) [consumed]
                        Node 6916 (Hash) [consumed]
                          Node 6917 (Seq Scan) [consumed]
              Node 6918 (Index Scan) [consumed]
            Node 6919 (Hash) [PATTERN ROOT]
              Node 6920 (Seq Scan) [consumed]
```
