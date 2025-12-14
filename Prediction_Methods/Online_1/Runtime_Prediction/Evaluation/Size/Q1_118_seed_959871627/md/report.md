# Online Prediction Report

**Test Query:** Q1_118_seed_959871627
**Timestamp:** 2025-12-13 02:19:49

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.10%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 5.2893 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 2.3734 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 6 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
## Query Tree

```
Node 96 (Aggregate) - ROOT
  Node 97 (Gather Merge)
    Node 98 (Sort)
      Node 99 (Aggregate)
        Node 100 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 4.27%
- Improvement: -0.17%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 96 | Aggregate | 1008.96 | 1052.01 | 4.3% | operator |
| 97 | Gather Merge | 1008.89 | 1079.38 | 7.0% | operator |
| 98 | Sort | 988.71 | 1152.39 | 16.6% | operator |
| 99 | Aggregate | 988.69 | 972.08 | 1.7% | operator |
| 100 | Seq Scan | 586.71 | 571.98 | 2.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 100 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1177331
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1962
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.93, rt=571.98

### Step 2: Node 99 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1177331
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=571.9823
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9287
  - st2=0.0000
  - startup_cost=168809.6200
  - total_cost=168809.7600
- **Output:** st=951.33, rt=972.08

### Step 3: Node 98 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.0811
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3332
  - st2=0.0000
  - startup_cost=168809.8400
  - total_cost=168809.8500
- **Output:** st=1150.41, rt=1152.39

### Step 4: Node 97 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.3897
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4075
  - st2=0.0000
  - startup_cost=169809.9100
  - total_cost=169813.5400
- **Output:** st=1075.01, rt=1079.38

### Step 5: Node 96 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3771
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0125
  - st2=0.0000
  - startup_cost=169809.9100
  - total_cost=169814.6800
- **Output:** st=1039.54, rt=1052.01
