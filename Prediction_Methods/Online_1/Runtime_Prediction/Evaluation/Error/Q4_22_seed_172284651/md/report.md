# Online Prediction Report

**Test Query:** Q4_22_seed_172284651
**Timestamp:** 2026-01-01 20:23:30

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.26%

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
| 2 | 2724c080 | 7.7852 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 3 | 1691f6f0 | 7.2969 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 4 | 29ee00db | 4.4636 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 5 | 715d5c92 | 4.3242 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 6 | f8231c4d | 3.4058 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 7 | 1393818c | 1.1761 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 8 | 6e6e9493 | 1.1761 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 9 | 3b447875 | 1.1741 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 10 | 260efc4f | 1.0354 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 11 | 80bd802d | 1.0354 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 12 | ab77776a | 0.3988 | N/A | SKIPPED_LOW_ERROR | 17.81% |
| 13 | f86f2b1b | 0.3988 | N/A | SKIPPED_LOW_ERROR | 17.81% |
## Query Tree

```
Node 6299 (Aggregate) - ROOT
  Node 6300 (Gather Merge)
    Node 6301 (Sort) [PATTERN: 1d35fb97]
      Node 6302 (Aggregate) [consumed]
        Node 6303 (Nested Loop)
          Node 6304 (Seq Scan) - LEAF
          Node 6305 (Index Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 6301 | 6302 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 2.84%
- Improvement: 0.42%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 6299 | Aggregate | 1052.31 | 1022.46 | 2.8% | operator |
| 6300 | Gather Merge | 1052.30 | 1112.78 | 5.7% | operator |
| 6301 | Sort | 1047.54 | 1055.43 | 0.8% | pattern |
| 6303 | Nested Loop | 1045.66 | 1106.40 | 5.8% | operator |
| 6304 | Seq Scan | 165.01 | 157.03 | 4.8% | operator |
| 6305 | Index Scan | 0.06 | 0.38 | 513.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 6304 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=17869
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0119
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=33394.0600
- **Output:** st=0.23, rt=157.03

### Step 2: Node 6305 (Index Scan) - LEAF

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
  - total_cost=2.3300
- **Output:** st=0.06, rt=0.38

### Step 3: Node 6303 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=14572
  - nt1=17869
  - nt2=2
  - parallel_workers=0
  - plan_width=16
  - reltuples=0.0000
  - rt1=157.0309
  - rt2=0.3804
  - sel=0.4077
  - st1=0.2257
  - st2=0.0614
  - startup_cost=0.4300
  - total_cost=65507.8400
- **Output:** st=31.34, rt=1106.40

### Step 4: Node 6301 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 6302
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=5
  - Aggregate_Outer_nt1=14572
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=24
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0003
  - Aggregate_Outer_startup_cost=65580.7000
  - Aggregate_Outer_total_cost=65580.7500
  - Sort_np=0
  - Sort_nt=5
  - Sort_nt1=5
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=24
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=65580.8100
  - Sort_total_cost=65580.8200
- **Output:** st=1054.27, rt=1055.43

### Step 5: Node 6300 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15
  - nt1=5
  - nt2=0
  - parallel_workers=3
  - plan_width=24
  - reltuples=0.0000
  - rt1=1055.4296
  - rt2=0.0000
  - sel=3.0000
  - st1=1054.2665
  - st2=0.0000
  - startup_cost=66580.8500
  - total_cost=66582.6200
- **Output:** st=1109.53, rt=1112.78

### Step 6: Node 6299 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5
  - nt1=15
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=1112.7754
  - rt2=0.0000
  - sel=0.3333
  - st1=1109.5318
  - st2=0.0000
  - startup_cost=66580.8500
  - total_cost=66582.7500
- **Output:** st=1025.27, rt=1022.46
