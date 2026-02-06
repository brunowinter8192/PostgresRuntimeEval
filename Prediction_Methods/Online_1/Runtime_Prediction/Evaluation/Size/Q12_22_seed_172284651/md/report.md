# Online Prediction Report

**Test Query:** Q12_22_seed_172284651
**Timestamp:** 2026-01-11 16:25:21

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.14%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 4.4% | 2.1302 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 5.9% | 2.8144 |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 24 | 9.2% | 2.1961 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 147.6% | 141.6847 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 3.2% | 1.5375 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 5.9% | 2.8144 |
| fbf3ebe8 | Aggregate -> Sort -> Nested Loop (Outer)... | 3 | 24 | 4.0% | 0.9714 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 3.2% | 1.5375 |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 24 | 9.2% | 2.1961 |
| 898abd49 | Gather Merge -> Aggregate -> Sort -> Nes... | 4 | 24 | 6.8% | 1.6208 |
| a0631e25 | Aggregate -> Sort -> Nested Loop -> [Seq... | 4 | 24 | 4.0% | 0.9714 |
| b692b3d9 | Aggregate -> Gather Merge -> Aggregate -... | 5 | 24 | 4.6% | 1.0973 |
| 3a2624e2 | Gather Merge -> Aggregate -> Sort -> Nes... | 5 | 24 | 6.8% | 1.6208 |
| f9c97829 | Aggregate -> Gather Merge -> Aggregate -... | 6 | 24 | 4.6% | 1.0973 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 2724c080 | 19.6008 | 0.0222% | ACCEPTED | 17.90% |
| 1 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 2 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 3 | 263b40d6 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 4 | c53c4396 | 141.6847 | 0.0000% | ACCEPTED | 17.90% |
| 5 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 6 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 7 | fbf3ebe8 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 8 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 9 | 5b623fa1 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 10 | 898abd49 | 1.6208 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 11 | a0631e25 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 12 | b692b3d9 | 1.0973 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 13 | 3a2624e2 | 1.6208 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 14 | f9c97829 | 1.0973 | N/A | SKIPPED_LOW_ERROR | 17.90% |
## Query Tree

```
Node 24768 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 24769 (Gather Merge) [consumed]
    Node 24770 (Aggregate)
      Node 24771 (Sort)
        Node 24772 (Nested Loop) [PATTERN: c53c4396]
          Node 24773 (Seq Scan) [consumed] - LEAF
          Node 24774 (Index Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge (Out | 2724c080 | 24768 | 24769, 24772, 24773, 24774 |
| Nested Loop -> [Seq Scan (Oute | c53c4396 | 24772 | 24768, 24769, 24773, 24774 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.13%
- Improvement: 3.01%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24768 | Aggregate | 1005.60 | 1027.05 | 2.1% | pattern |
| 24770 | Aggregate | 986.72 | 940.64 | 4.7% | operator |
| 24771 | Sort | 986.11 | 1050.78 | 6.6% | operator |
| 24772 | Nested Loop | 985.06 | 975.94 | 0.9% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24772 (Nested Loop) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** c53c4396 (Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)])
- **Consumes:** Nodes 24768, 24769, 24773, 24774
- **Input Features:**
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
  - NestedLoop_np=0
  - NestedLoop_nt=5717
  - NestedLoop_nt1=5717
  - NestedLoop_nt2=1
  - NestedLoop_parallel_workers=0
  - NestedLoop_plan_width=27
  - NestedLoop_reltuples=0.0000
  - NestedLoop_sel=1.0000
  - NestedLoop_startup_cost=0.4300
  - NestedLoop_total_cost=147120.7800
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=5717
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=15
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0010
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=139605.4700
- **Output:** st=10.44, rt=975.94

### Step 2: Node 24771 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5717
  - nt1=5717
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=975.9450
  - rt2=0.0000
  - sel=1.0000
  - st1=10.4376
  - st2=0.0000
  - startup_cost=147477.5500
  - total_cost=147491.8400
- **Output:** st=1049.80, rt=1050.78

### Step 3: Node 24770 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5717
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1050.7846
  - rt2=0.0000
  - sel=0.0012
  - st1=1049.8033
  - st2=0.0000
  - startup_cost=147477.5500
  - total_cost=147591.9600
- **Output:** st=925.98, rt=940.64

### Step 4: Node 24768 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 24769, 24772, 24773, 24774
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=7
  - Aggregate_nt1=35
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=27
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=148477.6300
  - Aggregate_total_cost=148596.5900
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=35
  - GatherMerge_Outer_nt1=7
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=5
  - GatherMerge_Outer_plan_width=27
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=5.0000
  - GatherMerge_Outer_startup_cost=148477.6300
  - GatherMerge_Outer_total_cost=148596.2500
- **Output:** st=1022.92, rt=1027.05
