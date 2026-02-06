# Online Prediction Report

**Test Query:** Q12_133_seed_1082932092
**Timestamp:** 2026-01-18 19:48:55

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 7.73%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.2% | 21.8723 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 30 | 4.4% | 1.3306 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 30 | 5.8% | 1.7441 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 193.2% | 173.8566 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 30 | 1.2% | 0.3537 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 30 | 5.8% | 1.7441 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 30 | 1.2% | 0.3537 |
| b692b3d9 | Aggregate -> Gather Merge -> Aggregate -... | 5 | 0 | - | - |
| f9c97829 | Aggregate -> Gather Merge -> Aggregate -... | 6 | 0 | - | - |
| 898abd49 | Gather Merge -> Aggregate -> Sort -> Nes... | 4 | 0 | - | - |
| 3a2624e2 | Gather Merge -> Aggregate -> Sort -> Nes... | 5 | 0 | - | - |
| fbf3ebe8 | Aggregate -> Sort -> Nested Loop (Outer)... | 3 | 0 | - | - |
| a0631e25 | Aggregate -> Sort -> Nested Loop -> [Seq... | 4 | 0 | - | - |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 0 | - | - |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 2724c080 | 21.8723 | -0.5018% | REJECTED | 17.11% |
| 1 | 3754655c | 1.3306 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 2 | 46f37744 | 1.7441 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 3 | c53c4396 | 173.8566 | -0.0000% | REJECTED | 17.11% |
| 4 | 8a8c43c6 | 0.3537 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 5 | e6c1e0d8 | 1.7441 | N/A | SKIPPED_LOW_ERROR | 17.11% |
| 6 | 460af52c | 0.3537 | N/A | SKIPPED_LOW_ERROR | 17.11% |
## Query Tree

```
Node 24572 (Aggregate) - ROOT
  Node 24573 (Gather Merge)
    Node 24574 (Aggregate)
      Node 24575 (Sort)
        Node 24576 (Nested Loop)
          Node 24577 (Seq Scan) - LEAF
          Node 24578 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.92%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24572 | Aggregate | 998.09 | 919.07 | 7.9% | operator |
| 24573 | Gather Merge | 998.06 | 1111.84 | 11.4% | operator |
| 24574 | Aggregate | 975.90 | 895.31 | 8.3% | operator |
| 24575 | Sort | 975.29 | 1092.81 | 12.0% | operator |
| 24576 | Nested Loop | 974.36 | 1127.41 | 15.7% | operator |
| 24577 | Seq Scan | 845.65 | 745.19 | 11.9% | operator |
| 24578 | Index Scan | 0.03 | 0.07 | 187.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24577 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5758
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

### Step 2: Node 24578 (Index Scan) - LEAF

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

### Step 3: Node 24576 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5758
  - nt1=5758
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=745.1923
  - rt2=0.0719
  - sel=1.0000
  - st1=1.6083
  - st2=0.1246
  - startup_cost=0.4300
  - total_cost=147157.6000
- **Output:** st=38.33, rt=1127.41

### Step 4: Node 24575 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5758
  - nt1=5758
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1127.4092
  - rt2=0.0000
  - sel=1.0000
  - st1=38.3269
  - st2=0.0000
  - startup_cost=147517.2200
  - total_cost=147531.6200
- **Output:** st=1092.39, rt=1092.81

### Step 5: Node 24574 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5758
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1092.8077
  - rt2=0.0000
  - sel=0.0012
  - st1=1092.3947
  - st2=0.0000
  - startup_cost=147517.2200
  - total_cost=147632.4500
- **Output:** st=868.97, rt=895.31

### Step 6: Node 24573 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=895.3137
  - rt2=0.0000
  - sel=5.0000
  - st1=868.9675
  - st2=0.0000
  - startup_cost=148517.3000
  - total_cost=148636.7500
- **Output:** st=1109.22, rt=1111.84

### Step 7: Node 24572 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1111.8364
  - rt2=0.0000
  - sel=0.2000
  - st1=1109.2224
  - st2=0.0000
  - startup_cost=148517.3000
  - total_cost=148637.0800
- **Output:** st=903.60, rt=919.07
