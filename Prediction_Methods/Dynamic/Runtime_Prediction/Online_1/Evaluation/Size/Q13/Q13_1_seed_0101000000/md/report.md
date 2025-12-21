# Online Prediction Report

**Test Query:** Q13_1_seed_0101000000
**Timestamp:** 2025-12-21 18:01:56

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 17.82%

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
Node 25797 (Sort) - ROOT
  Node 25798 (Aggregate)
    Node 25799 (Aggregate)
      Node 25800 (Hash Join)
        Node 25801 (Seq Scan) - LEAF
        Node 25802 (Hash)
          Node 25803 (Index Only Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 17.20%
- Improvement: 0.62%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25797 | Sort | 923.16 | 1081.93 | 17.2% | operator |
| 25798 | Aggregate | 923.13 | 1000.32 | 8.4% | operator |
| 25799 | Aggregate | 917.05 | 1014.59 | 10.6% | operator |
| 25800 | Hash Join | 702.76 | 787.83 | 12.1% | operator |
| 25801 | Seq Scan | 492.27 | 264.27 | 46.3% | operator |
| 25802 | Hash | 15.40 | 80.15 | 420.5% | operator |
| 25803 | Index Only Scan | 10.37 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25803 (Index Only Scan) - LEAF

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 2: Node 25801 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1490982
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.9940
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=44886.0000
- **Output:** st=-1.97, rt=264.27

### Step 3: Node 25802 (Hash)

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

### Step 4: Node 25800 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1490982
  - nt1=1490982
  - nt2=150000
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=264.2662
  - rt2=80.1470
  - sel=0.0000
  - st1=-1.9658
  - st2=80.1460
  - startup_cost=4587.9200
  - total_cost=53387.8600
- **Output:** st=145.01, rt=787.83

### Step 5: Node 25799 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=1490982
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=787.8302
  - rt2=0.0000
  - sel=0.1006
  - st1=145.0116
  - st2=0.0000
  - startup_cost=60842.7700
  - total_cost=62342.7700
- **Output:** st=916.99, rt=1014.59

### Step 6: Node 25798 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1014.5946
  - rt2=0.0000
  - sel=0.0013
  - st1=916.9884
  - st2=0.0000
  - startup_cost=64592.7700
  - total_cost=64594.7700
- **Output:** st=968.69, rt=1000.32

### Step 7: Node 25797 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=200
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1000.3169
  - rt2=0.0000
  - sel=1.0000
  - st1=968.6925
  - st2=0.0000
  - startup_cost=64602.4100
  - total_cost=64602.9100
- **Output:** st=1080.39, rt=1081.93
