# Online Prediction Report

**Test Query:** Q12_64_seed_516853953
**Timestamp:** 2025-12-13 03:34:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.20%

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
Node 25090 (Aggregate) - ROOT
  Node 25091 (Gather Merge)
    Node 25092 (Aggregate)
      Node 25093 (Sort)
        Node 25094 (Nested Loop)
          Node 25095 (Seq Scan) - LEAF
          Node 25096 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 4.12%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25090 | Aggregate | 995.69 | 954.69 | 4.1% | operator |
| 25091 | Gather Merge | 995.65 | 1060.96 | 6.6% | operator |
| 25092 | Aggregate | 974.52 | 941.96 | 3.3% | operator |
| 25093 | Sort | 973.91 | 1058.10 | 8.6% | operator |
| 25094 | Nested Loop | 972.75 | 1101.31 | 13.2% | operator |
| 25095 | Seq Scan | 838.29 | 750.46 | 10.5% | operator |
| 25096 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25095 (Seq Scan) - LEAF

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

### Step 2: Node 25096 (Index Scan) - LEAF

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

### Step 3: Node 25094 (Nested Loop)

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
  - total_cost=147181.9800
- **Output:** st=21.28, rt=1101.31

### Step 4: Node 25093 (Sort)

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
  - startup_cost=147543.4900
  - total_cost=147557.9500
- **Output:** st=1057.11, rt=1058.10

### Step 5: Node 25092 (Aggregate)

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
  - startup_cost=147543.4900
  - total_cost=147659.2600
- **Output:** st=927.03, rt=941.96

### Step 6: Node 25091 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9613
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0323
  - st2=0.0000
  - startup_cost=148543.5600
  - total_cost=148663.5500
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 25090 (Aggregate) - ROOT

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
  - startup_cost=148543.5600
  - total_cost=148663.8800
- **Output:** st=951.96, rt=954.69
