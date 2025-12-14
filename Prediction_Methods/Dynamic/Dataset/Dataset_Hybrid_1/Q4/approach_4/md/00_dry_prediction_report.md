# Dry Prediction Report: Q4

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 188 |
| Patterns Used | 3 |
| Reduction | 98.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| 3b44787560c6... | Aggregate -> Nested Loop (Outer) |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |