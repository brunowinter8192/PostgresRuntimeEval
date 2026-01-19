# Dry Prediction Report: Q8

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 53
- **Patterns Used:** 5
- **Reduction:** 90.6%

## Used Patterns

- `29ee00dbeea6...` Aggregate -> Gather Merge -> Sort (Outer) (Outer)
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `3cfa90d7df3c...` Nested Loop -> [Hash Join (Outer), Index Scan (Inner)]
- `9d0e407c0aa5...` Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)]
- `f4cb205adfd1...` Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q8_100_seed_812199069)

```
Node 13201 (Aggregate) [PATTERN ROOT] - ROOT
  Node 13202 (Gather Merge) [consumed]
    Node 13203 (Sort) [consumed]
      Node 13204 (Hash Join)
        Node 13205 (Nested Loop) [PATTERN ROOT]
          Node 13206 (Hash Join) [consumed]
            Node 13207 (Nested Loop) [PATTERN ROOT]
              Node 13208 (Hash Join) [consumed]
                Node 13209 (Seq Scan) [consumed]
                Node 13210 (Hash) [consumed]
                  Node 13211 (Hash Join) [consumed]
                    Node 13212 (Seq Scan) [consumed]
                    Node 13213 (Hash) [consumed]
                      Node 13214 (Hash Join) [PATTERN ROOT]
                        Node 13215 (Seq Scan) [consumed]
                        Node 13216 (Hash) [consumed]
                          Node 13217 (Seq Scan) [consumed]
              Node 13218 (Index Scan) [consumed]
            Node 13219 (Hash) [PATTERN ROOT]
              Node 13220 (Seq Scan) [consumed]
          Node 13221 (Index Scan) [consumed]
        Node 13222 (Hash) [PATTERN ROOT]
          Node 13223 (Seq Scan) [consumed]
```
