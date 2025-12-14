# Online Prediction Report

**Test Query:** Q1_117_seed_951667596
**Timestamp:** 2025-12-13 02:19:49

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 11.17%

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
Node 91 (Aggregate) - ROOT
  Node 92 (Gather Merge)
    Node 93 (Sort)
      Node 94 (Aggregate)
        Node 95 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 11.36%
- Improvement: -0.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 91 | Aggregate | 944.72 | 1052.01 | 11.4% | operator |
| 92 | Gather Merge | 944.67 | 1079.37 | 14.3% | operator |
| 93 | Sort | 925.37 | 1152.40 | 24.5% | operator |
| 94 | Aggregate | 925.34 | 972.14 | 5.1% | operator |
| 95 | Seq Scan | 511.52 | 571.44 | 11.7% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 95 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1179622
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1966
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.92, rt=571.44

### Step 2: Node 94 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1179622
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=571.4358
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9243
  - st2=0.0000
  - startup_cost=168889.8100
  - total_cost=168889.9400
- **Output:** st=951.34, rt=972.14

### Step 3: Node 93 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.1380
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3397
  - st2=0.0000
  - startup_cost=168890.0200
  - total_cost=168890.0400
- **Output:** st=1150.42, rt=1152.40

### Step 4: Node 92 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4035
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4210
  - st2=0.0000
  - startup_cost=169890.1000
  - total_cost=169893.7300
- **Output:** st=1075.01, rt=1079.37

### Step 5: Node 91 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3733
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0086
  - st2=0.0000
  - startup_cost=169890.1000
  - total_cost=169894.8700
- **Output:** st=1039.52, rt=1052.01
