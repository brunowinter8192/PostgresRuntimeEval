# Datasets Module Documentation

## Directory Structure

```
Datasets/
├── 01_Split_Train_Test.py          # Stratified train/test split by template
├── DOCS.md                          # This file
└── Baseline/                        # [outputs]
    ├── training_data.csv            # Training set (120 samples/template)
    └── test_data.csv                # Test set (30 samples/template)
```

## Purpose

Prepare stratified train/test splits from the complete dataset generated in the Data_Generation phase. The split maintains template distribution to ensure representative sampling across all TPC-H query templates.

## Script Documentation

---

### 01 - Split_Train_Test.py

**Purpose**: Split complete dataset into training and test sets with stratification by template

**Workflow**:
1. Load complete dataset from Data_Generation output
2. Validate that each template has exactly 150 samples (120 + 30)
3. For each template:
   - Shuffle samples with fixed random seed
   - Take first 120 samples for training
   - Take next 30 samples for test
4. Concatenate all template splits
5. Export training and test sets to CSV

**Split Strategy**:
- **Per Template**: 120 training / 30 test samples
- **Overall Ratio**: 80% training / 20% test
- **Stratification**: By template ID (ensures all templates represented equally)
- **Random Seed**: 42 (for reproducibility)

**Rationale**:
- Template-based stratification ensures model sees all query patterns during training
- 80/20 split provides sufficient training data while maintaining robust test set
- Fixed seed allows reproducible experiments across different model architectures

**Inputs**:
- `../Data_Generation/csv/complete_dataset.csv` (semicolon-delimited)
- 2,850 samples total (150 per template for 19 TPC-H templates)

**Outputs**:
- `Baseline/training_data.csv` - 2,280 samples (120 × 19 templates), semicolon-delimited
- `Baseline/test_data.csv` - 570 samples (30 × 19 templates), semicolon-delimited

**Output Format**:
- **Delimiter**: Semicolon (`;`) for consistency with Data_Generation and Runtime_Prediction scripts
- **Columns**: Same as input (53 columns: 3 metadata + 50 features)
- **Order**: Grouped by template, shuffled within template

**Usage**:
```bash
# Default usage (uses ../Data_Generation/csv/complete_dataset.csv)
python 01_Split_Train_Test.py

# Custom input file
python 01_Split_Train_Test.py /path/to/custom_dataset.csv

# Custom output directory
python 01_Split_Train_Test.py --output-dir CustomSplit

# Custom split ratio (e.g., 100 train / 50 test per template)
python 01_Split_Train_Test.py --train-size 100 --test-size 50

# Custom random seed
python 01_Split_Train_Test.py --seed 123
```

**Arguments**:
- `input_csv` (positional, optional): Path to input CSV file (default: `../Data_Generation/csv/complete_dataset.csv`)
- `--output-dir`: Output directory for train/test files (default: `Baseline`)
- `--train-size`: Number of training samples per template (default: 120)
- `--test-size`: Number of test samples per template (default: 30)
- `--seed`: Random seed for reproducibility (default: 42)

**Validation**:
- Checks that each template has expected number of samples (train_size + test_size)
- Reports sample counts per template
- Verifies successful split and file creation

**Output Example**:
```
Loading dataset from: ../Data_Generation/csv/complete_dataset.csv
Total samples: 2850
Total features: 50
Templates: ['Q1', 'Q2', 'Q3', ..., 'Q19']

Template sample counts:
  ✓ Q1: 150 samples
  ✓ Q2: 150 samples
  ...
  ✓ Q19: 150 samples

✓ All templates have exactly 150 samples

Splitting dataset (120/30 per template, seed=42):
  Template Q1: 120 train, 30 test
  Template Q2: 120 train, 30 test
  ...
  Template Q19: 120 train, 30 test

✓ Training data saved: Baseline/training_data.csv (2280 samples)
✓ Test data saved: Baseline/test_data.csv (570 samples)

Split ratio: 80.0% train / 20.0% test
Templates in training set: 19
Templates in test set: 19
```

---

## Baseline Dataset Philosophy

The Baseline dataset represents the starting point for all model experiments:
- **Full feature set**: All 50 extracted features without modifications
- **No preprocessing**: Raw features as extracted from PostgreSQL EXPLAIN output
- **Standard split**: 80/20 train/test ratio with template stratification

This baseline serves as the foundation for:
- Forward feature selection (reducing from 50 features to optimal subset)
- Model comparison (SVM, Random Forest, XGBoost)
- Baseline performance benchmarking

For alternative dataset configurations (feature engineering, different splits, etc.), create new subdirectories alongside `Baseline/`.
