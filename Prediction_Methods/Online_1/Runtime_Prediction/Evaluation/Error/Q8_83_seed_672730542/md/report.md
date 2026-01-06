# Online Prediction Report

**Test Query:** Q8_83_seed_672730542
**Timestamp:** 2026-01-01 20:42:43

## Data Summary

| Dataset | Rows | Purpose |
|---------|------|---------|
| Training_Training | 15559 | Operator + Pattern Training |
| Training_Test | 3892 | Pattern Selection Eval |
| Training | 19451 | Final Model Training |
| Test | 4868 | Final Prediction |

## Phase B: Operator Baseline

- Baseline MRE: 4.11%

## Phase C: Patterns in Query

- Total Patterns: 82

| Hash | Pattern String | Length | Occ | Avg MRE | Error Score |
|------|----------------|--------|-----|---------|-------------|
| 3aab37be | Hash -> Seq Scan (Outer) | 2 | 336 | 33781.0% | 113504.2307 |
| 895c6e8c | Hash Join -> [Seq Scan (Outer), Hash (In... | 2 | 364 | 20806.6% | 75736.1626 |
| f4cb205a | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 168 | 44967.0% | 75544.5822 |
| 7df893ad | Hash -> Hash Join (Outer) | 2 | 172 | 3565.0% | 6131.8766 |
| c0a8d3de | Hash -> Hash Join -> [Seq Scan (Outer), ... | 3 | 148 | 4130.8% | 6113.5159 |
| a54055ce | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 96 | 6342.9% | 6089.1983 |
| bb930825 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 3 | 148 | 116.8% | 172.9284 |
| 37515ad8 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 4 | 124 | 135.7% | 168.3286 |
| 545b5e57 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 72 | 212.7% | 153.1732 |
| 2e0f44ef | Hash Join -> [Nested Loop (Outer), Hash ... | 2 | 144 | 75.1% | 108.1438 |
| 444761fb | Hash -> Hash Join -> [Seq Scan (Outer), ... | 4 | 52 | 46.8% | 24.3176 |
| 314469b0 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 5 | 48 | 43.2% | 20.7410 |
| 54cb7f90 | Hash -> Hash Join -> [Seq Scan (Outer), ... | 6 | 48 | 43.2% | 20.7410 |
| 2724c080 | Aggregate -> Gather Merge (Outer) | 2 | 168 | 11.7% | 19.6008 |
| 3e2d5a00 | Sort -> Hash Join (Outer) | 2 | 96 | 19.3% | 18.5586 |
| ec92bdaa | Hash Join -> [Seq Scan (Outer), Hash -> ... | 5 | 52 | 29.1% | 15.1555 |
| c302739b | Hash Join -> [Seq Scan (Outer), Hash -> ... | 7 | 48 | 27.6% | 13.2381 |
| e1d7e5b4 | Hash Join -> [Seq Scan (Outer), Hash -> ... | 6 | 48 | 27.6% | 13.2381 |
| 2422d111 | Hash Join -> [Nested Loop -> [Hash Join ... | 3 | 72 | 15.0% | 10.7757 |
| 1691f6f0 | Gather Merge -> Sort (Outer) | 2 | 96 | 7.6% | 7.3257 |
| 3cfa90d7 | Nested Loop -> [Hash Join (Outer), Index... | 2 | 140 | 4.5% | 6.2375 |
| 3d4c3db9 | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 48 | 12.3% | 5.9049 |
| 440e6274 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 48 | 12.3% | 5.9049 |
| 4db07220 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 48 | 12.3% | 5.9049 |
| 9ce781b0 | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 48 | 12.3% | 5.9049 |
| a95bee4e | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 48 | 12.3% | 5.9049 |
| f4603221 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 48 | 12.3% | 5.9049 |
| 6981af52 | Hash Join -> [Nested Loop -> [Hash Join ... | 5 | 24 | 20.3% | 4.8707 |
| 800ffecc | Hash Join -> [Nested Loop -> [Hash Join ... | 7 | 24 | 20.3% | 4.8707 |
| 910f6702 | Hash Join -> [Nested Loop -> [Hash Join ... | 10 | 24 | 20.3% | 4.8707 |
| 9d50c2fc | Hash Join -> [Nested Loop -> [Hash Join ... | 8 | 24 | 20.3% | 4.8707 |
| b88a3db4 | Hash Join -> [Nested Loop -> [Hash Join ... | 6 | 24 | 20.3% | 4.8707 |
| c5dad784 | Hash Join -> [Nested Loop -> [Hash Join ... | 4 | 24 | 20.3% | 4.8707 |
| cee0b988 | Hash Join -> [Nested Loop -> [Hash Join ... | 9 | 24 | 20.3% | 4.8707 |
| fb7bcc0c | Hash Join -> [Nested Loop -> [Hash Join ... | 11 | 24 | 20.3% | 4.8707 |
| 29ee00db | Aggregate -> Gather Merge -> Sort (Outer... | 3 | 96 | 4.7% | 4.4662 |
| e0e3c3e1 | Nested Loop -> [Hash Join -> [Seq Scan (... | 3 | 116 | 3.5% | 4.0772 |
| 91d6e559 | Sort -> Hash Join -> [Nested Loop (Outer... | 3 | 72 | 5.4% | 3.8546 |
| bd9dfa7b | Nested Loop -> [Hash Join -> [Seq Scan (... | 4 | 92 | 3.7% | 3.3601 |
| 3c6d8006 | Gather Merge -> Sort -> Hash Join -> [Ne... | 4 | 48 | 6.2% | 2.9727 |
| 98d4ff98 | Gather Merge -> Sort -> Hash Join (Outer... | 3 | 48 | 6.2% | 2.9727 |
| 9d0e407c | Nested Loop -> [Hash Join -> [Seq Scan (... | 5 | 72 | 4.1% | 2.9587 |
| 12e6457c | Sort -> Hash Join -> [Nested Loop -> [Ha... | 4 | 48 | 6.0% | 2.9009 |
| 06857491 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 11 | 24 | 10.2% | 2.4503 |
| 1d069442 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 9 | 24 | 10.2% | 2.4503 |
| 58ed95a8 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 5 | 24 | 10.2% | 2.4503 |
| 5d01b240 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 7 | 24 | 10.2% | 2.4503 |
| 8febc667 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 12 | 24 | 10.2% | 2.4503 |
| be705a2d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 6 | 24 | 10.2% | 2.4503 |
| c7b8fb6d | Sort -> Hash Join -> [Nested Loop -> [Ha... | 8 | 24 | 10.2% | 2.4503 |
| d00b75d6 | Sort -> Hash Join -> [Nested Loop -> [Ha... | 10 | 24 | 10.2% | 2.4503 |
| 19fc9abd | Nested Loop -> [Hash Join -> [Nested Loo... | 10 | 24 | 9.0% | 2.1603 |
| 45158dca | Nested Loop -> [Hash Join -> [Nested Loo... | 6 | 24 | 9.0% | 2.1603 |
| 473ac852 | Nested Loop -> [Hash Join -> [Nested Loo... | 7 | 24 | 9.0% | 2.1603 |
| 959de0c2 | Nested Loop -> [Hash Join -> [Nested Loo... | 8 | 24 | 9.0% | 2.1603 |
| 9b49df80 | Nested Loop -> [Hash Join -> [Nested Loo... | 5 | 24 | 9.0% | 2.1603 |
| bf197fca | Nested Loop -> [Hash Join -> [Nested Loo... | 9 | 24 | 9.0% | 2.1603 |
| c5a9eefd | Nested Loop -> [Hash Join -> [Nested Loo... | 4 | 24 | 9.0% | 2.1603 |
| f62279eb | Nested Loop -> [Hash Join -> [Nested Loo... | 3 | 24 | 9.0% | 2.1603 |
| 5ae97df8 | Nested Loop -> [Hash Join -> [Seq Scan (... | 8 | 48 | 4.4% | 2.1340 |
| 5bfce159 | Nested Loop -> [Hash Join -> [Seq Scan (... | 6 | 48 | 4.4% | 2.1340 |
| ef93d4fc | Nested Loop -> [Hash Join -> [Seq Scan (... | 7 | 48 | 4.4% | 2.1340 |
| 50ace808 | Gather Merge -> Sort -> Hash Join -> [Ne... | 11 | 24 | 7.9% | 1.8886 |
| 82a8bdb2 | Gather Merge -> Sort -> Hash Join -> [Ne... | 9 | 24 | 7.9% | 1.8886 |
| 839648da | Gather Merge -> Sort -> Hash Join -> [Ne... | 6 | 24 | 7.9% | 1.8886 |
| 860d9d3a | Gather Merge -> Sort -> Hash Join -> [Ne... | 12 | 24 | 7.9% | 1.8886 |
| d8d77761 | Gather Merge -> Sort -> Hash Join -> [Ne... | 7 | 24 | 7.9% | 1.8886 |
| db6a761f | Gather Merge -> Sort -> Hash Join -> [Ne... | 5 | 24 | 7.9% | 1.8886 |
| e31c99cb | Gather Merge -> Sort -> Hash Join -> [Ne... | 10 | 24 | 7.9% | 1.8886 |
| ef63c60f | Gather Merge -> Sort -> Hash Join -> [Ne... | 8 | 24 | 7.9% | 1.8886 |
| ffc3be98 | Gather Merge -> Sort -> Hash Join -> [Ne... | 13 | 24 | 7.9% | 1.8886 |
| 53f9aa07 | Aggregate -> Gather Merge -> Sort -> Has... | 5 | 48 | 2.2% | 1.0579 |
| b149ff28 | Aggregate -> Gather Merge -> Sort -> Has... | 4 | 48 | 2.2% | 1.0579 |
| 264d1e57 | Aggregate -> Gather Merge -> Sort -> Has... | 13 | 24 | 3.2% | 0.7651 |
| 59f6581f | Aggregate -> Gather Merge -> Sort -> Has... | 7 | 24 | 3.2% | 0.7651 |
| 7f3b31ff | Aggregate -> Gather Merge -> Sort -> Has... | 8 | 24 | 3.2% | 0.7651 |
| 96f339c9 | Aggregate -> Gather Merge -> Sort -> Has... | 11 | 24 | 3.2% | 0.7651 |
| 9b77a70e | Aggregate -> Gather Merge -> Sort -> Has... | 12 | 24 | 3.2% | 0.7651 |
| acd22c74 | Aggregate -> Gather Merge -> Sort -> Has... | 14 | 24 | 3.2% | 0.7651 |
| b659e5bf | Aggregate -> Gather Merge -> Sort -> Has... | 10 | 24 | 3.2% | 0.7651 |
| c9736a93 | Aggregate -> Gather Merge -> Sort -> Has... | 6 | 24 | 3.2% | 0.7651 |
| cb7eed03 | Aggregate -> Gather Merge -> Sort -> Has... | 9 | 24 | 3.2% | 0.7651 |

**Legend:**
- **Occ:** Pattern occurrences in Training_Test
- **Avg MRE:** Average MRE of operator predictions at pattern root nodes
- **Error Score:** Occ x Avg MRE (initial ranking metric)

## Phase D: Pattern Selection

| Iter | Pattern | Error Score | Delta | Status | Global MRE |
|------|---------|-------------|-------|--------|-----------|
| 0 | 3aab37be | 113504.2307 | -0.0000% | REJECTED | 17.92% |
| 1 | 895c6e8c | 75736.1626 | 0.0004% | ACCEPTED | 17.92% |
| 2 | f4cb205a | 41652.9228 | 0.0005% | ACCEPTED | 17.92% |
| 3 | 7df893ad | 628.5971 | N/A | REJECTED | 17.92% |
| 4 | c0a8d3de | 540.8859 | 0.0000% | ACCEPTED | 17.92% |
| 5 | a54055ce | 350.8449 | 0.0000% | ACCEPTED | 17.92% |
| 6 | bb930825 | 184.4803 | -0.0000% | REJECTED | 17.92% |
| 7 | 37515ad8 | 173.2469 | -0.0000% | REJECTED | 17.92% |
| 8 | 545b5e57 | 152.9942 | -0.0000% | REJECTED | 17.92% |
| 9 | 2e0f44ef | 108.1203 | 0.0001% | ACCEPTED | 17.92% |
| 10 | 444761fb | 50.2829 | 0.0000% | ACCEPTED | 17.92% |
| 11 | ec92bdaa | 20.2515 | -0.0000% | REJECTED | 17.92% |
| 12 | 2724c080 | 19.6006 | 0.0222% | ACCEPTED | 17.90% |
| 13 | 3e2d5a00 | 18.4265 | N/A | REJECTED | 17.90% |
| 14 | c302739b | 18.3306 | N/A | REJECTED | 17.90% |
| 15 | e1d7e5b4 | 18.3306 | N/A | REJECTED | 17.90% |
| 16 | 29ee00db | 4.4857 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 17 | 3cfa90d7 | 4.0055 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 18 | 91d6e559 | 3.7031 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 19 | e0e3c3e1 | 3.3189 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 20 | 12e6457c | 2.7493 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 21 | bd9dfa7b | 2.5412 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 22 | 9d0e407c | 2.4738 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 23 | 06857491 | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 24 | 1d069442 | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 25 | 58ed95a8 | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 26 | 5d01b240 | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 27 | 8febc667 | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 28 | be705a2d | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 29 | c7b8fb6d | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 30 | d00b75d6 | 2.2555 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 31 | 2422d111 | 1.5987 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 32 | 53f9aa07 | 1.5277 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 33 | b149ff28 | 1.5277 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 34 | 3d4c3db9 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 35 | 440e6274 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 36 | 4db07220 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 37 | 9ce781b0 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 38 | a95bee4e | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 39 | f4603221 | 1.1101 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 40 | 264d1e57 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 41 | 59f6581f | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 42 | 7f3b31ff | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 43 | 96f339c9 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 44 | 9b77a70e | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 45 | acd22c74 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 46 | b659e5bf | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 47 | c9736a93 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 48 | cb7eed03 | 1.0519 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 49 | 6981af52 | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 50 | 800ffecc | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 51 | 910f6702 | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 52 | 9d50c2fc | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 53 | b88a3db4 | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 54 | c5dad784 | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 55 | cee0b988 | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
| 56 | fb7bcc0c | 0.4886 | N/A | SKIPPED_LOW_ERROR | 17.90% |
## Query Tree

```
Node 16214 (Aggregate) [PATTERN: 2724c080] - ROOT
  Node 16215 (Gather Merge) [consumed]
    Node 16216 (Sort)
      Node 16217 (Hash Join) [PATTERN: 2e0f44ef]
        Node 16218 (Nested Loop) [consumed]
          Node 16219 (Hash Join) [PATTERN: 2e0f44ef]
            Node 16220 (Nested Loop) [consumed]
              Node 16221 (Hash Join) [PATTERN: 895c6e8c]
                Node 16222 (Seq Scan) [consumed] - LEAF
                Node 16223 (Hash) [consumed]
                  Node 16224 (Hash Join)
                    Node 16225 (Seq Scan) - LEAF
                    Node 16226 (Hash) [PATTERN: a54055ce]
                      Node 16227 (Hash Join) [consumed]
                        Node 16228 (Seq Scan) [consumed] - LEAF
                        Node 16229 (Hash) [consumed]
                          Node 16230 (Seq Scan) [consumed] - LEAF
              Node 16231 (Index Scan) - LEAF
            Node 16232 (Hash) [consumed]
              Node 16233 (Seq Scan) - LEAF
          Node 16234 (Index Scan) - LEAF
        Node 16235 (Hash) [consumed]
          Node 16236 (Seq Scan) - LEAF
```

## Pattern Assignments

| Pattern | Hash | Root Node | Consumed Nodes |
|---------|------|-----------|----------------|
| Hash -> Hash Join -> [Seq Scan | a54055ce | 16226 | 16214, 16215, 16217, 16218, 16219, 16220, 16221, 16222, 16223, 16227, 16228, 16229, 16230, 16232, 16235 |
| Hash Join -> [Seq Scan (Outer) | 895c6e8c | 16221 | 16214, 16215, 16217, 16218, 16219, 16220, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 16217 | 16214, 16215, 16218, 16219, 16220, 16221, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235 |
| Hash Join -> [Nested Loop (Out | 2e0f44ef | 16219 | 16214, 16215, 16217, 16218, 16220, 16221, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235 |
| Aggregate -> Gather Merge (Out | 2724c080 | 16214 | 16215, 16217, 16218, 16219, 16220, 16221, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235 |


**Legend:**
- **Error Score:** Score at iteration time (recalculated after each ACCEPT)
- **Delta:** MRE improvement if pattern is added
- **Global MRE:** Overall MRE on Training_Test after this iteration

## Phase E: Final Prediction

- Final MRE: 4.60%
- Improvement: -0.49%

| Node | Type | Actual | Predicted | MRE | Source |
|------|------|--------|-----------|-----|--------|
| 16214 | Aggregate | 1237.48 | 1180.60 | 4.6% | pattern |
| 16216 | Sort | 1229.83 | 1096.01 | 10.9% | operator |
| 16217 | Hash Join | 1229.58 | 1199.17 | 2.5% | pattern |
| 16219 | Hash Join | 1225.29 | 1192.86 | 2.6% | pattern |
| 16234 | Index Scan | 0.01 | 0.05 | 753.5% | operator |
| 16236 | Seq Scan | 0.02 | 7.19 | 44865.5% | operator |
| 16221 | Hash Join | 218.70 | 260.30 | 19.0% | pattern |
| 16231 | Index Scan | 0.04 | 0.09 | 112.3% | operator |
| 16233 | Seq Scan | 37.90 | 44.50 | 17.4% | operator |
| 16224 | Hash Join | 38.35 | 67.79 | 76.8% | operator |
| 16225 | Seq Scan | 36.72 | 24.87 | 32.3% | operator |
| 16226 | Hash | 0.23 | 0.20 | 14.0% | pattern |

## Prediction Chain (Bottom-Up)

### Step 1: Node 16225 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=3600
  - nt=62500
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=150000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.4167
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=4225.0000
- **Output:** st=0.28, rt=24.87

### Step 2: Node 16226 (Hash) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** a54055ce (Hash -> Hash Join -> [Seq Scan (Outer), Hash -> Seq Scan (Outer) (Inner)] (Outer))
- **Consumes:** Nodes 16214, 16215, 16217, 16218, 16219, 16220, 16221, 16222, 16223, 16227, 16228, 16229, 16230, 16232, 16235
- **Input Features:**
  - HashJoin_Outer_np=0
  - HashJoin_Outer_nt=5
  - HashJoin_Outer_nt1=25
  - HashJoin_Outer_nt2=1
  - HashJoin_Outer_parallel_workers=0
  - HashJoin_Outer_plan_width=4
  - HashJoin_Outer_reltuples=0.0000
  - HashJoin_Outer_sel=0.2000
  - HashJoin_Outer_startup_cost=1.0700
  - HashJoin_Outer_total_cost=2.4000
  - Hash_Inner_np=0
  - Hash_Inner_nt=1
  - Hash_Inner_nt1=1
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.0600
  - Hash_Inner_total_cost=1.0600
  - Hash_np=0
  - Hash_nt=5
  - Hash_nt1=5
  - Hash_nt2=0
  - Hash_parallel_workers=0
  - Hash_plan_width=4
  - Hash_reltuples=0.0000
  - Hash_sel=1.0000
  - Hash_startup_cost=2.4000
  - Hash_total_cost=2.4000
  - SeqScan_Outer_np=1
  - SeqScan_Outer_nt=1
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=4
  - SeqScan_Outer_reltuples=5.0000
  - SeqScan_Outer_sel=0.2000
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=1.0600
- **Output:** st=0.19, rt=0.20

### Step 3: Node 16224 (Hash Join)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=12500
  - nt1=62500
  - nt2=5
  - parallel_workers=0
  - plan_width=4
  - reltuples=0.0000
  - rt1=24.8735
  - rt2=0.1953
  - sel=0.0400
  - st1=0.2761
  - st2=0.1946
  - startup_cost=2.4600
  - total_cost=4586.8400
- **Output:** st=2.08, rt=67.79

### Step 4: Node 16221 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 895c6e8c (Hash Join -> [Seq Scan (Outer), Hash (Inner)])
- **Consumes:** Nodes 16214, 16215, 16217, 16218, 16219, 16220, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=29497
  - HashJoin_nt1=147487
  - HashJoin_nt2=12500
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=8
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=4743.0900
  - HashJoin_total_cost=38813.1400
  - Hash_Inner_np=0
  - Hash_Inner_nt=12500
  - Hash_Inner_nt1=12500
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=4586.8400
  - Hash_Inner_total_cost=4586.8400
  - SeqScan_Outer_np=26136
  - SeqScan_Outer_nt=147487
  - SeqScan_Outer_nt1=0
  - SeqScan_Outer_nt2=0
  - SeqScan_Outer_parallel_workers=0
  - SeqScan_Outer_plan_width=12
  - SeqScan_Outer_reltuples=1500000.0000
  - SeqScan_Outer_sel=0.0983
  - SeqScan_Outer_startup_cost=0.0000
  - SeqScan_Outer_total_cost=33394.0600
- **Output:** st=32.76, rt=260.30

### Step 5: Node 16231 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=112600
  - nt=5
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=24
  - reltuples=6001215.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0000
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.4300
  - total_cost=0.8300
- **Output:** st=0.04, rt=0.09

### Step 6: Node 16233 (Seq Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=4128
  - nt=517
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=4
  - reltuples=200000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0026
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.0000
  - total_cost=5169.6700
- **Output:** st=0.42, rt=44.50

### Step 7: Node 16219 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 16214, 16215, 16217, 16218, 16220, 16221, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=732
  - HashJoin_nt1=118013
  - HashJoin_nt2=517
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=20
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0000
  - HashJoin_startup_cost=9919.6500
  - HashJoin_total_cost=70271.1300
  - Hash_Inner_np=0
  - Hash_Inner_nt=517
  - Hash_Inner_nt1=517
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=4
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=5169.6700
  - Hash_Inner_total_cost=5169.6700
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=118013
  - NestedLoop_Outer_nt1=29497
  - NestedLoop_Outer_nt2=5
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=24
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=0.8002
  - NestedLoop_Outer_startup_cost=4743.5200
  - NestedLoop_Outer_total_cost=64785.2000
- **Output:** st=80.11, rt=1192.86

### Step 8: Node 16234 (Index Scan) - LEAF

- **Source:** operator
- **Input Features:**
  - np=223
  - nt=1
  - nt1=0
  - nt2=0
  - parallel_workers=0
  - plan_width=8
  - reltuples=10000.0000
  - rt1=0.0000
  - rt2=0.0000
  - sel=0.0001
  - st1=0.0000
  - st2=0.0000
  - startup_cost=0.2900
  - total_cost=0.3000
- **Output:** st=0.01, rt=0.05

### Step 9: Node 16236 (Seq Scan) - LEAF

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
- **Output:** st=0.06, rt=7.19

### Step 10: Node 16217 (Hash Join) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2e0f44ef (Hash Join -> [Nested Loop (Outer), Hash (Inner)])
- **Consumes:** Nodes 16214, 16215, 16218, 16219, 16220, 16221, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235
- **Input Features:**
  - HashJoin_np=0
  - HashJoin_nt=732
  - HashJoin_nt1=732
  - HashJoin_nt2=25
  - HashJoin_parallel_workers=0
  - HashJoin_plan_width=148
  - HashJoin_reltuples=0.0000
  - HashJoin_sel=0.0400
  - HashJoin_startup_cost=9921.5000
  - HashJoin_total_cost=70498.2300
  - Hash_Inner_np=0
  - Hash_Inner_nt=25
  - Hash_Inner_nt1=25
  - Hash_Inner_nt2=0
  - Hash_Inner_parallel_workers=0
  - Hash_Inner_plan_width=108
  - Hash_Inner_reltuples=0.0000
  - Hash_Inner_sel=1.0000
  - Hash_Inner_startup_cost=1.2500
  - Hash_Inner_total_cost=1.2500
  - NestedLoop_Outer_np=0
  - NestedLoop_Outer_nt=732
  - NestedLoop_Outer_nt1=732
  - NestedLoop_Outer_nt2=1
  - NestedLoop_Outer_parallel_workers=0
  - NestedLoop_Outer_plan_width=20
  - NestedLoop_Outer_reltuples=0.0000
  - NestedLoop_Outer_sel=1.0000
  - NestedLoop_Outer_startup_cost=9919.9400
  - NestedLoop_Outer_total_cost=70492.5900
- **Output:** st=80.32, rt=1199.17

### Step 11: Node 16216 (Sort)

- **Source:** operator
- **Input Features:**
  - np=0
  - nt=732
  - nt1=732
  - nt2=0
  - parallel_workers=0
  - plan_width=148
  - reltuples=0.0000
  - rt1=1199.1651
  - rt2=0.0000
  - sel=1.0000
  - st1=80.3217
  - st2=0.0000
  - startup_cost=70533.0600
  - total_cost=70534.8900
- **Output:** st=1095.01, rt=1096.01

### Step 12: Node 16214 (Aggregate) - PATTERN ROOT

- **Source:** pattern
- **Pattern:** 2724c080 (Aggregate -> Gather Merge (Outer))
- **Consumes:** Nodes 16215, 16217, 16218, 16219, 16220, 16221, 16222, 16223, 16226, 16227, 16228, 16229, 16230, 16232, 16235
- **Input Features:**
  - Aggregate_np=0
  - Aggregate_nt=2268
  - Aggregate_nt1=2268
  - Aggregate_nt2=0
  - Aggregate_parallel_workers=0
  - Aggregate_plan_width=64
  - Aggregate_reltuples=0.0000
  - Aggregate_sel=1.0000
  - Aggregate_startup_cost=71533.1000
  - Aggregate_total_cost=71892.1400
  - GatherMerge_Outer_np=0
  - GatherMerge_Outer_nt=2268
  - GatherMerge_Outer_nt1=732
  - GatherMerge_Outer_nt2=0
  - GatherMerge_Outer_parallel_workers=3
  - GatherMerge_Outer_plan_width=148
  - GatherMerge_Outer_reltuples=0.0000
  - GatherMerge_Outer_sel=3.0984
  - GatherMerge_Outer_startup_cost=71533.1000
  - GatherMerge_Outer_total_cost=71801.4200
- **Output:** st=1178.12, rt=1180.60
