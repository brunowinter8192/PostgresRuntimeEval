# Online Prediction Report

**Test Query:** Q18_24_seed_188692713
**Timestamp:** 2025-12-21 18:26:36

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17531 | Operator + Pattern Training |
| Training_Test | 4388 | Pattern Selection Eval |
| Training | 21919 | Final Model Training |
| Test | 2400 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 61.29%

## Phase C: Patterns in Query

- Total Patterns: 67

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 428 | 14583.3% | 62416.6571 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 6.3% | 13.1538 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 180 | 3.2% | 5.8409 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 90 | 5.4% | 4.8997 |
| e296a71f | Limit -> Sort (Outer) | 2 | 60 | 1.3% | 0.7659 |
| 7bcfec22 | Limit -> Sort -> Aggregate (Outer) (Oute... | 3 | 60 | 1.3% | 0.7659 |
| ddb1e0ca | Sort -> Aggregate -> Gather Merge (Outer... | 3 | 30 | 1.2% | 0.3706 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 62416.6571 | 0.0028% | REJECTED | 5.12% |
| 1 | 1d35fb97 | 13.1538 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 2 | 2724c080 | 5.8409 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 3 | 3e2d5a00 | 4.8997 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 4 | e296a71f | 0.7659 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 5 | 7bcfec22 | 0.7659 | N/A | SKIPPED_LOW_ERROR | 5.12% |
| 6 | ddb1e0ca | 0.3706 | N/A | SKIPPED_LOW_ERROR | 5.12% |
## Query Tree

```
Node 29876 (Limit) - ROOT
  Node 29877 (Sort)
    Node 29878 (Aggregate)
      Node 29879 (Gather Merge)
        Node 29880 (Incremental Sort)
          Node 29881 (Nested Loop)
            Node 29882 (Merge Join)
              Node 29883 (Sort)
                Node 29884 (Hash Join)
                  Node 29885 (Seq Scan) - LEAF
                  Node 29886 (Hash)
                    Node 29887 (Aggregate)
                      Node 29888 (Index Scan) - LEAF
              Node 29889 (Sort)
                Node 29890 (Seq Scan) - LEAF
            Node 29891 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 61.29%
- Improvement: -0.00%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 29876 | Limit | 3036.05 | 1175.21 | 61.3% | operator |
| 29877 | Sort | 2924.36 | 1127.81 | 61.4% | operator |
| 29878 | Aggregate | 2924.32 | 1073.15 | 63.3% | operator |
| 29879 | Gather Merge | 2924.30 | 1073.95 | 63.3% | operator |
| 29880 | Incremental Sort | 2903.69 | 0.00 | 100.0% | operator |
| 29881 | Nested Loop | 2903.64 | 1111.34 | 61.7% | operator |
| 29882 | Merge Join | 2903.57 | 0.00 | 100.0% | operator |
| 29891 | Index Scan | 0.02 | 0.05 | 88.1% | operator |
| 29883 | Sort | 2835.34 | 1099.77 | 61.2% | operator |
| 29889 | Sort | 65.33 | 1074.66 | 1545.0% | operator |
| 29884 | Hash Join | 2835.33 | 686.33 | 75.8% | operator |
| 29890 | Seq Scan | 53.06 | 18.25 | 65.6% | operator |
| 29885 | Seq Scan | 190.60 | 170.37 | 10.6% | operator |
| 29886 | Hash | 2614.34 | 21.04 | 99.2% | operator |
| 29887 | Aggregate | 2614.31 | 1073.15 | 59.0% | operator |
| 29888 | Index Scan | 2118.63 | 0.00 | 100.0% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 29888 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=6001215
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=9
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=225647.6600
- **Output:** st=0.00, rt=0.00

### Step 2: Node 29887 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=407734
  - nt1=6001215
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=0.0047
  - rt2=0.0000
  - sel=0.0679
  - st1=0.0007
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=274001.7700
- **Output:** st=1069.76, rt=1073.15

### Step 3: Node 29885 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=483871
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=20
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.3226
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=30974.7100
- **Output:** st=0.84, rt=170.37

### Step 4: Node 29886 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=407734
  - nt1=407734
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=1073.1530
  - rt2=0.0000
  - sel=1.0000
  - st1=1069.7556
  - st2=0.0000
  - startup_cost=274001.7700
  - total_cost=274001.7700
- **Output:** st=21.04, rt=21.04

### Step 5: Node 29884 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=483871
  - nt2=407734
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=170.3739
  - rt2=21.0400
  - sel=0.0000
  - st1=0.8382
  - st2=21.0402
  - startup_cost=279098.4400
  - total_cost=311343.3100
- **Output:** st=66.37, rt=686.33

### Step 6: Node 29890 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=150000
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=23
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5100.0000
- **Output:** st=1.32, rt=18.25

### Step 7: Node 29883 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=131527
  - nt1=131527
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=0.0000
  - rt1=686.3336
  - rt2=0.0000
  - sel=1.0000
  - st1=66.3738
  - st2=0.0000
  - startup_cost=322526.4000
  - total_cost=322855.2200
- **Output:** st=1098.50, rt=1099.77

### Step 8: Node 29889 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=150000
  - nt1=150000
  - nt2=0
  - parallel_workers=0
  - plan_width=23
  - reltuples=0.0000
  - rt1=18.2462
  - rt2=0.0000
  - sel=1.0000
  - st1=1.3221
  - st2=0.0000
  - startup_cost=17995.9500
  - total_cost=18370.9500
- **Output:** st=1073.84, rt=1074.66

### Step 9: Node 29882 (Merge Join)

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 10: Node 29891 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=9
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.6100
- **Output:** st=0.04, rt=0.05

### Step 11: Node 29881 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=526215
  - nt1=131527
  - nt2=5
  - parallel_workers=0
  - plan_width=44
  - reltuples=0.0000
  - rt1=0.0000
  - rt2=0.0451
  - sel=0.8002
  - st1=0.0000
  - st2=0.0433
  - startup_cost=340522.8000
  - total_cost=430663.5800
- **Output:** st=72.40, rt=1111.34

### Step 12: Node 29880 (Incremental Sort)

- **Source:** operator
- **Output:** st=0.00, rt=0.00

### Step 13: Node 29879 (Gather Merge)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1631266
  - nt1=526215
  - nt2=0
  - parallel_workers=3
  - plan_width=44
  - reltuples=0.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=3.1000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=341523.4700
  - total_cost=637679.1300
- **Output:** st=1069.75, rt=1073.95

### Step 14: Node 29878 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1631266
  - nt1=1631266
  - nt2=0
  - parallel_workers=0
  - plan_width=71
  - reltuples=0.0000
  - rt1=1073.9540
  - rt2=0.0000
  - sel=1.0000
  - st1=1069.7474
  - st2=0.0000
  - startup_cost=341523.4700
  - total_cost=670304.4500
- **Output:** st=1069.76, rt=1073.15

### Step 15: Node 29877 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=1631266
  - nt1=1631266
  - nt2=0
  - parallel_workers=0
  - plan_width=71
  - reltuples=0.0000
  - rt1=1073.1534
  - rt2=0.0000
  - sel=1.0000
  - st1=1069.7560
  - st2=0.0000
  - startup_cost=732650.2600
  - total_cost=736728.4200
- **Output:** st=1126.40, rt=1127.81

### Step 16: Node 29876 (Limit) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=100
  - nt1=1631266
  - nt2=0
  - parallel_workers=0
  - plan_width=71
  - reltuples=0.0000
  - rt1=1127.8063
  - rt2=0.0000
  - sel=0.0001
  - st1=1126.3987
  - st2=0.0000
  - startup_cost=732650.2600
  - total_cost=732650.5100
- **Output:** st=1173.93, rt=1175.21
