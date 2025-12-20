# Dry Prediction Report: Q6

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 308
- **Patterns Used:** 2
- **Reduction:** 99.4%

## Used Patterns

- `184f44dea835...` Aggregate -> Seq Scan (Outer)
- `4fc84c77ced1...` Aggregate -> Gather (Outer)

## Query Trees

### Plan 1 (Example: Q6_100_seed_812199069)

```
Node 9901 (Aggregate) [PATTERN ROOT] - ROOT
  Node 9902 (Gather) [consumed]
    Node 9903 (Aggregate) [PATTERN ROOT]
      Node 9904 (Seq Scan) [consumed]
```
