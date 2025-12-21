# Online Prediction Report

**Test Query:** Q13_21_seed_164080620
**Timestamp:** 2025-12-21 18:04:16

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 20.80%

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
Node 25811 (Sort) - ROOT
  Node 25812 (Aggregate)
    Node 25813 (Aggregate)
      Node 25814 (Hash Join)
        Node 25815 (Seq Scan) - LEAF
        Node 25816 (Hash)
          Node 25817 (Index Only Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 20.17%
- Improvement: 0.63%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25811 | Sort | 900.37 | 1081.93 | 20.2% | operator |
| 25812 | Aggregate | 900.35 | 1000.33 | 11.1% | operator |
| 25813 | Aggregate | 893.52 | 1014.39 | 13.5% | operator |
| 25814 | Hash Join | 681.39 | 787.83 | 15.6% | operator |
| 25815 | Seq Scan | 468.55 | 264.19 | 43.6% | operator |
| 25816 | Hash | 15.27 | 80.15 | 424.9% | operator |
| 25817 | Index Only Scan | 9.98 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25817 (Index Only Scan) - LEAF

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 2: Node 25815 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1487976
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.9920
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=44886.0000
- **Output:** st=-1.96, rt=264.19

### Step 3: Node 25816 (Hash)

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

### Step 4: Node 25814 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1487976
  - nt1=1487976
  - nt2=150000
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=264.1925
  - rt2=80.1470
  - sel=0.0000
  - st1=-1.9574
  - st2=80.1460
  - startup_cost=4587.9200
  - total_cost=53379.9700
- **Output:** st=145.01, rt=787.83

### Step 5: Node 25813 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=1487976
  - nt2=0
  - parallel_workers=0
  - plan_width=12
  - reltuples=0.0000
  - rt1=787.8302
  - rt2=0.0000
  - sel=0.1008
  - st1=145.0116
  - st2=0.0000
  - startup_cost=60819.8500
  - total_cost=62319.8500
- **Output:** st=917.02, rt=1014.39

### Step 6: Node 25812 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1014.3875
  - rt2=0.0000
  - sel=0.0013
  - st1=917.0178
  - st2=0.0000
  - startup_cost=64569.8500
  - total_cost=64571.8500
- **Output:** st=968.70, rt=1000.33

### Step 7: Node 25811 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=200
  - nt1=200
  - nt2=0
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=1000.3283
  - rt2=0.0000
  - sel=1.0000
  - st1=968.6999
  - st2=0.0000
  - startup_cost=64579.4900
  - total_cost=64579.9900
- **Output:** st=1080.39, rt=1081.93
