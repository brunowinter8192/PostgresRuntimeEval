# Query Prediction Report (Hybrid_1)

**Query:** Q9_111_seed_902443410
**Timestamp:** 2026-01-09 20:50:46

## Pattern Assignments

**Total Patterns Matched:** 4

| Root Node | Pattern Hash | Pattern String |
|-----------|--------------|----------------|
| 16869 | a5f39f08c510... | Aggregate -> Gather -> Aggregate (Outer) (Outer) |
| 16872 | ec92bdaa27b4... | Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer) (Inner)] |
| 16879 | 2873b8c3a175... | Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)] |
| 16885 | 3aab37bea1a8... | Hash -> Seq Scan (Outer) |

## Query Tree

```
Node 16868 (Sort) - ROOT
  Node 16869 (Aggregate) [PATTERN ROOT]
    Node 16870 (Gather) [consumed]
      Node 16871 (Aggregate) [consumed]
        Node 16872 (Hash Join) [PATTERN ROOT]
          Node 16873 (Seq Scan) [consumed]
          Node 16874 (Hash) [consumed]
            Node 16875 (Hash Join) [consumed]
              Node 16876 (Seq Scan) [consumed]
              Node 16877 (Hash) [consumed]
                Node 16878 (Hash Join) [consumed]
                  Node 16879 (Hash Join) [PATTERN ROOT]
                    Node 16880 (Nested Loop) [consumed]
                      Node 16881 (Seq Scan) [consumed]
                      Node 16882 (Index Scan) [consumed]
                    Node 16883 (Hash) [consumed]
                      Node 16884 (Seq Scan) [consumed]
                  Node 16885 (Hash) [PATTERN ROOT]
                    Node 16886 (Seq Scan) [consumed]
```

## Prediction Chain (Bottom-Up)

### Step 1 (depth 9): Pattern Match

- **Pattern:** Hash Join -> [Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer), Hash -> Seq Scan (Outer) (Inner)]
- **Hash:** 2873b8c3a1759afe345ffbdfc9bdcba7
- **Root:** Node 16879 (Hash Join)
- **Consumed Children:** Node 16880 (Nested Loop), Node 16883 (Hash)
- **Output:** st=17.31, rt=616.38

### Step 2 (depth 9): Pattern Match

- **Pattern:** Hash -> Seq Scan (Outer)
- **Hash:** 3aab37bea1a884da206eb32f2c1ae5ba
- **Root:** Node 16885 (Hash)
- **Consumed Children:** Node 16886 (Seq Scan)
- **Output:** st=0.01, rt=0.01

### Step 3 (depth 4): Pattern Match

- **Pattern:** Hash Join -> [Seq Scan (Outer), Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Hash Join (Outer) (Inner)] (Outer) (Inner)]
- **Hash:** ec92bdaa27b47a2a45a6787f34350878
- **Root:** Node 16872 (Hash Join)
- **Consumed Children:** Node 16873 (Seq Scan), Node 16874 (Hash)
- **Output:** st=52.57, rt=231.74

### Step 4 (depth 1): Pattern Match

- **Pattern:** Aggregate -> Gather -> Aggregate (Outer) (Outer)
- **Hash:** a5f39f08c510532e02e96e109e48c0cd
- **Root:** Node 16869 (Aggregate)
- **Consumed Children:** Node 16870 (Gather)
- **Output:** st=818.83, rt=824.42

### Step 5 (depth 0): Operator Fallback

- **Node:** 16868 (Sort)
- **Reason:** No pattern match
- **Output:** st=1092.95, rt=1094.81

## Prediction Results

| Node | Type | Depth | Pred Type | Actual RT | Pred RT | MRE (%) |
|------|------|-------|-----------|-----------|---------|---------|
| 16868 | Sort | 0 | operator | 1280.36 | 1094.81 | 14.5 |
| 16869 | Aggregate | 1 | pattern | 1280.22 | 824.42 | 35.6 |
| 16872 | Hash Join | 4 | pattern | 1233.78 | 231.74 | 81.2 |
| 16879 | Hash Join | 9 | pattern | 199.50 | 616.38 | 209.0 |
| 16885 | Hash | 9 | pattern | 14.70 | 0.01 | 99.9 |
