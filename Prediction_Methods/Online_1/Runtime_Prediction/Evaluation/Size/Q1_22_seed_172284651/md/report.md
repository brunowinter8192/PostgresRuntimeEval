# Online Prediction Report

**Test Query:** Q1_22_seed_172284651
**Timestamp:** 2025-12-13 02:19:49

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 12.06%

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
Node 321 (Aggregate) - ROOT
  Node 322 (Gather Merge)
    Node 323 (Sort)
      Node 324 (Aggregate)
        Node 325 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 12.24%
- Improvement: -0.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 321 | Aggregate | 937.30 | 1052.01 | 12.2% | operator |
| 322 | Gather Merge | 937.22 | 1079.39 | 15.2% | operator |
| 323 | Sort | 916.93 | 1152.35 | 25.7% | operator |
| 324 | Aggregate | 916.91 | 971.93 | 6.0% | operator |
| 325 | Seq Scan | 514.33 | 573.40 | 11.5% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 325 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1171373
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1952
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.94, rt=573.40

### Step 2: Node 324 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1171373
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=573.4043
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9399
  - st2=0.0000
  - startup_cost=168601.0900
  - total_cost=168601.2300
- **Output:** st=951.32, rt=971.93

### Step 3: Node 323 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=971.9343
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3169
  - st2=0.0000
  - startup_cost=168601.3100
  - total_cost=168601.3200
- **Output:** st=1150.37, rt=1152.35

### Step 4: Node 322 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.3538
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.3725
  - st2=0.0000
  - startup_cost=169601.3800
  - total_cost=169605.0100
- **Output:** st=1075.02, rt=1079.39

### Step 5: Node 321 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3868
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0228
  - st2=0.0000
  - startup_cost=169601.3800
  - total_cost=169606.1500
- **Output:** st=1039.57, rt=1052.01
