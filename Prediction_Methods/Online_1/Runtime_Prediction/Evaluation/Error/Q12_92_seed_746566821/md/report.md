# Online Prediction Report

**Test Query:** Q12_92_seed_746566821
**Timestamp:** 2026-01-11 19:40:55

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.93%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 24 | 9.2% | 2.1961 |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 24 | 9.2% | 2.1961 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| 3a2624e2 | Gather Merge -> Aggregate -> Sort -> Nes... | 5 | 24 | 6.8% | 1.6208 |
| 898abd49 | Gather Merge -> Aggregate -> Sort -> Nes... | 4 | 24 | 6.8% | 1.6208 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| b692b3d9 | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 4.6% | 1.0973 |
| f9c97829 | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 4.6% | 1.0973 |
| a0631e25 | Aggregate -> Sort -> Nested Loop -> [Seq... | 4 | 24 | 4.0% | 0.9714 |
| fbf3ebe8 | Aggregate -> Sort -> Nested Loop (Outer)... | 3 | 24 | 4.0% | 0.9714 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | ACCEPTED | 17.90% |
| 2 | 263b40d6 | 2.1961 | N/A | REJECTED | 17.90% |
| 3 | 5b623fa1 | 2.1961 | N/A | REJECTED | 17.90% |
| 4 | 3754655c | 2.1302 | N/A | REJECTED | 17.90% |
| 5 | 460af52c | 1.5019 | 0.2317% | ACCEPTED | 17.67% |
| 6 | 8a8c43c6 | 0.5598 | N/A | REJECTED | 17.67% |
| 7 | b692b3d9 | 0.2218 | 0.0061% | ACCEPTED | 17.66% |
| 8 | f9c97829 | 0.2013 | 0.0000% | ACCEPTED | 17.66% |
## Query Tree

```
Node 25307 (Aggregate) [PATTERN: f9c97829] - ROOT
  Node 25308 (Gather Merge) [consumed]
    Node 25309 (Aggregate) [consumed]
      Node 25310 (Sort) [consumed]
        Node 25311 (Nested Loop) [consumed]
          Node 25312 (Seq Scan) [consumed] - LEAF
          Node 25313 (Index Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> A | f9c97829 | 25307 | 25308, 25309, 25310, 25311, 25312, 25313 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 0.48%
- Improvement: 4.45%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25307 | Aggregate | 1003.31 | 998.49 | 0.5% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25307 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f9c97829 (Aggregate -> Gather Merge -> Aggregate -> Sort -> Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)] (Outer) (Outer) (Outer) (Outer))
- **Consumes:** Nodes 25308, 25309, 25310, 25311, 25312, 25313
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=7
  - Aggregate_Outer_nt1=5773
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=27
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0012
  - Aggregate_Outer_startup_cost=147532.1100
  - Aggregate_Outer_total_cost=147647.6400
  - Aggregate_np=0
  - Aggregate_nt=7
  - Aggregate_nt1=35
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=27
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=148532.1900
  - Aggregate_total_cost=148652.2600
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=35
  - GatherMerge_Outer_nt1=7
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=5
  - GatherMerge_Outer_plan_width=27
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=5.0000
  - GatherMerge_Outer_startup_cost=148532.1900
  - GatherMerge_Outer_total_cost=148651.9300
  - IndexScan_Inner_np=26136
  - IndexScan_Inner_nt=1
  - IndexScan_Inner_nt1=0
  - IndexScan_Inner_nt2=0
  - IndexScan_Inner_parallel_workers=0
  - IndexScan_Inner_plan_width=20
  - IndexScan_Inner_reltuples=1500000.0000
  - IndexScan_Inner_sel=0.0000
  - IndexScan_Inner_startup_cost=0.4300
  - IndexScan_Inner_total_cost=1.3100
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=5773
  - NestedLoop_Outer_nt1=5773
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=27
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=0.4300
  - NestedLoop_Outer_total_cost=147171.4400
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=5773
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=15
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0010
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=139605.4700
  - Sort_Outer_np=0
  - Sort_Outer_nt=5773
  - Sort_Outer_nt1=5773
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=27
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=147532.1100
  - Sort_Outer_total_cost=147546.5400
- **Output:** st=993.89, rt=998.49
