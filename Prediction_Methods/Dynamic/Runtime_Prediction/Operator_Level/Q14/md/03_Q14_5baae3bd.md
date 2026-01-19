# Query Prediction Report (Dynamic/LOTO)

**Query:** Q14_100_seed_812199069
**Timestamp:** 2026-01-11 21:34:35

## Input Summary

- **Test File:** Prediction_Methods/Dynamic/Dataset/Dataset_Operator/Q14/test.csv
- **Overview File:** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/SVM/two_step_evaluation_overview.csv
- **Models Directory:** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model

## Query Tree

```
Node 26420 (Aggregate) - ROOT
  Node 26421 (Gather)
    Node 26422 (Aggregate)
      Node 26423 (Hash Join)
        Node 26424 (Seq Scan) - LEAF
        Node 26425 (Hash)
          Node 26426 (Seq Scan) - LEAF
```

## Prediction Chain (Bottom-Up)

### Step 1: Node 26424 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=112600.0000, plan_width=16.0000, sel=0.0026
**Input Features (start_time):** nt=15630.0000, nt1=0.0000, total_cost=130603.6400

**Output:** predicted_startup_time=11.11, predicted_total_time=746.88

### Step 2: Node 26426 (Seq Scan) - LEAF

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Seq_Scan/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Seq_Scan/model.pkl

**Input Features (execution_time):** np=4128.0000, plan_width=25.0000, sel=0.4167
**Input Features (start_time):** nt=83333.0000, nt1=0.0000, total_cost=4961.3300

**Output:** predicted_startup_time=0.16, predicted_total_time=37.30

### Step 3: Node 26425 (Hash)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Hash/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Hash/model.pkl

**Input Features (execution_time):** nt1=83333.0000, nt2=0.0000, rt1=37.2972, rt2=0.0000, st1=0.1558, st2=0.0000, startup_cost=4961.3300, total_cost=4961.3300
**Input Features (start_time):** nt1=83333.0000, nt2=0.0000, rt1=37.2972, rt2=0.0000, st1=0.1558, st2=0.0000, startup_cost=4961.3300, total_cost=4961.3300

**Output:** predicted_startup_time=29.90, predicted_total_time=29.90

### Step 4: Node 26423 (Hash Join)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Hash_Join/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Hash_Join/model.pkl

**Input Features (execution_time):** nt1=15630.0000, nt2=83333.0000, rt1=746.8799, rt2=29.8981, st1=11.1090, st2=29.8981, total_cost=136647.6700
**Input Features (start_time):** nt1=15630.0000, nt2=83333.0000, plan_width=33.0000, rt1=746.8799, rt2=29.8981, st1=11.1090, st2=29.8981, total_cost=136647.6700

**Output:** predicted_startup_time=84.30, predicted_total_time=874.62

### Step 5: Node 26422 (Aggregate)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=15630.0000, nt2=0.0000, rt1=874.6156, rt2=0.0000, st1=84.2962, st2=0.0000
**Input Features (start_time):** nt1=15630.0000, nt2=0.0000, rt1=874.6156, rt2=0.0000, st1=84.2962, st2=0.0000

**Output:** predicted_startup_time=962.19, predicted_total_time=991.96

### Step 6: Node 26421 (Gather)

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Gather/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Gather/model.pkl

**Input Features (execution_time):** nt1=1.0000, nt2=0.0000, rt1=991.9605, rt2=0.0000, st1=962.1927, st2=0.0000
**Input Features (start_time):** nt1=1.0000, nt2=0.0000, rt1=991.9605, rt2=0.0000, st1=962.1927, st2=0.0000, startup_cost=137921.2000

**Output:** predicted_startup_time=634.94, predicted_total_time=917.22

### Step 7: Node 26420 (Aggregate) - ROOT

**Model (execution_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/execution_time/Aggregate/model.pkl
**Model (start_time):** Prediction_Methods/Dynamic/Runtime_Prediction/Operator_Level/Q14/Model/start_time/Aggregate/model.pkl

**Input Features (execution_time):** nt1=5.0000, nt2=0.0000, rt1=917.2152, rt2=0.0000, st1=634.9353, st2=0.0000
**Input Features (start_time):** nt1=5.0000, nt2=0.0000, rt1=917.2152, rt2=0.0000, st1=634.9353, st2=0.0000

**Output:** predicted_startup_time=971.43, predicted_total_time=962.64

## Prediction Results

| Node | Type | Pred Type | Actual ST | Actual RT | Pred ST | Pred RT | MRE ST (%) | MRE RT (%) |
|------|------|-----------|-----------|-----------|---------|---------|------------|------------|
| 26424 | Seq Scan | model | 0.80 | 708.36 | 11.11 | 746.88 | 1290.4 | 5.4 |
| 26426 | Seq Scan | model | 7.44 | 36.95 | 0.16 | 37.30 | 97.9 | 1.0 |
| 26425 | Hash | model | 41.96 | 41.96 | 29.90 | 29.90 | 28.8 | 28.8 |
| 26423 | Hash Join | model | 44.07 | 758.66 | 84.30 | 874.62 | 91.3 | 15.3 |
| 26422 | Aggregate | model | 761.13 | 761.13 | 962.19 | 991.96 | 26.4 | 30.3 |
| 26421 | Gather | model | 774.37 | 783.51 | 634.94 | 917.22 | 18.0 | 17.1 |
| 26420 | Aggregate | model | 774.40 | 783.52 | 971.43 | 962.64 | 25.4 | 22.9 |
