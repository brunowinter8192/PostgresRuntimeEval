# Query Prediction Report (Dynamic/LOTO)

**Query:** Q19_100_seed_812199069
**Timestamp:** 2026-01-11 21:34:42

## Input Summary

- **Test File:** Prediction_Methods/Dynamic/Dataset/Dataset_Operator/Q19/test.csv
- **Overview File:** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/SVM/two_step_evaluation_overview.csv
- **Models Directory:** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model

## Query Tree

```
Node 31220 (Aggregate) - ROOT
  Node 31221 (Gather)
    Node 31222 (Aggregate)
      Node 31223 (Hash Join)
        Node 31224 (Seq Scan) - LEAF
        Node 31225 (Hash)
          Node 31226 (Seq Scan) - LEAF
```

## Prediction Chain (Bottom-Up)

### Step 1: Node 31224 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=112600.0000, plan_width=21.0000, sel=0.0037
**Input Features (start_time):** sel=0.0037, total_cost=148607.2900

**Output:** predicted_startup_time=11.34, predicted_total_time=734.19

### Step 2: Node 31226 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=4128.0000, plan_width=30.0000, sel=0.0010
**Input Features (start_time):** sel=0.0010, total_cost=7669.6700

**Output:** predicted_startup_time=0.46, predicted_total_time=33.24

### Step 3: Node 31225 (Hash)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt=204.0000, nt1=204.0000, nt2=0.0000, rt1=33.2397, rt2=0.0000, st1=0.4602, st2=0.0000, startup_cost=7669.6700
**Input Features (start_time):** nt=204.0000, nt1=204.0000, nt2=0.0000, rt1=33.2397, rt2=0.0000, st1=0.4602, st2=0.0000, startup_cost=7669.6700

**Output:** predicted_startup_time=18.73, predicted_total_time=18.73

### Step 4: Node 31223 (Hash Join)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=22493.0000, nt2=204.0000, rt1=734.1901, rt2=18.7313, st1=11.3353, st2=18.7300, total_cost=156338.5500
**Input Features (start_time):** nt1=22493.0000, nt2=204.0000, rt1=734.1901, rt2=18.7313, st1=11.3353, st2=18.7300, total_cost=156338.5500

**Output:** predicted_startup_time=59.54, predicted_total_time=862.21

### Step 5: Node 31222 (Aggregate)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=23.0000, nt2=0.0000, rt1=862.2143, rt2=0.0000, st1=59.5366, st2=0.0000
**Input Features (start_time):** nt1=23.0000, nt2=0.0000, rt1=862.2143, rt2=0.0000, st1=59.5366, st2=0.0000

**Output:** predicted_startup_time=957.54, predicted_total_time=989.79

### Step 6: Node 31221 (Gather)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Gather/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Gather/model.pkl

**Input Features (execution_time):** nt1=1.0000, nt2=0.0000, rt1=989.7855, rt2=0.0000, st1=957.5379, st2=0.0000
**Input Features (start_time):** nt1=1.0000, nt2=0.0000, parallel_workers=5.0000, rt1=989.7855, rt2=0.0000, st1=957.5379, st2=0.0000

**Output:** predicted_startup_time=585.84, predicted_total_time=908.17

### Step 7: Node 31220 (Aggregate) - ROOT

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q19/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=5.0000, nt2=0.0000, rt1=908.1697, rt2=0.0000, st1=585.8363, st2=0.0000
**Input Features (start_time):** nt1=5.0000, nt2=0.0000, rt1=908.1697, rt2=0.0000, st1=585.8363, st2=0.0000

**Output:** predicted_startup_time=965.29, predicted_total_time=956.81

## Prediction Results

| Node | Type | Pred Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |
|------|------|-----------|-----------|-----------|---------|---------|------------|------------|
| 31224 | Seq Scan | model | 0.67 | 742.41 | 11.34 | 734.19 | 1602.0 | 1.1 |
| 31226 | Seq Scan | model | 14.57 | 47.75 | 0.46 | 33.24 | 96.8 | 30.4 |
| 31225 | Hash | model | 47.84 | 47.84 | 18.73 | 18.73 | 60.8 | 60.8 |
| 31223 | Hash Join | model | 107.85 | 792.36 | 59.54 | 862.21 | 44.8 | 8.8 |
| 31222 | Aggregate | model | 792.42 | 792.42 | 957.54 | 989.79 | 20.8 | 24.9 |
| 31221 | Gather | model | 804.50 | 810.86 | 585.84 | 908.17 | 27.2 | 12.0 |
| 31220 | Aggregate | model | 805.47 | 810.87 | 965.29 | 956.81 | 19.8 | 18.0 |
