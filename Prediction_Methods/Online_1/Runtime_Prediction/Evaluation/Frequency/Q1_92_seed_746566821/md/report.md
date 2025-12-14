# Online Prediction Report

**Test Query:** Q1_92_seed_746566821
**Timestamp:** 2025-12-13 03:29:20

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 13.29%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.4662 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 4.0548 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 3.4083 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 5.2893 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 2.3734 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 7 | dc1b1da7 | 5.2893 | 0.0025% | REJECTED | 17.92% |
| 8 | 52c5ec81 | 3.1739 | 0.1045% | REJECTED | 17.92% |
## Query Tree

```
Node 706 (Aggregate) - ROOT
  Node 707 (Gather Merge)
    Node 708 (Sort)
      Node 709 (Aggregate)
        Node 710 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 13.47%
- Improvement: -0.19%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 706 | Aggregate | 927.11 | 1052.02 | 13.5% | operator |
| 707 | Gather Merge | 927.06 | 1079.36 | 16.4% | operator |
| 708 | Sort | 910.08 | 1152.45 | 26.6% | operator |
| 709 | Aggregate | 910.06 | 972.31 | 6.8% | operator |
| 710 | Seq Scan | 499.25 | 569.80 | 14.1% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 710 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1186496
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1977
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=1.91, rt=569.80

### Step 2: Node 709 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1186496
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=569.7970
  - rt2=0.0000
  - sel=0.0000
  - st1=1.9111
  - st2=0.0000
  - startup_cost=169130.4000
  - total_cost=169130.5300
- **Output:** st=951.36, rt=972.31

### Step 3: Node 708 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=972.3101
  - rt2=0.0000
  - sel=1.0000
  - st1=951.3599
  - st2=0.0000
  - startup_cost=169130.6100
  - total_cost=169130.6300
- **Output:** st=1150.46, rt=1152.45

### Step 4: Node 707 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1152.4452
  - rt2=0.0000
  - sel=5.0000
  - st1=1150.4617
  - st2=0.0000
  - startup_cost=170130.6900
  - total_cost=170134.3200
- **Output:** st=1075.00, rt=1079.36

### Step 5: Node 706 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1079.3623
  - rt2=0.0000
  - sel=0.2000
  - st1=1074.9969
  - st2=0.0000
  - startup_cost=170130.6900
  - total_cost=170135.4600
- **Output:** st=1039.48, rt=1052.02
