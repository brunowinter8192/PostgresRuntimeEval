# Dry Prediction Report: Q9

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 2
- **Total Patterns Available:** 303
- **Patterns Used:** 5
- **Reduction:** 98.3%

## Used Patterns

- `2873b8c3a175...` Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)]
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `a5f39f08c510...` Aggregate -> Gather -> Aggregate (Outer) (Outer)
- `bd9dfa7bb8f3...` Nested Loop -> [Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer), Index Scan (Inner)]
- `ec92bdaa27b4...` Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer) (Inner)]

## Query Trees

### Plan 1 (Example: Q9_100_seed_812199069)

```
Node 16651 (Sort) - ROOT
  Node 16652 (Aggregate) [PATTERN ROOT]
    Node 16653 (Gather) [consumed]
      Node 16654 (Aggregate) [consumed]
        Node 16655 (Hash Join) [PATTERN ROOT]
          Node 16656 (Seq Scan) [consumed]
          Node 16657 (Hash) [consumed]
            Node 16658 (Hash Join) [consumed]
              Node 16659 (Seq Scan) [consumed]
              Node 16660 (Hash) [consumed]
                Node 16661 (Hash Join) [consumed]
                  Node 16662 (Hash Join) [PATTERN ROOT]
                    Node 16663 (Nested Loop) [consumed]
                      Node 16664 (Seq Scan) [consumed]
                      Node 16665 (Index Scan) [consumed]
                    Node 16666 (Hash) [consumed]
                      Node 16667 (Seq Scan) [consumed]
                  Node 16668 (Hash) [PATTERN ROOT]
                    Node 16669 (Seq Scan) [consumed]
```

### Plan 2 (Example: Q9_101_seed_820403100)

```
Node 16670 (Sort) - ROOT
  Node 16671 (Aggregate) [PATTERN ROOT]
    Node 16672 (Gather) [consumed]
      Node 16673 (Aggregate) [consumed]
        Node 16674 (Nested Loop) [PATTERN ROOT]
          Node 16675 (Hash Join) [consumed]
            Node 16676 (Seq Scan) [consumed]
            Node 16677 (Hash) [consumed]
              Node 16678 (Hash Join) [consumed]
                Node 16679 (Hash Join) [PATTERN ROOT]
                  Node 16680 (Nested Loop) [consumed]
                    Node 16681 (Seq Scan) [consumed]
                    Node 16682 (Index Scan) [consumed]
                  Node 16683 (Hash) [consumed]
                    Node 16684 (Seq Scan) [consumed]
                Node 16685 (Hash) [PATTERN ROOT]
                  Node 16686 (Seq Scan) [consumed]
          Node 16687 (Index Scan) [consumed]
```
