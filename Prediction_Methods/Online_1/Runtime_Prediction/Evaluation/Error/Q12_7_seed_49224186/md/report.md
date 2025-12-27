# Online Prediction Report

**Test Query:** Q12_7_seed_49224186
**Timestamp:** 2025-12-22 02:36:04

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
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 2 | 46f37744 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 3 | e6c1e0d8 | 2.8144 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 4 | 263b40d6 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 5 | 5b623fa1 | 2.1961 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 6 | 3754655c | 2.1302 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 7 | 3a2624e2 | 1.6208 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 8 | 898abd49 | 1.6208 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 9 | 460af52c | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 10 | 8a8c43c6 | 1.5375 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 11 | b692b3d9 | 1.0973 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 12 | f9c97829 | 1.0973 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 13 | a0631e25 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.92% |
| 14 | fbf3ebe8 | 0.9714 | N/A | SKIPPED_LOW_ERROR | 17.92% |
## Query Tree

```
Node 25209 (Aggregate) - ROOT
  Node 25210 (Gather Merge)
    Node 25211 (Aggregate)
      Node 25212 (Sort)
        Node 25213 (Nested Loop)
          Node 25214 (Seq Scan) - LEAF
          Node 25215 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.08%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25209 | Aggregate | 995.28 | 954.69 | 4.1% | operator |
| 25210 | Gather Merge | 995.26 | 1060.96 | 6.6% | operator |
| 25211 | Aggregate | 975.91 | 941.96 | 3.5% | operator |
| 25212 | Sort | 975.24 | 1058.11 | 8.5% | operator |
| 25213 | Nested Loop | 974.25 | 1101.32 | 13.0% | operator |
| 25214 | Seq Scan | 839.70 | 750.46 | 10.6% | operator |
| 25215 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25214 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5802
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

### Step 2: Node 25215 (Index Scan) - LEAF

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

### Step 3: Node 25213 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5802
  - nt1=5802
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4580
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147197.0700
- **Output:** st=21.29, rt=1101.32

### Step 4: Node 25212 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5802
  - nt1=5802
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3162
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2858
  - st2=0.0000
  - startup_cost=147559.7600
  - total_cost=147574.2700
- **Output:** st=1057.12, rt=1058.11

### Step 5: Node 25211 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5802
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1081
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1155
  - st2=0.0000
  - startup_cost=147559.7600
  - total_cost=147675.8700
- **Output:** st=927.03, rt=941.96

### Step 6: Node 25210 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9595
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0272
  - st2=0.0000
  - startup_cost=148559.8400
  - total_cost=148680.1700
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 25209 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9608
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9884
  - st2=0.0000
  - startup_cost=148559.8400
  - total_cost=148680.5000
- **Output:** st=951.95, rt=954.69
