# Online Prediction Report

**Test Query:** Q1_39_seed_311753178
**Timestamp:** 2025-12-22 04:35:06

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.87%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 22.0% | 5.2893 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 13.2% | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 9.9% | 2.3734 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 2 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | 184f44de | 4.0548 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 7 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
| 9 | 3dfa6025 | 2.3734 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 411 (Aggregate) - ROOT
  Node 412 (Gather Merge)
    Node 413 (Sort)
      Node 414 (Aggregate)
        Node 415 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.04%
- Improvement: -0.17%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 411 | Aggregate | 992.08 | 1052.02 | 6.0% | operator |
| 412 | Gather Merge | 992.03 | 1079.37 | 8.8% | operator |
| 413 | Sort | 972.09 | 1152.42 | 18.6% | operator |
| 414 | Aggregate | 972.05 | 972.22 | 0.0% | operator |
| 415 | Seq Scan | 596.39 | 570.62 | 4.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 415 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1183059
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1971
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.92, rt=570.62

### Step 2: Node 414 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1183059
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=570.6162
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9177
  - st2=0.0000
  - startup_cost=169010.1000
  - total_cost=169010.2400
- **Output:** st=951.35, rt=972.22

### Step 3: Node 413 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.2238
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3497
  - st2=0.0000
  - startup_cost=169010.3200
  - total_cost=169010.3300
- **Output:** st=1150.44, rt=1152.42

### Step 4: Node 412 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4243
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4413
  - st2=0.0000
  - startup_cost=170010.3900
  - total_cost=170014.0200
- **Output:** st=1075.00, rt=1079.37

### Step 5: Node 411 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3678
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0027
  - st2=0.0000
  - startup_cost=170010.3900
  - total_cost=170015.1600
- **Output:** st=1039.50, rt=1052.02
