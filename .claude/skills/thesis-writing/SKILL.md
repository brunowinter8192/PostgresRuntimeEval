---
name: thesis-writing
description: Thesis prose style guide and rules. (project)
---

# Writing Skill

## Overview

Style guide for academic prose. Contains rules, prohibitions, and terminology standards.

**Language is German** - examples remain in German as they demonstrate correct German academic writing.

---

## Workflow (Loop-Based)

**Skill activation → always in one of 2 phases:**

📋 **PLAN (iterative)**
- Clarify context
- **Write prose ARTEFACT** - never show prose in chat response
- Footnotes: Write as (F) - user handles numbering

**3 Checkpoints (address all in every iteration):**

1. **Spelling**
   - Orthography and grammar
   - Correct umlauts (ä ö ü ß, never ae oe ue)
   - Punctuation

2. **Wording**
   - Check all rules from CRITICAL WORDING section
   - Style rules (no colloquialisms, passive voice, technical terms)
   - Terminology consistency (see Terminology table)

3. **Logic** (primary checkpoint) — THINK. USE YOUR BRAIN.
   - Every sentence must have meaning - if you can't explain WHY, delete it
   - No empty phrases ("differenziert", "zeigt sich" mean NOTHING without content)
   - Before writing: What is the POINT? What does the reader LEARN?
   - Fact-check against training data and general knowledge
   - Challenge incorrect statements directly
   - Content coherence of argumentation

**Workflow:**
- Always ask for Remarks
- **Active participation:** Be ruthless. Find every weak spot. If it sounds smart but says nothing → call it out. User wants a critical partner, not a yes-man.
- When ready: ExitPlanMode

**Remarks workflow:**
1. List all Remarks (corrections, suggestions, issues)
2. List explicit Questions separately below the Remarks
3. If user responds without addressing specific Remarks → all Remarks are valid → apply all corrections automatically
4. Only Questions require explicit user answers

✍️ **IMPLEMENT**
- After Plan Phase: transfer prose to Artefact
- **Each workflow starts a new Artefact**
- **Ad-hoc mode:** User remarks → immediately apply to Artefact, then ask for next Remarks

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

**MRE terminology:**
- WRONG: "MRE verbessern", "MRE verschlechtern"
- RIGHT: "MRE reduzieren", "MRE erhöhen"
- Rule: MRE is a metric - it goes up or down, not better or worse

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
- RIGHT: Nummerierte Überschriften oder Absatzstruktur

**4b. No informal sub-headers**
- WRONG: "*Template-Unterscheidung durch Features:*" (kursive Zwischenüberschrift)
- WRONG: "A) Erste Analyse" / "B) Zweite Analyse" (Buchstaben-Gliederung)
- RIGHT: Nummerierte Überschriften (3.2.1) ODER nur Absatzstruktur
- Richtlinien: Überschriften müssen nummeriert + fett sein

### Language

**5. English words in German text**

a) **Capitalization:** English nouns are capitalized (German grammar applies)
   - RIGHT: "die Prediction", "das Pattern", "die Query"

b) **English compounds:** Separated, NEVER hyphenated
   - WRONG: "Pattern-Selection", "Length-First", "Hash-Join"
   - RIGHT: "Pattern Selection", "Length First", "Hash Join"

c) **English-German:** NEVER mix (neither hyphen nor compound)
   - WRONG: "Prediction-Methode", "Workloadwechsel", "Querystruktur", "Query-Ebene", "Operator-Ebene"
   - RIGHT: Komplett Englisch ODER komplett Deutsch umformulieren
   - RIGHT: "den veränderten Workload", "die Struktur der Query", "auf Ebene der Queries", "auf Ebene der Operators"

d) **German compounds:** Hyphen only when it sounds bad otherwise
   - Normal: "Datensatzstruktur", "Vorhersagemethode" (zusammen)
   - Selten: Bindestrich nur bei Lesbarkeit

e) **Proper names (folder names, product names):** Keep original, no hyphen
   - RIGHT: "der Dataset Ordner", "das iPhone Update" (separated)
   - Proper names stay unchanged, German noun follows separately

f) **Hyphen avoidance:** German spelling rules apply. If wording already has hyphen → accept. When reworking wording → avoid hyphens by reformulating. Not critical, but prefer hyphen-free.

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

**9. Technical terms → Thesis terms**
- Code-Variablen werden in lesbare Fließtext-Begriffe umgewandelt
- WRONG: "die actual_total_time", "der node_type"
- RIGHT: "die Total Time", "die Art des Operators"
- Rule: Unterstriche entfernen, Wörter kapitalisieren, ggf. übersetzen

### Content

**10. No academic fillers**
- WRONG: "Zu beachten ist", "Es ist zu beachten"
- RIGHT: Formulate directly

**11. No text-comparison tables**
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

**12. No bullet points in thesis prose**
- WRONG: `- Item`
- RIGHT: Numbered lists (`1.`, `2.`, `3.`) or flowing prose
- Rule: Avoid bullet points, numbering is acceptable (per guidelines)

**13. No code snippets in thesis**
- WRONG: `df_sorted = df.sort_values(...)` or `if len(pattern_assignments) == 1:`
- RIGHT: Explain algorithms in prose or numbered steps
- Allowed: References to .py files in parentheses, e.g., `(tree.py:158-161)`
- Rule: Code stays in repo, thesis explains what the code does

**14. No filenames in prose**
- WRONG: "Die Details lassen sich in `01_Feature_Selection.py` nachvollziehen."
- RIGHT: "Die Details lassen sich in der Feature Selection nachvollziehen.¹"
- Rule: Filenames belong in footnotes, not in thesis text. Use descriptive German text instead.

---

# Project specific Rules

*Swap for different project. Project: Thesis_Final*

## Algorithm Description

**Beschreibungsgrad:** Algorithmen werden auf mittlerer Granularität beschrieben - die wesentlichen Schritte, ohne Code-Details.

**Regeln:**
- Keine technischen Variablennamen (st1, rt1, st2, rt2)
- Keine englischen Wörter außer eingeführte Begriffe (Terminologie)
- Keine Redundanz ("Children Map, die Children speichert")
- Implizites weglassen (wenn Child Features ohnehin Teil des Prozesses sind, nicht extra erwähnen)

**Beispiel (Bottom-Up Prediction):**

1. Query Tree aufbauen mit allen Operators der Query
2. Mapping der Kindknoten erstellen
3. Leaf Operators identifizieren
4. Für jeden Leaf Operator das entsprechende Modell laden und Prediction ausführen
5. Für jeden verbleibenden Operator prüfen, ob alle Children bereits predicted wurden
6. Wenn alle Children predicted wurden, deren Predictions als Features extrahieren
7. Modell des Operators laden und Prediction ausführen
8. Schritte 5-7 wiederholen, bis der Root Operator erreicht ist

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

**Reference by content location:**
- Info in paper prose → "Abschnitt X.X"
- Info in table → "Table X" (keep English, paper uses English)
- Info in figure → "Figure X"
- Rule: Reference where the information actually is, not the surrounding section

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

**Chapter headings:** Every new chapter gets a footnote with the relative path to its directory. All further paths within the chapter are relative to this directory. Exception: `Misc/` can be referenced absolutely from repo root.
```
## 4.1 Plan-Level Modeling¹

---
¹ Prediction_Methods/Plan_Level_1
```

**Passive wording for footnote references:** Do not use "Hier" when referencing repo files via footnote - it suggests content follows directly in text.
- WRONG: "Hier beispielhaft die Ausgabe von EXPLAIN..."¹
- RIGHT: "...verschiedene Pläne gewählt werden können, siehe dazu Q9."¹

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
- Every figure must be referenced in text before it appears
- Tables are NOT referenced in preceding text - they follow directly after context

---

### Figure Reference Rules

**NIEMALS:**
1. Caption wiederholen ("Abbildung 3.1 zeigt den MRE pro Template" → Caption: "MRE pro Template")
2. Zahlen vorlesen ("Q18 hat 49.7%, Q11 hat 14.2%...")
3. Analyse vorwegnehmen ("Abbildung 3.1 zeigt, dass Q18 ein Ausreißer ist")

**Überleitung = WARUM, nicht WAS:**
- WRONG: "Abbildung 3.1 zeigt den MRE pro Template."
- RIGHT: "Dieser Wert verdeckt jedoch deutliche Unterschiede, wie Abbildung 3.1 verdeutlicht."

**Abwechslung bei Übergangswörtern:**
Nicht immer "verdeutlicht" oder "zeigt" - variieren:
- veranschaulicht
- illustriert
- belegt
- macht sichtbar
- lässt erkennen
- offenbart

---

### Flow-Patterns

**Pattern A: Bild allein**
```
[Überleitung: WARUM]
[Bild + Caption]
[Interpretation: nur wenn nicht offensichtlich]
```

**Pattern B: Bild → Tabelle (Überblick → Detail)**
```
[Überleitung: WARUM]
[Bild + Caption]
[Tabelle + Caption]  ← keine Überleitung wenn Zusammenhang offensichtlich
[Interpretation]
```

**Pattern C: Tabelle allein**
```
[Überleitung: WARUM]
[Tabelle + Caption]
[Interpretation: nur wenn nicht offensichtlich]
```

---

### Beispiel (Pattern B)

```
Der Overall MRE liegt bei 6.74%. Dieser Wert verdeckt jedoch
deutliche Unterschiede zwischen den Templates, wie Abbildung 3.1
verdeutlicht.

*Abbildung 3.1: MRE pro Template bei Plan-Level Modellierung*
*Quelle: Eigene Darstellung.(F)*

*Tabelle 3.1: MRE der Templates mit der schlechtesten Performance*
[Tabelle]
*Quelle: Eigene Darstellung.(F)*

Vergleicht man diese drei Templates, fällt auf, dass sie an den
Extremen der Mean Template Runtimes liegen...
```

