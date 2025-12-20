# Dry Prediction Report: Q9

## Summary

- **Total Test Queries:** 150
- **Unique Plan Structures:** 2
- **Total Patterns Available:** 303
- **Patterns Used:** 7
- **Reduction:** 97.7%

## Used Patterns

- `1d35fb978b37...` Sort -> Aggregate (Outer)
- `3aab37bea1a8...` Hash -> Seq Scan (Outer)
- `3cfa90d7df3c...` Nested Loop -> [Hash Join (Outer), Index Scan (Inner)]
- `634cdbe24fda...` Gather -> Aggregate (Outer)
- `7df893ad48ca...` Hash -> Hash Join (Outer)
- `895c6e8c1a30...` Hash Join -> [Seq Scan (Outer), Hash (Inner)]
- `c53c43965386...` Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)]

## Query Trees

### Plan 1 (Example: Q9_100_seed_812199069)

```
Node 16651 (Sort) [PATTERN ROOT] - ROOT
  Node 16652 (Aggregate) [consumed]
    Node 16653 (Gather) [PATTERN ROOT]
      Node 16654 (Aggregate) [consumed]
        Node 16655 (Hash Join) [PATTERN ROOT]
          Node 16656 (Seq Scan) [consumed]
          Node 16657 (Hash) [consumed]
            Node 16658 (Hash Join) [PATTERN ROOT]
              Node 16659 (Seq Scan) [consumed]
              Node 16660 (Hash) [consumed]
                Node 16661 (Hash Join)
                  Node 16662 (Hash Join)
                    Node 16663 (Nested Loop) [PATTERN ROOT]
                      Node 16664 (Seq Scan) [consumed]
                      Node 16665 (Index Scan) [consumed]
                    Node 16666 (Hash) [PATTERN ROOT]
                      Node 16667 (Seq Scan) [consumed]
                  Node 16668 (Hash) [PATTERN ROOT]
                    Node 16669 (Seq Scan) [consumed]
```

### Plan 2 (Example: Q9_101_seed_820403100)

```
Node 16670 (Sort) [PATTERN ROOT] - ROOT
  Node 16671 (Aggregate) [consumed]
    Node 16672 (Gather) [PATTERN ROOT]
      Node 16673 (Aggregate) [consumed]
        Node 16674 (Nested Loop) [PATTERN ROOT]
          Node 16675 (Hash Join) [consumed]
            Node 16676 (Seq Scan)
            Node 16677 (Hash) [PATTERN ROOT]
              Node 16678 (Hash Join) [consumed]
                Node 16679 (Hash Join)
                  Node 16680 (Nested Loop) [PATTERN ROOT]
                    Node 16681 (Seq Scan) [consumed]
                    Node 16682 (Index Scan) [consumed]
                  Node 16683 (Hash) [PATTERN ROOT]
                    Node 16684 (Seq Scan) [consumed]
                Node 16685 (Hash) [PATTERN ROOT]
                  Node 16686 (Seq Scan) [consumed]
          Node 16687 (Index Scan) [consumed]
```
