# Dry Prediction Report: Q8

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 72 |
| Patterns Used | 6 |
| Reduction | 91.7% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| 3e2d5a00246f... | Sort -> Hash Join (Outer) |
| 7df893ad48ca... | Hash -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |