# Online Prediction Report

**Test Query:** Q12_129_seed_1050115968
**Timestamp:** 2025-12-22 04:43:29

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.91%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 24 | 9.2% | 2.1961 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| fbf3ebe8 | Aggregate -> Sort -> Nested Loop (Outer)... | 3 | 24 | 4.0% | 0.9714 |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 24 | 9.2% | 2.1961 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 898abd49 | Gather Merge -> Aggregate -> Sort -> Nes... | 4 | 24 | 6.8% | 1.6208 |
| a0631e25 | Aggregate -> Sort -> Nested Loop -> [Seq... | 4 | 24 | 4.0% | 0.9714 |
| b692b3d9 | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 4.6% | 1.0973 |
| 3a2624e2 | Gather Merge -> Aggregate -> Sort -> Nes... | 5 | 24 | 6.8% | 1.6208 |
| f9c97829 | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 4.6% | 1.0973 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 1 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 2 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 263b40d6 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | fbf3ebe8 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | 5b623fa1 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 9 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | 898abd49 | 1.6208 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 11 | a0631e25 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | b692b3d9 | 1.0973 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | 3a2624e2 | 1.6208 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | f9c97829 | 1.0973 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 24537 (Aggregate) - ROOT
  Node 24538 (Gather Merge)
    Node 24539 (Aggregate)
      Node 24540 (Sort)
        Node 24541 (Nested Loop)
          Node 24542 (Seq Scan) - LEAF
          Node 24543 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.83%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24537 | Aggregate | 1003.12 | 954.69 | 4.8% | operator |
| 24538 | Gather Merge | 1003.10 | 1060.96 | 5.8% | operator |
| 24539 | Aggregate | 984.32 | 941.96 | 4.3% | operator |
| 24540 | Sort | 983.68 | 1058.11 | 7.6% | operator |
| 24541 | Nested Loop | 982.64 | 1101.32 | 12.1% | operator |
| 24542 | Seq Scan | 845.84 | 750.46 | 11.3% | operator |
| 24543 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24542 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5799
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
- **Output:** st=3.98, rt=750.46

### Step 2: Node 24543 (Index Scan) - LEAF

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
- **Output:** st=0.03, rt=-0.02

### Step 3: Node 24541 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5799
  - nt1=5799
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4578
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147194.7200
- **Output:** st=21.29, rt=1101.32

### Step 4: Node 24540 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5799
  - nt1=5799
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3151
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2852
  - st2=0.0000
  - startup_cost=147557.2000
  - total_cost=147571.7000
- **Output:** st=1057.11, rt=1058.11

### Step 5: Node 24539 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5799
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1074
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1148
  - st2=0.0000
  - startup_cost=147557.2000
  - total_cost=147673.2500
- **Output:** st=927.03, rt=941.96

### Step 6: Node 24538 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9598
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0280
  - st2=0.0000
  - startup_cost=148557.2800
  - total_cost=148677.5400
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 24537 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9609
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9885
  - st2=0.0000
  - startup_cost=148557.2800
  - total_cost=148677.8700
- **Output:** st=951.95, rt=954.69
