# Online Prediction Report

**Test Query:** Q1_80_seed_648118449
**Timestamp:** 2026-01-11 19:29:04

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 9.96%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 24 | 22.0% | 5.2893 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 48 | 8.4% | 4.0548 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
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
| 1 | 2724c080 | 7.7852 | 0.0346% | ACCEPTED | 17.77% |
| 2 | 184f44de | 5.7958 | 0.0023% | ACCEPTED | 17.77% |
| 3 | 29ee00db | 4.4857 | 0.2706% | ACCEPTED | 17.50% |
| 4 | f8231c4d | 2.1781 | 0.2456% | ACCEPTED | 17.25% |
| 5 | 3dfa6025 | 0.8661 | 0.0234% | ACCEPTED | 17.23% |
## Query Tree

```
Node 641 (Aggregate) [PATTERN: 3dfa6025] - ROOT
  Node 642 (Gather Merge) [consumed]
    Node 643 (Sort) [consumed]
      Node 644 (Aggregate) [consumed]
        Node 645 (Seq Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> S | 3dfa6025 | 641 | 642, 643, 644, 645 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.13%
- Improvement: 9.83%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 641 | Aggregate | 955.18 | 953.98 | 0.1% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 641 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 3dfa6025 (Aggregate -> Gather Merge -> Sort -> Aggregate -> Seq Scan (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 642, 643, 644, 645
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=6
  - Aggregate_Outer_nt1=1188459
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=236
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=169199.1000
  - Aggregate_Outer_total_cost=169199.2400
  - Aggregate_np=0
  - Aggregate_nt=6
  - Aggregate_nt1=30
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=236
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=170199.3900
  - Aggregate_total_cost=170204.1600
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=30
  - GatherMerge_Outer_nt1=6
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=5
  - GatherMerge_Outer_plan_width=236
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=5.0000
  - GatherMerge_Outer_startup_cost=170199.3900
  - GatherMerge_Outer_total_cost=170203.0200
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=1188459
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=25
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.1980
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
  - Sort_Outer_startup_cost=169199.3200
  - Sort_Outer_total_cost=169199.3300
- **Output:** st=949.38, rt=953.98
