# Online Prediction Report

**Test Query:** Q12_33_seed_262528992
**Timestamp:** 2025-12-13 01:08:45

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.65%

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
Node 24852 (Aggregate) - ROOT
  Node 24853 (Gather Merge)
    Node 24854 (Aggregate)
      Node 24855 (Sort)
        Node 24856 (Nested Loop)
          Node 24857 (Seq Scan) - LEAF
          Node 24858 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.56%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24852 | Aggregate | 989.96 | 954.70 | 3.6% | operator |
| 24853 | Gather Merge | 989.95 | 1060.96 | 7.2% | operator |
| 24854 | Aggregate | 969.71 | 941.97 | 2.9% | operator |
| 24855 | Sort | 969.10 | 1058.09 | 9.2% | operator |
| 24856 | Nested Loop | 968.16 | 1101.29 | 13.8% | operator |
| 24857 | Seq Scan | 825.61 | 750.45 | 9.1% | operator |
| 24858 | Index Scan | 0.03 | -0.02 | 161.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24857 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5735
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

### Step 2: Node 24858 (Index Scan) - LEAF

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

### Step 3: Node 24856 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5735
  - nt1=5735
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4549
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9753
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147137.0200
- **Output:** st=21.27, rt=1101.29

### Step 4: Node 24855 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5735
  - nt1=5735
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.2924
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2726
  - st2=0.0000
  - startup_cost=147495.0500
  - total_cost=147509.3800
- **Output:** st=1057.10, rt=1058.09

### Step 5: Node 24854 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5735
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.0919
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.0994
  - st2=0.0000
  - startup_cost=147495.0500
  - total_cost=147609.8200
- **Output:** st=927.05, rt=941.97

### Step 6: Node 24853 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9669
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0476
  - st2=0.0000
  - startup_cost=148495.1200
  - total_cost=148614.1100
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 24852 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9628
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9906
  - st2=0.0000
  - startup_cost=148495.1200
  - total_cost=148614.4400
- **Output:** st=951.97, rt=954.70
