# Dry Prediction Report: Q9

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 2 |
| Total Patterns Available | 67 |
| Patterns Used | 8 |
| Reduction | 88.1% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 1d35fb978b37... | Sort -> Aggregate (Outer) |
| 2e0f44eff91c... | Hash Join -> [Nested Loop (Outer), Hash (Inner)] |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| 634cdbe24fda... | Gather -> Aggregate (Outer) |
| 7df893ad48ca... | Hash -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |