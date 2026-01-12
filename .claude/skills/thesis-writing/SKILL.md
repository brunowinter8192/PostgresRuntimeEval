---
name: thesis-writing
description: Thesis prose style guide and rules. (project)
---

# Writing Skill

## Overview

Style guide for academic prose. Contains rules, prohibitions, and terminology standards.

**Language is German** - examples remain in German as they demonstrate correct German academic writing.

**On skill activation:**
1. Ask user for the Write File path (e.g., `/Users/.../Text/writing.md`)
2. ALL writing happens ONLY in this file
3. Never write thesis prose anywhere else

---

## Workflow (Loop-Based)

**Skill activation → always in one of 3 phases:**

📋 **PLAN (iterative)**
- Ask for Write File path on first activation
- Clarify context
- Write bullet points in Plan File (what to discuss)
- Always ask for Remarks
- Iterate until content is clear

✍️ **IMPLEMENT**
- Write prose in Write File
- Ask for Remarks at the end
- Ad-hoc changes directly in file

🧹 **CLEANUP**
- Clean up Plan File (remove completed items)
- Ask "New cycle?" → back to PLAN for next topic

**Rule:** In EVERY response show current phase with emoji: 📋 PLAN, ✍️ IMPLEMENT, or 🧹 CLEANUP

---

## Style Guide

### Academic Prose Standards

- Short, clear sentences (max 1.5 lines)
- Passive voice common ("wurde bestätigt", "wurden widerlegt")
- English technical terms standalone (Feature Pool, Feature Set, Operators)
- Formal register, no colloquialisms
- Technical details embedded in flowing prose (not bullet lists)

**No colloquialisms - transform to academic:**
- "helfen" → "den MRE reduzieren" / "die Vorhersagegenauigkeit verbessern"
- "besser" → "niedrigere Fehlerrate" / "geringerer MRE"
- "funktioniert" → "erzielt signifikant bessere Ergebnisse"
- "das Pattern matched" → "das Pattern wird dem Subtree zugewiesen"

### Tense Rules

| Section | Tense | Example |
|---------|-------|---------|
| Introduction | Present | "Diese Arbeit untersucht..." |
| Methods | Past | "Es wurden Modelle trainiert..." |
| Results | Past | "Die Analyse zeigte..." |
| Discussion | Mix | Results past, conclusions present |
| Citing sources | Present | "Akdere und Çetintemel (2011) zeigen..." |

**General rule:**
- Present: What the thesis does, general truths, citing other authors
- Past: What was concretely done/measured (methods, results)

---

## CRITICAL WORDING

Check EVERY sentence against these rules.

### Punctuation & Formatting

**1. No colons as sentence connectors**
- WRONG: "Die Schlussfolgerung ist zweischneidig: Einerseits..."
- WRONG: "Der Grund: Die Features..."
- RIGHT: "Die Schlussfolgerung ist zweischneidig. Einerseits..."
- RIGHT: "Der Grund ist, dass die Features..."

**2. No hyphen after parenthesis**
- WRONG: "... - die Optimizer-Costs"
- RIGHT: "... . Die Optimizer-Costs"

**3. No long parenthetical explanations**
- WRONG: "(8 Basis-Features plus Operator-Zähler)"
- RIGHT: Separate sentence or reformulate

**4. No bold in thesis prose**
- WRONG: "**Warum funktioniert das?**", "**Kernfragen**"
- RIGHT: Use `##` headers or `*italic*` for emphasis

### Language

**5. English words in German text**

a) **Capitalization:** English nouns are capitalized (German grammar applies)
   - RIGHT: "die Prediction", "das Pattern", "die Query"

b) **English compounds:** Separated, NEVER hyphenated
   - WRONG: "Pattern-Selection", "Length-First", "Hash-Join"
   - RIGHT: "Pattern Selection", "Length First", "Hash Join"

c) **English-German:** NEVER mix (neither hyphen nor compound)
   - WRONG: "Prediction-Methode", "Workloadwechsel", "Querystruktur"
   - RIGHT: Komplett Englisch ODER komplett Deutsch umformulieren
   - RIGHT: "den veränderten Workload", "die Struktur der Query"

d) **German compounds:** Hyphen only when it sounds bad otherwise
   - Normal: "Datensatzstruktur", "Vorhersagemethode" (zusammen)
   - Selten: Bindestrich nur bei Lesbarkeit

