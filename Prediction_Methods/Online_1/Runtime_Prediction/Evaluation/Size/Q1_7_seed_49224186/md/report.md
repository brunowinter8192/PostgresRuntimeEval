# Online Prediction Report

**Test Query:** Q1_7_seed_49224186
**Timestamp:** 2025-12-13 02:20:33

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.99%

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
Node 636 (Aggregate) - ROOT
  Node 637 (Gather Merge)
    Node 638 (Sort)
      Node 639 (Aggregate)
        Node 640 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 12.18%
- Improvement: -0.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 636 | Aggregate | 937.80 | 1052.02 | 12.2% | operator |
| 637 | Gather Merge | 937.77 | 1079.37 | 15.1% | operator |
| 638 | Sort | 920.87 | 1152.42 | 25.1% | operator |
| 639 | Aggregate | 920.85 | 972.19 | 5.6% | operator |
| 640 | Seq Scan | 510.47 | 570.98 | 11.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 640 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1181531
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1969
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.92, rt=570.98

### Step 2: Node 639 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1181531
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=570.9805
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9207
  - st2=0.0000
  - startup_cost=168956.6200
  - total_cost=168956.7600
- **Output:** st=951.35, rt=972.19

### Step 3: Node 638 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.1856
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3452
  - st2=0.0000
  - startup_cost=168956.8400
  - total_cost=168956.8500
- **Output:** st=1150.43, rt=1152.42

### Step 4: Node 637 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4151
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4323
  - st2=0.0000
  - startup_cost=169956.9100
  - total_cost=169960.5400
- **Output:** st=1075.01, rt=1079.37

### Step 5: Node 636 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3703
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0053
  - st2=0.0000
  - startup_cost=169956.9100
  - total_cost=169961.6800
- **Output:** st=1039.51, rt=1052.02
