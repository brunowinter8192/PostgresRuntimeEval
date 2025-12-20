# Dry Prediction Report: Q4

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 72 |
| Patterns Used | 3 |
| Reduction | 95.8% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 1d35fb978b37... | Sort -> Aggregate (Outer) |
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |