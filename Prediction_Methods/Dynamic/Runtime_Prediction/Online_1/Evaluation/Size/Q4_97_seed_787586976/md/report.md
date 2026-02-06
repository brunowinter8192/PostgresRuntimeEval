# Online Prediction Report

**Test Query:** Q4_97_seed_787586976
**Timestamp:** 2026-01-18 16:41:45

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18611 | Operator + Pattern Training |
| Training_Test | 4658 | Pattern Selection Eval |
| Training | 23269 | Final Model Training |
| Test | 1050 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.57%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 15.3% | 32.1945 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 12.7% | 22.7741 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 8.6% | 7.7136 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 22 | 2.4% | 0.5216 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 5.0% | 4.4553 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 191.2% | 172.0722 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 30 | 12.8% | 3.8426 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 30 | 10.7% | 3.1984 |
| 260efc4f | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 0 | - | - |
| 80bd802d | Aggregate -> Gather Merge -> Sort -> Agg... | 6 | 0 | - | - |
| 1393818c | Gather Merge -> Sort -> Aggregate -> Nes... | 4 | 0 | - | - |
| 6e6e9493 | Gather Merge -> Sort -> Aggregate -> Nes... | 5 | 0 | - | - |
| f86f2b1b | Sort -> Aggregate -> Nested Loop (Outer)... | 3 | 0 | - | - |
| ab77776a | Sort -> Aggregate -> Nested Loop -> [Seq... | 4 | 0 | - | - |
| 3f1648ef | Aggregate -> Nested Loop -> [Seq Scan (O... | 3 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 32.1945 | 0.0571% | ACCEPTED | 17.71% |
| 1 | 2724c080 | 22.7741 | -0.1115% | REJECTED | 17.71% |
| 2 | 1691f6f0 | 7.7136 | N/A | SKIPPED_LOW_ERROR | 17.71% |
| 3 | 3b447875 | 0.5216 | N/A | SKIPPED_LOW_ERROR | 17.71% |
| 4 | 29ee00db | 4.4553 | N/A | SKIPPED_LOW_ERROR | 17.71% |
| 5 | c53c4396 | 172.0722 | -0.0001% | REJECTED | 17.71% |
| 6 | 715d5c92 | 3.8426 | 0.1356% | ACCEPTED | 17.57% |
| 7 | f8231c4d | 3.1984 | 0.4953% | ACCEPTED | 17.08% |
## Query Tree

```
Node 6873 (Aggregate) [PATTERN: f8231c4d] - ROOT
  Node 6874 (Gather Merge) [consumed]
    Node 6875 (Sort) [consumed]
      Node 6876 (Aggregate) [consumed]
        Node 6877 (Nested Loop)
          Node 6878 (Seq Scan) - LEAF
          Node 6879 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Aggregate -> Gather Merge -> S | f8231c4d | 6873 | 6874, 6875, 6876 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 8.77%
- Improvement: -5.20%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6873 | Aggregate | 1043.70 | 952.19 | 8.8% | pattern |
| 6877 | Nested Loop | 1036.71 | 1255.45 | 21.1% | operator |
| 6878 | Seq Scan | 166.49 | 154.67 | 7.1% | operator |
| 6879 | Index Scan | 0.06 | 11.10 | 18103.9% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6878 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17775
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0118
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.94, rt=154.67

### Step 2: Node 6879 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=2
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=2.3400
- **Output:** st=-0.00, rt=11.10

### Step 3: Node 6877 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14495
  - nt1=17775
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=154.6690
  - rt2=11.1044
  - sel=0.4077
  - st1=0.9399
  - st2=-0.0035
  - startup_cost=0.4300
  - total_cost=65433.4100
- **Output:** st=199.80, rt=1255.45

### Step 4: Node 6873 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** f8231c4d (Aggregate -> Gather Merge -> Sort -> Aggregate (Outer) (Outer) (Outer))
- **Consumes:** Nodes 6874, 6875, 6876
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=14495
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=65505.8900
  - Aggregate_Outer_total_cost=65505.9400
  - Aggregate_np=0
  - Aggregate_nt=5
  - Aggregate_nt1=15
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=24
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=0.3333
  - Aggregate_startup_cost=66506.0300
  - Aggregate_total_cost=66507.9300
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=15
  - GatherMerge_Outer_nt1=5
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=24
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0000
  - GatherMerge_Outer_startup_cost=66506.0300
  - GatherMerge_Outer_total_cost=66507.8100
  - Sort_Outer_np=0
  - Sort_Outer_nt=5
  - Sort_Outer_nt1=5
  - Sort_Outer_nt2=0
  - Sort_Outer_parallel_workers=0
  - Sort_Outer_plan_width=24
  - Sort_Outer_reltuples=0.0000
  - Sort_Outer_sel=1.0000
  - Sort_Outer_startup_cost=65505.9900
  - Sort_Outer_total_cost=65506.0100
- **Output:** st=946.37, rt=952.19
