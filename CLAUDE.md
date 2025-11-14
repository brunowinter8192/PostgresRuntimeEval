# CLAUDE.MD - Thesis Project Engineering Reference

## 1. PROJECT IDENTITY

**Research Domain:** ML-based runtime prediction for SQL queries
**Benchmark:** TPC-H queries on PostgreSQL
**Methodology:** Exploration and evaluation of various ML approaches
**Pipeline:** Dataset → Feature Selection → Model Training → Prediction → Evaluation

**Critical Constraint:** Large, mature codebase requiring focused, session-based navigation with strict context management.

**Hierarchy:**
- User + Claude Desktop → Meta-level, review, decisions
- Claude Code → Code implementation
- Subagents → Specialized tasks

---

## 2. COLLABORATION PROTOCOL

### Context Management (RAG Approach)

- NO persistent working memory - context rebuilt per session
- On-demand information retrieval via code exploration
- User defines scope at session start
- Meta-level understanding > exhaustive codebase knowledge

---

## 3. CRITICAL STANDARDS

- ❌ NO console outputs (print, console.log, echo)
- ❌ NO logging statements (logger.info, logging.debug)
- ❌ NO inline comments (only functions + section markers)
- ❌ NO test files by default (only when requested)
- ❌ NO emotes
- ❌ NO hardcoded paths (always use argparse)

**Fail-Fast:** Let exceptions fly. No try-catch unless handling adds business value.

### PRE-EDIT CHECKLIST

Before ANY code change:
1. How does this connect? (callers, callees, data flow)
2. How will changes affect others? (impacts, side effects)
3. Is integration guaranteed? (types, flow)
4. Do you understand WHY? (problem, approach, trade-offs)

**If uncertain → ASK.**

---

## 4. THESIS-SPECIFIC RULES

### CSV Files

- ALL CSV files MUST use semicolon `;` as delimiter, never comma
- Excel on macOS requires semicolon to parse correctly
- When generating: use `delimiter=';'` in csv.writer() or `sep=';'` in pd.to_csv()
- Fix tool: `/Users/brunowinter2000/Documents/Thesis/2025_2026/convert_csv_delimiter.py`
- Usage: `python3 convert_csv_delimiter.py <csv_file>` (in-place conversion)

### Script Output Rules

- Output ONLY: .md or .csv exports
- Export location: Dedicated folder in same directory as script
- Folder naming: Descriptive (e.g., `md/`, `csv/`, `analysis/`, `execution_time/`, `start_time/`, `predictions/`)
- Scripts run **silently** - no prints, no logging
- User manually orchestrates module execution in correct order

### Module Architecture

- Modules are standalone - NO workflow.py
- No automatic cross-module orchestration
- Each module: Fixed Input (argparse) → Processing → Fixed Output (export folder)

---

## 5. CODE ORGANIZATION

Every script: **INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS**

```python
# INFRASTRUCTURE
import pandas as pd
from pathlib import Path
import argparse

BATCH_SIZE = 100
OUTPUT_FOLDER = "csv"

# ORCHESTRATOR
def process_workflow(input_file: str, output_dir: str) -> None:
    raw = load_data(input_file)
    cleaned = clean_data(raw)
    results = analyze_data(cleaned)
    export_results(results, output_dir)

# FUNCTIONS

# Load raw data from CSV with semicolon delimiter
def load_data(input_file: str) -> pd.DataFrame:
    return pd.read_csv(input_file, delimiter=';')

# Remove invalid rows and null values
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

# Calculate statistics grouped by category
def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('category').agg({'value': 'mean'})

# Save results to CSV with semicolon delimiter
def export_results(results: pd.DataFrame, output_dir: str) -> None:
    Path(output_dir).mkdir(exist_ok=True)
    results.to_csv(f'{output_dir}/results.csv', sep=';', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to input CSV")
    parser.add_argument("--output-dir", default="./csv", help="Output directory")
    parser.add_argument("--param", type=int, default=5, help="Parameter")
    args = parser.parse_args()

    process_workflow(args.input_file, args.output_dir)
```

**INFRASTRUCTURE:** Imports, constants, argparse. NO functions.
**ORCHESTRATOR:** ONE function. Calls only. ZERO logic.
**FUNCTIONS:** Ordered by call sequence. One responsibility each.

### Comment Rules

**Section Markers:**
```python
# INFRASTRUCTURE
# ORCHESTRATOR
# FUNCTIONS
```

**Function Descriptions:**
```python
# Load validated customer data from CSV
def load_customer_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=';')
```

Describe WHAT, never HOW. No inline comments.

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

## 6. ARCHITECTURE STANDARDS

### Naming Conventions

**Scripts:** `NN_Two_Words.py`
- `NN`: Workflow position (01-99)
- `Two_Words`: Max 2 words, capitals
- Examples: `01_Process_Data.py`, `05_Extract_Features.py`, `07_Merge_Data.py`

**Directories:** `Capital_Words/`
- Capital first letters, underscores between words
- Examples: `Data_Generation/`, `Raw_Data/`, `Runtime_Prediction/`

**Output Files:** `NN_descriptive_name.ext`
- Use same `NN` prefix as the script that generates them
- Timestamp for multiple runs: `NN_name_{timestamp}.ext`
- Examples: `05_features_20251102_135531.csv`, `07_operator_dataset_20251102_140747.csv`

**Rationale:** Immediate visual connection between script and its outputs

### Shared Infrastructure (config.py)

**Include:**
- Configuration helpers
- Utility functions
- Shared constants
- Functions used by 2+ scripts

**Exclude:**
- Business logic
- Script-specific functions
- Orchestration logic

### Import Pattern

**Root-level scripts:**
```python
# From config.py: Build DB configuration from parameters
from config import get_db_config

# From mapping_config.py: Get operator feature column names
from mapping_config import get_operator_features
```

**Subdirectory scripts:**
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# From config.py: Build DB configuration from parameters
from config import get_db_config
```

**CRITICAL:** ALL cross-module imports MUST have comments explaining WHAT the imported function does.

Format: `# From <module>.py: <what it does>`

### README Structure

**Five Required Sections:**

1. **Directory Structure**
   - 2-3 directory levels with inline comments
   - Show output folders, NOT generated files (use `[outputs]` placeholder)
   - config.py: Brief description + "Used by: [scripts]"

2. **Documentation Files**
   - One subsection per .md file (except README)
   - Brief description + list key topics

3. **Shared Infrastructure (config.py)**
   - Document configuration flags
   - List all functions with brief descriptions
   - List all constants with their purpose
   - Show which scripts import from config.py

4. **Workflow Execution Order**
   - Numbered list with script paths
   - Inline purpose comment
   - Mark optional vs required

5. **Script Documentation**
   - Purpose: One sentence
   - Input: Positional arguments
   - Variables: Script-specific argparse flags (exclude config flags)
   - Output: Files with format and columns
   - Important Notes: Critical information

### Folder Structure

```
Project/
├── config.py           # Shared infrastructure
├── debug/              # ALL test files (test_*.py, debug_*.py)
├── todo/               # Implementation TODOs
└── logs/               # Runtime logs (optional)
```

### Common Patterns

**Orchestrator Pattern:**
```python
def main_workflow(input_path, output_dir, config):
    data = load_data(input_path)
    processed = process_step1(data, config)
    results = process_step2(processed)
    export_results(results, output_dir)
```

**Rules:**
- ONE orchestrator per script
- ZERO business logic
- Only function calls
- No transformations

**CSV Export Pattern:**
```python
def export_to_csv(data, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = output_path / f'data_{timestamp}.csv'

    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
        writer.writeheader()
        writer.writerows(data)
```

**Rules:**
- Semicolon delimiter (`;`)
- Create directory if needed
- Timestamp in filename
- `newline=''` with csv module

**Function Ordering:**
```python
# ORCHESTRATOR
def main_workflow(input, output):
    data = load_data(input)        # First
    cleaned = clean_data(data)     # Second
    results = analyze_data(cleaned) # Third
    export_results(results, output) # Fourth

# FUNCTIONS

# Load data from input
def load_data(input_path):
    pass

# Clean loaded data
def clean_data(data):
    pass

# Analyze cleaned data
def analyze_data(cleaned):
    pass

# Export results
def export_results(results, output_dir):
    pass
```

Order by call sequence in orchestrator.

---
