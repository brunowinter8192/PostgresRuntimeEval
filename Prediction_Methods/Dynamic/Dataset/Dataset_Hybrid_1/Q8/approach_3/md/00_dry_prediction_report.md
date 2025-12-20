# Dry Prediction Report: Q8

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 268
- **Patterns Used:** 2
- **Reduction:** 99.3%

## Used Patterns

- `53f9aa07d736...` Aggregate -> Gather Merge -> Sort -> Hash Join -> [Nested Loop (Outer), Hash (Inner)] (Outer) (Outer) (Outer)
- `a95bee4e9ae5...` Hash Join -> [Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer) (Inner)] (Outer) (Inner)] (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q8_100_seed_812199069)

```
Node 13201 (Aggregate) [PATTERN ROOT] - ROOT
  Node 13202 (Gather Merge) [consumed]
    Node 13203 (Sort) [consumed]
      Node 13204 (Hash Join) [consumed]
        Node 13205 (Nested Loop) [consumed]
          Node 13206 (Hash Join) [PATTERN ROOT]
            Node 13207 (Nested Loop) [consumed]
              Node 13208 (Hash Join) [consumed]
                Node 13209 (Seq Scan) [consumed]
                Node 13210 (Hash) [consumed]
                  Node 13211 (Hash Join) [consumed]
                    Node 13212 (Seq Scan) [consumed]
                    Node 13213 (Hash) [consumed]
                      Node 13214 (Hash Join) [consumed]
                        Node 13215 (Seq Scan) [consumed]
                        Node 13216 (Hash) [consumed]
                          Node 13217 (Seq Scan) [consumed]
              Node 13218 (Index Scan) [consumed]
            Node 13219 (Hash) [consumed]
              Node 13220 (Seq Scan) [consumed]
          Node 13221 (Index Scan)
        Node 13222 (Hash) [consumed]
          Node 13223 (Seq Scan)
```
