# Online Prediction Report

**Test Query:** Q12_127_seed_1033707906
**Timestamp:** 2025-12-13 01:07:08

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.63%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 2.8144 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 2.8144 |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 24 | 2.1961 |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 24 | 2.1961 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 2.1302 |
| 898abd49 | Gather Merge -> Aggregate -> Sort -> Nes... | 4 | 24 | 1.6208 |
| 3a2624e2 | Gather Merge -> Aggregate -> Sort -> Nes... | 5 | 24 | 1.6208 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 1.5375 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
| 1 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
## Query Tree

```
Node 24523 (Aggregate) - ROOT
  Node 24524 (Gather Merge)
    Node 24525 (Aggregate)
      Node 24526 (Sort)
        Node 24527 (Nested Loop)
          Node 24528 (Seq Scan) - LEAF
          Node 24529 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 5.54%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24523 | Aggregate | 1010.74 | 954.70 | 5.5% | operator |
| 24524 | Gather Merge | 1010.72 | 1060.96 | 5.0% | operator |
| 24525 | Aggregate | 990.53 | 941.96 | 4.9% | operator |
| 24526 | Sort | 989.90 | 1058.10 | 6.9% | operator |
| 24527 | Nested Loop | 988.91 | 1101.31 | 11.4% | operator |
| 24528 | Seq Scan | 848.98 | 750.46 | 11.6% | operator |
| 24529 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24528 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5780
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

### Step 2: Node 24529 (Index Scan) - LEAF

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

### Step 3: Node 24527 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5780
  - nt1=5780
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4570
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147177.5500
- **Output:** st=21.28, rt=1101.31

### Step 4: Node 24526 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5780
  - nt1=5780
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3084
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2814
  - st2=0.0000
  - startup_cost=147538.7100
  - total_cost=147553.1600
- **Output:** st=1057.11, rt=1058.10

### Step 5: Node 24525 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5780
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1028
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1102
  - st2=0.0000
  - startup_cost=147538.7100
  - total_cost=147654.3800
- **Output:** st=927.03, rt=941.96

### Step 6: Node 24524 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9619
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0338
  - st2=0.0000
  - startup_cost=148538.7900
  - total_cost=148658.6800
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 24523 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9614
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9891
  - st2=0.0000
  - startup_cost=148538.7900
  - total_cost=148659.0100
- **Output:** st=951.96, rt=954.70
