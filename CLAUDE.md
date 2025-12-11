# CLAUDE.MD - Thesis1 Project Engineering Reference

## 1. PROJECT IDENTITY

**Research Domain:** ML-based runtime prediction for SQL queries
**Benchmark:** TPC-H queries on PostgreSQL
**Methodology:** Exploration and evaluation of various ML approaches
**Pipeline:** Dataset → Feature Selection → Model Training → Prediction → Evaluation

**Critical Constraint:** Large, mature codebase requiring focused, session-based navigation with strict context management.

---

## 2. SCIENTIFIC FOUNDATION

**Base Paper:** "Learning-based Query Performance Modeling and Prediction" (Akdere, Cetintemel, Upfal - Brown University, 2012)

**Paper Source:** `Misc/Learning-based_Query_Performance_Modeling_and_Pred.md`

---

## 3. PRIORITY LEVELS

**CRITICAL:** Must follow - violations break the system
**IMPORTANT:** Should follow - violations reduce quality
**RECOMMENDED:** Good practice - improves maintainability

---

## 4. CRITICAL STANDARDS

- NO comments inside function bodies (only function header comments + section markers)
- NO test files in root (ONLY in debug/ folder when requested)
- NO emojis in code AND documentation
- NO hardcoded paths (always use argparse)

**Type hints:** RECOMMENDED but optional

**Fail-Fast:** Let exceptions fly. No try-catch that silently swallows errors affecting business logic. Script must fail if it cannot fulfill its purpose.

**Immediate Stop on Problems:**
- On ANY unexpected problem during execution: STOP IMMEDIATELY
- Inform user with clear problem description
- NEVER autonomously "fix" or implement workarounds
- Wait for explicit user decision before proceeding

**Examples:** NaN values, missing files, unexpected formats, algorithm errors, dependency issues, etc.

**Why:** An autonomous "fix" can invalidate the entire project. Better to ask once too often than once too little.

---

## 5. THESIS-SPECIFIC RULES

### CSV Files

**CRITICAL:** ALL CSV files MUST use semicolon `;` as delimiter, never comma

**Rationale:** Excel on macOS requires semicolon to parse correctly

**Implementation:**
- When reading: `pd.read_csv(file, delimiter=';')` or `csv.reader(f, delimiter=';')`
- When writing: `pd.to_csv(file, sep=';')` or `csv.writer(f, delimiter=';')`

**Fix tool:** `/Users/brunowinter2000/Documents/Thesis/2025_2026/convert_csv_delimiter.py`
**Usage:** `python3 convert_csv_delimiter.py <csv_file>` (in-place conversion)

---

### Script Output Rules

**Output ONLY:** .md or .csv exports
**Export location:** Flexibler `--output-dir` Parameter - User entscheidet wo Output landet
**Script behavior:** Completely silent - no prints, no logging, no verbose output

---

### Module Architecture

**Standalone modules:**
- Each module: Fixed Input (argparse) → Processing → Fixed Output (export folder)
- NO automatic cross-module orchestration
- User orchestrates execution manually

---

## 6. CODE ORGANIZATION

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

---

## 7. COMMENT RULES

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

## 8. ARGPARSE TEMPLATE

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

## 9. ARCHITECTURE STANDARDS

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
- Timestamp for multiple runs: `NN_name_{timestamp}.ext`
- Examples: `05_features_20251102_135531.csv`, `07_operator_dataset_20251102_140747.csv`

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

## 10. DOCUMENTATION STRUCTURE

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

**Purpose:** High-level overview of multi-phase workflow orchestration

**Placement:**
- **Location:** Workflow root (e.g., `Plan_Level_1/`)
- **Relationship:** One README per workflow
- **Scope:** Tree to directories only, links to DOCS.md

**Required Sections:**

#### 1. Directory Structure

Tree showing only directories with `[See DOCS.md]` references:

```
Plan_Level_1/
├── README.md                            # This file
├── mapping_config.py                    # Shared configuration
├── Data_Generation/                     [See DOCS.md]
├── Datasets/                            [See DOCS.md]
└── Runtime_Prediction/                  [See DOCS.md]
```

**Rule:** No `.py` files, no subdirectories - only top-level directories with DOCS links.

#### 2. Shared Infrastructure

Config files with bullet list of exports:

```markdown
**mapping_config.py:**
- `DB_CONFIG`: PostgreSQL connection parameters
- `OPERATOR_TYPES`: 13 plan operator types
- `PLAN_METADATA`: ['query_file', 'template']
```

#### 3. Workflow Overview

Phase dependencies as flow diagram:

```
Phase 1: Data_Generation
Phase 2: Datasets
Phase 3: Runtime_Prediction

Data_Generation -> Datasets -> Runtime_Prediction
```

#### 4. Phase Documentation

Per phase: Purpose, Input, Output, Details link:

```markdown
### Phase 1: Data_Generation

**Purpose:** Extract features and measure runtime for TPC-H queries

**Input:** Query directory with SQL files

**Output:** `complete_dataset.csv`

**Details:** [Data_Generation/DOCS.md](Data_Generation/DOCS.md)
```

---

### DOCS.md (Directory-Level)

**Purpose:** Detailed documentation of all modules within one directory

**Placement:**
- **Location:** Directory root (e.g., `Data_Generation/`)
- **Relationship:** Multiple DOCS can exist under one README
- **Scope:** Tree to modules, every function documented in Module Documentation

**Required Sections:**

#### 1. Directory Structure

Tree showing modules (no functions in tree):

```
Data_Generation/
├── DOCS.md
├── 01a_Runtime_Data.py
├── 01b_Plan_Features.py
└── csv/
```

#### 2. Shared Infrastructure (if applicable)

Directory-specific config files with exports.

#### 3. Module Documentation

Per module (`## module_name.py`) with Purpose, Input, Output, then all functions (`### function_name()`):

```markdown
## 01a_Runtime_Data.py
**Purpose:** Measure query execution time with cold cache
**Input:** Query directory path
**Output:** CSV with runtime measurements

### process_workflow()
Orchestrator function that coordinates the full measurement pipeline.
Calls load_queries, iterates through queries calling execute_query and
measure_runtime for each, then exports all results.

### load_queries()
Loads all SQL files from the specified directory. Returns list of
query file paths sorted alphabetically.

### execute_query()
Executes a single SQL query against PostgreSQL with cold cache.
Clears shared buffers before execution to ensure consistent measurements.

### export_results()
Saves runtime measurements to CSV with semicolon delimiter.
Creates output directory if it does not exist.
```

**Rule:** Every function in the module must be documented. Undocumented functions indicate dead code or outdated docs.
- timestamp fix