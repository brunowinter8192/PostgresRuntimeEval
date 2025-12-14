# Dry Prediction Report: Q10

## Summary

| Metric | Value |
|--------|-------|
| Total Test Queries | 150 |
| Unique Plan Structures | 1 |
| Total Patterns Available | 187 |
| Patterns Used | 5 |
| Reduction | 97.3% |

## Used Patterns

| Hash | Pattern |
|------|---------|
| 2e0f44eff91c... | Hash Join -> [Nested Loop (Outer), Hash (Inner)] |
| 3aab37bea1a8... | Hash -> Seq Scan (Outer) |
| 4fc84c77ced1... | Aggregate -> Gather (Outer) |
| 7d4e78be8512... | Hash Join -> [Hash Join (Outer), Hash (Inner)] |
| c53c43965386... | Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] |