# Online Prediction Report

**Test Query:** Q13_127_seed_1033707906
**Timestamp:** 2025-12-13 02:26:34

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 14.52%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 75736.1626 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 26.4017 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 5.2190 |
| 3d5edd2b | Aggregate -> Aggregate (Outer) | 2 | 24 | 1.0091 |
| deb558a9 | Hash -> Index Only Scan (Outer) | 2 | 24 | 30.2295 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 5.2190 |
| 35ffb644 | Sort -> Aggregate -> Aggregate (Outer) (... | 3 | 24 | 4.0145 |
| 57bf6442 | Aggregate -> Aggregate -> Hash Join (Out... | 3 | 24 | 1.0091 |
| 24e458a8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 0.9883 |
| 46baed7f | Sort -> Aggregate -> Aggregate -> Hash J... | 4 | 24 | 4.0145 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 4 | deb558a9 | 30.2295 | 0.0000% | REJECTED | 17.92% |
| 6 | 35ffb644 | 4.0145 | 1.0634% | ACCEPTED | 16.86% |
## Query Tree

```
Node 25573 (Sort) [PATTERN: 35ffb644] - ROOT
  Node 25574 (Aggregate) [consumed]
    Node 25575 (Aggregate) [consumed]
      Node 25576 (Hash Join)
        Node 25577 (Seq Scan) - LEAF
        Node 25578 (Hash)
          Node 25579 (Index Only Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Aggregate | 35ffb644 | 25573 | 25574, 25575 |


## Phase E: Final Prediction

- Final MRE: 2.38%
- Improvement: 12.14%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25573 | Sort | 937.65 | 915.33 | 2.4% | pattern |
| 25576 | Hash Join | 719.08 | 705.85 | 1.8% | operator |
| 25577 | Seq Scan | 506.15 | 412.66 | 18.5% | operator |
| 25578 | Hash | 15.70 | 37.64 | 139.7% | operator |
| 25579 | Index Only Scan | 10.29 | 10.09 | 2.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25579 (Index Only Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=150000
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4200
  - total_cost=2712.9200
- **Output:** st=0.01, rt=10.09

### Step 2: Node 25577 (Seq Scan) - LEAF

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
- **Output:** st=0.23, rt=412.66

### Step 3: Node 25578 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=10.0855
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0110
  - st2=0.0000
  - startup_cost=2712.9200
  - total_cost=2712.9200
- **Output:** st=37.63, rt=37.64

### Step 4: Node 25576 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1487976
  - nt1=1487976
  - nt2=150000
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=412.6621
  - rt2=37.6351
  - sel=0.0000
  - st1=0.2327
  - st2=37.6337
  - startup_cost=4587.9200
  - total_cost=53379.9700
- **Output:** st=17.69, rt=705.85

### Step 5: Node 25573 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 35ffb644 (Sort -> Aggregate -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 25574, 25575
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=150000
  - Aggregate_Outer_nt1=1487976
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=12
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.1008
  - Aggregate_Outer_startup_cost=60819.8500
  - Aggregate_Outer_total_cost=62319.8500
  - Sort_np=0
  - Sort_nt=200
  - Sort_nt1=200
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=16
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=64579.4900
  - Sort_total_cost=64579.9900
- **Output:** st=915.33, rt=915.33
