# Online Prediction Report

**Test Query:** Q9_43_seed_344569302
**Timestamp:** 2025-12-21 17:18:11

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.45%

## Phase C: Patterns in Query

- Total Patterns: 56

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 420 | 12818.3% | 53836.8732 |
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 360 | 40658.7% | 146371.3776 |
| 1d35fb97 | Sort -> Aggregate (Outer) | 2 | 210 | 14.4% | 30.2509 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 180 | 4284.6% | 7712.2590 |
| 4fc84c77 | Aggregate -> Gather (Outer) | 2 | 150 | 5.7% | 8.5422 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 150 | 4.6% | 6.8991 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 150 | 9.7% | 14.5467 |
| 634cdbe2 | Gather -> Aggregate (Outer) | 2 | 90 | 3.4% | 3.0966 |
| c53c4396 | Nested Loop -> [Seq Scan (Outer), Index ... | 2 | 90 | 11.3% | 10.1670 |
| 3b447875 | Aggregate -> Nested Loop (Outer) | 2 | 30 | 10.6% | 3.1651 |
| 7d4e78be | Hash Join -> [Hash Join (Outer), Hash (I... | 2 | 30 | 5.5% | 1.6532 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 150 | 79.2% | 118.8648 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 120 | 3.5% | 4.1629 |
| a5f39f08 | Aggregate -> Gather -> Aggregate (Outer)... | 3 | 90 | 8.1% | 7.2489 |
| b3a45093 | Sort -> Aggregate -> Gather (Outer) (Out... | 3 | 60 | 3.5% | 2.1270 |
| 30d6e09b | Hash Join -> [Hash Join -> [Nested Loop ... | 3 | 30 | 5.5% | 1.6532 |
| 2873b8c3 | Hash Join -> [Nested Loop -> [Seq Scan (... | 3 | 30 | 3.4% | 1.0295 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 90 | 3.8% | 3.3937 |
| 7a51ce50 | Hash Join -> [Hash Join -> [Nested Loop ... | 4 | 30 | 5.5% | 1.6532 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 895c6e8c | 53836.8732 | 0.0007% | REJECTED | 17.17% |
| 1 | 3aab37be | 146371.3776 | -0.0000% | REJECTED | 17.17% |
| 2 | 1d35fb97 | 30.2509 | 0.2650% | REJECTED | 17.17% |
| 3 | 7df893ad | 7712.2590 | -0.0000% | REJECTED | 17.17% |
| 4 | 4fc84c77 | 8.5422 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 5 | 3cfa90d7 | 6.8991 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 6 | 2e0f44ef | 14.5467 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 7 | 634cdbe2 | 3.0966 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 8 | c53c4396 | 10.1670 | -0.0000% | REJECTED | 17.17% |
| 9 | 3b447875 | 3.1651 | 0.0002% | REJECTED | 17.17% |
| 10 | 7d4e78be | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 11 | bb930825 | 118.8648 | -0.0000% | REJECTED | 17.17% |
| 12 | e0e3c3e1 | 4.1629 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 13 | a5f39f08 | 7.2489 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 14 | b3a45093 | 2.1270 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 15 | 30d6e09b | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 16 | 2873b8c3 | 1.0295 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 17 | bd9dfa7b | 3.3937 | N/A | SKIPPED_LOW_ERROR | 17.17% |
| 18 | 7a51ce50 | 1.6532 | N/A | SKIPPED_LOW_ERROR | 17.17% |
## Query Tree

```
Node 18228 (Sort) - ROOT
  Node 18229 (Aggregate)
    Node 18230 (Gather)
      Node 18231 (Aggregate)
        Node 18232 (Nested Loop)
          Node 18233 (Hash Join)
            Node 18234 (Seq Scan) - LEAF
            Node 18235 (Hash)
              Node 18236 (Hash Join)
                Node 18237 (Hash Join)
                  Node 18238 (Nested Loop)
                    Node 18239 (Seq Scan) - LEAF
                    Node 18240 (Index Scan) - LEAF
                  Node 18241 (Hash)
                    Node 18242 (Seq Scan) - LEAF
                Node 18243 (Hash)
                  Node 18244 (Seq Scan) - LEAF
          Node 18245 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.72%
- Improvement: -0.28%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18228 | Sort | 1185.22 | 1117.39 | 5.7% | operator |
| 18229 | Aggregate | 1185.10 | 897.56 | 24.3% | operator |
| 18230 | Gather | 1183.99 | 955.76 | 19.3% | operator |
| 18231 | Aggregate | 1166.06 | 1141.46 | 2.1% | operator |
| 18232 | Nested Loop | 1141.99 | 1252.17 | 9.6% | operator |
| 18233 | Hash Join | 967.74 | 632.25 | 34.7% | operator |
| 18245 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 18234 | Seq Scan | 693.94 | 509.93 | 26.5% | operator |
| 18235 | Hash | 179.84 | 47.23 | 73.7% | operator |
| 18236 | Hash Join | 177.98 | 924.09 | 419.2% | operator |
| 18237 | Hash Join | 164.01 | 837.43 | 410.6% | operator |
| 18243 | Hash | 13.36 | 14.95 | 11.9% | operator |
| 18238 | Nested Loop | 156.98 | 1251.76 | 697.4% | operator |
| 18241 | Hash | 4.51 | 15.94 | 253.6% | operator |
| 18244 | Seq Scan | 13.35 | 2.94 | 78.0% | operator |
| 18239 | Seq Scan | 20.04 | 44.44 | 121.8% | operator |
| 18240 | Index Scan | 0.07 | -1.39 | 1951.3% | operator |
| 18242 | Seq Scan | 3.94 | 9.45 | 139.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18239 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3841
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0192
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.84, rt=44.44

### Step 2: Node 18240 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=17560
  - nt=4
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=14
  - reltuples=800000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4200
  - total_cost=2.1600
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18242 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=223
  - nt=10000
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=10000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=323.0000
- **Output:** st=0.04, rt=9.45

### Step 4: Node 18238 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=3841
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.4408
  - rt2=-1.3884
  - sel=0.9999
  - st1=1.8399
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13635.2500
- **Output:** st=153.58, rt=1251.76

### Step 5: Node 18241 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=10000
  - nt1=10000
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=0.0000
  - rt1=9.4454
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0398
  - st2=0.0000
  - startup_cost=323.0000
  - total_cost=323.0000
- **Output:** st=15.94, rt=15.94

### Step 6: Node 18244 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=1
  - nt=25
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=25.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=1.2500
- **Output:** st=0.05, rt=2.94

### Step 7: Node 18237 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=15363
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7624
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5752
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=14123.6000
- **Output:** st=121.42, rt=837.43

### Step 8: Node 18243 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=25
  - nt1=25
  - nt2=0
  - parallel_workers=0
  - plan_width=108
  - reltuples=0.0000
  - rt1=2.9371
  - rt2=0.0000
  - sel=1.0000
  - st1=0.0513
  - st2=0.0000
  - startup_cost=1.2500
  - total_cost=1.2500
- **Output:** st=14.95, rt=14.95

### Step 9: Node 18236 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=15363
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.4348
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4210
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=14172.3300
- **Output:** st=105.82, rt=924.09

### Step 10: Node 18234 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=1200243
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=29
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.2000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=124602.4300
- **Output:** st=7.90, rt=509.93

### Step 11: Node 18235 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=15363
  - nt1=15363
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.0921
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8170
  - st2=0.0000
  - startup_cost=14172.3300
  - total_cost=14172.3300
- **Output:** st=47.22, rt=47.23

### Step 12: Node 18233 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=55319
  - nt1=1200243
  - nt2=15363
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=47.2257
  - sel=0.0000
  - st1=7.9002
  - st2=47.2243
  - startup_cost=14402.7800
  - total_cost=148007.1200
- **Output:** st=74.59, rt=632.25

### Step 13: Node 18245 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=26136
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=1500000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.4500
- **Output:** st=0.00, rt=-5.54

### Step 14: Node 18232 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=55319
  - nt1=55319
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=632.2458
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.5851
  - st2=0.0041
  - startup_cost=14403.2000
  - total_cost=173069.1200
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 18231 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=55319
  - nt1=55319
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=174037.2000
  - total_cost=174866.9900
- **Output:** st=1129.00, rt=1141.46

### Step 16: Node 18230 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=276595
  - nt1=55319
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.4628
  - rt2=0.0000
  - sel=5.0000
  - st1=1129.0010
  - st2=0.0000
  - startup_cost=175037.2000
  - total_cost=203526.4900
- **Output:** st=483.91, rt=955.76

### Step 17: Node 18229 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=276595
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=955.7588
  - rt2=0.0000
  - sel=0.2175
  - st1=483.9070
  - st2=0.0000
  - startup_cost=206292.4400
  - total_cost=207194.6900
- **Output:** st=899.51, rt=897.56

### Step 18: Node 18228 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=897.5573
  - rt2=0.0000
  - sel=1.0000
  - st1=899.5101
  - st2=0.0000
  - startup_cost=211969.4800
  - total_cost=212119.8500
- **Output:** st=1116.65, rt=1117.39
