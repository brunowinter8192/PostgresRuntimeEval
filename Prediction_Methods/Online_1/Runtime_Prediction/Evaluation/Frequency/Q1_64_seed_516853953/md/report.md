# Online Prediction Report

**Test Query:** Q1_64_seed_516853953
**Timestamp:** 2025-12-22 06:30:52

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.35%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 22.0% | 5.2893 |
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
| 3 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 184f44de | 4.0548 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
| 9 | 3dfa6025 | 2.3734 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 551 (Aggregate) - ROOT
  Node 552 (Gather Merge)
    Node 553 (Sort)
      Node 554 (Aggregate)
        Node 555 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 6.52%
- Improvement: -0.17%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 551 | Aggregate | 987.62 | 1052.01 | 6.5% | operator |
| 552 | Gather Merge | 987.58 | 1079.38 | 9.3% | operator |
| 553 | Sort | 971.66 | 1152.38 | 18.6% | operator |
| 554 | Aggregate | 971.64 | 972.04 | 0.0% | operator |
| 555 | Seq Scan | 564.25 | 572.42 | 1.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 555 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1175498
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1959
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.93, rt=572.42

### Step 2: Node 554 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1175498
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=572.4196
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9321
  - st2=0.0000
  - startup_cost=168745.4700
  - total_cost=168745.6000
- **Output:** st=951.33, rt=972.04

### Step 3: Node 553 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.0358
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3281
  - st2=0.0000
  - startup_cost=168745.6800
  - total_cost=168745.7000
- **Output:** st=1150.40, rt=1152.38

### Step 4: Node 552 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.3786
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.3967
  - st2=0.0000
  - startup_cost=169745.7600
  - total_cost=169749.3900
- **Output:** st=1075.02, rt=1079.38

### Step 5: Node 551 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3800
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0157
  - st2=0.0000
  - startup_cost=169745.7600
  - total_cost=169750.5300
- **Output:** st=1039.55, rt=1052.01
