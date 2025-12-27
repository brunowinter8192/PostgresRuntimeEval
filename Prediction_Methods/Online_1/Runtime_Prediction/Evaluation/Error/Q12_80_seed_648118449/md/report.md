# Online Prediction Report

**Test Query:** Q12_80_seed_648118449
**Timestamp:** 2025-12-22 02:36:26

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.96%

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
Node 25216 (Aggregate) - ROOT
  Node 25217 (Gather Merge)
    Node 25218 (Aggregate)
      Node 25219 (Sort)
        Node 25220 (Nested Loop)
          Node 25221 (Seq Scan) - LEAF
          Node 25222 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 3.88%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25216 | Aggregate | 993.21 | 954.70 | 3.9% | operator |
| 25217 | Gather Merge | 993.20 | 1060.96 | 6.8% | operator |
| 25218 | Aggregate | 973.75 | 941.96 | 3.3% | operator |
| 25219 | Sort | 973.15 | 1058.10 | 8.7% | operator |
| 25220 | Nested Loop | 972.19 | 1101.31 | 13.3% | operator |
| 25221 | Seq Scan | 843.44 | 750.46 | 11.0% | operator |
| 25222 | Index Scan | 0.02 | -0.02 | 168.6% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25221 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5778
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

### Step 2: Node 25222 (Index Scan) - LEAF

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

### Step 3: Node 25220 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5778
  - nt1=5778
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4569
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147175.9100
- **Output:** st=21.28, rt=1101.31

### Step 4: Node 25219 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5778
  - nt1=5778
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3076
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2810
  - st2=0.0000
  - startup_cost=147536.9300
  - total_cost=147551.3800
- **Output:** st=1057.11, rt=1058.10

### Step 5: Node 25218 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5778
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1023
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1098
  - st2=0.0000
  - startup_cost=147536.9300
  - total_cost=147652.5600
- **Output:** st=927.03, rt=941.96

### Step 6: Node 25217 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9621
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0344
  - st2=0.0000
  - startup_cost=148537.0100
  - total_cost=148656.8500
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 25216 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9615
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9892
  - st2=0.0000
  - startup_cost=148537.0100
  - total_cost=148657.1900
- **Output:** st=951.96, rt=954.70
