# Query Prediction Report (Dynamic/LOTO)

**Query:** Q9_100_seed_812199069
**Timestamp:** 2026-01-11 21:34:21

## Input Summary

- **Test File:** Prediction_Methods/Dynamic/Dataset/Dataset_Operator/Q9/test.csv
- **Overview File:** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/SVM/two_step_evaluation_overview.csv
- **Models Directory:** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model

## Query Tree

```
Node 16651 (Sort) - ROOT
  Node 16652 (Aggregate)
    Node 16653 (Gather)
      Node 16654 (Aggregate)
        Node 16655 (Hash Join)
          Node 16656 (Seq Scan) - LEAF
          Node 16657 (Hash)
            Node 16658 (Hash Join)
              Node 16659 (Seq Scan) - LEAF
              Node 16660 (Hash)
                Node 16661 (Hash Join)
                  Node 16662 (Hash Join)
                    Node 16663 (Nested Loop)
                      Node 16664 (Seq Scan) - LEAF
                      Node 16665 (Index Scan) - LEAF
                    Node 16666 (Hash)
                      Node 16667 (Seq Scan) - LEAF
                  Node 16668 (Hash)
                    Node 16669 (Seq Scan) - LEAF
```

## Prediction Chain (Bottom-Up)

### Step 1: Node 16656 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=26136.0000, plan_width=8.0000, sel=0.3226
**Input Features (start_time):** np=26136.0000, nt=483871.0000, sel=0.3226, total_cost=30974.7100

**Output:** predicted_startup_time=0.24, predicted_total_time=152.89

### Step 2: Node 16659 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=112600.0000, plan_width=29.0000, sel=0.2000
**Input Features (start_time):** np=112600.0000, nt=1200243.0000, sel=0.2000, total_cost=124602.4300

**Output:** predicted_startup_time=8.40, predicted_total_time=633.82

### Step 3: Node 16664 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=4128.0000, plan_width=4.0000, sel=0.0334
**Input Features (start_time):** np=4128.0000, nt=6680.0000, sel=0.0334, total_cost=5169.6700

**Output:** predicted_startup_time=0.54, predicted_total_time=36.25

### Step 4: Node 16665 (Index Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Index_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Index_Scan/model.pkl

**Input Features (execution_time):** nt1=0.0000, nt2=0.0000, parallel_workers=0.0000, plan_width=14.0000, reltuples=800000.0000, startup_cost=0.4200
**Input Features (start_time):** plan_width=14.0000, reltuples=800000.0000, sel=0.0000

**Output:** predicted_startup_time=0.01, predicted_total_time=0.01

### Step 5: Node 16667 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=223.0000, plan_width=8.0000, sel=1.0000
**Input Features (start_time):** np=223.0000, nt=10000.0000, sel=1.0000, total_cost=323.0000

**Output:** predicted_startup_time=0.05, predicted_total_time=5.39

### Step 6: Node 16669 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=1.0000, plan_width=108.0000, sel=1.0000
**Input Features (start_time):** np=1.0000, nt=25.0000, sel=1.0000, total_cost=1.2500

**Output:** predicted_startup_time=0.05, predicted_total_time=0.58

### Step 7: Node 16663 (Nested Loop)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Nested_Loop/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Nested_Loop/model.pkl

**Input Features (execution_time):** nt=26720.0000, nt1=6680.0000, nt2=4.0000, rt1=36.2502, rt2=0.0117, st1=0.5382, st2=0.0103
**Input Features (start_time):** nt1=6680.0000, nt2=4.0000, plan_width=18.0000, rt1=36.2502, rt2=0.0117, st1=0.5382, st2=0.0103

**Output:** predicted_startup_time=24.73, predicted_total_time=1097.98

### Step 8: Node 16666 (Hash)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=10000.0000, nt2=0.0000, plan_width=8.0000, rt1=5.3886, rt2=0.0000, st1=0.0490, st2=0.0000
**Input Features (start_time):** nt1=10000.0000, nt2=0.0000, plan_width=8.0000, rt1=5.3886, rt2=0.0000, st1=0.0490, st2=0.0000

**Output:** predicted_startup_time=17.31, predicted_total_time=17.31

### Step 9: Node 16668 (Hash)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=25.0000, nt2=0.0000, plan_width=108.0000, rt1=0.5775, rt2=0.0000, st1=0.0452, st2=0.0000
**Input Features (start_time):** nt1=25.0000, nt2=0.0000, plan_width=108.0000, rt1=0.5775, rt2=0.0000, st1=0.0452, st2=0.0000

**Output:** predicted_startup_time=14.06, predicted_total_time=14.06

### Step 10: Node 16662 (Hash Join)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=26720.0000, nt2=10000.0000, rt1=1097.9810, rt2=17.3095, st1=24.7342, st2=17.3088
**Input Features (start_time):** nt1=26720.0000, nt2=10000.0000, rt1=1097.9810, rt2=17.3095, st1=24.7342, st2=17.3088, total_cost=16627.4000

**Output:** predicted_startup_time=39.59, predicted_total_time=1104.12

### Step 11: Node 16661 (Hash Join)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=26720.0000, nt2=25.0000, rt1=1104.1225, rt2=14.0570, st1=39.5927, st2=14.0566
**Input Features (start_time):** nt1=26720.0000, nt2=25.0000, rt1=1104.1225, rt2=14.0570, st1=39.5927, st2=14.0566, total_cost=16710.9900

**Output:** predicted_startup_time=45.60, predicted_total_time=1134.11

### Step 12: Node 16660 (Hash)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=26720.0000, nt2=0.0000, plan_width=126.0000, rt1=1134.1065, rt2=0.0000, st1=45.6045, st2=0.0000
**Input Features (start_time):** nt1=26720.0000, nt2=0.0000, plan_width=126.0000, rt1=1134.1065, rt2=0.0000, st1=45.6045, st2=0.0000

**Output:** predicted_startup_time=76.11, predicted_total_time=76.11

### Step 13: Node 16658 (Hash Join)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=1200243.0000, nt2=26720.0000, rt1=633.8210, rt2=76.1140, st1=8.3999, st2=76.1136
**Input Features (start_time):** nt1=1200243.0000, nt2=26720.0000, rt1=633.8210, rt2=76.1140, st1=8.3999, st2=76.1136, total_cost=150716.2100

**Output:** predicted_startup_time=60.21, predicted_total_time=729.09

### Step 14: Node 16657 (Hash)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=96211.0000, nt2=0.0000, plan_width=131.0000, rt1=729.0898, rt2=0.0000, st1=60.2087, st2=0.0000
**Input Features (start_time):** nt1=96211.0000, nt2=0.0000, plan_width=131.0000, rt1=729.0898, rt2=0.0000, st1=60.2087, st2=0.0000

**Output:** predicted_startup_time=70.60, predicted_total_time=70.60

### Step 15: Node 16655 (Hash Join)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=483871.0000, nt2=96211.0000, rt1=152.8871, rt2=70.5968, st1=0.2364, st2=70.5969
**Input Features (start_time):** nt1=483871.0000, nt2=96211.0000, rt1=152.8871, rt2=70.5968, st1=0.2364, st2=70.5969, total_cost=185406.3800

**Output:** predicted_startup_time=88.07, predicted_total_time=331.74

### Step 16: Node 16654 (Aggregate)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=155180.0000, nt2=0.0000, rt1=331.7352, rt2=0.0000, st1=88.0747, st2=0.0000
**Input Features (start_time):** nt1=155180.0000, nt2=0.0000, rt1=331.7352, rt2=0.0000, st1=88.0747, st2=0.0000

**Output:** predicted_startup_time=792.60, predicted_total_time=840.63

### Step 17: Node 16653 (Gather)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Gather/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Gather/model.pkl