**6. Always use proper umlauts**
- WRONG: "fuehren", "wuerde", "aendern", "Ueberblick"
- RIGHT: "führen", "würde", "ändern", "Überblick"
- Rule: ä ö ü ß - never ae oe ue ss substitutes

**7. No first person pronouns**
- WRONG: "wir haben zwei Variablen", "Ich analysiere"
- RIGHT: "es liegen zwei Variablen vor", "die Analyse zeigt"
- Rule: Use passive voice or impersonal constructions

**8. No "adressieren" in any form**
- WRONG: "adressiert", "adressieren", "adressierte"
- RIGHT: "behandelt", "behebt", "löst", "zielt auf"
- Rule: Always replace with context-appropriate German verb

### Content

**9. No academic fillers**
- WRONG: "Zu beachten ist", "Es ist zu beachten"
- RIGHT: Formulate directly

**10. No text-comparison tables**
- Tables with numeric data (MRE values, counts) → OK
- Tables with text comparisons (Aspekt/Status, Ja/Nein, Beschreibung) → WRONG

WRONG:
```
| Aspekt | Paper | Diese Arbeit | Status |
|--------|-------|--------------|--------|
| FFS    | Ja    | Ja           | Bestätigt |
```

RIGHT: "FFS wurde bestätigt. Sowohl das Paper als auch diese Arbeit setzen FFS erfolgreich ein."

Rule: If a table cell contains prose/categories instead of numbers, convert to sentences.

**11. No bullet points in thesis prose**
- WRONG: `- Item`
- RIGHT: Numbered lists (`1.`, `2.`, `3.`) or flowing prose
- Rule: Avoid bullet points, numbering is acceptable (per guidelines)

**12. No code snippets in thesis**
- WRONG: `df_sorted = df.sort_values(...)` or `if len(pattern_assignments) == 1:`
- RIGHT: Explain algorithms in prose or numbered steps
- Allowed: References to .py files in parentheses, e.g., `(tree.py:158-161)`
- Rule: Code stays in repo, thesis explains what the code does

**13. No filenames in prose**
- WRONG: "Die Details lassen sich in `01_Feature_Selection.py` nachvollziehen."
- RIGHT: "Die Details lassen sich in der Feature Selection nachvollziehen.¹"
- Rule: Filenames belong in footnotes, not in thesis text. Use descriptive German text instead.

---

## Citations

### Two Systems

| Type | Format | Example |
|------|--------|---------|
| **Literature** (external sources) | In-text citation | Akdere und Çetintemel (2011, Abschnitt 3.4) |
| **Repository** (own code/output) | Footnote with relative path | ¹ |

### Literature Citations

**3 Variants:**

1. **General reference (whole work, no section):**
   `Akdere und Çetintemel (2011) begegnen diesen Fragen...`

2. **Integrated with section (author = subject):**
   `Akdere und Çetintemel (2011, Abschnitt 3.4) schlagen drei Strategien vor.`

3. **Separate note (after statement, NO comma after author!):**
   `Diese Definition folgt dem Paper (Akdere und Çetintemel 2011, Abschnitt 3.2).`

**Comma rule:**
- Integrated (Variant 1+2): `Author (Year, Section)` ← comma before section
- Separate (Variant 3): `(Author Year, Section)` ← NO comma after author!

**"Das Paper" in text:**
- OK when citation follows at sentence end
- Otherwise use inline citation

**Short citations:**

| Source | Integrated | Separate (no comma after author!) |
|--------|------------|----------------------------------|
| Paper | Akdere und Çetintemel (2011) | (Akdere und Çetintemel 2011, Abschnitt X.X) |
| TPC-H Spec | TPC (2022) | (TPC 2022, S. X) |
| PostgreSQL Docs | PostgreSQL (2025) | (PostgreSQL 2025, S. X) |
| GitHub Repo | — | Footnotes only |

**Note:** Paper PDF has no page numbers → use section references ("Abschnitt X.X")

### Repository References (Footnotes)

Footnotes for scripts, CSVs, PNGs from the repository.

**In text:**
```
Das Script trainiert die Modelle.¹
```

**In footnote:**
```
¹ Hybrid_2/Runtime_Prediction/02_Train.py
```

**Path format:** Relative from repo root, e.g.:
- `Hybrid_2/Runtime_Prediction/02_Train.py`
- `Hybrid_2/Dataset/Operators/Training_Training/`
- `Prediction_Methods/Dynamic/Runtime_Prediction/A_01a_overview.png`

### Appendix

Appendix files live in repo as `.md` files and get copy-pasted into Word.

**Different rules than main text:**

| Aspect | Main Text | Appendix |
|--------|-----------|----------|
| Repo references | Footnotes | Inline `*Bezug:*` paths |
| Formatting | — | `*kursiv*` only (no `**fett**`) |

**Rationale:** Appendix = technical reference documentation, read alongside open repo. Footnotes would reduce readability.

**Source reference:** Single footnote at appendix title pointing to source file:
```
# Anhang A: Technisches Setup¹

---
¹ Misc/Setup/A_Setup.md.
```

**MD preparation:** Convert `**text**` → `*text*` before Word import (Richtlinien 3.8.2: no bold in Fließtext).

---

## Word Formatting

### Code Blocks (Appendix)

- Font: Courier New
- Size: 10pt
- Optional: light gray background

### Figures (Richtlinien 3.6)

**Structure:**
- Figure centered
- Title + number **below** figure: `Abbildung 3.1: Beschreibung`
- Source **below** title: `Quelle: Eigene Darstellung.¹⁹`
- Numbering: `Abbildung {Kapitel}.{Zähler}` (independent from tables)

**Formatting (all centered):**
- Font: Times, 10pt, italic
- Title: `Abbildung 3.1: Beschreibender Titel`
- Source: `Quelle: Eigene Darstellung.` + footnote

**Requirements:**
- Every figure must be mentioned in text before it appears
- Reference: "siehe Abbildung 3.1" or "Abbildung 3.1 zeigt..."

**Example in Word:**

[PNG centered]

*Abbildung 3.1: MRE pro Template bei Plan-Level Modellierung*

*Quelle: Eigene Darstellung.*¹⁹

**Note:** Footnote ¹⁹ points to repo PNG path.

---

### Tables (Richtlinien 3.6)

**Structure:**
- Title + number **above** table: `Tabelle 3.1: Beschreibung`
- Source **below** table: `Quelle: Eigene Darstellung.²⁰`
- Numbering: `Tabelle {Kapitel}.{Zähler}` (independent from figures)

**Formatting (all centered):**
- Font: Times, 10pt, italic
- Title: `Tabelle 3.1: Beschreibender Titel`
- Source: `Quelle: Eigene Darstellung.` + footnote

**Requirements:**
- Every table must be mentioned and explained in text
- Place table in immediate proximity to text reference

**Difference to Figures:**
- Figures: Title **below**
- Tables: Title **above**

**Example in Word:**

*Tabelle 3.1: MRE der Templates mit der schlechtesten Performance*

| Rank | Template | Mean Actual | Mean Predicted | MRE   |
|------|----------|-------------|----------------|-------|
| 1    | Q18      | 3163ms      | 1590ms         | 49.7% |
| 2    | Q11      | 211ms       | 241ms          | 14.2% |
| 3    | Q16      | 200ms       | 227ms          | 13.7% |

*Quelle: Eigene Darstellung.*²⁰

**Note:** Footnote ²⁰ points to repo CSV path.

---

## Sources

Internet sources managed in Word bibliography.

### Word Formatting

- Alphabetical by surname
- Hanging indent: Paragraph → Special indent → Hanging, 1.25 cm

---

## Terminology

Consistent terms throughout the thesis. List is iteratively extended.

| Correct | Meaning | Source | Forbidden |
|---------|---------|--------|-----------|
| Modellierungsansatz | Modeling approach (Plan-Level, Operator-Level, Hybrid) | Paper: "modeling approach" | Vorhersagemethode, Methode, Ansatz |
| Methoden | Overarching procedures | Paper | Methodiken, Vorgehensweisen |
| MRE | Mean Relative Error | Paper | |
| Prediction | Forecast/prediction | User | Vorhersage |
| Query | Database query | User | Abfrage, Datenbankabfrage |
| Optimizer Cost Model | Cost-based prediction model of the optimizer | (Akdere und Çetintemel, 2011) | |
| Tech-Stack | Technology stack (hardware, software, config) | User | |
| Pattern Selection | Selection of patterns for model training | User | Greedy Pattern Selection |
| Plan | Tree structure of Nodes/Operators | Thesis 3.1 | Planbaum |
| Frequency | Anzahl Vorkommen eines Patterns in Trainingsdaten | User | Occurrence |
