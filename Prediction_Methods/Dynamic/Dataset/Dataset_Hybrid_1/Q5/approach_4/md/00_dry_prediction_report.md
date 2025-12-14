# Dry Prediction Report: Q5

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 173 |
| Patterns Used | 7 |
| Reduction | 96.0% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| 2e0f44eff91c... | Hash Join -> [Nested Loop (Outer), Hash (Inner)] |
| 3754655cfe1a... | Aggregate -> Sort (Outer) |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| 7df893ad48ca... | Hash -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |