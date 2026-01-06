# Online Prediction Report

**Test Query:** Q12_39_seed_311753178
**Timestamp:** 2026-01-01 20:01:51

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.79%

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
| 2 | 263b40d6 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 3 | 5b623fa1 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 4 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 5 | 460af52c | 1.5019 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 6 | 8a8c43c6 | 1.5019 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 7 | a0631e25 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 8 | fbf3ebe8 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 9 | b692b3d9 | 0.9589 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 10 | f9c97829 | 0.9589 | N/A | SKIPPED_LOW_ERROR | 17.90% |
## Query Tree

```
Node 24894 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 24895 (Gather Merge) [consumed]
    Node 24896 (Aggregate)
      Node 24897 (Sort)
        Node 24898 (Nested Loop)
          Node 24899 (Seq Scan) - LEAF
          Node 24900 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge (Out | 2724c080 | 24894 | 24895 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.59%
- Improvement: 0.20%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24894 | Aggregate | 991.43 | 1027.05 | 3.6% | pattern |
| 24896 | Aggregate | 972.30 | 941.96 | 3.1% | operator |
| 24897 | Sort | 971.63 | 1058.11 | 8.9% | operator |
| 24898 | Nested Loop | 970.49 | 1101.32 | 13.5% | operator |
| 24899 | Seq Scan | 838.89 | 750.46 | 10.5% | operator |
| 24900 | Index Scan | 0.03 | -0.02 | 165.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24899 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5801
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=15
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0010
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=139605.4700
- **Output:** st=3.98, rt=750.46

### Step 2: Node 24900 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=1.3100
- **Output:** st=0.03, rt=-0.02

### Step 3: Node 24898 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5801
  - nt1=5801
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4579
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147196.1900
- **Output:** st=21.29, rt=1101.32

### Step 4: Node 24897 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5801
  - nt1=5801
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3158
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2856
  - st2=0.0000
  - startup_cost=147558.8100
  - total_cost=147573.3100
- **Output:** st=1057.12, rt=1058.11

### Step 5: Node 24896 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5801
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1078
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1152
  - st2=0.0000
  - startup_cost=147558.8100
  - total_cost=147674.9000
- **Output:** st=927.03, rt=941.96

### Step 6: Node 24894 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 24895
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=7
  - Aggregate_nt1=35
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=27
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.2000
  - Aggregate_startup_cost=148558.8900
  - Aggregate_total_cost=148679.5300
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=35
  - GatherMerge_Outer_nt1=7
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=5
  - GatherMerge_Outer_plan_width=27
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=5.0000
  - GatherMerge_Outer_startup_cost=148558.8900
  - GatherMerge_Outer_total_cost=148679.1900
- **Output:** st=1022.92, rt=1027.05
