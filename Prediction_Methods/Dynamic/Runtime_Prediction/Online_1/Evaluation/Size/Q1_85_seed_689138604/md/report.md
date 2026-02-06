# Online Prediction Report

**Test Query:** Q1_85_seed_689138604
**Timestamp:** 2026-01-18 16:05:25

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18851 | Operator + Pattern Training |
| Training_Test | 4718 | Pattern Selection Eval |
| Training | 23569 | Final Model Training |
| Test | 750 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 23.05%

## Phase C: Patterns in Query

- Total Patterns: 10

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 12.1% | 25.4704 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 10.9% | 19.6991 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 90 | 4.7% | 4.2081 |
| 184f44de | Aggregate -> Seq Scan (Outer) | 2 | 30 | 11.0% | 3.2970 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 90 | 2.4% | 2.1972 |
| 715d5c92 | Gather Merge -> Sort -> Aggregate (Outer... | 3 | 30 | 5.0% | 1.5106 |
| f8231c4d | Aggregate -> Gather Merge -> Sort -> Agg... | 4 | 30 | 3.3% | 0.9962 |
| 3dfa6025 | Aggregate -> Gather Merge -> Sort -> Agg... | 5 | 0 | - | - |
| 52c5ec81 | Gather Merge -> Sort -> Aggregate -> Seq... | 4 | 0 | - | - |
| dc1b1da7 | Sort -> Aggregate -> Seq Scan (Outer) (O... | 3 | 0 | - | - |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 25.4704 | 0.1652% | ACCEPTED | 17.26% |
| 1 | 2724c080 | 19.6991 | -0.2238% | REJECTED | 17.26% |
| 2 | 1691f6f0 | 4.2081 | N/A | SKIPPED_LOW_ERROR | 17.26% |
| 3 | 184f44de | 3.2970 | 0.0045% | ACCEPTED | 17.25% |
| 4 | 29ee00db | 2.1972 | N/A | SKIPPED_LOW_ERROR | 17.25% |
| 5 | 715d5c92 | 1.5106 | N/A | SKIPPED_LOW_ERROR | 17.25% |
| 6 | f8231c4d | 0.9962 | N/A | SKIPPED_LOW_ERROR | 17.25% |
## Query Tree

```
Node 666 (Aggregate) - ROOT
  Node 667 (Gather Merge)
    Node 668 (Sort) [PATTERN: 1d35fb97]
      Node 669 (Aggregate) [consumed]
        Node 670 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 668 | 669 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 25.22%
- Improvement: -2.17%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 666 | Aggregate | 954.99 | 1195.83 | 25.2% | operator |
| 667 | Gather Merge | 954.94 | 1165.89 | 22.1% | operator |
| 668 | Sort | 937.97 | 1200.30 | 28.0% | pattern |
| 670 | Seq Scan | 527.19 | 681.04 | 29.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 670 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1177789
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1963
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=0.85, rt=681.04

### Step 2: Node 668 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 669
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=6
  - Aggregate_Outer_nt1=1177789
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=236
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=168825.6500
  - Aggregate_Outer_total_cost=168825.7900
  - Sort_np=0
  - Sort_nt=6
  - Sort_nt1=6
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=236
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=168825.8700
  - Sort_total_cost=168825.8800
- **Output:** st=1196.20, rt=1200.30

### Step 3: Node 667 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1200.2993
  - rt2=0.0000
  - sel=5.0000
  - st1=1196.2029
  - st2=0.0000
  - startup_cost=169825.9400
  - total_cost=169829.5700
- **Output:** st=1161.77, rt=1165.89

### Step 4: Node 666 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1165.8900
  - rt2=0.0000
  - sel=0.2000
  - st1=1161.7667
  - st2=0.0000
  - startup_cost=169825.9400
  - total_cost=169830.7100
- **Output:** st=1149.89, rt=1195.83
