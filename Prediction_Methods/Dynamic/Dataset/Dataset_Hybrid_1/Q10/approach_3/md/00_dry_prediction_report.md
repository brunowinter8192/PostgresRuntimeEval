# Dry Prediction Report: Q10

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 67 |
| Patterns Used | 5 |
| Reduction | 92.5% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 1d35fb978b37... | Sort -> Aggregate (Outer) |
| 2e0f44eff91c... | Hash Join -> [Nested Loop (Outer), Hash (Inner)] |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |
| e296a71f8301... | Limit -> Sort (Outer) |