# Dry Prediction Report: Q12

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 187 |
| Patterns Used | 3 |
| Reduction | 98.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| 3754655cfe1a... | Aggregate -> Sort (Outer) |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |