# Online Prediction Report

**Test Query:** Q9_89_seed_721954728
**Timestamp:** 2025-12-21 17:22:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 7.48%

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
Node 19135 (Sort) - ROOT
  Node 19136 (Aggregate)
    Node 19137 (Gather)
      Node 19138 (Aggregate)
        Node 19139 (Nested Loop)
          Node 19140 (Hash Join)
            Node 19141 (Seq Scan) - LEAF
            Node 19142 (Hash)
              Node 19143 (Hash Join)
                Node 19144 (Hash Join)
                  Node 19145 (Nested Loop)
                    Node 19146 (Seq Scan) - LEAF
                    Node 19147 (Index Scan) - LEAF
                  Node 19148 (Hash)
                    Node 19149 (Seq Scan) - LEAF
                Node 19150 (Hash)
                  Node 19151 (Seq Scan) - LEAF
          Node 19152 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.73%
- Improvement: -0.24%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 19135 | Sort | 1212.65 | 1118.92 | 7.7% | operator |
| 19136 | Aggregate | 1212.54 | 896.90 | 26.0% | operator |
| 19137 | Gather | 1211.00 | 964.87 | 20.3% | operator |
| 19138 | Aggregate | 1193.31 | 1117.47 | 6.4% | operator |
| 19139 | Nested Loop | 1167.69 | 1252.17 | 7.2% | operator |
| 19140 | Hash Join | 989.17 | 632.96 | 36.0% | operator |
| 19152 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 19141 | Seq Scan | 702.64 | 509.93 | 27.4% | operator |
| 19142 | Hash | 189.81 | 47.68 | 74.9% | operator |
| 19143 | Hash Join | 187.95 | 924.32 | 391.8% | operator |
| 19144 | Hash Join | 173.84 | 837.55 | 381.8% | operator |
| 19150 | Hash | 13.47 | 14.95 | 11.0% | operator |
| 19145 | Nested Loop | 167.21 | 1251.76 | 648.6% | operator |
| 19148 | Hash | 4.42 | 15.94 | 260.5% | operator |
| 19151 | Seq Scan | 13.45 | 2.94 | 78.2% | operator |
| 19146 | Seq Scan | 20.64 | 44.17 | 113.9% | operator |
| 19147 | Index Scan | 0.08 | -1.39 | 1835.6% | operator |
| 19149 | Seq Scan | 3.84 | 9.45 | 145.8% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 19146 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=4509
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0225
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.81, rt=44.17

### Step 2: Node 19147 (Index Scan) - LEAF

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
  - total_cost=1.9700
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 19149 (Seq Scan) - LEAF

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

### Step 4: Node 19145 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=4509
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.1658
  - rt2=-1.3885
  - sel=1.0001
  - st1=1.8136
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=14242.4200
- **Output:** st=153.58, rt=1251.76

### Step 5: Node 19148 (Hash)

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

### Step 6: Node 19151 (Seq Scan) - LEAF

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

### Step 7: Node 19144 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7646
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5758
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=14737.7900
- **Output:** st=121.44, rt=837.55

### Step 8: Node 19150 (Hash)

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

### Step 9: Node 19143 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.5511
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4359
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=14794.7200
- **Output:** st=105.84, rt=924.32

### Step 10: Node 19141 (Seq Scan) - LEAF

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

### Step 11: Node 19142 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=18037
  - nt1=18037
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=924.3188
  - rt2=0.0000
  - sel=1.0000
  - st1=105.8424
  - st2=0.0000
  - startup_cost=14794.7200
  - total_cost=14794.7200
- **Output:** st=47.68, rt=47.68

### Step 12: Node 19140 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=64945
  - nt1=1200243
  - nt2=18037
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=47.6773
  - sel=0.0000
  - st1=7.9002
  - st2=47.6759
  - startup_cost=15065.2800
  - total_cost=148669.6400
- **Output:** st=74.17, rt=632.96

### Step 13: Node 19152 (Index Scan) - LEAF

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

### Step 14: Node 19139 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=64945
  - nt1=64945
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=632.9609
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.1694
  - st2=0.0041
  - startup_cost=15065.7100
  - total_cost=178092.6500
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 19138 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=64945
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=0.9262
  - st1=154.1042
  - st2=0.0000
  - startup_cost=179229.1900
  - total_cost=180131.4400
- **Output:** st=1109.63, rt=1117.47

### Step 16: Node 19137 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=300750
  - nt1=60150
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1117.4675
  - rt2=0.0000
  - sel=5.0000
  - st1=1109.6260
  - st2=0.0000
  - startup_cost=180229.1900
  - total_cost=211206.4400
- **Output:** st=471.08, rt=964.87

### Step 17: Node 19136 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=300750
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=964.8677
  - rt2=0.0000
  - sel=0.2000
  - st1=471.0807
  - st2=0.0000
  - startup_cost=214213.9400
  - total_cost=215116.1900
- **Output:** st=894.47, rt=896.90

### Step 18: Node 19135 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=896.9033
  - rt2=0.0000
  - sel=1.0000
  - st1=894.4744
  - st2=0.0000
  - startup_cost=219890.9800
  - total_cost=220041.3600
- **Output:** st=1118.18, rt=1118.92
