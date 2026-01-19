# Query Prediction Report (Hybrid_1)

**Query:** Q14_109_seed_886035348
**Timestamp:** 2026-01-09 20:50:29

## Pattern Assignments

**Total Patterns Matched:** 1

| Root Node | Pattern Hash | Pattern String |
|-----------|--------------|----------------|
| 26486 | 895c6e8c1a30... | Hash Join -> [Seq Scan (Outer), Hash (Inner)] |

## Query Tree

```
Node 26483 (Aggregate) - ROOT
  Node 26484 (Gather)
    Node 26485 (Aggregate)
      Node 26486 (Hash Join) [PATTERN ROOT]
        Node 26487 (Seq Scan) [consumed]
        Node 26488 (Hash) [consumed]
          Node 26489 (Seq Scan)
```

## Prediction Chain (Bottom-Up)

### Step 1 (depth 5): Operator Fallback

- **Node:** 26489 (Seq Scan)
- **Reason:** No pattern match
- **Output:** st=2.62, rt=32.94

### Step 2 (depth 3): Pattern Match

- **Pattern:** Hash Join -> [Seq Scan (Outer), Hash (Inner)]
- **Hash:** 895c6e8c1a30a094329d71cef3111fbd
- **Root:** Node 26486 (Hash Join)
- **Consumed Children:** Node 26487 (Seq Scan), Node 26488 (Hash)
- **Output:** st=35.46, rt=99.97

### Step 3 (depth 2): Operator Fallback

- **Node:** 26485 (Aggregate)
- **Reason:** No pattern match
- **Output:** st=878.67, rt=920.43

### Step 4 (depth 1): Operator Fallback

- **Node:** 26484 (Gather)
- **Reason:** No pattern match
- **Output:** st=629.65, rt=917.37

### Step 5 (depth 0): Operator Fallback

- **Node:** 26483 (Aggregate)
- **Reason:** No pattern match
- **Output:** st=934.82, rt=931.67

## Prediction Results

| Node | Type | Depth | Pred Type | Actual RT | Pred RT | MRE (%) |
|------|------|-------|-----------|-----------|---------|---------|
| 26483 | Aggregate | 0 | operator | 810.16 | 931.67 | 15.0 |
| 26484 | Gather | 1 | operator | 810.15 | 917.37 | 13.2 |
| 26485 | Aggregate | 2 | operator | 791.17 | 920.43 | 16.3 |
| 26486 | Hash Join | 3 | pattern | 788.86 | 99.97 | 87.3 |
| 26489 | Seq Scan | 5 | operator | 36.39 | 32.94 | 9.5 |
