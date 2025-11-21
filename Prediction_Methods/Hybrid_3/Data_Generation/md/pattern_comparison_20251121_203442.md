# Pattern Comparison: Hybrid_2 vs Hybrid_3

## Summary

- **Hybrid_2 patterns:** 31
- **Hybrid_3 patterns:** 20
- **Removed patterns:** 11
- **New patterns:** 0

## Removed Patterns (Hybrid_2 → Hybrid_3)

### Pass-Through Parent Patterns (11)

1. `Hash → Aggregate (Outer)` [PT: Hash]
2. `Hash → Hash Join (Outer)` [PT: Hash]
3. `Hash → Index Only Scan (Outer)` [PT: Hash]
4. `Hash → Seq Scan (Outer)` [PT: Hash]
5. `Incremental Sort → Nested Loop (Outer)` [PT: Incremental Sort]
6. `Limit → Sort (Outer)` [PT: Limit]
7. `Merge Join → [Sort (Outer), Sort (Inner)]` [PT: Merge Join]
8. `Sort → Aggregate (Outer)` [PT: Sort]
9. `Sort → Hash Join (Outer)` [PT: Sort]
10. `Sort → Nested Loop (Outer)` [PT: Sort]
11. `Sort → Seq Scan (Outer)` [PT: Sort]

## Verification

- ✓ All removed patterns are Pass-Through parent patterns
- ✓ Pass-Through operators: Incremental Sort, Merge Join, Limit, Sort, Hash
