# Online Prediction Report

**Test Query:** Q12_27_seed_213304806
**Timestamp:** 2025-12-13 03:34:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 3.41%

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
Node 24803 (Aggregate) - ROOT
  Node 24804 (Gather Merge)
    Node 24805 (Aggregate)
      Node 24806 (Sort)
        Node 24807 (Nested Loop)
          Node 24808 (Seq Scan) - LEAF
          Node 24809 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 3.32%
- Improvement: 0.09%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 24803 | Aggregate | 987.51 | 954.69 | 3.3% | operator |
| 24804 | Gather Merge | 987.50 | 1060.96 | 7.4% | operator |
| 24805 | Aggregate | 968.53 | 941.96 | 2.7% | operator |
| 24806 | Sort | 967.89 | 1058.10 | 9.3% | operator |
| 24807 | Nested Loop | 966.88 | 1101.31 | 13.9% | operator |
| 24808 | Seq Scan | 828.35 | 750.46 | 9.4% | operator |
| 24809 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 24808 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5785
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

### Step 2: Node 24809 (Index Scan) - LEAF

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

### Step 3: Node 24807 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5785
  - nt1=5785
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4572
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147181.8100
- **Output:** st=21.28, rt=1101.31

### Step 4: Node 24806 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5785
  - nt1=5785
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3101
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2824
  - st2=0.0000
  - startup_cost=147543.3100
  - total_cost=147557.7800
- **Output:** st=1057.11, rt=1058.10

### Step 5: Node 24805 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5785
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1040
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1114
  - st2=0.0000
  - startup_cost=147543.3100
  - total_cost=147659.0800
- **Output:** st=927.03, rt=941.96

### Step 6: Node 24804 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9614
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0324
  - st2=0.0000
  - startup_cost=148543.3900
  - total_cost=148663.3800
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 24803 (Aggregate) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=35
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1060.9613
  - rt2=0.0000
  - sel=0.2000
  - st1=1055.9890
  - st2=0.0000
  - startup_cost=148543.3900
  - total_cost=148663.7100
- **Output:** st=951.96, rt=954.69
