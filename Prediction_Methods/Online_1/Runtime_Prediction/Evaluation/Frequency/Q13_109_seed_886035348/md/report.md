# Online Prediction Report

**Test Query:** Q13_109_seed_886035348
**Timestamp:** 2025-12-22 06:40:41

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 14.95%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 3d5edd2b | Aggregate -> Aggregate (Outer) | 2 | 24 | 4.2% | 1.0091 |
| deb558a9 | Hash -> Index Only Scan (Outer) | 2 | 24 | 126.0% | 30.2295 |
| 35ffb644 | Sort -> Aggregate -> Aggregate (Outer) (... | 3 | 24 | 16.7% | 4.0145 |
| 57bf6442 | Aggregate -> Aggregate -> Hash Join (Out... | 3 | 24 | 4.2% | 1.0091 |
| 24e458a8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 4.1% | 0.9883 |
| 46baed7f | Sort -> Aggregate -> Aggregate -> Hash J... | 4 | 24 | 16.7% | 4.0145 |
| fc9b94fb | Aggregate -> Aggregate -> Hash Join -> [... | 4 | 24 | 4.2% | 1.0091 |
| 5ad512ef | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 24 | 3.9% | 0.9476 |
| a396b865 | Sort -> Aggregate -> Aggregate -> Hash J... | 5 | 24 | 16.7% | 4.0145 |
| 32b96b54 | Aggregate -> Aggregate -> Hash Join -> [... | 5 | 24 | 4.2% | 1.0091 |
| f592ee11 | Sort -> Aggregate -> Aggregate -> Hash J... | 6 | 24 | 16.7% | 4.0145 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 2 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | 422ae017 | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 3d5edd2b | 1.0091 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | deb558a9 | 30.2295 | 0.0000% | REJECTED | 17.92% |
| 6 | 35ffb644 | 4.0145 | 1.0634% | ACCEPTED | 16.86% |
| 7 | 24e458a8 | 0.9883 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 8 | 46baed7f | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 9 | a396b865 | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 10 | f592ee11 | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
## Query Tree

```
Node 25433 (Sort) [PATTERN: 35ffb644] - ROOT
  Node 25434 (Aggregate) [consumed]
    Node 25435 (Aggregate) [consumed]
      Node 25436 (Hash Join)
        Node 25437 (Seq Scan) - LEAF
        Node 25438 (Hash)
          Node 25439 (Index Only Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Aggregate | 35ffb644 | 25433 | 25434, 25435 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.01%
- Improvement: 12.95%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25433 | Sort | 934.07 | 915.33 | 2.0% | pattern |
| 25436 | Hash Join | 722.61 | 705.78 | 2.3% | operator |
| 25437 | Seq Scan | 513.92 | 412.35 | 19.8% | operator |
| 25438 | Hash | 14.69 | 37.64 | 156.3% | operator |
| 25439 | Index Only Scan | 9.32 | 10.09 | 8.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25439 (Index Only Scan) - LEAF

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

### Step 2: Node 25437 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1484970
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.9900
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=44886.0000
- **Output:** st=0.23, rt=412.35

### Step 3: Node 25438 (Hash)

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

### Step 4: Node 25436 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1484970
  - nt1=1484970
  - nt2=150000
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=412.3512
  - rt2=37.6351
  - sel=0.0000
  - st1=0.2339
  - st2=37.6337
  - startup_cost=4587.9200
  - total_cost=53372.0800
- **Output:** st=17.74, rt=705.78

### Step 5: Node 25433 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 35ffb644 (Sort -> Aggregate -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 25434, 25435
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=150000
  - Aggregate_Outer_nt1=1484970
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=12
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.1010
  - Aggregate_Outer_startup_cost=60796.9300
  - Aggregate_Outer_total_cost=62296.9300
  - Sort_np=0
  - Sort_nt=200
  - Sort_nt1=200
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=16
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=64556.5700
  - Sort_total_cost=64557.0700
- **Output:** st=915.33, rt=915.33
