# Online Prediction Report

**Test Query:** Q1_111_seed_902443410
**Timestamp:** 2025-12-13 01:01:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 12.56%

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
Node 61 (Aggregate) - ROOT
  Node 62 (Gather Merge)
    Node 63 (Sort)
      Node 64 (Aggregate)
        Node 65 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 12.75%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 61 | Aggregate | 933.05 | 1052.02 | 12.8% | operator |
| 62 | Gather Merge | 933.00 | 1079.35 | 15.7% | operator |
| 63 | Sort | 911.76 | 1152.48 | 26.4% | operator |
| 64 | Aggregate | 911.74 | 972.44 | 6.7% | operator |
| 65 | Seq Scan | 497.85 | 568.57 | 14.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 65 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1191651
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1986
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.90, rt=568.57

### Step 2: Node 64 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1191651
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=568.5690
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9011
  - st2=0.0000
  - startup_cost=169310.8200
  - total_cost=169310.9600
- **Output:** st=951.38, rt=972.44

### Step 3: Node 63 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.4406
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3757
  - st2=0.0000
  - startup_cost=169311.0400
  - total_cost=169311.0500
- **Output:** st=1150.49, rt=1152.48

### Step 4: Node 62 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4765
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4923
  - st2=0.0000
  - startup_cost=170311.1100
  - total_cost=170314.7400
- **Output:** st=1074.99, rt=1079.35

### Step 5: Node 61 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3540
  - rt2=0.0000
  - sel=0.2000
  - st1=1074.9882
  - st2=0.0000
  - startup_cost=170311.1100
  - total_cost=170315.8800
- **Output:** st=1039.45, rt=1052.02
