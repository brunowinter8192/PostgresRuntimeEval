# CLAUDE.MD - Thesis1 Project Engineering Reference

## 1. PROJECT CONTEXT

**Research Domain:** ML-based runtime prediction for SQL queries
**Benchmark:** TPC-H queries on PostgreSQL

**Base Paper:** "Learning-based Query Performance Modeling and Prediction" (Akdere, Cetintemel, Upfal - Brown University, 2012)
**Paper Source:** `Misc/Learning-based_Query_Performance_Modeling_and_Pred.md`

---

## 2. THESIS-SPECIFIC RULES

### Formatting: Bullet Lists over Tables

**CRITICAL:** User-facing outputs MUST use bullet lists, never tables.

**Applies to:**
- Thesis text (anything the user reads/submits)
- Script outputs (.md exports, evaluation reports)

**Does NOT apply to:**
- README.md, DOCS.md (Claude-facing, tables allowed)
- CLAUDE.md itself (Claude-facing)

**Rationale:** Tables have formatting issues in Word/PDF export. Internal docs stay in markdown viewers where tables render correctly.

**Example:**
```markdown
WRONG (in thesis/outputs):
| Strategy | MRE |
|----------|-----|
| Size | 3.15% |

RIGHT (in thesis/outputs):
- **Size:** 3.15%
- **Frequency:** 3.15%
```

---

### CSV Files

**CRITICAL:** ALL CSV files MUST use semicolon `;` as delimiter, never comma

**Rationale:** Excel on macOS requires semicolon to parse correctly

**Implementation:**
- When reading: `pd.read_csv(file, delimiter=';')` or `csv.reader(f, delimiter=';')`
- When writing: `pd.to_csv(file, sep=';')` or `csv.writer(f, delimiter=';')`

**Fix tool:** External script (not in repo)

---

### Script Output Rules

**Output ONLY:** .md or .csv exports
**Export location:** Flexible `--output-dir` parameter - user decides where output goes
**Script behavior:** Completely silent - no prints, no logging, no verbose output

---

## 3. CODE ORGANIZATION

**CRITICAL:** Every script follows this structure:

**INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS**

### INFRASTRUCTURE
- Imports and constants
- Argparse setup (positional + optional flags)
- NO functions, NO logic

### ORCHESTRATOR
- ONE function calling other functions in sequence
- ZERO functional logic (no calculations, transformations, business rules)
- Meta-logic allowed: conditional workflow execution, parameter routing

### FUNCTIONS
- Ordered by call sequence
- One responsibility each
- Can call other functions internally

**Example:**
```python
# INFRASTRUCTURE
import pandas as pd
from pathlib import Path

# ORCHESTRATOR
def process_workflow(input_file: str, output_dir: str) -> None:
    raw = load_data(input_file)
    cleaned = clean_data(raw)
    export_results(analyze_data(cleaned), output_dir)

# FUNCTIONS
# Load raw data from CSV with semicolon delimiter
def load_data(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')

# Remove invalid rows
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

# Calculate statistics
def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('category').mean()

# Save results to CSV
def export_results(results: pd.DataFrame, output_dir: str) -> None:
    Path(output_dir).mkdir(exist_ok=True)
    results.to_csv(f'{output_dir}/results.csv', sep=';', index=False)
```

### Type Hints

RECOMMENDED but optional. Type annotations in function signatures help IDE catch errors.

### Fail-Fast

Let exceptions fly. No try-catch that silently swallows errors affecting business logic. Script must fail if it cannot fulfill its purpose.

### Argparse Template

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Positional arguments
    parser.add_argument("input", help="Input path")

    # Required flags
    parser.add_argument("--output-dir", required=True, help="Output directory")

    # Optional with defaults
    parser.add_argument("--param", type=int, default=5, help="Parameter")

    args = parser.parse_args()

    main_workflow(Path(args.input), args.output_dir, args.param)
```

---

## 4. COMMENT RULES

**CRITICAL:** Three types of allowed comments only

### 1. Section Markers
`# INFRASTRUCTURE`, `# ORCHESTRATOR`, `# FUNCTIONS`

### 2. Function Header Comments
One line describing WHAT the function does, placed directly above function definition.
```python
# Load validated customer data from CSV
def load_customer_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')
```

### 3. Cross-Module Import Comments
Format: `# From <module>.py: <what it does>`
```python
# From data_loader.py: Load and validate CSV
from data_loader import load_validated_data
```

**CRITICAL:** ALL cross-module imports MUST have comments. NO inline comments inside function bodies.

---

## 5. ARCHITECTURE STANDARDS

### Naming Conventions

**Scripts:** `NN_Two_Words.py`
- `NN`: Workflow position (01-99)
- `Two_Words`: Max 2 words, capitals
- Examples: `01_Process_Data.py`, `05_Extract_Features.py`, `07_Merge_Data.py`

**Parallel Scripts:** `NNx_Two_Words.py`
- Scripts on same level that can run in parallel: `01a`, `01b`, `01c`
- Successor script uses next number: `02` (requires all `01x` outputs)
- Examples: `01a_Runtime_Data.py`, `01b_Plan_Features.py` -> `02_Merge_Data.py`

**Analysis Scripts:** `A_NNx_Two_Words.py`
- Standalone analysis tools, NOT part of main workflow
- `A_` prefix distinguishes from workflow scripts
- Parallel numbering (`A_01a`, `A_01b`) since no dependencies between them
- Examples: `A_01a_Correlation_Analysis.py`, `A_01b_Scatter_Plots.py`

**Directories:** `Capital_Words/`
- Capital first letters, underscores between words
- Examples: `Data_Generation/`, `Raw_Data/`, `Runtime_Prediction/`

**Output Files:** `NN_descriptive_name.ext`
- Use same `NN` prefix as the script that generates them
- use no timestamps, pipeline structure requires overwriting for redundant files
- Examples: `05_features.csv`, `07_operator_dataset.csv`

**Rationale:** Immediate visual connection between script and its outputs

---

### Mapping Configuration Pattern

**Purpose:** Central mapping files (e.g., `mapping_config.py`) define dataset schema, folder naming, and feature sets for consistency.

**Use mapping for block operations** where multiple related values must stay synchronized:
- Folder naming (ensures consistent structure across scripts)
- Feature sets (column names that change together)
- Type definitions (operator types, node categories)

**Example:**
```python
from mapping_config import CHILD_FEATURES_TIMING
df = df.drop(columns=CHILD_FEATURES_TIMING)  # NOT ['st1', 'rt1', 'st2', 'rt2']
```

**Skip mapping for individual column access** where script uses subset of columns:
```python
df_filtered = df[['query_file', 'node_type']]  # Hardcoded is fine
```

**Split maps for semantic differences:**
```python
CHILD_FEATURES_TIMING = ['st1', 'rt1', 'st2', 'rt2']      # Unknown at prediction
CHILD_FEATURES_STRUCTURAL = ['nt1', 'nt2']                # Known at prediction
```

**Principle:** Mapping for coherent blocks, not arbitrary individual accesses.

---

### Subdirectory-Modules

When a module is a directory (e.g., `10_Pattern_Selection/`):

**Structure:**
```
10_Pattern_Selection/
├── DOCS.md                     # Entry-point documentation
├── 10_Pattern_Selection.py     # Entry-point (argparse + orchestrator)
└── src/                        [See DOCS.md](src/DOCS.md)
    ├── tree.py                 # Helper modules
    ├── io.py
    ├── prediction.py
    └── DOCS.md                 # Module-level documentation
```

**Rules:**
- Entry-point script in root: `NN_Module_Name.py`
- Own `DOCS.md` at module root for entry-point documentation
- Helper functions in `src/`
- `src/DOCS.md` for module-level documentation
- Parent DOCS.md references with `[See DOCS.md]` link only

---

## 6. DOCUMENTATION STRUCTURE

### Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Workflow** | README.md level directory containing a complete INDEPENDENT pipeline | `Plan_Level/` |
| **Directory** | Subdirectory within a workflow (a phase) | `Data_Generation/` |
| **Module** | Python script (`.py` file) | `01a_Runtime_Data.py` |
| **Function** | Python function within a module | `load_queries()` |

### Hierarchy

```
Workflow/          -> README.md (tree to directories)
├── Directory_A/   -> DOCS.md (tree to functions)
├── Directory_B/   -> DOCS.md
└── Directory_C/   -> DOCS.md
```

**Principle:** No redundancy - README stops where DOCS begins.

---

### README.md (Workflow-Level)

**Purpose:** High-level overview linking to DOCS.md for details

**Placement:**
- **Location:** Workflow root (e.g., `Hybrid_2/`)
- **Relationship:** One README per workflow
- **Scope:** Tree to directories, links to DOCS.md

**Required Sections:**

#### 1. Title + Description

Workflow name as H1, followed by 1-2 sentence description:

```markdown
# Hybrid_2 - Pattern-Level Prediction

Pattern-based query runtime prediction using greedy pattern selection.
```

#### 2. Directory Structure

Tree showing root-level files AND directories with `[See DOCS.md]` links:

```
Hybrid_2/
    mapping_config.py
    Parameter.md
    README.md
    Data_Generation/                     [See DOCS.md]
    Dataset/                             [See DOCS.md]
    Runtime_Prediction/                  [See DOCS.md]
```

**Rule:** Only root-level files. Scripts inside directories belong in their DOCS.md.

**Root-Level Config Files:** Files like `mapping_config.py` are self-documenting and only listed in Directory Structure. No separate documentation needed - they contain only constants and simple mappings.

#### 3. Workflow

Per phase: Purpose, Input, Output, Details link:

```markdown
## Workflow

### Phase 1: Data_Generation

**Purpose:** Mine structural patterns from query execution plans

**Input:** Operator dataset

**Output:** Pattern definitions with occurrence counts

**Details:** [Data_Generation/DOCS.md](Data_Generation/DOCS.md)
```

---

### DOCS.md (Directory-Level)

**Purpose:** Detailed documentation of all modules within one directory

**Placement:**
- **Location:** Directory root (e.g., `Data_Generation/`)
- **Relationship:** Multiple DOCS can exist under one README
- **Scope:** Tree to modules, script-level documentation

**Required Sections:**

#### 1. Working Directory (CRITICAL)

All commands assume CWD = this directory. Users must cd here before execution.

```markdown
## Working Directory

**CRITICAL:** All commands assume CWD = `Runtime_Prediction/`

bash
cd /path/to/Hybrid_2/Runtime_Prediction
```

#### 2. Directory Structure

Tree showing modules (no functions in tree):

```
Data_Generation/
├── DOCS.md
├── 01a_Runtime_Data.py
├── 01b_Plan_Features.py
└── csv/
```

#### 3. Workflow Dependency Graph (if applicable)

ASCII diagram showing script execution order and dependencies:

```markdown
## Workflow Dependency Graph

02_Operator_Train
       |
       v
04_Query_Prediction
       |
       v
06_Extract_Patterns --> 07_Order_Patterns --> 09_Pretrain
```

#### 4. Output Structure (if applicable)

Tree showing generated outputs (models, CSVs, etc.):

```markdown
## Output Structure

Runtime_Prediction/
├── Model/
│   └── Training_Training/
│       ├── Operator/{target}/{Operator}/model.pkl
│       └── Pattern/{hash}/model_*.pkl
├── Pattern_Selection/
│   └── {Strategy}/selected_patterns.csv
└── Evaluation/
    └── predictions.csv
```

#### 5. Shared Infrastructure (if applicable)

Directory-specific config files with exports.

#### 6. Module Documentation

Per module (`## NN - Module_Name.py`) with Purpose, Inputs, Outputs, Variables, Implementation Details (if applicable):

```markdown
## 02 - Operator_Train.py

**Purpose:** Train SVM models for each operator-target combination

**Inputs:**
- `dataset_dir`: Directory with operator CSV files
- `overview_file`: Path to two_step_evaluation_overview.csv
- `--output-dir`: Output directory for trained models (required)

**Outputs:**
- `{output-dir}/{target}/{Operator}/model.pkl`

**Usage:**
python3 02_Operator_Train.py ../Dataset/Operators/Training_Training overview.csv --output-dir Model/Operator

**Implementation Details:** (if applicable)

Critical algorithm logic, invariants, or non-obvious behavior that affects correctness.
```

**Inputs vs Variables:**

| Type | Argparse | Without it | Example |
|------|----------|------------|---------|
| Input | positional + required flags | workflow FAILS | `dataset_dir`, `--output-dir` |
| Variable | optional flags with default | workflow uses defaults | `--epsilon 0.0`, `--n-jobs -1` |

**Variables Section:** MUST be included if script has optional flags with defaults. Undocumented variables = documentation bug.

```markdown
**Variables:**
- `--epsilon`: Min MRE improvement required (default: 0.0)
- `--n-jobs`: Parallel jobs (default: -1 = all cores)
```

**Source References:** When code or logic is derived from another module, document the source:

```markdown
**Source:** `Hybrid_1/Runtime_Prediction/03_Predict_Queries/src/tree.py`
- `build_pattern_assignments()` - Pattern matching logic
- `compute_pattern_hash()` - Hash computation
```

This makes dependencies explicit and prevents reinventing existing logic.