→ Keine Überleitung zwischen Bild und Tabelle (Zusammenhang offensichtlich)
→ Keine Zahlen vorlesen
→ Interpretation erst NACH der Tabelle
→ Interpretation = WARUM, nicht WAS

---

### Interpretation vs. Zahlen ablesen

**WRONG (Zahlen ablesen):**
- "Q18 hat einen MRE von 49.7%."
- "Q11 weist 14.2% auf, Q16 13.7%."
- "Die Mean Runtime von Q18 beträgt 3167ms."

**RIGHT (Interpretation):**
- "Q18 sticht als Ausreißer hervor."
- "Diese Templates liegen an den Extremen der Runtimes."
- "Das Modell scheitert bei Templates mit extremen Runtimes."

**Rule:** Wenn der Leser es selbst aus der Tabelle/dem Bild ablesen kann → NICHT hinschreiben. Nur schreiben was NICHT offensichtlich ist.

---

### Zahlenformatierung

**Nachkommastellen:**
- PNG Runtime (ms): 0 Nachkommastellen (ganze Zahlen)
- PNG MRE (%): 1 Nachkommastelle
- Tabellen: 2 Nachkommastellen
- Fließtext: 2 Nachkommastellen

**Einheiten:**
- Tabellen: Einheiten IMMER im Header, nicht in den Zellen
- WRONG: `| 211 ms |`
- RIGHT: Header `| Mean Actual (ms) |` → Zelle `| 211.37 |`

**Tabellen-Header Formatierung:**
1. Technische Spaltennamen lesbar machen (Leerzeichen, Großbuchstaben)
2. Einheit aus dem Namen extrahieren
3. Einheit in Klammern dahinter

| Technisch | Thesis |
|-----------|--------|
| `mean_actual_ms` | Mean Actual (ms) |
| `mean_predicted_ms` | Mean Predicted (ms) |
| `mre` | MRE (%) |
| `runtime` | Runtime (ms) |
| `p_tot_cost` | Total Cost |
| `template` | Template |

**Quellenangaben bei eigenen Daten:**
- "Quelle: Eigene Darstellung." ist optional (Richtlinien fordern es nicht)
- Footnote zum Repo-Pfad ist optional, nicht Pflicht

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
| MRE | Mean Relative Error | Paper | Fehler |
| Prediction | Forecast/prediction | User | Vorhersage |
| Query | Database query | User | Abfrage, Datenbankabfrage |
| Optimizer Cost Model | Cost-based prediction model of the optimizer | (Akdere und Çetintemel, 2011) | Baseline, Kostenmodell des Optimizers, Optimizer Kostenmodell |
| Tech-Stack | Technology stack (hardware, software, config) | User | |
| Pattern Selektion | Auswahl von Patterns für Modelltraining | User | Pattern Selection, Greedy Pattern Selection |
| Plan | Tree structure of Nodes/Operators | Thesis 3.1 | Planbaum |
| Frequency | Anzahl Vorkommen eines Patterns in Trainingsdaten | User | Occurrence |
| Plan-Level (Modeling) | Modellierungsansatz auf Query-Ebene | Paper | |
| Baumstruktur | Tree structure (auch: Tree) | User | |
| Teilbaum | Subtree | User | Subtree |
| Cold Cache | Ausführung ohne gecachte Daten vorheriger Runs | User | Cold Start (Paper) |

### English Terms (intentionally English)

Technical terms that remain in English (no German translation).

| Term | Source | Reason |
|------|--------|--------|
| Feature Pool | User | Alle Features die zur Auswahl stehen |
| Feature Set | User | Alle final gewählten Features |
| Operators | PostgreSQL Docs | Fachbegriff für Planknoten |
| Arten von Operators | Kategorien von Operators | User | Operatorarten, Operator-Typen, Operator Types |
| Node | PostgreSQL Docs | Synonym zu Operator |
| Runtime | PostgreSQL Docs | Actual/gemessene Ausführungszeit (Gegenstück zu Total Time) |
| Prediction | Paper | Kernbegriff der Arbeit |
| Pattern | User | Strukturmuster in Plänen |
| Root | PostgreSQL Docs | Wurzelknoten im Plan |
| Leaf | PostgreSQL Docs | Blattknoten im Plan |
| Child | PostgreSQL Docs | Kindknoten |
| Parent | PostgreSQL Docs | Elternknoten |
| Depth | PostgreSQL Docs | Tiefe im Plan (Abstand zur Root) |
| Two Step | Code | Zweistufiges FFS-Verfahren |
| Bottom-Up | Paper | Algorithmus von Leaves zur Root |
| Total Time | Code/PostgreSQL | Predicted Gesamtzeit eines Operators |
| Startup Time | Code/PostgreSQL | Startzeit eines Operators |
| konsumiert | User | Pattern deckt Operator ab, keine eigene Prediction |
