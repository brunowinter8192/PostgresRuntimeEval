# Online Prediction Report

**Test Query:** Q1_129_seed_1050115968
**Timestamp:** 2025-12-13 01:01:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 10.05%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 5.2893 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 2.3734 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 3 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
## Query Tree

```
Node 156 (Aggregate) - ROOT
  Node 157 (Gather Merge)
    Node 158 (Sort)
      Node 159 (Aggregate)
        Node 160 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 10.23%
- Improvement: -0.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 156 | Aggregate | 954.39 | 1052.01 | 10.2% | operator |
| 157 | Gather Merge | 954.33 | 1079.38 | 13.1% | operator |
| 158 | Sort | 934.53 | 1152.39 | 23.3% | operator |
| 159 | Aggregate | 934.50 | 972.07 | 4.0% | operator |
| 160 | Seq Scan | 519.83 | 572.09 | 10.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 160 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1176872
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1961
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.93, rt=572.09

### Step 2: Node 159 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1176872
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=572.0918
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9295
  - st2=0.0000
  - startup_cost=168793.5600
  - total_cost=168793.6900
- **Output:** st=951.33, rt=972.07

### Step 3: Node 158 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.0697
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3319
  - st2=0.0000
  - startup_cost=168793.7700
  - total_cost=168793.7900
- **Output:** st=1150.40, rt=1152.39

### Step 4: Node 157 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.3869
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4048
  - st2=0.0000
  - startup_cost=169793.8500
  - total_cost=169797.4800
- **Output:** st=1075.01, rt=1079.38

### Step 5: Node 156 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3778
  - rt2=0.0000
  - sel=0.2000
  - st1=1075.0133
  - st2=0.0000
  - startup_cost=169793.8500
  - total_cost=169798.6200
- **Output:** st=1039.54, rt=1052.01
