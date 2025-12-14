# Dry Prediction Report: Q13

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
| 7524c54c59c3... | Aggregate -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |