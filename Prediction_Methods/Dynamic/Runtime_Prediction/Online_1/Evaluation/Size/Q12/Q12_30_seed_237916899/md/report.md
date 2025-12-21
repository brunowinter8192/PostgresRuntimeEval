# Online Prediction Report

**Test Query:** Q12_30_seed_237916899
**Timestamp:** 2025-12-21 17:58:34

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 8.01%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.2% | 21.8723 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 193.2% | 173.8566 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 30 | 5.8% | 1.7441 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 30 | 4.4% | 1.3306 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 30 | 1.2% | 0.3537 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 30 | 5.8% | 1.7441 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 30 | 1.2% | 0.3537 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 2724c080 | 21.8723 | -0.5018% | REJECTED | 17.11% |
| 1 | c53c4396 | 173.8566 | -0.0000% | REJECTED | 17.11% |
| 2 | 46f37744 | 1.7441 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 3 | 3754655c | 1.3306 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 4 | 8a8c43c6 | 0.3537 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 5 | e6c1e0d8 | 1.7441 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 6 | 460af52c | 0.3537 | N/A | SKIPPED_LOW_ERROR | 17.11% |
## Query Tree

```
Node 24831 (Aggregate) - ROOT
  Node 24832 (Gather Merge)
    Node 24833 (Aggregate)
      Node 24834 (Sort)
        Node 24835 (Nested Loop)
          Node 24836 (Seq Scan) - LEAF
          Node 24837 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 8.20%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24831 | Aggregate | 1001.15 | 919.03 | 8.2% | operator |
| 24832 | Gather Merge | 1001.13 | 1111.84 | 11.1% | operator |
| 24833 | Aggregate | 983.24 | 895.28 | 8.9% | operator |
| 24834 | Sort | 982.63 | 1092.83 | 11.2% | operator |
| 24835 | Nested Loop | 981.64 | 1127.42 | 14.8% | operator |
| 24836 | Seq Scan | 851.70 | 745.20 | 12.5% | operator |
| 24837 | Index Scan | 0.03 | 0.07 | 187.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24836 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5840
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=15
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0010
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=139605.4700
- **Output:** st=1.61, rt=745.20

### Step 2: Node 24837 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=1.3100
- **Output:** st=0.12, rt=0.07

### Step 3: Node 24835 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5840
  - nt1=5840
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=745.1966
  - rt2=0.0719
  - sel=1.0000
  - st1=1.6089
  - st2=0.1246
  - startup_cost=0.4300
  - total_cost=147231.6100
- **Output:** st=38.32, rt=1127.42

### Step 4: Node 24834 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5840
  - nt1=5840
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1127.4165
  - rt2=0.0000
  - sel=1.0000
  - st1=38.3181
  - st2=0.0000
  - startup_cost=147596.9600
  - total_cost=147611.5600
- **Output:** st=1092.42, rt=1092.83

### Step 5: Node 24833 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5840
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1092.8337
  - rt2=0.0000
  - sel=0.0012
  - st1=1092.4205
  - st2=0.0000
  - startup_cost=147596.9600
  - total_cost=147713.8300
- **Output:** st=868.91, rt=895.28

### Step 6: Node 24832 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=895.2800
  - rt2=0.0000
  - sel=5.0000
  - st1=868.9123
  - st2=0.0000
  - startup_cost=148597.0300
  - total_cost=148718.1200
- **Output:** st=1109.23, rt=1111.84

### Step 7: Node 24831 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1111.8393
  - rt2=0.0000
  - sel=0.2000
  - st1=1109.2251
  - st2=0.0000
  - startup_cost=148597.0300
  - total_cost=148718.4500
- **Output:** st=903.54, rt=919.03
