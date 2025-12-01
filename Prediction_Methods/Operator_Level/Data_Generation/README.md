### Data_Generation

**Purpose:** Extract operator-level features and runtime targets from TPC-H queries

**Input:** Query directory with Q1-Q22 templates (SQL files)

**Output:** `operator_dataset_{timestamp}.csv` - 18 columns (6 metadata, 10 features, 2 targets)

**Key Scripts:**
- 01a/01b (parallel): Feature + Target extraction
- 02: Merge into final dataset

**Details:** See [Data_Generation/DOCS.md](Data_Generation/DOCS.md)
