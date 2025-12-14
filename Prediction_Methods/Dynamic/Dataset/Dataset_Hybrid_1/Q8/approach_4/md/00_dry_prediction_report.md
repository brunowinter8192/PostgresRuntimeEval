# Dry Prediction Report: Q8

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 166 |
| Patterns Used | 6 |
| Reduction | 96.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2724c08067c0... | Aggregate -> Gather Merge (Outer) |
| 2e0f44eff91c... | Hash Join -> [Nested Loop (Outer), Hash (Inner)] |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| 7df893ad48ca... | Hash -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |