# Dry Prediction Report: Q19

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

### Plan 1 (Example: Q19_100_seed_812199069)

```
Node 31220 (Aggregate) [PATTERN ROOT] - ROOT
  Node 31221 (Gather) [consumed]
    Node 31222 (Aggregate)
      Node 31223 (Hash Join) [PATTERN ROOT]
        Node 31224 (Seq Scan) [consumed]
        Node 31225 (Hash) [consumed]
          Node 31226 (Seq Scan)
```
