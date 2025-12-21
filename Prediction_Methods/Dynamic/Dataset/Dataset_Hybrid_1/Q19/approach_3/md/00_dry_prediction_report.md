# Dry Prediction Report: Q19

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 310
- **Patterns Used:** 1
- **Reduction:** 99.7%

## Used Patterns

- `310134da512a...` Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Outer) (Outer)

## Query Trees

### Plan 1 (Example: Q19_100_seed_812199069)

```
Node 31220 (Aggregate) [PATTERN ROOT] - ROOT
  Node 31221 (Gather) [consumed]
    Node 31222 (Aggregate) [consumed]
      Node 31223 (Hash Join) [consumed]
        Node 31224 (Seq Scan) [consumed]
        Node 31225 (Hash) [consumed]
          Node 31226 (Seq Scan)
```
