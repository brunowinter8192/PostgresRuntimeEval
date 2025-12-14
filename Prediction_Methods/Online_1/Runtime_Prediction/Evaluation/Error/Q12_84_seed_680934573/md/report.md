# Online Prediction Report

**Test Query:** Q12_84_seed_680934573
**Timestamp:** 2025-12-13 01:09:12

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.31%

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
Node 25244 (Aggregate) - ROOT
  Node 25245 (Gather Merge)
    Node 25246 (Aggregate)
      Node 25247 (Sort)
        Node 25248 (Nested Loop)
          Node 25249 (Seq Scan) - LEAF
          Node 25250 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 4.23%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25244 | Aggregate | 996.84 | 954.69 | 4.2% | operator |
| 25245 | Gather Merge | 996.83 | 1060.96 | 6.4% | operator |
| 25246 | Aggregate | 975.14 | 941.96 | 3.4% | operator |
| 25247 | Sort | 974.55 | 1058.11 | 8.6% | operator |
| 25248 | Nested Loop | 973.53 | 1101.32 | 13.1% | operator |
| 25249 | Seq Scan | 838.79 | 750.46 | 10.5% | operator |
| 25250 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25249 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5801
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

### Step 2: Node 25250 (Index Scan) - LEAF

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

### Step 3: Node 25248 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5801
  - nt1=5801
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
  - total_cost=147196.5300
- **Output:** st=21.29, rt=1101.32

### Step 4: Node 25247 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5801
  - nt1=5801
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3158
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2856
  - st2=0.0000
  - startup_cost=147559.1600
  - total_cost=147573.6600
- **Output:** st=1057.12, rt=1058.11

### Step 5: Node 25246 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5801
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1079
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1153
  - st2=0.0000
  - startup_cost=147559.1600
  - total_cost=147675.2500
- **Output:** st=927.03, rt=941.96

### Step 6: Node 25245 (Gather Merge)

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
  - st1=927.0274
  - st2=0.0000
  - startup_cost=148559.2300
  - total_cost=148679.5400
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 25244 (Aggregate) - ROOT

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
  - startup_cost=148559.2300
  - total_cost=148679.8700
- **Output:** st=951.95, rt=954.69
