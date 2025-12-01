# Check Mapping

Analyze mapping_config.py usage across all scripts in a workflow directory.

**Target:** $ARGUMENTS (directory containing mapping_config.py)

## Workflow

### Phase 1: Analyse

1. Read mapping_config.py in target directory
2. Extract all mapping values (strings, lists of strings)
3. Find all Python scripts in target directory (recursive)
4. For each script:
   a. Identify imports from mapping_config
   b. Scan for hardcoded string values that match mapping values

### Phase 2: Questions

Ask user clarifying questions about:
- Unclear mapping purposes
- Ambiguous usage patterns

### Phase 3: Assessment

Present findings to user:

**A. Current Mapping Usage**

| Mapping | Scripts Using It |
|---------|------------------|
| ... | ... |

**B. Unused Mappings**

Mappings defined but never imported by any script.

**C. Mapping Chains**

Mappings that only exist to build other mappings (no direct external use).
Rule: MAPPING -> DIRECT USE, not MAPPING_A -> MAPPING_B -> MAPPING_C

**D. Hardcoded Values**

Values that appear hardcoded in multiple scripts but could use existing mappings.

**E. Inkonsistenzen**

Scripts that hardcode values which ARE defined in mapping_config but don't import them.

### Phase 4: Recommendation

Present concrete recommendations:
- Mappings to remove (unused or chain-only)
- Scripts to fix (should use existing mappings)
- New mappings to add (if hardcoded values appear in 2+ scripts)

### Phase 5: User Confirmation

Wait for explicit user confirmation before any changes.

### Phase 6: Implementation

If approved:
1. Remove unused mappings from mapping_config.py
2. Update scripts to use existing mappings
3. Add new mappings if requested

### Phase 7: Report

Present final report:
- Mappings removed
- Mappings added
- Scripts updated

## Principle

**Mapping nur wenn:**
1. Direkt von Script importiert UND genutzt
2. In 2+ Scripts verwendet (sonst hardcoden)
3. Keine Ketten - flache Struktur
