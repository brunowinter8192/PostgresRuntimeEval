# Online Prediction Report

**Test Query:** Q13_59_seed_475833798
**Timestamp:** 2025-12-21 21:01:38

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 17.62%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 35ffb644 | Sort -> Aggregate -> Aggregate (Outer) (... | 3 | 24 | 16.7% | 4.0145 |
| 46baed7f | Sort -> Aggregate -> Aggregate -> Hash J... | 4 | 24 | 16.7% | 4.0145 |
| a396b865 | Sort -> Aggregate -> Aggregate -> Hash J... | 5 | 24 | 16.7% | 4.0145 |
| f592ee11 | Sort -> Aggregate -> Aggregate -> Hash J... | 6 | 24 | 16.7% | 4.0145 |
| 3d5edd2b | Aggregate -> Aggregate (Outer) | 2 | 24 | 4.2% | 1.0091 |
| 57bf6442 | Aggregate -> Aggregate -> Hash Join (Out... | 3 | 24 | 4.2% | 1.0091 |
| fc9b94fb | Aggregate -> Aggregate -> Hash Join -> [... | 4 | 24 | 4.2% | 1.0091 |
| 32b96b54 | Aggregate -> Aggregate -> Hash Join -> [... | 5 | 24 | 4.2% | 1.0091 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
| 5ad512ef | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 24 | 3.9% | 0.9476 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 24e458a8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 24 | 4.1% | 0.9883 |
| deb558a9 | Hash -> Index Only Scan (Outer) | 2 | 24 | 126.0% | 30.2295 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | REJECTED | 17.92% |
| 1 | deb558a9 | 30.2295 | 0.0000% | REJECTED | 17.92% |
| 2 | 1d35fb97 | 26.4017 | 0.1167% | REJECTED | 17.92% |
| 3 | 422ae017 | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 35ffb644 | 4.0145 | 1.0634% | ACCEPTED | 16.86% |
| 6 | 24e458a8 | 0.9883 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 7 | 46baed7f | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 8 | a396b865 | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 9 | f592ee11 | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
## Query Tree

```
Node 26098 (Sort) [PATTERN: 35ffb644] - ROOT
  Node 26099 (Aggregate) [consumed]
    Node 26100 (Aggregate) [consumed]
      Node 26101 (Hash Join)
        Node 26102 (Seq Scan) - LEAF
        Node 26103 (Hash)
          Node 26104 (Index Only Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Aggregate | 35ffb644 | 26098 | 26099, 26100 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.26%
- Improvement: 17.35%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 26098 | Sort | 912.93 | 915.33 | 0.3% | pattern |
| 26101 | Hash Join | 692.08 | 705.85 | 2.0% | operator |
| 26102 | Seq Scan | 479.22 | 412.66 | 13.9% | operator |
| 26103 | Hash | 15.47 | 37.64 | 143.3% | operator |
| 26104 | Index Only Scan | 10.06 | 10.09 | 0.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 26104 (Index Only Scan) - LEAF

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

### Step 2: Node 26102 (Seq Scan) - LEAF

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

### Step 3: Node 26103 (Hash)

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

### Step 4: Node 26101 (Hash Join)

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

### Step 5: Node 26098 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 35ffb644 (Sort -> Aggregate -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 26099, 26100
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
