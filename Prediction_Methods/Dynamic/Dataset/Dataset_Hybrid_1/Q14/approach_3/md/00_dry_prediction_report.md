# Dry Prediction Report: Q14

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 1
- **Total Patterns Available:** 69
- **Patterns Used:** 1
- **Reduction:** 98.6%

## Used Patterns

- `310134da512a...` Aggregate -> Gather -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash (Inner)] (Outer) (Outer) (Outer)

## Query Trees

### Plan 1 (Example: Q14_100_seed_812199069)

```
Node 26420 (Aggregate) [PATTERN ROOT] - ROOT
  Node 26421 (Gather) [consumed]
    Node 26422 (Aggregate) [consumed]
      Node 26423 (Hash Join) [consumed]
        Node 26424 (Seq Scan) [consumed]
        Node 26425 (Hash) [consumed]
          Node 26426 (Seq Scan)
```
