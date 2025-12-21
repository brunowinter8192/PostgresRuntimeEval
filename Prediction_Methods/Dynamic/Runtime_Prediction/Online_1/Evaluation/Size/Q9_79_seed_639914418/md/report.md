# Online Prediction Report

**Test Query:** Q9_79_seed_639914418
**Timestamp:** 2025-12-21 17:22:54

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 17280 | Operator + Pattern Training |
| Training_Test | 4320 | Pattern Selection Eval |
| Training | 21600 | Final Model Training |
| Test | 2719 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 7.66%

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
Node 18934 (Sort) - ROOT
  Node 18935 (Aggregate)
    Node 18936 (Gather)
      Node 18937 (Aggregate)
        Node 18938 (Nested Loop)
          Node 18939 (Hash Join)
            Node 18940 (Seq Scan) - LEAF
            Node 18941 (Hash)
              Node 18942 (Hash Join)
                Node 18943 (Hash Join)
                  Node 18944 (Nested Loop)
                    Node 18945 (Seq Scan) - LEAF
                    Node 18946 (Index Scan) - LEAF
                  Node 18947 (Hash)
                    Node 18948 (Seq Scan) - LEAF
                Node 18949 (Hash)
                  Node 18950 (Seq Scan) - LEAF
          Node 18951 (Index Scan) - LEAF
```

## Pattern Assignments

No patterns selected.


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 7.95%
- Improvement: -0.29%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 18934 | Sort | 1212.62 | 1116.22 | 7.9% | operator |
| 18935 | Aggregate | 1212.48 | 901.35 | 25.7% | operator |
| 18936 | Gather | 1211.61 | 941.00 | 22.3% | operator |
| 18937 | Aggregate | 1192.65 | 1141.96 | 4.3% | operator |
| 18938 | Nested Loop | 1168.71 | 1252.17 | 7.1% | operator |
| 18939 | Hash Join | 997.79 | 631.63 | 36.7% | operator |
| 18951 | Index Scan | 0.00 | -5.54 | 184812.7% | operator |
| 18940 | Seq Scan | 717.45 | 509.93 | 28.9% | operator |
| 18941 | Hash | 187.24 | 46.85 | 75.0% | operator |
| 18942 | Hash Join | 180.50 | 923.84 | 411.8% | operator |
| 18943 | Hash Join | 166.35 | 837.31 | 403.3% | operator |
| 18949 | Hash | 13.53 | 14.95 | 10.5% | operator |
| 18944 | Nested Loop | 159.80 | 1251.76 | 683.3% | operator |
| 18947 | Hash | 4.55 | 15.94 | 250.5% | operator |
| 18950 | Seq Scan | 13.52 | 2.94 | 78.3% | operator |
| 18945 | Seq Scan | 21.24 | 44.65 | 110.2% | operator |
| 18946 | Index Scan | 0.08 | -1.39 | 1926.9% | operator |
| 18948 | Seq Scan | 4.07 | 9.45 | 132.3% | operator |

## Prediction Chain (Bottom-Up)

### Step 1: Node 18945 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=3340
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=1.86, rt=44.65

### Step 2: Node 18946 (Index Scan) - LEAF

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
  - total_cost=2.3100
- **Output:** st=0.01, rt=-1.39

### Step 3: Node 18948 (Seq Scan) - LEAF

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

### Step 4: Node 18944 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=13360
  - nt1=3340
  - nt2=4
  - parallel_workers=0
  - plan_width=18
  - reltuples=0.0000
  - rt1=44.6498
  - rt2=-1.3884
  - sel=1.0000
  - st1=1.8597
  - st2=0.0113
  - startup_cost=0.4200
  - total_cost=13007.1200
- **Output:** st=153.57, rt=1251.76

### Step 5: Node 18947 (Hash)

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

### Step 6: Node 18950 (Seq Scan) - LEAF

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

### Step 7: Node 18943 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=13360
  - nt1=13360
  - nt2=10000
  - parallel_workers=0
  - plan_width=26
  - reltuples=0.0000
  - rt1=1251.7609
  - rt2=15.9407
  - sel=0.0001
  - st1=153.5748
  - st2=15.9407
  - startup_cost=448.4300
  - total_cost=13490.2000
- **Output:** st=121.41, rt=837.31

### Step 8: Node 18949 (Hash)

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

### Step 9: Node 18942 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=13360
  - nt1=13360
  - nt2=25
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=837.3104
  - rt2=14.9479
  - sel=0.0400
  - st1=121.4053
  - st2=14.9467
  - startup_cost=449.9900
  - total_cost=13532.7700
- **Output:** st=105.79, rt=923.84

### Step 10: Node 18940 (Seq Scan) - LEAF

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

### Step 11: Node 18941 (Hash)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=13360
  - nt1=13360
  - nt2=0
  - parallel_workers=0
  - plan_width=126
  - reltuples=0.0000
  - rt1=923.8438
  - rt2=0.0000
  - sel=1.0000
  - st1=105.7882
  - st2=0.0000
  - startup_cost=13532.7700
  - total_cost=13532.7700
- **Output:** st=46.85, rt=46.85

### Step 12: Node 18939 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=48106
  - nt1=1200243
  - nt2=13360
  - parallel_workers=0
  - plan_width=131
  - reltuples=0.0000
  - rt1=509.9269
  - rt2=46.8547
  - sel=0.0000
  - st1=7.9002
  - st2=46.8534
  - startup_cost=13733.1700
  - total_cost=147337.5000
- **Output:** st=74.87, rt=631.63

### Step 13: Node 18951 (Index Scan) - LEAF

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

### Step 14: Node 18938 (Nested Loop)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=48106
  - nt1=48106
  - nt2=1
  - parallel_workers=0
  - plan_width=159
  - reltuples=0.0000
  - rt1=631.6297
  - rt2=-5.5414
  - sel=1.0000
  - st1=74.8730
  - st2=0.0041
  - startup_cost=13733.6000
  - total_cost=169131.6900
- **Output:** st=154.10, rt=1252.17

### Step 15: Node 18937 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=48106
  - nt1=48106
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=1252.1681
  - rt2=0.0000
  - sel=1.0000
  - st1=154.1042
  - st2=0.0000
  - startup_cost=169973.5400
  - total_cost=170695.1300
- **Output:** st=1130.86, rt=1141.96

### Step 16: Node 18936 (Gather)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=240530
  - nt1=48106
  - nt2=0
  - parallel_workers=5
  - plan_width=168
  - reltuples=0.0000
  - rt1=1141.9632
  - rt2=0.0000
  - sel=5.0000
  - st1=1130.8626
  - st2=0.0000
  - startup_cost=170973.5400
  - total_cost=195748.1300
- **Output:** st=504.39, rt=941.00

### Step 17: Node 18935 (Aggregate)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=240530
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=941.0019
  - rt2=0.0000
  - sel=0.2501
  - st1=504.3893
  - st2=0.0000
  - startup_cost=198153.4300
  - total_cost=199055.6800
- **Output:** st=908.01, rt=901.35

### Step 18: Node 18934 (Sort) - ROOT

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=60150
  - nt1=60150
  - nt2=0
  - parallel_workers=0
  - plan_width=168
  - reltuples=0.0000
  - rt1=901.3453
  - rt2=0.0000
  - sel=1.0000
  - st1=908.0069
  - st2=0.0000
  - startup_cost=203830.4700
  - total_cost=203980.8500
- **Output:** st=1115.47, rt=1116.22
