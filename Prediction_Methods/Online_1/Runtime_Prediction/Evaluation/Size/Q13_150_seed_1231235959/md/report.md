# Online Prediction Report

**Test Query:** Q13_150_seed_1231235959
**Timestamp:** 2026-01-01 17:59:37

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 17.06%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 7524c54c | Aggregate -> Hash Join (Outer) | 2 | 76 | 6.9% | 5.2190 |
| 3d5edd2b | Aggregate -> Aggregate (Outer) | 2 | 24 | 4.2% | 1.0091 |
| deb558a9 | Hash -> Index Only Scan (Outer) | 2 | 24 | 126.0% | 30.2295 |
| 422ae017 | Aggregate -> Hash Join -> [Seq Scan (Out... | 3 | 76 | 6.9% | 5.2190 |
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
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 1d35fb97 | 26.4006 | 0.1163% | ACCEPTED | 17.81% |
| 2 | 7524c54c | 5.0128 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 3 | 422ae017 | 5.0128 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 4 | 35ffb644 | 3.6169 | 0.9450% | ACCEPTED | 16.86% |
| 5 | 24e458a8 | 4.7518 | N/A | REJECTED | 16.86% |
| 6 | 46baed7f | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 7 | a396b865 | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 8 | f592ee11 | 0.4416 | N/A | SKIPPED_LOW_ERROR | 16.86% |
## Query Tree

```
Node 25755 (Sort) [PATTERN: 35ffb644] - ROOT
  Node 25756 (Aggregate) [consumed]
    Node 25757 (Aggregate) [consumed]
      Node 25758 (Hash Join) [PATTERN: 895c6e8c]
        Node 25759 (Seq Scan) [consumed] - LEAF
        Node 25760 (Hash) [consumed]
          Node 25761 (Index Only Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Aggregate | 35ffb644 | 25755 | 25756, 25757, 25758, 25759, 25760 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 25758 | 25755, 25756, 25757, 25759, 25760 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.21%
- Improvement: 16.86%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25755 | Sort | 917.24 | 915.33 | 0.2% | pattern |
| 25758 | Hash Join | 698.38 | 599.79 | 14.1% | pattern |
| 25761 | Index Only Scan | 9.75 | 10.09 | 3.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25761 (Index Only Scan) - LEAF

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

### Step 2: Node 25758 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 25755, 25756, 25757, 25759, 25760
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=1478958
  - HashJoin_nt1=1478958
  - HashJoin_nt2=150000
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=8
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4587.9200
  - HashJoin_total_cost=53356.3000
  - Hash_Inner_np=0
  - Hash_Inner_nt=150000
  - Hash_Inner_nt1=150000
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=2712.9200
  - Hash_Inner_total_cost=2712.9200
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=1478958
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.9860
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=44886.0000
- **Output:** st=17.09, rt=599.79

### Step 3: Node 25755 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 35ffb644 (Sort -> Aggregate -> Aggregate (Outer) (Outer))
- **Consumes:** Nodes 25756, 25757, 25758, 25759, 25760
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=150000
  - Aggregate_Outer_nt1=1478958
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=12
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.1014
  - Aggregate_Outer_startup_cost=60751.0900
  - Aggregate_Outer_total_cost=62251.0900
  - Sort_np=0
  - Sort_nt=200
  - Sort_nt1=200
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=16
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=64510.7300
  - Sort_total_cost=64511.2300
- **Output:** st=915.33, rt=915.33
