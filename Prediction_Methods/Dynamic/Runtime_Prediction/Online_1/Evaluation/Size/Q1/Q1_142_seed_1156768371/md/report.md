# Online Prediction Report

**Test Query:** Q1_142_seed_1156768371
**Timestamp:** 2025-12-21 14:28:58

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 18851 | Operator + Pattern Training |
| Training_Test | 4718 | Pattern Selection Eval |
| Training | 23569 | Final Model Training |
| Test | 750 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 17.58%

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

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 1d35fb97 | 25.4704 | 0.1652% | REJECTED | 17.42% |
| 1 | 2724c080 | 19.6991 | -0.2283% | REJECTED | 17.42% |
| 2 | 1691f6f0 | 4.2081 | N/A | SKIPPED_LOW_ERROR | 17.42% |
| 3 | 184f44de | 3.2970 | 0.0045% | REJECTED | 17.42% |
| 4 | 29ee00db | 2.1972 | N/A | SKIPPED_LOW_ERROR | 17.42% |
| 5 | 715d5c92 | 1.5106 | N/A | SKIPPED_LOW_ERROR | 17.42% |
| 6 | f8231c4d | 0.9962 | N/A | SKIPPED_LOW_ERROR | 17.42% |
## Query Tree

```
Node 231 (Aggregate) - ROOT
  Node 232 (Gather Merge)
    Node 233 (Sort)
      Node 234 (Aggregate)
        Node 235 (Seq Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 19.65%
- Improvement: -2.07%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 231 | Aggregate | 999.33 | 1195.71 | 19.7% | operator |
| 232 | Gather Merge | 999.25 | 1165.55 | 16.6% | operator |
| 233 | Sort | 979.95 | 1181.93 | 20.6% | operator |
| 234 | Aggregate | 979.91 | 1112.52 | 13.5% | operator |
| 235 | Seq Scan | 571.17 | 682.20 | 19.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 235 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1171832
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=25
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.1953
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=127603.0400
- **Output:** st=0.85, rt=682.20

### Step 2: Node 234 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=1171832
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=682.2009
  - rt2=0.0000
  - sel=0.0000
  - st1=0.8467
  - st2=0.0000
  - startup_cost=168617.1600
  - total_cost=168617.2900
- **Output:** st=1037.35, rt=1112.52

### Step 3: Node 233 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=6
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1112.5189
  - rt2=0.0000
  - sel=1.0000
  - st1=1037.3514
  - st2=0.0000
  - startup_cost=168617.3700
  - total_cost=168617.3900
- **Output:** st=1180.86, rt=1181.93

### Step 4: Node 232 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=30
  - nt1=6
  - nt2=0
  - parallel_workers=5
  - plan_width=236
  - reltuples=0.0000
  - rt1=1181.9340
  - rt2=0.0000
  - sel=5.0000
  - st1=1180.8645
  - st2=0.0000
  - startup_cost=169617.4500
  - total_cost=169621.0800
- **Output:** st=1161.43, rt=1165.55

### Step 5: Node 231 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=6
  - nt1=30
  - nt2=0
  - parallel_workers=0
  - plan_width=236
  - reltuples=0.0000
  - rt1=1165.5536
  - rt2=0.0000
  - sel=0.2000
  - st1=1161.4300
  - st2=0.0000
  - startup_cost=169617.4500
  - total_cost=169622.2200
- **Output:** st=1149.83, rt=1195.71
