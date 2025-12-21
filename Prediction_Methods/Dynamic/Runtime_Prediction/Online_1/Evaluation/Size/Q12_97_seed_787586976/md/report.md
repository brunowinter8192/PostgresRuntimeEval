# Online Prediction Report

**Test Query:** Q12_97_seed_787586976
**Timestamp:** 2025-12-21 18:01:28

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.65%

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
Node 25342 (Aggregate) - ROOT
  Node 25343 (Gather Merge)
    Node 25344 (Aggregate)
      Node 25345 (Sort)
        Node 25346 (Nested Loop)
          Node 25347 (Seq Scan) - LEAF
          Node 25348 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 9.84%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25342 | Aggregate | 1019.33 | 919.05 | 9.8% | operator |
| 25343 | Gather Merge | 1019.32 | 1111.84 | 9.1% | operator |
| 25344 | Aggregate | 998.92 | 895.29 | 10.4% | operator |
| 25345 | Sort | 998.33 | 1092.82 | 9.5% | operator |
| 25346 | Nested Loop | 997.23 | 1127.41 | 13.1% | operator |
| 25347 | Seq Scan | 861.53 | 745.19 | 13.5% | operator |
| 25348 | Index Scan | 0.03 | 0.07 | 176.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25347 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5805
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
- **Output:** st=1.61, rt=745.19

### Step 2: Node 25348 (Index Scan) - LEAF

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

### Step 3: Node 25346 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5805
  - nt1=5805
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=745.1948
  - rt2=0.0719
  - sel=1.0000
  - st1=1.6086
  - st2=0.1246
  - startup_cost=0.4300
  - total_cost=147200.0300
- **Output:** st=38.32, rt=1127.41

### Step 4: Node 25345 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5805
  - nt1=5805
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1127.4134
  - rt2=0.0000
  - sel=1.0000
  - st1=38.3218
  - st2=0.0000
  - startup_cost=147562.9300
  - total_cost=147577.4400
- **Output:** st=1092.41, rt=1092.82

### Step 5: Node 25344 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5805
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1092.8226
  - rt2=0.0000
  - sel=0.0012
  - st1=1092.4095
  - st2=0.0000
  - startup_cost=147562.9300
  - total_cost=147679.1000
- **Output:** st=868.94, rt=895.29

### Step 6: Node 25343 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=895.2943
  - rt2=0.0000
  - sel=5.0000
  - st1=868.9359
  - st2=0.0000
  - startup_cost=148563.0000
  - total_cost=148683.3900
- **Output:** st=1109.22, rt=1111.84

### Step 7: Node 25342 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1111.8381
  - rt2=0.0000
  - sel=0.2000
  - st1=1109.2239
  - st2=0.0000
  - startup_cost=148563.0000
  - total_cost=148683.7200
- **Output:** st=903.57, rt=919.05
