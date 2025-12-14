# Online Prediction Report

**Test Query:** Q12_62_seed_500445891
**Timestamp:** 2025-12-13 02:26:07

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 6.38%

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
Node 25076 (Aggregate) - ROOT
  Node 25077 (Gather Merge)
    Node 25078 (Aggregate)
      Node 25079 (Sort)
        Node 25080 (Nested Loop)
          Node 25081 (Seq Scan) - LEAF
          Node 25082 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


## Phase E: Final Prediction

- Final MRE: 6.30%
- Improvement: 0.08%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 25076 | Aggregate | 1018.89 | 954.69 | 6.3% | operator |
| 25077 | Gather Merge | 1018.88 | 1060.96 | 4.1% | operator |
| 25078 | Aggregate | 995.03 | 941.96 | 5.3% | operator |
| 25079 | Sort | 994.42 | 1058.11 | 6.4% | operator |
| 25080 | Nested Loop | 993.43 | 1101.31 | 10.9% | operator |
| 25081 | Seq Scan | 856.68 | 750.46 | 12.4% | operator |
| 25082 | Index Scan | 0.03 | -0.02 | 163.4% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 25081 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5797
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

### Step 2: Node 25082 (Index Scan) - LEAF

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

### Step 3: Node 25080 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5797
  - nt1=5797
  - nt2=1
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=750.4577
  - rt2=-0.0165
  - sel=1.0000
  - st1=3.9755
  - st2=0.0258
  - startup_cost=0.4300
  - total_cost=147192.6500
- **Output:** st=21.28, rt=1101.31

### Step 4: Node 25079 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=5797
  - nt1=5797
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1101.3144
  - rt2=0.0000
  - sel=1.0000
  - st1=21.2848
  - st2=0.0000
  - startup_cost=147554.9900
  - total_cost=147569.4800
- **Output:** st=1057.11, rt=1058.11

### Step 5: Node 25078 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=7
  - nt1=5797
  - nt2=0
  - parallel_workers=0
  - plan_width=27
  - reltuples=0.0000
  - rt1=1058.1069
  - rt2=0.0000
  - sel=0.0012
  - st1=1057.1143
  - st2=0.0000
  - startup_cost=147554.9900
  - total_cost=147671.0000
- **Output:** st=927.03, rt=941.96

### Step 6: Node 25077 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=35
  - nt1=7
  - nt2=0
  - parallel_workers=5
  - plan_width=27
  - reltuples=0.0000
  - rt1=941.9600
  - rt2=0.0000
  - sel=5.0000
  - st1=927.0287
  - st2=0.0000
  - startup_cost=148555.0700
  - total_cost=148675.2900
- **Output:** st=1055.99, rt=1060.96

### Step 7: Node 25076 (Aggregate) - ROOT

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
  - st1=1055.9886
  - st2=0.0000
  - startup_cost=148555.0700
  - total_cost=148675.6300
- **Output:** st=951.95, rt=954.69
