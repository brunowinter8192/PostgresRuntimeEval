# Online Prediction Report

**Test Query:** Q12_117_seed_951667596
**Timestamp:** 2025-12-13 03:33:26

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.13%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 2.8144 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 2.1302 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 1.5375 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 2.8144 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 1.5375 |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 24 | 2.1961 |
| fbf3ebe8 | Aggregate -> Sort -> Nested Loop (Outer)... | 3 | 24 | 0.9714 |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 24 | 2.1961 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 1 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
## Query Tree

```
Node 24446 (Aggregate) - ROOT
  Node 24447 (Gather Merge)
    Node 24448 (Aggregate)
      Node 24449 (Sort)
        Node 24450 (Nested Loop)
          Node 24451 (Seq Scan) - LEAF
          Node 24452 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.05%
- Improvement: 0.09%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24446 | Aggregate | 984.71 | 954.69 | 3.0% | operator |
| 24447 | Gather Merge | 984.69 | 1060.96 | 7.7% | operator |
| 24448 | Aggregate | 965.69 | 941.96 | 2.5% | operator |
| 24449 | Sort | 965.07 | 1058.11 | 9.6% | operator |
| 24450 | Nested Loop | 964.09 | 1101.32 | 14.2% | operator |
| 24451 | Seq Scan | 827.64 | 750.46 | 9.3% | operator |
| 24452 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24451 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5800
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

### Step 2: Node 24452 (Index Scan) - LEAF

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

### Step 3: Node 24450 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5800
  - nt1=5800
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
  - total_cost=147195.3000
- **Output:** st=21.29, rt=1101.32

### Step 4: Node 24449 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5800
  - nt1=5800
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3155
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2854
  - st2=0.0000
  - startup_cost=147557.8600
  - total_cost=147572.3600
- **Output:** st=1057.11, rt=1058.11

### Step 5: Node 24448 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5800
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1076
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1150
  - st2=0.0000
  - startup_cost=147557.8600
  - total_cost=147673.9300
- **Output:** st=927.03, rt=941.96

### Step 6: Node 24447 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9597
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0278
  - st2=0.0000
  - startup_cost=148557.9300
  - total_cost=148678.2200
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 24446 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9609
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9885
  - st2=0.0000
  - startup_cost=148557.9300
  - total_cost=148678.5500
- **Output:** st=951.95, rt=954.69
