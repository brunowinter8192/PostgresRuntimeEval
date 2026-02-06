# Online Prediction Report

**Test Query:** Q1_27_seed_213304806
**Timestamp:** 2026-01-11 17:51:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.53%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 22.0% | 5.2893 |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 24 | 13.2% | 3.1739 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 9.9% | 2.3734 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 1 | 2724c080 | 19.6008 | 0.0346% | ACCEPTED | 17.77% |
| 2 | 1691f6f0 | 7.3257 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 3 | 29ee00db | 4.4662 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 4 | 184f44de | 4.0548 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 5 | 715d5c92 | 4.3530 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 6 | f8231c4d | 3.4083 | N/A | SKIPPED_LOW_ERROR | 17.77% |
| 7 | dc1b1da7 | 5.2893 | N/A | REJECTED | 17.77% |
| 8 | 52c5ec81 | 3.1739 | 0.0894% | ACCEPTED | 17.68% |
| 9 | 3dfa6025 | 2.3734 | N/A | SKIPPED_LOW_ERROR | 17.68% |
## Query Tree

```
Node 346 (Aggregate) - ROOT
  Node 347 (Gather Merge) [PATTERN: 52c5ec81]
    Node 348 (Sort) [consumed]
      Node 349 (Aggregate) [consumed]
        Node 350 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Gather Merge -> Sort -> Aggreg | 52c5ec81 | 347 | 348, 349, 350 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.96%
- Improvement: 1.58%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 346 | Aggregate | 958.88 | 1035.17 | 8.0% | operator |
| 347 | Gather Merge | 958.82 | 953.93 | 0.5% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 347 (Gather Merge) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 52c5ec81 (Gather Merge -> Sort -> Aggregate -> Seq Scan (Outer) (Outer) (Outer))
- **Consumes:** Nodes 348, 349, 350
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=6
  - Aggregate_Outer_nt1=1185350
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=236
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=169090.2900
  - Aggregate_Outer_total_cost=169090.4200
  - GatherMerge_np=0
  - GatherMerge_nt=30
  - GatherMerge_nt1=6
  - GatherMerge_nt2=0
  - GatherMerge_parallel_workers=5
  - GatherMerge_plan_width=236
  - GatherMerge_reltuples=0.0000
  - GatherMerge_sel=5.0000
  - GatherMerge_startup_cost=170090.5800
  - GatherMerge_total_cost=170094.2100
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=1185350
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=25
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.1975
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=127603.0400
  - Sort_Outer_np=0
  - Sort_Outer_nt=6
  - Sort_Outer_nt1=6
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=236
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=169090.5000
  - Sort_Outer_total_cost=169090.5200
- **Output:** st=949.34, rt=953.93

### Step 2: Node 346 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=953.9293
  - rt2=0.0000
  - sel=0.2000
  - st1=949.3411
  - st2=0.0000
  - startup_cost=170090.5800
  - total_cost=170095.3500
- **Output:** st=1026.45, rt=1035.17
