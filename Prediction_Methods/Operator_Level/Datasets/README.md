# Datasets Module

Dataset preparation pipeline - transforms raw operator data into training/test splits with child features.

## Input

Raw operator dataset from Data_Generation: `Raw/operator_dataset_*.csv`

## Output

| Output | Script | Purpose |
|--------|--------|---------|
| 01_operator_dataset_cleaned.csv | 01 | Templates Q2/Q11/Q16/Q22 removed |
| 02_operator_dataset_with_children.csv | 02 | st1, rt1, st2, rt2 features added |
| 03_training.csv / 03_test.csv | 03 | 80/20 split by seed ranges |
| 04b_test_cleaned.csv | 04b | Test set without child timing features |
| 04a_{NodeType}/ | 04a | Per-operator training sets (optional) |

## Key Outputs

- **03_training.csv** - Training data (120 seeds/template) with child features
- **04b_test_cleaned.csv** - Test data (30 seeds/template) without child features
- **04a_{NodeType}/** folders - Training data split by operator type (optional)

## Details

See [DOCS.md](DOCS.md)
