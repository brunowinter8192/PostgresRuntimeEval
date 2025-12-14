# Dry Prediction Report: Q3

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 71 |
| Patterns Used | 4 |
| Reduction | 94.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 1d35fb978b37... | Sort -> Aggregate (Outer) |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| e296a71f8301... | Limit -> Sort (Outer) |