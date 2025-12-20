# Dry Prediction Report: Q18

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 72 |
| Patterns Used | 5 |
| Reduction | 93.1% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 1d35fb978b37... | Sort -> Aggregate (Outer) |
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| 3e2d5a00246f... | Sort -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |
| e296a71f8301... | Limit -> Sort (Outer) |