# Dry Prediction Report: Q14

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 191 |
| Patterns Used | 3 |
| Reduction | 98.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 4fc84c77ced1... | Aggregate -> Gather (Outer) |
| 7524c54c59c3... | Aggregate -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |