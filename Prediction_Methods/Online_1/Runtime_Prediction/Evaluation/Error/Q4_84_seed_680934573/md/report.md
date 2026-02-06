# Online Prediction Report

**Test Query:** Q4_84_seed_680934573
**Timestamp:** 2026-01-11 20:16:52

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.80%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 192 | 13.8% | 26.4017 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 48 | 9.1% | 4.3530 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 44 | 8.1% | 3.5717 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 48 | 7.1% | 3.4083 |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 24 | 12.7% | 3.0380 |
| 1393818c | Gather Merge -> Sort -> Aggregate -> Nes... | 4 | 24 | 4.9% | 1.1790 |
| 6e6e9493 | Gather Merge -> Sort -> Aggregate -> Nes... | 5 | 24 | 4.9% | 1.1790 |
| 260efc4f | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 24 | 4.3% | 1.0349 |
| 80bd802d | Aggregate -> Gather Merge -> Sort -> Agg... | 6 | 24 | 4.3% | 1.0349 |
| ab77776a | Sort -> Aggregate -> Nested Loop -> [Seq... | 4 | 24 | 2.1% | 0.5091 |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 24 | 2.1% | 0.5091 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 1 | 1d35fb97 | 26.4017 | 0.1167% | ACCEPTED | 17.81% |
| 2 | 2724c080 | 7.7852 | 0.0346% | ACCEPTED | 17.77% |
| 3 | 29ee00db | 4.4857 | 0.2706% | ACCEPTED | 17.50% |
| 4 | 3b447875 | 3.5717 | N/A | REJECTED | 17.50% |
| 5 | 3f1648ef | 3.0380 | N/A | REJECTED | 17.50% |
| 6 | f8231c4d | 2.1781 | 0.2456% | ACCEPTED | 17.26% |
| 7 | 260efc4f | 0.4868 | 0.0308% | ACCEPTED | 17.23% |
| 8 | 80bd802d | 0.3833 | 0.0000% | ACCEPTED | 17.23% |
## Query Tree

```
Node 6775 (Aggregate) [PATTERN: 80bd802d] - ROOT
  Node 6776 (Gather Merge) [consumed]
    Node 6777 (Sort) [consumed]
      Node 6778 (Aggregate) [consumed]
        Node 6779 (Nested Loop) [consumed]
          Node 6780 (Seq Scan) [consumed] - LEAF
          Node 6781 (Index Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> S | 80bd802d | 6775 | 6776, 6777, 6778, 6779, 6780, 6781 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 1.07%
- Improvement: 3.73%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6775 | Aggregate | 1069.25 | 1057.79 | 1.1% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6775 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 80bd802d (Aggregate -> Gather Merge -> Sort -> Aggregate -> Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 6776, 6777, 6778, 6779, 6780, 6781
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=14842
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=65847.1600
  - Aggregate_Outer_total_cost=65847.2100
  - Aggregate_np=0
  - Aggregate_nt=5
  - Aggregate_nt1=15
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=24
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=66847.3100
  - Aggregate_total_cost=66849.2100
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=15
  - GatherMerge_Outer_nt1=5
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=24
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0000
  - GatherMerge_Outer_startup_cost=66847.3100
  - GatherMerge_Outer_total_cost=66849.0800
  - IndexScan_Inner_np=112600
  - IndexScan_Inner_nt=2
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=4
  - IndexScan_Inner_reltuples=6001215.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=2.3100
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=14842
  - NestedLoop_Outer_nt1=18201
  - NestedLoop_Outer_nt2=2
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=16
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.4077
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=65772.9500
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=18201
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=20
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.0121
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=33394.0600
  - Sort_Outer_np=0
  - Sort_Outer_nt=5
  - Sort_Outer_nt1=5
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=24
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=65847.2700
  - Sort_Outer_total_cost=65847.2800
- **Output:** st=1055.76, rt=1057.79
