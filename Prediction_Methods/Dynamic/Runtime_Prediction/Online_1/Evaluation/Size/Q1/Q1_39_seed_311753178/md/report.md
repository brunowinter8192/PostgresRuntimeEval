# Online Prediction Report

**Test Query:** Q1_39_seed_311753178
**Timestamp:** 2025-12-21 14:30:26

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18851 | Operator + Pattern Training |
| Training_Test | 4718 | Pattern Selection Eval |
| Training | 23569 | Final Model Training |
| Test | 750 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 18.45%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 12.1% | 25.4704 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 10.9% | 19.6991 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 4.7% | 4.2081 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 30 | 11.0% | 3.2970 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 2.4% | 2.1972 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 30 | 5.0% | 1.5106 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 30 | 3.3% | 0.9962 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 25.4704 | 0.1652% | REJECTED | 17.42% |
| 1 | 2724c080 | 19.6991 | -0.2283% | REJECTED | 17.42% |
| 2 | 1691f6f0 | 4.2081 | N/A | SKIPPED_LOW_ERROR | 17.42% |
| 3 | 184f44de | 3.2970 | 0.0045% | REJECTED | 17.42% |
| 4 | 29ee00db | 2.1972 | N/A | SKIPPED_LOW_ERROR | 17.42% |
| 5 | 715d5c92 | 1.5106 | N/A | SKIPPED_LOW_ERROR | 17.42% |
| 6 | f8231c4d | 0.9962 | N/A | SKIPPED_LOW_ERROR | 17.42% |
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

- Final MRE: 20.54%
- Improvement: -2.09%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 411 | Aggregate | 992.08 | 1195.86 | 20.5% | operator |
| 412 | Gather Merge | 992.03 | 1165.59 | 17.5% | operator |
| 413 | Sort | 972.09 | 1182.05 | 21.6% | operator |
| 414 | Aggregate | 972.05 | 1112.95 | 14.5% | operator |
| 415 | Seq Scan | 596.39 | 680.00 | 14.0% | operator |

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
- **Output:** st=0.85, rt=680.00

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
  - rt1=680.0004
  - rt2=0.0000
  - sel=0.0000
  - st1=0.8505
  - st2=0.0000
  - startup_cost=169010.1000
  - total_cost=169010.2400
- **Output:** st=1037.41, rt=1112.95

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
  - rt1=1112.9450
  - rt2=0.0000
  - sel=1.0000
  - st1=1037.4110
  - st2=0.0000
  - startup_cost=169010.3200
  - total_cost=169010.3300
- **Output:** st=1180.98, rt=1182.05

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
  - rt1=1182.0525
  - rt2=0.0000
  - sel=5.0000
  - st1=1180.9828
  - st2=0.0000
  - startup_cost=170010.3900
  - total_cost=170014.0200
- **Output:** st=1161.46, rt=1165.59

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
  - rt1=1165.5889
  - rt2=0.0000
  - sel=0.2000
  - st1=1161.4641
  - st2=0.0000
  - startup_cost=170010.3900
  - total_cost=170015.1600
- **Output:** st=1149.88, rt=1195.86
