# Online Prediction Report

**Test Query:** Q1_138_seed_1123952247
**Timestamp:** 2026-01-18 15:59:50

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18851 | Operator + Pattern Training |
| Training_Test | 4718 | Pattern Selection Eval |
| Training | 23569 | Final Model Training |
| Test | 750 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 23.73%

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
Node 206 (Aggregate) - ROOT
  Node 207 (Gather Merge)
    Node 208 (Sort) [PATTERN: 1d35fb97]
      Node 209 (Aggregate) [consumed]
        Node 210 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Sort -> Aggregate (Outer) | 1d35fb97 | 208 | 209 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 25.91%
- Improvement: -2.18%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 206 | Aggregate | 949.77 | 1195.88 | 25.9% | operator |
| 207 | Gather Merge | 949.70 | 1165.90 | 22.8% | operator |
| 208 | Sort | 927.97 | 1200.49 | 29.4% | pattern |
| 210 | Seq Scan | 522.28 | 680.30 | 30.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 210 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1181531
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1969
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=0.85, rt=680.30

### Step 2: Node 208 (Sort) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 1d35fb97 (Sort -> Aggregate (Outer))
- **Consumes:** Nodes 209
- **Input Features:**
  - Aggregate_Outer_np=0
  - Aggregate_Outer_nt=6
  - Aggregate_Outer_nt1=1181531
  - Aggregate_Outer_nt2=0
  - Aggregate_Outer_parallel_workers=0
  - Aggregate_Outer_plan_width=236
  - Aggregate_Outer_reltuples=0.0000
  - Aggregate_Outer_sel=0.0000
  - Aggregate_Outer_startup_cost=168956.6200
  - Aggregate_Outer_total_cost=168956.7600
  - Sort_np=0
  - Sort_nt=6
  - Sort_nt1=6
  - Sort_nt2=0
  - Sort_parallel_workers=0
  - Sort_plan_width=236
  - Sort_reltuples=0.0000
  - Sort_sel=1.0000
  - Sort_startup_cost=168956.8400
  - Sort_total_cost=168956.8500
- **Output:** st=1196.40, rt=1200.49

### Step 3: Node 207 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1200.4933
  - rt2=0.0000
  - sel=5.0000
  - st1=1196.3975
  - st2=0.0000
  - startup_cost=169956.9100
  - total_cost=169960.5400
- **Output:** st=1161.78, rt=1165.90

### Step 4: Node 206 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1165.9048
  - rt2=0.0000
  - sel=0.2000
  - st1=1161.7811
  - st2=0.0000
  - startup_cost=169956.9100
  - total_cost=169961.6800
- **Output:** st=1149.90, rt=1195.88
