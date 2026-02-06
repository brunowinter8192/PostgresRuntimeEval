# Online Prediction Report

**Test Query:** Q12_7_seed_49224186
**Timestamp:** 2026-01-11 16:25:21

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.16%

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
Node 25209 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 25210 (Gather Merge) [consumed]
    Node 25211 (Aggregate)
      Node 25212 (Sort)
        Node 25213 (Nested Loop) [PATTERN: c53c4396]
          Node 25214 (Seq Scan) [consumed] - LEAF
          Node 25215 (Index Scan) [consumed] - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge (Out | 2724c080 | 25209 | 25210, 25213, 25214, 25215 |
| Nested Loop -> [Seq Scan (Oute | c53c4396 | 25213 | 25209, 25210, 25214, 25215 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.19%
- Improvement: 0.97%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25209 | Aggregate | 995.28 | 1027.05 | 3.2% | pattern |
| 25211 | Aggregate | 975.91 | 940.64 | 3.6% | operator |
| 25212 | Sort | 975.24 | 1050.81 | 7.7% | operator |
| 25213 | Nested Loop | 974.25 | 976.10 | 0.2% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25213 (Nested Loop) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** c53c4396 (Nested Loop -> [Seq Scan (Outer), Index Scan (Inner)])
- **Consumes:** Nodes 25209, 25210, 25214, 25215
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
  - NestedLoop_nt=5802
  - NestedLoop_nt1=5802
  - NestedLoop_nt2=1
  - NestedLoop_parallel_workers=0
  - NestedLoop_plan_width=27
  - NestedLoop_reltuples=0.0000
  - NestedLoop_sel=1.0000
  - NestedLoop_startup_cost=0.4300
  - NestedLoop_total_cost=147197.0700
  - SeqScan_Outer_np=112600
  - SeqScan_Outer_nt=5802
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=15
  - SeqScan_Outer_reltuples=6001215.0000
  - SeqScan_Outer_sel=0.0010
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=139605.4700
- **Output:** st=10.43, rt=976.10

### Step 2: Node 25212 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5802
  - nt1=5802
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=976.0966
  - rt2=0.0000
  - sel=1.0000
  - st1=10.4316
  - st2=0.0000
  - startup_cost=147559.7600
  - total_cost=147574.2700
- **Output:** st=1049.83, rt=1050.81

### Step 3: Node 25211 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5802
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1050.8112
  - rt2=0.0000
  - sel=0.0012
  - st1=1049.8297
  - st2=0.0000
  - startup_cost=147559.7600
  - total_cost=147675.8700
- **Output:** st=925.95, rt=940.64

### Step 4: Node 25209 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 25210, 25213, 25214, 25215
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=7
  - Aggregate_nt1=35
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=27
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=148559.8400
  - Aggregate_total_cost=148680.5000
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=35
  - GatherMerge_Outer_nt1=7
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=5
  - GatherMerge_Outer_plan_width=27
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=5.0000
  - GatherMerge_Outer_startup_cost=148559.8400
  - GatherMerge_Outer_total_cost=148680.1700
- **Output:** st=1022.92, rt=1027.05
