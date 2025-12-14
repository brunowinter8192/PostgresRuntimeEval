# Dry Prediction Report: Q9

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 2 |
| Total Patterns Available | 151 |
| Patterns Used | 10 |
| Reduction | 93.4% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2e0f44eff91c... | Hash Join -> [Nested Loop (Outer), Hash (Inner)] |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 3b44787560c6... | Aggregate -> Nested Loop (Outer) |
| 3cfa90d7df3c... | Nested Loop -> [Hash Join (Outer), Index Scan (Inner)] |
| 4fc84c77ced1... | Aggregate -> Gather (Outer) |
| 7524c54c59c3... | Aggregate -> Hash Join (Outer) |
| 7d4e78be8512... | Hash Join -> [Hash Join (Outer), Hash (Inner)] |
| 7df893ad48ca... | Hash -> Hash Join (Outer) |
| 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |