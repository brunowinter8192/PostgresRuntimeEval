# 1. Datenbank Setup und Datengenerierung

## 1.1 TPC H kit downloaden 
--> https://www.tpc.org/tpc_documents_current_versions/current_specifications5.asp
--> `/TPC-H V3.0.1` 

## 1.2 Postgres Container einrichten 
--> https://github.com/docker-library/postgres
    --> offizielles Source Repository für die PostgreSQL Docker Images auf Docker Hub

--> https://github.com/docker-library/postgres/tree/master/17/alpine3.22
    --> Das ist der Quellcode, wie das Image gebaut wird, welches ich im Projekt verwende
    
--> docker pull postgres:17-alpine3.22 
    --> Vorgang wird automatisch in der docker compose yaml gestartet, wenn das Image beim ersten Containerstart nicht bereits gepullt ist, so wird es dann gepullt. 
        
--> `/Postgres_Docker/docker-compose.yaml` 
    --> Mit diesen Konfigurationen habe ich den Container gestartet. 
    --> wie diese Konfiguration zustande kommt werde ich im folgenden ausführlich erklären.

### 1.2.1 PostgreSQL Performance Configuration
--> https://pgtune.leopard.in.ua/
--> pgtune ist eine Website welche auf Basis von user - Eingaben eine Empfehlung über konfigurierbare Parameter der Postgres Instanz liefert. 
--> Die folgenden Werte sind die einzugebenden Systemparameter:
    DB Version: 17
    OS Type: linux
    DB Type: dw
    Total Memory (RAM): 48 GB
    CPUs num: 14
    Data Storage: ssd

--> alle Werte bis auf den DB Type sind Hardware Parameter welche sich aus dem Systembericht meiner verwendeten Maschine auslesen lassen
--> alles wurde auf einem MacBook Pro, Apple M4 Pro ausgeführt 
--> als DB Type wurde data warehouse gewählt, dabei stütze ich mich auf die Angaben in der TPC-H Specification (TPC 2022, S. 93):
    „The configuration and initialization of the SUT, the database, or the session, including any relevant parameter, switch or option settings, must be based only on externally documented capabilities of the system that can be reasonably interpreted as useful for an ad-hoc decision support workload. This workload is characterized by:
        • Sequential scans of large amounts of data;
        • Aggregation of large amounts of data;
        • Multi-table joins;
        • Possibly extensive sorting."
        
--> Das System, die Datenbank sowie die session darf also nur auf basis von extern dokumentierten Informationen konfiguriert werden, pgtune ist so eine Datenquelle
--> Bei der TPC H benchmark geht es um decision support workloads, welche durch die oben genannten Punkte charakterisiert sind. Diese Punkte matchen exakt mit den data warehouse Angaben in pgtune. 

--> pgtune gab auf Basis meiner Eingabewerte die Ausgaben:
    max_connections = 40
    shared_buffers = 12GB
    effective_cache_size = 36GB
    maintenance_work_mem = 2GB
    checkpoint_completion_target = 0.9
    wal_buffers = 16MB
    default_statistics_target = 500
    random_page_cost = 1.1
    effective_io_concurrency = 200
    work_mem = 116508kB
    huge_pages = try
    min_wal_size = 4GB
    max_wal_size = 16GB
    max_worker_processes = 14
    max_parallel_workers_per_gather = 7
    max_parallel_workers = 14
    max_parallel_maintenance_workers = 4

#### 1.2.1.1 Bezug
--> diese Werte wurden entsprechend in Zeile 32 - 66 in `/Postgres_Docker/docker-compose.yaml` eingesetzt

### 1.2.2 Shared Buffers
--> Shared Buffers ist der RAM Cache für PostgreSQL. Queries lesen Millionen Rows, Shared Buffers cached häufig gescannte Tables/Indexes, Performance-Steigerung.
--> Sets the amount of memory the database server uses for shared memory buffers. postgresql.org/docs/current/runtime-config-resource.html
--> If you have a dedicated database server with 1GB or more of RAM, a reasonable starting value for shared_buffers is 25% of the memory in your system. https://www.postgresql.org/docs/current/runtime-config-resource.html

#### 1.2.2.1 Bezug
--> Zeile 7 in `/Postgres_Docker/docker-compose.yaml`

### 1.2.3 Network und Ports 
--> der Container ist vom Host, Mac OS System auf Port 5432 erreichbar.
--> Container wird zusätzlich in virtuelles Docker Network tpch-network eingebunden.
--> zu Beachten, ein Network ist nicht zwingend notwendig um den container zu starten. 
--> ich habe dennoch eine Network config eingerichtet da ich einen MCP Server mit der Datenbank verbinden wollte welcher auch als Container läuft und eine Verbindung ohne custom Network gescheitert ist. 
--> Ich werde ggf. in einem späteren Teil, sofern Ich einen Use case ermitteln kann, den bestehenden MCP Server basierend auf Erkenntnissen aus dieser Arbeit erweitern.
    --> https://github.com/crystaldba/postgres-mcp
    --> https://modelcontextprotocol.io/docs/getting-started/intro
    
#### 1.2.3.1 Bezug
--> Zeile 71 - 73, 9 - 10, 17 - 18
--> in `/Postgres_Docker/docker-compose.yaml`

### 1.2.4 Umgebungsvariablen
--> Docker Compose liest automatisch .env Datei im selben Verzeichnis. `/Postgres_Docker`
--> nur das Passwort ist zwingend zu setzen. This environment variable is required for you to use the PostgreSQL image 
--> Es wurden zusätzlich noch der User und der DB Name konfiguriert
--> https://github.com/docker-library/docs/blob/master/postgres/README.md

#### 1.2.4.1 Bezug
--> Zeilen 12 - 15 in `/Postgres_Docker/docker-compose.yaml`

### 1.2.5 Schema.sql
--> `/Postgres_Docker/init/01-schema.sql`
--> Schema.sql wird beim ersten Start des Containers geladen. Es orientiert sich an der TPC-H Specification, Abschnitt „Database Entities, Relationships, and Characteristics" (TPC 2022, S. 13).
--> Es werden die Tabellen erstellt. 
--> in Zeile 86 - 93 wurde ein Workaround gewählt. Da mit dem dbgen - tool die generierten Tabellen alle einen trailing Delimiter am Anfang und Ende jeder Spalte haben, so hat auch die letzte Spalte diese Syntax. Merke, die mit dbgen generierten Daten dürfen nicht verändert werden. Aber so wie sie generiert sind, sind sie mit PostgreSQL nicht kompatibel. PostgreSQL interpretiert den trailing delimiter ganz rechts als weitere Spalte. Um also die generierten Daten unverändert zu halten und dennoch Postgres kompatibel zu machen wurde dieser Workaround gewählt um eine korrekte Syntax für PostgreSQL zu gewährleisten. 


## 1.3 Table Daten und Queries generieren
--> hier ergaben sich viele Herausforderungen. Die TPC-H Benchmark ist nativ nicht für PostgreSQL ausgelegt, dennoch habe ich versucht in meinen Implementierungen so nah wie möglich an der Specification zu bleiben. 
--> im folgenden werden alle Änderungen in `/Diff_TPCH` besprochen und warum sie in dieser Form nötig waren.
--> Zuerst aber die relevanten Auszüge aus der Specification welche eben diese Änderungen erst einmal nötig gemacht haben. 
--> Daraus geht zunächst einmal hervor, dass die tbl files und die queries mit den zu kompilierenden executables generiert werden müssen. Im Folgenden gehe ich davon aus, dass ohne irgendwelche Änderungen an den files im dbgen Ordner, die generierten Daten den in den respektiven Abschnitten spezifizierten Anforderungen entsprechen. Was also im folgenden geprüft wird ist, ob und in welcher Form die von mir durchgeführten Änderungen den Output der Daten beeinflussen. Wenn der Output beeinflusst wird in einer Form welche über reine Syntax herausgeht muss festgestellt werden ob dies wiederum TPC H konforme Daten hervorbringt. 

--> nach diesen Änderungen war ich in der Lage die executables zu kompilieren, dbgen mit dem scale factor 1. Genaue Befehle wie dies Systemübergreifend möglich ist finden sich in der Specification


### 1.3.1 Key Points aus der TPC-H Specification

„The test database and the qualification database must be populated with data that meets the requirements of Clause 4.2.2 and Clause 4.2.3. DBGen is a TPC provided software package that must be used to produce the data used to populate the database." (TPC 2022, S. 80)

„Executable query text must be generated according to the requirements of Clause 2.1.2 and Clause 2.1.3. QGen is a TPC provided software package that must be used to generate the query text." (TPC 2022, S. 80)


### 1.3.2 Änderungen an Files im dbgen - Ordner 
--> in `/Diff_TPCH/diff_output.txt` sind alle Änderungen Dokumentiert

#### 1.3.2.1 macOS malloc.h Zeile 1 - 17 
--> macOS (Darwin) hat malloc.h deprecated
--> malloc() Funktionen sind auf macOS in stdlib.h
--> Conditional compilation für Platform-Kompatibilität
--> Kein Impact auf generierten Output - reine Compile-Zeit Anpassung

#### 1.3.2.2 Build - Config Zeile 18 - 41 
Build-Konfiguration vervollständigt durch Setzen von 4 leeren Variablen:
    Compiler-Name
    Ziel-Datenbank
    Ziel-Betriebssystem
    Benchmark-Typ                                                                        
--> notwendige Änderungen ohne welche dbgen nicht kompiliert


#### 1.3.2.3 PostgreSQL Syntax Zeile 42 - 460 
--> hier stellten sich die größten Herausforderungen. Diese sind alle Syntaktischer Art und hängen mit der nicht nativen unterstützung von PostgreSQL zusammen. 

Problem 1: SQL-92 → PostgreSQL Syntax Konvertierung
--> SQL-92 Standard (TPC-H Spec):
interval '90' day (3)
date '1998-12-01'

--> PostgreSQL erwartet:
INTERVAL '90 days'
DATE '1998-12-01'

Lösung in: postgresql_fix_intervals(line), String-Transformation während Query-Generierung, Spec standard wird zu PostgreSQL Syntax angepasst 

Problem 2: LIMIT Clause Handling
--> TPC-H Queries nutzen :n Directive für Row-Limit:

SELECT ... :n 100

--> Standard-Verhalten (andere Datenbanken):
sqlSET ROWCOUNT 100;
SELECT ...

--> PostgreSQL braucht:
sqlSELECT ...
LIMIT 100;

Lösung: Pre-Scan des Query-Templates nach :n Directive, Buffer komplette Query, Füge LIMIT vor Semicolon ein

Problem 3 Buffer-Management System

Lösung, Query muss komplett gelesen werden BEVOR sie ausgegeben wird (für LIMIT-Platzierung am Ende).:
--> buffer_init() - Allokiert Query-Buffer
--> buffer_append() - Fügt Text hinzu (mit automatischem Resize)
--> buffer_flush_with_limit() - Schreibt Query mit LIMIT

#### 1.3.2.4 PostgreSQL-spezifischen Makros Zeile 461 - 480 
--> definieren datenbankspezifische SQL-Syntax für verschiedene Operationen.
--> Diese Makros werden in qgen.c verwendet für datenbankspezifische SQL-Befehle
--> Änderungen sind notwendig da ohne sie qgenc nicht kompilieren würde, jede db braucht diese Makro-Definitionen 

#### 1.3.2.5 macOS malloc.h Zeile 481 - 496
--> gleiche Änderung wie in 1.3.2.1

#### 1.3.2.4 Spec-Bezug
--> in den Anpassungen 1 und 2 wurden die ausgegebenen Tables und Queries nicht verändert, es gab lediglich Anpassungen in Hinblick darauf das diese überhaupt erst erstellt werden können. In Anpassung 3 gab es jedoch Änderungen welche die generierten Templates beeinflussten, daher musste hier die Specification einbezogen werden.

Die TPC-H Specification erlaubt explizit vendor-spezifische Anpassungen:
--> „Date expressions - vendor-specific syntax may be used instead of specified SQL-92 syntax" (TPC 2022, Clause 2.2.3.3c)
--> „Vendor-specific SQL syntax may be added to SELECT statement to limit rows returned" (TPC 2022, Clause 2.2.3.3)

--> das heißt die Änderungen waren in sofern valide als das sie sich nur auf die beiden in der Specification explizit angesprochenen Punkte beziehen und diese respektieren. 

## 1.4 Ergänzungen
--> das script zum generieren der `/Diff_TPCH/diff_output.txt` wird nicht in das repo aufgenommen da es den offiziellen dbgen Ordner erfordert, jedoch können die genauen Änderungen an den Files im erwähnten txt File nachvollzogen werden







# 2. Überblick über die Problemstellung 
--> wird eine Query mit dem explain Operator in Postgres ausgeführt, so berechnet der Postgres interne Optimizer einen Execution Plan welcher den Ablauf der Ausführung sowie die verwendeten Node Types beinhaltet. 
--> Das Paper welches als Inspiration für diese Arbeit diente will ein fundamentales Problem lösen. in Postgres gibt der optimizer zwar die total costs an, jedoch lässt sich daraus keine Laufzeit ableiten. Das paper und diese Arbeit sucht nach einem Weg auf Basis der Informationen welche der Optimizer liefert und mit Ausführung der Queries und der Runtime als Zielgröße ein ML Modell zu Trainieren welches die Runtime einer Query auf Basis der Infos welche der Optimizer liefert vorhersagt. 
--> Es wird sich zunächst einmal nur mit dem Plan based Modeling 3.1 befasst und im weiteren Verlauf der Arbeit werden andere Modelle getestet.

# 3. Sammeln der Daten
--> im Paper sind eine ganze Reihe an features relevant die sich alle mit dem Explain Operator ermitteln lassen.
--> Auf die genaue Berechnung der Featurewerte wird im Verlauf eingegangen, zunächst einmal muss die Grundlage geschaffen werden die features auslesen zu können. 

## 3.1 Generieren der Queries
--> als ersten Schritt müssen mit Hilfe der zuvor generierten Templates die Queries generiert werden. Dazu dient dieses Script `/Generated_Queries/generate_all_variants.sh`
--> Es gibt 150 seeds welche sich auf jedes template anwenden lassen, dadurch können 150 Varianten mit unterschiedlichen Werten von jedem Template generiert werden.

## 3.2 Relevante Node Types identifizieren 
--> in Postgres 17.6 gibt es eine Vielzahl an Node-Types, da im folgenden nur solche gebraucht werden welche auch in den Queries 1 bis 22 vorkommen, müssen diese identifiziert werden.
--> `/Feature_Exploration/Feature_Calculation/text_explain.py`
--> Das Script führt EXPLAIN im TEXT-Format aus, das war für mich erstmal einfacher zu verstehen um was es überhaupt geht. 
--> Allerdings schleichen sich hier schnell falsche Erkenntnisse ein, im text format sieht man zb: 

Finalize GroupAggregate
Partial HashAggregate
Nested Loop Semi Join
Parallel Hash Join
Index Scan using tenk1_unique1
Bitmap Index Scan on tenk1_unique2

--> Der Trugschluss, Man denkt, dies seien die Node Types, es sind jedoch zusammengesetzte, menschenlesbare Beschreibungen aus mehreren Attributen.

JSON-Struktur:
TEXT: "Finalize GroupAggregate"
json{
  "Node Type": "Aggregate",
  "Strategy": "Sorted",
  "Partial Mode": "Finalize"
}
Tatsächlicher Node Type: "Aggregate"
Nicht: "Finalize GroupAggregate"

TEXT: "Partial HashAggregate"
json{
  "Node Type": "Aggregate",
  "Strategy": "Hashed",
  "Partial Mode": "Partial"
}
Tatsächlicher Node Type: "Aggregate"
Nicht: "Partial HashAggregate"

--> in `/Feature_Exploration/Feature_Calculation/Node_Type_finding/find_all_node_types.py` werden erstmal alle node types der Queries ermittelt. 
--> Query 15 wurde Ausgeschlossen (Multi-Statement-Query)
--> für Explain, es muss ein einzelnes ausführbares Statement sein. EXPLAIN funktioniert nicht mit: DDL-Statements (CREATE, DROP, ALTER), Multi-Statement-Queries, Transaktionssteuerung (BEGIN, COMMIT)
--> Query 17 und 20 hatte ich bereits entfernt da sie in einem Initial run eine so lange Laufzeit aufwiesen, dass hier eine Datengenerierung bezogen auf die Laufzeit unsinnig erschien.
--> Die so ermittelten node types ergaben sich zu, `/Feature_Exploration/Feature_Calculation/Node_Type_finding/csv/all_unique_node_types.csv`
--> Insgesamt 13 unique node types über alle 2850 analysierten queries

# 3.3 Feature calculation
--> im Paper wurden in 3.1 eine ganze Reihe an features angeführt welche neben den node types und deren counts ( op_count , <operator_name>_cnt) auch die folgenden umfassen:

# p_tot_cost, p_st_cost 
--> erste cost zahl sind die estimated start cost, das sind die Kosten die es erfordert bevor mit dem jeweiligen operator an der stelle begonnen werden kann
--> zweite cost zahl sind die estimated total cost, das sind die Kosten die es braucht um alle output Tuples zu erzeugen

# p_rows  
--> sind die rows welche am Ende einer operation vorliegen 12.485 zb 
--> diese können dann weitergegeben werden und dienen der nächsten operation als input Tuples 

# p_width 
--> Physische Width in Bytes
--> Speichergröße der Daten = z.B. 40 bytes
--> tupel zeile, width in bytes ist der speicherplatz eines tuples 

--> `/Feature_Exploration/Feature_Calculation/features_part1.py` 
--> `/Feature_Exploration/Feature_Calculation/csv/all_seeds_Part1.csv`
--> das script exportiert die csv welche all diese features berechnet

--> die komplette feature berechnung habe ich zweigeteilt da die Logik zur berechnung von row count und byte count etwas komplizierter ist. 

# row_count 
--> zu beachten ist, dass sub-pläne, bzw. der output aus sub Plänen, nicht als Input für den Hauptplan gerechnet wird. 
--> im json format sind die sub Pläne und init Pläne etwas anders gekennzeichnet als im Text format, die Logik zur Berechnung lässt sich aus dem script nachvollziehen.
--> Im folgenden eine beispielhafte Berechnung von row_count für Q16 seed_0101000000


HAUPTPLAN:
1. Parallel Seq Scan customer (rows=729)
   Input: 0, Output: 729 → 729

2. Parallel Hash (rows=729)
   Input: 729, Output: 729 → 1,458

3. Parallel Seq Scan orders (rows=483,871)
   Input: 0, Output: 483,871 → 483,871

4. Parallel Hash Right Anti Join (rows=216)
   Input: 483,871 + 729 = 484,600, Output: 216 → 484,816

5. Sort (rows=216)
   Input: 216, Output: 216 → 432

6. Gather Merge (rows=670)  ← AKTUELL
   Input: 216, Output: 670 → 886

7. GroupAggregate (rows=670)  ← AKTUELL
   Input: 670, Output: 670 → 1,340
Hauptplan Subtotal: 729 + 1,458 + 483,871 + 484,816 + 432 + 886 + 1,340 = 973,532

INITPLAN:
1. Parallel Seq Scan customer_1 (rows=1,988)
   Input: 0, Output: 1,988 → 1,988

2. Partial Aggregate (rows=1)
   Input: 1,988, Output: 1 → 1,989

3. Gather (rows=2)
   Input: 1, Output: 2 → 3

4. Finalize Aggregate (rows=1)
   Input: 2, Output: 1 → 3
InitPlan Subtotal: 1,988 + 1,989 + 3 + 3 = 3,983

TOTAL row_count:
973,532 + 3,983 = 977,515


# byte_count
--> wie row count nur das immer mit der average width des jeweiligen Schritts multipliziert wird 

--> `/Feature_Exploration/Feature_Calculation/features_part2.py`
--> `/Feature_Exploration/Feature_Calculation/csv/features_part2.csv`
--> berechnet row und byte count, 


## 3.3 Runtime values
--> als nächstes müssen alle 2850 queries ausgeführt werden und die entsprechende runtime muss abgetragen werden. 

### 3.3.1 Cold_Cache validation
--> Cold cache ist notwendig um die einzelnen Ausführungen nicht in einem Gegenseitsverhältnis zu beeinflussen. 
--> Die einzige Methode die hier Erfolg hatte und eine dauerhaft niedrige Abweichung zwischen den runs sicherstellen konnte war:

osascript -e 'quit app "OrbStack"'                       → OrbStack beenden
Warten bis OrbStack gestoppt
sudo purge                                                         → OS-Level Cache leeren
open -a OrbStack                                               → OrbStack neu starten
Docker Container starten
Auf Postgres warten
Query ausführen


--> bei der Verifizierung ob caching aktiv ist geht es darum die einzelnen runtimes miteinander zu vergleichen, besonders interessant ist hier der vergleich der ersten Ausführung eines seeds mit allen weiteren Ausführungen.
--> sollte caching aktiv sein wird erwartet das der erste Durchlauf des ersten seeds bedeutend länger dauert als die nachfolgenden Ausführungen.
--> da die Datenbank im vergleich zum shared buffer des containers eher klein ist, 1 GB im vergleich zu 12 GB shared buffers, wird auch erwartet das das alle folgenden Ausführungen anderer templates ebenfalls wesentlich weniger zeit in Anspruch nehmen und das sich hier die zeit im vergleich erste Ausführung des seeds zu weiteren Ausführungen des seeds kaum unterscheidet 
--> Jedoch sollte zwischen der Ausführung in cold cache im vergleich zur Ausführung in warm cache über alle seeds aller templates gesehen eine deutliche Abweichung in Hinblick auf die reine runtime in ms ergeben.
--> CV = (Standardabweichung / Mittelwert) × 100%
--> dieser Koeffizient soll als Maß gelten, dabei wird gemeinhin festgehalten: 
CV < 3%: Exzellente Konsistenz und Stabilität
CV 3-5%: Gute, akzeptable Konsistenz für Cold Cache Tests
CV > 5%: Fragwürdige Konsistenz, deutet auf Störfaktoren hin

--> `/Feature_Exploration/Cache_Validation/cold_chace_validation/restart_docker/execute_queries.py`
--> bei der ersten Ausführung ergaben sich die folgenden werte, festgehalten in einer csv
--> `/Feature_Exploration/Cache_Validation/cold_chace_validation/restart_docker/csv/runtime_20251006_160232.csv`

--> ausschließlich query 13 mit CV = 7.004697880349045 % stellt einen Ausreißer dar. 
--> ursächlich dafür war run 3 
Durchschnitt der Runs 1,2,4,5: (886 + 910 + 898 + 915) / 4 = 902ms
Run 3: 1046ms
Absolute Abweichung: 1046 - 902 = 144ms (ich hatte 160ms gerundet)
Relative Abweichung: (144 / 902) × 100 = 16%

--> in einem zweiten Durchlauf des scripts ergaben sich die folgenden Ergebnisse. 
--> kein CV über 5%
--> beim dritten run gab es 2 Queries minimal über 5% 

| Metrik                    | Run 1  | Run 2  | Run 3  |
|---------------------------|--------|--------|--------|
| Durchschnittlicher CV     | 2.48%  | 2.89%  | 3.25%  |
| Median CV                 | 2.06%  | 3.18%  | 3.18%  |
| Min CV                    | 0.58%  | 0.73%  | 1.29%  |
| Max CV                    | 7.00%  | 4.80%  | 6.93%  |
| Templates mit CV < 3%     | 73.7%  | 47.4%  | 47.4%  |
| Templates mit CV <= 5%    | 94.7%  | 100.0% | 89.5%  |
| Ausreisser (CV > 5%)      | 1      | 0      | 2      |

--> da 89% - 100% der templates in jedem run einen CV kleiner gleich 5% aufwiesen kann man von soliden cold cache Ergebnissen ausgehen und die vollständigen Laufzeitwerte ermitteln


#### 3.3.1.1 Vergleich mit den Warm Cache Ergebnissen
--> Wie ist die Abweichung des initial run von Q1 warm cache im vergleich zu allen folgeruns von Q1, wie ist die Abweichung der Laufzeitdurchschnitte der jeweiligen queries generell.
--> `/Feature_Exploration/Cache_Validation/Comparison/compare_cold_warm.py`

Die Ergebnisse zusammengefasst: 
--> Warm Cache First-Run Effekt:
11 von 19 Queries zeigen First-Run Effekt (Run 1 langsamer als Runs 2-5)
Durchschnittliche Abweichung bei diesen 11 Queries: +39.01%
Median über alle Queries: +0.54% (viele Queries zeigen kaum Effekt)

Extreme Fälle:
Q3: Run 1 ist 185.72% langsamer (364ms vs 127ms)
Q1: Run 1 ist 131.47% langsamer (1085ms vs 469ms)  
Q2: Run 1 ist 84.95% langsamer (143ms vs 78ms)

--> Ab Q4 stabilisiert: keine Abweichung mehr als ±11%
--> Interpretation: Erste 3 Queries müssen Cache-Strukturen aufbauen



### 3.3.2 Laufzeit Daten generieren
--> nun können die Laufzeitwerte der 19*150 abfragen generiert werden, das nimmt einige zeit in Anspruch. Ein voller run dauerte bei mir auf 1GB Data base ca 7 Stunden



# 4 Correlationsanalyse 

## 4.1 Pearson-Correlation
--> zunächst einmal war die Überlegung durch die große Last an Node type features diese herunterzubrechen auf die mit der höchsten Korrelation und dann die eigentliche feature extraction nur mit den 3 am stärksten korrelierenden node types durchzuführen. 
--> obwohl dieser Ansatz dann im späteren Verlauf verworfen wird, widme ich ihm trotzdem einen Absatz da er wichtige insights geliefert hat. 
--> `/Feature_Exploration/Correlation_Analysis/merge_data.py`
--> dieses script verbindet zunächst einmal nur die output csv der explain analysis part 1, wobei immer nur der erste seed berücksichtigt wird, mit dem output csv der cold cache analysis 
--> es entsteht eine csv welche den mean ms durchlaufzeit über die abfragen des ersten seeds mit dem count der jeweilige node types verbindet im entsprechenden seed 1 

--> auf diese merged csv wird jetzt eine Korrelations-Analyse ausgeführt `/Feature_Exploration/Correlation_Analysis/correlation_analysis.py`

Berechnet Pearson-Korrelation zwischen:
X: Anzahl dieses Node-Types in der Query (z.B. 2 Aggregates)
Y: Runtime der Query in ms (z.B. 1120ms)

Ergebnis: r-Wert zwischen -1 und +1
r > 0: Mehr Nodes → höhere Runtime
r < 0: Mehr Nodes → niedrigere Runtime (unwahrscheinlich)
r ≈ 0: Keine lineare Korrelation

--> es zeigt sich, dass 2 node types eine starke postive Korrelation mit der runtime aufweisen
Incremental_Sort_cnt	                  0.7840138802689908
Merge_Join_cnt	                          0.7840138802689908

--> `/Feature_Exploration/Correlation_Analysis/plots/scatter_grid.png`
--> schaut man sich aber die plots an stellt man schnell fest das diese beiden operatoren nur in Q18 jeweils einmal vorkommen, und das Query 18 eine hohe mean runtime aufweist 
--> das wirft fragen auf, es könnte tatsächlich sein das diese beiden operatoren ein starkes Signal für eine hohe runtime senden, es könnte aber auch sein das es nur Zufall ist
--> angesichts der tatsache, dass sie nur in Q18 vorkommen habe ich mich im folgenden dazu entschieden sie aus der feature ermittlung herauszunehmen, da sie nur in einer Query auftauchen und nur je einmal, das bietet keine Grundlage für eine fundierte analyse. 

--> key takeaway dieser kurzen analyse war also das ein Blick auf die Visualisierungen sich lohnt und das ein ansatz zur featureselektion gewählt werden muss welcher die daten am besten beschrieben kann. 


## 4.2 Feature selection
--> im Folgenden geht es nur um den Hauptordner `/Runtime_Prediction`
--> in diesem Ordner befinden sich Unterordner von denen jeder gleich aufgebaut ist 

#### Baseline
--> in der Baseline habe ich zunächst einmal die volle Anzahl an features verwendet
--> `/Runtime_Prediction/Baseline`
--> Zuerst einmal war es wichtig ein Gefühl für das Dataset zu bekommen um die parameter für das SVM richtig einstellen zu können 
--> dazu habe ich in `/Runtime_Prediction/Baseline/Evaluierung` einige scripts geschrieben welche es ermöglichen sich ein Bild über die Daten zu verschaffen 

#### Evaluation
--> dazu habe ich in `/Runtime_Prediction/Baseline/Evaluierung` einige scripts geschrieben welche es ermöglichen sich ein Bild über die Daten zu verschaffen 
--> die folgenden scripts dienen hauptsächlich pre filtering purposes, werden dann in weitere iterationen genauer unter die Lupe genommen bzw ausgewertet, in der baseline werden sie zunächst einmal erklärt aber zeigen noch keine entscheidungswirkung auf ein pre filtering da hier alle features verwendet werden

##### Scatterplots 
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/create_scatter_plots.py`
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/scatter_plots_20251011_194228.png` 
--> in diesem script werden zu jedem feature scatterplots erstellt welche die Pearson-Correlation ( r = Σ((xi - x̄)(yi - ȳ)) / √(Σ(xi - x̄)² · Σ(yi - ȳ)²) ) mit dem target (runtime) abbilden
--> das Haupproblem sind die klar erkennbaren vertikalen linien in vielen plots, das heißt dass die runtime nicht durch das eine feature, sondern vielmehr aus eine kombination verschiedener features bestimmt wird
--> das modell muss also in der lage sein über features hinweg eine, mit einer betrachtung der features in kombination, eine aussage über die runtime zu liefern

##### feature Correlations 
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/correlation_analysis.py`
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/csv/feature_correlations_20251011_193530.csv`
--> diese csv zeigt alle feature correlations über 0,95 das heißt alle paare die über 0,95 kommen. Wenn jetzt ein feature oft auf der linken seite steht dann heißt das, dass es potentiell einige andere features ersetzen kann, man kann also mit einem feature, so viel info bündeln wie mit 5
--> gut für schnelles noise entfernen
--> wenn nun auffällt, dass beim ffs im endergebnis viele feature kombinationen aufgenommen werden welche an sich redundant sind und kaum echten mehrwert bringen, kann das ein argument sein, um im folgenden diese features gleich zu entfernen um den algo schlanker zu machen und evtl eine prediktivere feature kombination zu finden


#### outliers und sparse
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/scale_outlier_analysis.py`
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/csv/feature_outliers_20251011_201406.csv`
lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR 
--> alles was darunter oder darüber liegt sind outlier features, das hilft features zu identifizieren welche sich in besonders ungewöhnlichem Maße über die verschiedenen templates verteilen
--> zudem wird auch immer die query angezeigt welche für die meisten dieser outliers verantwortlich ist und die respektive zahl
--> so lassen sich templates identifizieren welche die feature verteilung stark aus dem gleichgewicht bringen
--> man kann dann ein argument dafür machen zum einen features mit einem hohen outlier count zu entfernen für das training oder ganze queries welche diesen outlier count begünstigen
--> es fällt hier schnell ein hoher zusammenhang zum sparse anteil auf 
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/csv/feature_zeros_20251011_201406.csv`
--> wenn ein feature in einem template immer 0 ist und in den anderen templates existiert, so kann es schnell dazu kommen das die vollen 120 seeds dieses templates entsprechende outlier werte eines features verursachen

#### konsistenz innerhalb eines templates 
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/template_feature_constancy_matrix.py` 
--> `/Runtime_Prediction/Baseline/Evaluierung/Features/csv/template_feature_constancy_matrix_20251011_193540.csv` 
--> hier zeigt sich das extrem viele features innerhalb eines einzigen templates völlig konstant sind. Das ist in sofern problematisch, als das dann eher gelernt wird templates zu erkennen aber nicht erkannt werden kann wie sich die seeds innerhalb eines templates verhalten

#### FFS mit SVM
--> `/Runtime_Prediction/Baseline/SVM/forward_selection.py`
--> der SVM algo kann an mehreren stellen angepasst werden in hinblick auf die zu untersuchenden daten


1. MIN_FEATURES
pythonMIN_FEATURES = 10

--> das war eine Überlegung meinerseits welche zwar eine hohe Anzahl an features erzwingt, jedoch müssen ja nicht alle dann für das tatsächliche training verwendet werden
--> die Überlegung dahinter ist festzustellen ob zb in iteration 7 auf 8 der mre wieder besser wird oder stetig schlechter wird
--> so kann man evtl etwas einschätzen ob es perse sinnvoll ist mehr features hinzuzufügen oder ob dies die prediction immer weiter verschlechtert


2. NuSVR Modell-Konfiguration
pythonmodel = NuSVR(
    kernel='rbf',
    nu=0.5,
    C=0.5,
    gamma='scale',
    cache_size=500
)
kernel='rbf'

--> RBF ist Standard bei SVMs für non-linear regression.
--> nu=0.5 Sort_cnt	840	36.84210526315789, die höchsten outlier befinden sich in sort count mit 36,8%
    --> nu ist ein Maß dafür welcher Anteil von outliers toleriert wird, bei einem zu niedrigen nu wird versucht diese outliers mit in das modell zu quetschen wodurch es ungenau wird da es sich eben wie gesagt um outliers handelt, diese outliers werden sozusagen stärker gewichtet und als 'normale' datenpunkte klassifiziert
--> C=0.5 → nu=0.5 gibt Raum für Outliers → C=5.0 zwingt trotzdem gute Fits für normale Punkte, C bestraft outliers, C = 1 zb werden outliers nicht so stark bestraft, das modell erlaubt also eine hohe zahl an outliers bestraft sie aber nicht so stark, wenn man also nu auf 0,5 setzt dann sollte man auch die outliers entsprechend stärker bestrafen da eine höhere anzahl toleriert wird 
--> gamma='scale' berücksichtigt die scale der daten und behandelt sparse elemente. da teilweise die skalen im millionen und teilweise im einstelligen bereich liegen, und es viel sparse gibt, sinnvoll. 
--> cache_size=500 bestimmt die schnelligkeit


3. Scaler-Auswahl
pythonpipeline = Pipeline([
    ('scaler', MaxAbsScaler()),
    ('model', NuSVR(...))
])
MaxAbsScaler

--> Erhält Sparsity (Nullen bleiben Null), Bei hohem Sparse-Anteil (>50% Nullen) sinnvoll 


4. Cross-Validation Strategie
pythontemplate_ids = df['query_file'].apply(extract_template_id).values
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv.split(X[features], template_ids)
n_splits=5

--> paper konform, es werden im iterations prozess aus den trainingsdaten immer 4 anteile wiederum trainiert und einer getestet um die feature auswahl zu validieren
--> random state 42, es werden aus reproduzierbarkeitsgründen immer die selben seeds für training und test verwendet


5. Evaluation-Metrik
pythondef mean_relative_error(y_true, y_pred):
    epsilon = 1e-6
    relative_errors = np.abs((y_true - y_pred) / (y_true + epsilon))
    return np.mean(relative_errors)
epsilon=1e-6

--> paper konform, hier auch gleiches Entscheidungskriterium 

6. Multi-Seed Robustness (Optional)
pythonSEEDS =

results = []
for seed in SEEDS:
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    selected_features, mre = forward_selection(...)
    results.append({'seed': seed, 'mre': mre, 'features': selected_features})

mean_mre = np.mean([r['mre'] for r in results])
std_mre = np.std([r['mre'] for r in results])

--> Stabilität der Feature-Selektion über verschiedene CV-Splits testen



##### ergebnisse 
--> jetzt da die einzelnen Stellschrauben für den SVM besprochen und konfiguriert sind kann er ausgeführt werden
--> `/Runtime_Prediction/Baseline/SVM/csv`

1. p_rows
2. Aggregate_cnt
3. Index_Only_Scan_rows
4. Gather_cnt
5. Seq_Scan_rows
6. Index_Only_Scan_cnt
7. Seq_Scan_cnt

--> ein MRE von `/Runtime_Prediction/Baseline/SVM/csv/selected_features_seed42.csv` 
29,942%
--> das ist an sich erstmal eine akzeptable baseline die in weiteren durchläufen durch effektives pre filtering ggf noch optimiert werden kann

##### modell trainieren 
--> `/Runtime_Prediction/Baseline/Model/train_final_model.py` 
--> das modell wird entsprechend auf den trainingsdaten trainiert mit genau dem svm algo der gerade auch genutzt wurde um die optimale feature kombination zu ermitteln
--> `/Runtime_Prediction/Baseline/Model/csv/template_summary.csv` 
--> das modell performed besser auf den testdaten mit einem MRE overall von 24,23%
--> zeigt sich das die Templates: 2, 11, 16, 18, 22 probleme machen, hier ist die prediction weniger solide
--> diese templates haben im schnitt sehr kleine 




#### Baseline xg boost 
--> die daten bleiben alle genau gleich
--> es wird jetzt nur anstelle von SVM XGBoost genutzt um das Modell zu trainieren
--> `/Runtime_Prediction/Baseline_XGBoost/XGBoost/forward_selection.py` anstelle von SVM wird jetzt XGBoost mit den äquivalenten parametern genutzt welche auch in SVM verwendet wurden

--> `/Runtime_Prediction/Baseline_XGBoost/XGBoost/csv` es gibt hier einige interessante erkenntnisse


--> `/Runtime_Prediction/Baseline_XGBoost/XGBoost/csv/evaluation/csv/optimal_feature_frequency.csv`
--> jetzt 2 möglichkeiten. 1. trainieren des modells nur mit den 3 ersten features die am häufigsten vorkommen. 2. trainieren des modells mit allen features die größer gleich 2 mal vorkommen

--> 

#### Baseline random forest

#### neue Features 
--> Ich bin zu dem Schluss gekommen das es sinn macht das feature set zu erweitern
--> wie machen wir das, ganz einfach die Logik geht so gib mir mal die command die beiden py hier auszuführen: `/Data_Generation/Feature_Calculation/basic_explain`

## später evtl. noch mögliche Features die aber aktuell alle immer den selben Wert haben
Planned Partitions: Anzahl geplanter Partitionen --> nur bei großen daten, aktuell immer 0
Single Copy --> kann man auch mal im späteren Verlauf checken ob true bei irgendeiner query



# Legacy command (venv external to repo)



# Operator level modelling 
--> nach verschiedenen Überlegungen welche in 2 Richtungen gingen, 1. das Plan level weiter auszuarbeiten oder mit Operator level und hybrid fortzufahren, bin ich zu dem Schluss gekommen mit operator level und hybrid weiterzumachen
--> das hat den folgenden Hintergrund, ich möchte erstmal ein umfassendes Bild um die komplette Arbit bekommen und dann entscheiden an welchen stellen ich in die tiefe gehe, bzw es empfielt sich erstmal einen Plan zu haben wie auch der zeitliche Umfang ist, und dann eben bei bedarf in die tiefe zu gehen
--> gut 

## feature generierung
--> beim operator level modelling war es notwendig den explain Analyse operator auszufühen, was die datengenerierung extrem in die länge gezogen hat
--> beim operator level modelling sind die operators im query plan ausschlaggebend dafür wie viele Zeilen es zu einer unique template seed Kombi gibt

---

# Quellenverzeichnis

Docker Library (2024). *PostgreSQL Docker Official Images.* Abgerufen am 27.12.2025 von https://github.com/docker-library/postgres.

Docker Library (2024). *PostgreSQL Docker Image Documentation.* Abgerufen am 27.12.2025 von https://github.com/docker-library/docs/blob/master/postgres/README.md.

PGTune (o.J.). *PGTune - PostgreSQL Configuration Calculator.* Abgerufen am 27.12.2025 von https://pgtune.leopard.in.ua/.

PostgreSQL Global Development Group (2024). *PostgreSQL 17 Documentation: Resource Consumption.* Abgerufen am 27.12.2025 von https://www.postgresql.org/docs/current/runtime-config-resource.html.

TPC (2022). *TPC-H Benchmark Specification. Revision 3.0.1.* Transaction Processing Performance Council. Verfügbar im TPC-H Kit Download unter `TPC-H V3.0.1/specification.pdf`. Abgerufen am 27.12.2025 von https://www.tpc.org/tpc_documents_current_versions/current_specifications5.asp.




