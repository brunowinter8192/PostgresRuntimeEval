# Datasets Module Documentation

## Shared Infrastructure

### Parent mapping_config.py
- `FEATURES_TO_REMOVE_FOR_STATE_1`: Columns to drop for State_1 transformation
- `get_state_1_columns()`: Returns ordered column list for State_1 dataset

## Workflow Execution Order

```
01_Split_Train_Test.py -> 02_Create_State_1.py
```

**Dependencies:**
- 01 creates Baseline train/test split
- 02 transforms complete dataset to State_1 format

## Script Documentation

### 01 - Split_Train_Test.py

**Purpose**: Split complete dataset into training and test sets with stratification by template

**Workflow**:
1. Load complete dataset from input CSV
2. Validate each template has expected sample count (train_size + test_size)
3. For each template: shuffle and split into train/test portions
4. Export training and test datasets to output directory

**Inputs**:
- `input_csv` (positional): Path to complete dataset CSV

**Outputs**:
- `{output_dir}/training_data.csv`: Training samples, semicolon-delimited
- `{output_dir}/test_data.csv`: Test samples, semicolon-delimited

**Usage**:
```bash
python 01_Split_Train_Test.py ../Data_Generation/csv/complete_dataset.csv
python 01_Split_Train_Test.py ../Data_Generation/csv/complete_dataset.csv --output-dir Baseline
python 01_Split_Train_Test.py input.csv --train-size 100 --test-size 50 --seed 123
```

**Variables**:
- `--output-dir`: Output directory for train/test files (default: Baseline)
- `--train-size`: Training samples per template (default: 120)
- `--test-size`: Test samples per template (default: 30)
- `--seed`: Random seed for reproducibility (default: 42)

---

### 02 - Create_State_1.py

**Purpose**: Transform complete dataset to State_1 by removing advanced features

**Workflow**:
1. Load baseline complete dataset
2. Remove advanced features defined in FEATURES_TO_REMOVE_FOR_STATE_1
3. Reorder columns to match State_1 structure
4. Export State_1 dataset to output path

**Inputs**:
- `input_csv` (positional): Path to baseline complete dataset

**Outputs**:
- `{output_csv}`: State_1 complete dataset, semicolon-delimited

**Usage**:
```bash
python 02_Create_State_1.py ../Data_Generation/csv/complete_dataset.csv
python 02_Create_State_1.py ../Data_Generation/csv/complete_dataset.csv --output-csv State_1/complete_dataset.csv
```

**Variables**:
- `--output-csv`: Output path for State_1 dataset (default: State_1/complete_dataset.csv)
