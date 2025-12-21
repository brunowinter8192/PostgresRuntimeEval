# Online Prediction Report

**Test Query:** Q13_84_seed_680934573
**Timestamp:** 2025-12-21 18:07:47

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 21.00%

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
Node 26294 (Sort) - ROOT
  Node 26295 (Aggregate)
    Node 26296 (Aggregate)
      Node 26297 (Hash Join)
        Node 26298 (Seq Scan) - LEAF
        Node 26299 (Hash)
          Node 26300 (Index Only Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 20.37%
- Improvement: 0.64%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 26294 | Sort | 898.86 | 1081.92 | 20.4% | operator |
| 26295 | Aggregate | 898.84 | 1000.40 | 11.3% | operator |
| 26296 | Aggregate | 892.79 | 1013.15 | 13.5% | operator |
| 26297 | Hash Join | 683.34 | 787.83 | 15.3% | operator |
| 26298 | Seq Scan | 473.90 | 263.74 | 44.3% | operator |
| 26299 | Hash | 16.42 | 80.15 | 388.1% | operator |
| 26300 | Index Only Scan | 10.48 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 26300 (Index Only Scan) - LEAF

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 2: Node 26298 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1469940
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.9800
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=44886.0000
- **Output:** st=-1.91, rt=263.74

### Step 3: Node 26299 (Hash)

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

### Step 4: Node 26297 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1469940
  - nt1=1469940
  - nt2=150000
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=263.7364
  - rt2=80.1470
  - sel=0.0000
  - st1=-1.9059
  - st2=80.1460
  - startup_cost=4587.9200
  - total_cost=53332.6200
- **Output:** st=145.01, rt=787.83

### Step 5: Node 26296 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=1469940
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=787.8302
  - rt2=0.0000
  - sel=0.1020
  - st1=145.0116
  - st2=0.0000
  - startup_cost=60682.3200
  - total_cost=62182.3200
- **Output:** st=917.20, rt=1013.15

### Step 6: Node 26295 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1013.1535
  - rt2=0.0000
  - sel=0.0013
  - st1=917.1976
  - st2=0.0000
  - startup_cost=64432.3200
  - total_cost=64434.3200
- **Output:** st=968.75, rt=1000.40

### Step 7: Node 26294 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=200
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1000.3979
  - rt2=0.0000
  - sel=1.0000
  - st1=968.7454
  - st2=0.0000
  - startup_cost=64441.9700
  - total_cost=64442.4700
- **Output:** st=1080.38, rt=1081.92
