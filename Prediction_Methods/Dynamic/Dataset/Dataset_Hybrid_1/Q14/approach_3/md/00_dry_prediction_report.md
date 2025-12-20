# Dry Prediction Report: Q14

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 310
- **Patterns Used:** 2
- **Reduction:** 99.4%

## Used Patterns

- `4fc84c77ced1...` Aggregate -> Gather (Outer)
- `895c6e8c1a30...` Hash Join -> [Seq Scan (Outer), Hash (Inner)]

## Query Trees

### Plan 1 (Example: Q14_100_seed_812199069)

```
Node 26420 (Aggregate) [PATTERN ROOT] - ROOT
  Node 26421 (Gather) [consumed]
    Node 26422 (Aggregate)
      Node 26423 (Hash Join) [PATTERN ROOT]
        Node 26424 (Seq Scan) [consumed]
        Node 26425 (Hash) [consumed]
          Node 26426 (Seq Scan)
```
