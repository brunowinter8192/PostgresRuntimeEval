# Online Prediction Report

**Test Query:** Q13_59_seed_475833798
**Timestamp:** 2026-01-11 18:03:36

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
| 5ad512ef | Aggregate -> Hash Join -> [Seq Scan (Out... | 4 | 24 | 3.9% | 0.9476 |
| fc9b94fb | Aggregate -> Aggregate -> Hash Join -> [... | 4 | 24 | 4.2% | 1.0091 |
| 32b96b54 | Aggregate -> Aggregate -> Hash Join -> [... | 5 | 24 | 4.2% | 1.0091 |
| a396b865 | Sort -> Aggregate -> Aggregate -> Hash J... | 5 | 24 | 16.7% | 4.0145 |
| f592ee11 | Sort -> Aggregate -> Aggregate -> Hash J... | 6 | 24 | 16.7% | 4.0145 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1163% | ACCEPTED | 17.81% |
| 2 | 7524c54c | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 3 | 422ae017 | 5.2190 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 4 | 3d5edd2b | 1.0091 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | deb558a9 | 30.2295 | N/A | REJECTED | 17.81% |
| 6 | 35ffb644 | 4.0145 | 0.9450% | ACCEPTED | 16.86% |
| 7 | 57bf6442 | 1.0091 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 8 | 24e458a8 | 0.9883 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 9 | 46baed7f | 4.0145 | -0.0000% | REJECTED | 16.86% |
| 10 | 5ad512ef | 0.9476 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 11 | fc9b94fb | 1.0091 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 12 | 32b96b54 | 1.0091 | N/A | SKIPPED_LOW_ERROR | 16.86% |
| 13 | a396b865 | 4.0145 | -0.0000% | REJECTED | 16.86% |
| 14 | f592ee11 | 4.0145 | 0.0000% | ACCEPTED | 16.86% |
## Query Tree

```
Node 26098 (Sort) [PATTERN: f592ee11] - ROOT
  Node 26099 (Aggregate) [consumed]
    Node 26100 (Aggregate) [consumed]
      Node 26101 (Hash Join) [consumed]
        Node 26102 (Seq Scan) [consumed] - LEAF
        Node 26103 (Hash) [consumed]
          Node 26104 (Index Only Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate -> Aggregate | f592ee11 | 26098 | 26099, 26100, 26101, 26102, 26103, 26104 |


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

## Prediction Chain (Bottom-Up)

### Step 1: Node 26098 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f592ee11 (Sort -> Aggregate -> Aggregate -> Hash Join -> [Seq Scan (Outer), Hash -> Index Only Scan (Outer) (Inner)] (Outer) (Outer) (Outer))
- **Consumes:** Nodes 26099, 26100, 26101, 26102, 26103, 26104
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
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=1487976
  - HashJoin_Outer_nt1=1487976
  - HashJoin_Outer_nt2=150000
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=8
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.0000
  - HashJoin_Outer_startup_cost=4587.9200
  - HashJoin_Outer_total_cost=53379.9700
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
  - IndexOnlyScan_Outer_np=3600
  - IndexOnlyScan_Outer_nt=150000
  - IndexOnlyScan_Outer_nt1=0
  - IndexOnlyScan_Outer_nt2=0
  - IndexOnlyScan_Outer_parallel_workers=0
  - IndexOnlyScan_Outer_plan_width=4
  - IndexOnlyScan_Outer_reltuples=150000.0000
  - IndexOnlyScan_Outer_sel=1.0000
  - IndexOnlyScan_Outer_startup_cost=0.4200
  - IndexOnlyScan_Outer_total_cost=2712.9200
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=1487976
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=8
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.9920
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=44886.0000
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