**Input Features (execution_time):** nt1=60150.0000, nt2=0.0000, rt1=840.6346, rt2=0.0000, st1=792.6045, st2=0.0000
**Input Features (start_time):** nt1=60150.0000, nt2=0.0000, parallel_workers=3.0000, rt1=840.6346, rt2=0.0000, st1=792.6045, st2=0.0000

**Output:** predicted_startup_time=478.94, predicted_total_time=933.14

### Step 18: Node 16652 (Aggregate)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=180450.0000, nt2=0.0000, rt1=933.1411, rt2=0.0000, st1=478.9358, st2=0.0000
**Input Features (start_time):** nt1=180450.0000, nt2=0.0000, rt1=933.1411, rt2=0.0000, st1=478.9358, st2=0.0000

**Output:** predicted_startup_time=917.64, predicted_total_time=908.98

### Step 19: Node 16651 (Sort) - ROOT

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/execution_time/Sort/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q9/Model/start_time/Sort/model.pkl

**Input Features (execution_time):** nt1=60150.0000, nt2=0.0000, plan_width=168.0000, rt1=908.9839, rt2=0.0000, sel=1.0000, st1=917.6380, st2=0.0000
**Input Features (start_time):** nt1=60150.0000, nt2=0.0000, plan_width=168.0000, rt1=908.9839, rt2=0.0000, sel=1.0000, st1=917.6380, st2=0.0000

**Output:** predicted_startup_time=1094.90, predicted_total_time=1096.22

## Prediction Results

| Node | Type | Pred Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |
|------|------|-----------|-----------|-----------|---------|---------|------------|------------|
| 16656 | Seq Scan | model | 0.26 | 132.96 | 0.24 | 152.89 | 8.4 | 15.0 |
| 16659 | Seq Scan | model | 0.19 | 699.25 | 8.40 | 633.82 | 4321.0 | 9.4 |
| 16664 | Seq Scan | model | 0.21 | 29.57 | 0.54 | 36.25 | 161.3 | 22.6 |
| 16665 | Index Scan | model | 0.05 | 0.06 | 0.01 | 0.01 | 80.9 | 79.4 |
| 16667 | Seq Scan | model | 0.08 | 2.10 | 0.05 | 5.39 | 38.8 | 156.7 |
| 16669 | Seq Scan | model | 14.41 | 14.41 | 0.05 | 0.58 | 99.7 | 96.0 |
| 16663 | Nested Loop | model | 0.64 | 184.94 | 24.73 | 1097.98 | 3746.7 | 493.7 |
| 16666 | Hash | model | 2.50 | 2.50 | 17.31 | 17.31 | 591.0 | 591.0 |
| 16668 | Hash | model | 14.43 | 14.43 | 14.06 | 14.06 | 2.6 | 2.6 |
| 16662 | Hash Join | model | 3.17 | 189.93 | 39.59 | 1104.12 | 1149.8 | 481.3 |
| 16661 | Hash Join | model | 17.61 | 205.25 | 45.60 | 1134.11 | 159.0 | 452.5 |
| 16660 | Hash | model | 208.21 | 208.21 | 76.11 | 76.11 | 63.4 | 63.4 |
| 16658 | Hash Join | model | 209.06 | 1024.55 | 60.21 | 729.09 | 71.2 | 28.8 |
| 16657 | Hash | model | 1042.84 | 1042.87 | 70.60 | 70.60 | 93.2 | 93.2 |
| 16655 | Hash Join | model | 1043.44 | 1239.63 | 88.07 | 331.74 | 91.6 | 73.2 |
| 16654 | Aggregate | model | 1268.58 | 1269.00 | 792.60 | 840.63 | 37.5 | 33.8 |
| 16653 | Gather | model | 1280.14 | 1288.13 | 478.94 | 933.14 | 62.6 | 27.6 |
| 16652 | Aggregate | model | 1281.37 | 1288.88 | 917.64 | 908.98 | 28.4 | 29.5 |
| 16651 | Sort | model | 1281.89 | 1289.03 | 1094.90 | 1096.22 | 14.6 | 15.0 |
