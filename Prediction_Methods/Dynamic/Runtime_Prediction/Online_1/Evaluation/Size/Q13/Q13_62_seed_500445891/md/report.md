# Online Prediction Report

**Test Query:** Q13_62_seed_500445891
**Timestamp:** 2025-12-21 18:06:07

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 20.25%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 18066.2% | 77323.2906 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 13.3% | 28.0303 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 68 | 8.3% | 5.6254 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 68 | 8.3% | 5.6254 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 77323.2906 | 0.0004% | REJECTED | 17.07% |
| 1 | 1d35fb97 | 28.0303 | 0.0561% | REJECTED | 17.07% |
| 2 | 7524c54c | 5.6254 | N/A | SKIPPED_LOW_ERROR | 17.07% |
| 3 | 422ae017 | 5.6254 | N/A | SKIPPED_LOW_ERROR | 17.07% |
## Query Tree

```
Node 26126 (Sort) - ROOT
  Node 26127 (Aggregate)
    Node 26128 (Aggregate)
      Node 26129 (Hash Join)
        Node 26130 (Seq Scan) - LEAF
        Node 26131 (Hash)
          Node 26132 (Index Only Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 19.62%
- Improvement: 0.63%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 26126 | Sort | 904.47 | 1081.93 | 19.6% | operator |
| 26127 | Aggregate | 904.46 | 1000.35 | 10.6% | operator |
| 26128 | Aggregate | 898.41 | 1013.97 | 12.9% | operator |
| 26129 | Hash Join | 690.61 | 787.83 | 14.1% | operator |
| 26130 | Seq Scan | 482.64 | 264.04 | 45.3% | operator |
| 26131 | Hash | 15.80 | 80.15 | 407.2% | operator |
| 26132 | Index Only Scan | 10.62 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 26132 (Index Only Scan) - LEAF

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 2: Node 26130 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1481964
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.9880
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=44886.0000
- **Output:** st=-1.94, rt=264.04

### Step 3: Node 26131 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=2712.9200
  - total_cost=2712.9200
- **Output:** st=80.15, rt=80.15

### Step 4: Node 26129 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1481964
  - nt1=1481964
  - nt2=150000
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=264.0432
  - rt2=80.1470
  - sel=0.0000
  - st1=-1.9404
  - st2=80.1460
  - startup_cost=4587.9200
  - total_cost=53364.1900
- **Output:** st=145.01, rt=787.83

### Step 5: Node 26128 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=1481964
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=787.8302
  - rt2=0.0000
  - sel=0.1012
  - st1=145.0116
  - st2=0.0000
  - startup_cost=60774.0100
  - total_cost=62274.0100
- **Output:** st=917.08, rt=1013.97

### Step 6: Node 26127 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1013.9745
  - rt2=0.0000
  - sel=0.0013
  - st1=917.0771
  - st2=0.0000
  - startup_cost=64524.0100
  - total_cost=64526.0100
- **Output:** st=968.71, rt=1000.35

### Step 7: Node 26126 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=200
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1000.3513
  - rt2=0.0000
  - sel=1.0000
  - st1=968.7149
  - st2=0.0000
  - startup_cost=64533.6500
  - total_cost=64534.1500
- **Output:** st=1080.39, rt=1081.93
