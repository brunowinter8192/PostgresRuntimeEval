# Online Prediction Report

**Test Query:** Q9_64_seed_516853953
**Timestamp:** 2025-12-21 17:19:33

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 5.03%

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
Node 18643 (Sort) - ROOT
  Node 18644 (Aggregate)
    Node 18645 (Gather)
      Node 18646 (Aggregate)
        Node 18647 (Nested Loop)
          Node 18648 (Hash Join)
            Node 18649 (Seq Scan) - LEAF
            Node 18650 (Hash)
              Node 18651 (Hash Join)
                Node 18652 (Hash Join)
                  Node 18653 (Nested Loop)
                    Node 18654 (Seq Scan) - LEAF
                    Node 18655 (Index Scan) - LEAF
                  Node 18656 (Hash)
                    Node 18657 (Seq Scan) - LEAF
                Node 18658 (Hash)
                  Node 18659 (Seq Scan) - LEAF
          Node 18660 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 5.29%
- Improvement: -0.26%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18643 | Sort | 1180.81 | 1118.33 | 5.3% | operator |
| 18644 | Aggregate | 1180.68 | 896.44 | 24.1% | operator |
| 18645 | Gather | 1179.53 | 965.14 | 18.2% | operator |
| 18646 | Aggregate | 1157.97 | 1141.19 | 1.4% | operator |
| 18647 | Nested Loop | 1133.99 | 1252.17 | 10.4% | operator |
| 18648 | Hash Join | 961.10 | 632.60 | 34.2% | operator |
| 18660 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 18649 | Seq Scan | 693.80 | 509.93 | 26.5% | operator |
| 18650 | Hash | 174.92 | 47.45 | 72.9% | operator |
| 18651 | Hash Join | 172.83 | 924.21 | 434.7% | operator |
| 18652 | Hash Join | 159.30 | 837.49 | 425.7% | operator |
| 18658 | Hash | 12.84 | 14.95 | 16.4% | operator |
| 18653 | Nested Loop | 153.90 | 1251.76 | 713.3% | operator |
| 18656 | Hash | 3.18 | 15.94 | 401.8% | operator |
| 18659 | Seq Scan | 12.82 | 2.94 | 77.1% | operator |
| 18654 | Seq Scan | 19.30 | 44.30 | 129.6% | operator |
| 18655 | Index Scan | 0.08 | -1.39 | 1926.9% | operator |
| 18657 | Seq Scan | 2.65 | 9.45 | 256.2% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18654 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4175
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0209
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.83, rt=44.30

### Step 2: Node 18655 (Index Scan) - LEAF

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
  - total_cost=2.0600
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18657 (Seq Scan) - LEAF

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

### Step 4: Node 18653 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=4175
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.3028
  - rt2=-1.3885
  - sel=1.0000
  - st1=1.8268
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13941.0100
- **Output:** st=153.58, rt=1251.76

### Step 5: Node 18656 (Hash)

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

### Step 6: Node 18659 (Seq Scan) - LEAF

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

### Step 7: Node 18652 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=16700
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7635
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5755
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=14432.8700
- **Output:** st=121.43, rt=837.49

### Step 8: Node 18658 (Hash)

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

### Step 9: Node 18651 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=16700
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.4938
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4285
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=14485.7000
- **Output:** st=105.83, rt=924.21

### Step 10: Node 18649 (Seq Scan) - LEAF

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

### Step 11: Node 18650 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=16700
  - nt1=16700
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.2071
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8298
  - st2=0.0000
  - startup_cost=14485.7000
  - total_cost=14485.7000
- **Output:** st=47.45, rt=47.45

### Step 12: Node 18648 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60132
  - nt1=1200243
  - nt2=16700
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=47.4496
  - sel=0.0000
  - st1=7.9002
  - st2=47.4483
  - startup_cost=14736.2000
  - total_cost=148340.5600
- **Output:** st=74.38, rt=632.60

### Step 13: Node 18660 (Index Scan) - LEAF

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

### Step 14: Node 18647 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60132
  - nt1=60132
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=632.6019
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.3772
  - st2=0.0041
  - startup_cost=14736.6300
  - total_cost=175583.0600
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 18646 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60132
  - nt1=60132
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=176635.3700
  - total_cost=177537.3500
- **Output:** st=1127.82, rt=1141.19

### Step 16: Node 18645 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=300660
  - nt1=60132
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.1871
  - rt2=0.0000
  - sel=5.0000
  - st1=1127.8202
  - st2=0.0000
  - startup_cost=177635.3700
  - total_cost=208603.3500
- **Output:** st=470.65, rt=965.14

### Step 17: Node 18644 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=300660
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=965.1436
  - rt2=0.0000
  - sel=0.2001
  - st1=470.6527
  - st2=0.0000
  - startup_cost=211609.9500
  - total_cost=212512.2000
- **Output:** st=895.27, rt=896.44

### Step 18: Node 18643 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=896.4392
  - rt2=0.0000
  - sel=1.0000
  - st1=895.2666
  - st2=0.0000
  - startup_cost=217286.9900
  - total_cost=217437.3700
- **Output:** st=1117.60, rt=1118.33
