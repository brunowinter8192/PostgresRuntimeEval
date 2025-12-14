# Online Prediction Report

**Test Query:** Q12_83_seed_672730542
**Timestamp:** 2025-12-13 02:26:34

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.44%

## Phase C: Patterns in Query

- Total Patterns: 15

| Hash | Pattern String | Length | Occurrences | Error Score |
|------|----------------|--------|-------------|-------------|
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 19.6008 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 96 | 141.6847 |
| 46f37744 | Gather Merge -> Aggregate (Outer) | 2 | 48 | 2.8144 |
| 3754655c | Aggregate -> Sort (Outer) | 2 | 48 | 2.1302 |
| 263b40d6 | Sort -> Nested Loop (Outer) | 2 | 24 | 2.1961 |
| 8a8c43c6 | Aggregate -> Gather Merge -> Aggregate (... | 3 | 48 | 1.5375 |
| e6c1e0d8 | Gather Merge -> Aggregate -> Sort (Outer... | 3 | 48 | 2.8144 |
| fbf3ebe8 | Aggregate -> Sort -> Nested Loop (Outer)... | 3 | 24 | 0.9714 |
| 5b623fa1 | Sort -> Nested Loop -> [Seq Scan (Outer)... | 3 | 24 | 2.1961 |
| 460af52c | Aggregate -> Gather Merge -> Aggregate -... | 4 | 48 | 1.5375 |

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | MRE After |
|------|---------|-------------|-------|--------|-----------|
| 0 | 2724c080 | 19.6008 | 0.0222% | REJECTED | 17.92% |
| 1 | c53c4396 | 141.6847 | -0.0000% | REJECTED | 17.92% |
## Query Tree

```
Node 25237 (Aggregate) - ROOT
  Node 25238 (Gather Merge)
    Node 25239 (Aggregate)
      Node 25240 (Sort)
        Node 25241 (Nested Loop)
          Node 25242 (Seq Scan) - LEAF
          Node 25243 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.35%
- Improvement: 0.09%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25237 | Aggregate | 987.84 | 954.70 | 3.4% | operator |
| 25238 | Gather Merge | 987.82 | 1060.96 | 7.4% | operator |
| 25239 | Aggregate | 969.36 | 941.97 | 2.8% | operator |
| 25240 | Sort | 968.74 | 1058.09 | 9.2% | operator |
| 25241 | Nested Loop | 967.79 | 1101.29 | 13.8% | operator |
| 25242 | Seq Scan | 830.63 | 750.45 | 9.7% | operator |
| 25243 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25242 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5730
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
- **Output:** st=3.98, rt=750.45

### Step 2: Node 25243 (Index Scan) - LEAF

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

### Step 3: Node 25241 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5730
  - nt1=5730
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4547
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9753
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147132.5500
- **Output:** st=21.27, rt=1101.29

### Step 4: Node 25240 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5730
  - nt1=5730
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.2907
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2716
  - st2=0.0000
  - startup_cost=147490.2300
  - total_cost=147504.5500
- **Output:** st=1057.10, rt=1058.09

### Step 5: Node 25239 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5730
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.0906
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.0982
  - st2=0.0000
  - startup_cost=147490.2300
  - total_cost=147604.9000
- **Output:** st=927.05, rt=941.97

### Step 6: Node 25238 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9675
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0492
  - st2=0.0000
  - startup_cost=148490.3000
  - total_cost=148609.1900
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 25237 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9629
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9908
  - st2=0.0000
  - startup_cost=148490.3000
  - total_cost=148609.5200
- **Output:** st=951.98, rt=954.70
