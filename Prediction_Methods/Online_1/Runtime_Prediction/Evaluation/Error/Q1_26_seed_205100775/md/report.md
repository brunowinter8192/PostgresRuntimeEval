# Online Prediction Report

**Test Query:** Q1_26_seed_205100775
**Timestamp:** 2025-12-21 20:53:38

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 13.83%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 9.9% | 2.3734 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 13.2% | 3.1739 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 22.0% | 5.2893 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |

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
| 3 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 4 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | 184f44de | 4.0548 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
| 9 | 3dfa6025 | 2.3734 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 341 (Aggregate) - ROOT
  Node 342 (Gather Merge)
    Node 343 (Sort)
      Node 344 (Aggregate)
        Node 345 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 14.02%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 341 | Aggregate | 922.70 | 1052.02 | 14.0% | operator |
| 342 | Gather Merge | 922.64 | 1079.36 | 17.0% | operator |
| 343 | Sort | 901.86 | 1152.45 | 27.8% | operator |
| 344 | Aggregate | 901.83 | 972.33 | 7.8% | operator |
| 345 | Seq Scan | 497.48 | 569.56 | 14.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 345 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1187477
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1979
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.91, rt=569.56

### Step 2: Node 344 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1187477
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=569.5632
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9092
  - st2=0.0000
  - startup_cost=169164.7300
  - total_cost=169164.8700
- **Output:** st=951.36, rt=972.33

### Step 3: Node 343 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.3349
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3629
  - st2=0.0000
  - startup_cost=169164.9500
  - total_cost=169164.9600
- **Output:** st=1150.47, rt=1152.45

### Step 4: Node 342 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4511
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4675
  - st2=0.0000
  - startup_cost=170165.0200
  - total_cost=170168.6500
- **Output:** st=1075.00, rt=1079.36

### Step 5: Node 341 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3607
  - rt2=0.0000
  - sel=0.2000
  - st1=1074.9952
  - st2=0.0000
  - startup_cost=170165.0200
  - total_cost=170169.7900
- **Output:** st=1039.47, rt=1052.02
