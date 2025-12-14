# Dry Prediction Report: Q3

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 186 |
| Patterns Used | 3 |
| Reduction | 98.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| 4fc84c77ced1... | Aggregate -> Gather (Outer) |