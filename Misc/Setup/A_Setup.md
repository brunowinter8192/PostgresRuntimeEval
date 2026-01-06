# Anhang A: Technisches Setup

Dieser Anhang dokumentiert das vollständige technische Setup für das TPC-H DSS auf PostgreSQL.

## A.1 Systemkonfiguration

- *Hardware:* MacBook Pro, Apple M4 Pro
- *RAM:* 48 GB
- *CPUs:* 14
- *Storage:* SSD
- *Docker Runtime:* OrbStack v2.0.3 - v2.0.5 (OrbStack, 2024)

## A.2 TPC-H Kit

*Bezug:* `TPC-H V3.0.1/`

- *Download:* (TPC, 2026)


## A.3 PostgreSQL Docker Container

### A.3.1 Docker Image

*Bezug:* `Misc/Setup/Postgres_Docker/docker-compose.yaml`

- *Source:* https://hub.docker.com/_/postgres (Docker Library, 2024)
- *Image:* `postgres:17.6-alpine`
- *Digest:* `sha256:d5f196a551b5cef1c70853c6dd588f456d16ca4ea733e3f31c75bc1ae2f65f3f`
- *Pull:* `docker pull postgres:17.6-alpine` oder via Digest für exakte Reproduzierbarkeit


### A.3.2 PostgreSQL Performance-Konfiguration

*Bezug:* Zeile 32-66 in `Misc/Setup/Postgres_Docker/docker-compose.yaml`

*Konfigurationstool:* https://pgtune.leopard.in.ua/ (PGTune, o.J.)

Pgtune ist eine Website welche auf Basis von User-Eingaben eine Empfehlung über konfigurierbare Parameter der PostgreSQL-Instanz liefert.

Alle Werte bis auf DB Type sind Hardware-Parameter aus dem Systembericht der verwendeten Maschine MacBook Pro. DB Type "Data Warehouse" basiert auf der TPC-H Specification (TPC, 2022, S. 93):

> The configuration and initialization of the SUT, the database, or the session, including any relevant parameter, switch or option settings, must be based only on externally documented capabilities of the system that can be reasonably interpreted as useful for an ad-hoc decision support workload. This workload is characterized by:
> - Sequential scans of large amounts of data
> - Aggregation of large amounts of data
> - Multi-table joins
> - Possibly extensive sorting

*Eingabeparameter:*

- DB Version: 17
- OS Type: linux
- DB Type: dw (Data Warehouse)
- Total Memory (RAM): 48 GB
- CPUs num: 14
- Data Storage: ssd

*Generierte Konfigurationswerte:*

- max_connections = 40
- shared_buffers = 12GB
- effective_cache_size = 36GB
- maintenance_work_mem = 2GB
- checkpoint_completion_target = 0.9
- wal_buffers = 16MB
- default_statistics_target = 500
- random_page_cost = 1.1
- effective_io_concurrency = 200
- work_mem = 116508kB
- huge_pages = try
- min_wal_size = 4GB
- max_wal_size = 16GB
- max_worker_processes = 14
- max_parallel_workers_per_gather = 7
- max_parallel_workers = 14
- max_parallel_maintenance_workers = 4

### A.3.3 Shared Buffers

*Bezug:* Zeile 7 in `Misc/Setup/Postgres_Docker/docker-compose.yaml`

Shared Buffers ist der RAM-Cache für PostgreSQL und cached häufig gescannte Tables und Indexes (PostgreSQL, 2025, S. 632).

> If you have a dedicated database server with 1GB or more of RAM, a reasonable starting value for shared_buffers is 25% of the memory in your system.

### A.3.4 Network und Ports

*Bezug:* Zeile 71-73, 9-10, 17-18 in `Misc/Setup/Postgres_Docker/docker-compose.yaml`

Der Container ist vom Host auf Port 5432 erreichbar und wird zusätzlich in ein virtuelles Docker Network (`tpch-network`) eingebunden, welches für potenzielle Container-zu-Container Kommunikation eingerichtet wurde.

### A.3.5 Umgebungsvariablen

*Bezug:* Zeilen 12-15 in `Misc/Setup/Postgres_Docker/docker-compose.yaml`

Docker Compose liest die `.env` Datei aus dem Projekt-Root. Nur das Passwort ist zwingend zu setzen (Docker Library, 2024), zusätzlich werden User und DB Name konfiguriert.

### A.3.6 Schema.sql

*Bezug:* `Misc/Setup/Postgres_Docker/init/01-schema.sql`

Das Schema wird beim ersten Start des Containers geladen und entspricht der Spezifikation (TPC, 2022, S. 13).

*Zeile 86-93:*

Die mit dbgen generierten Daten haben einen trailing Delimiter am Ende jeder Zeile. Die generierten Daten dürfen nicht verändert werden, sind aber in dieser Form nicht PostgreSQL-kompatibel. PostgreSQL interpretiert den trailing Delimiter als zusätzliche leere Spalte.

Lösung: Workaround im Schema für korrekte PostgreSQL-Syntax, ohne die generierten Daten zu verändern.

## A.4 Daten- und Query-Generierung

Das TPC-H DSS ist nativ nicht für PostgreSQL ausgelegt. Im Folgenden werden alle Änderungen in `Misc/Setup/Diff_TPCH` dokumentiert und begründet.

### A.4.1 Specification-Grundlagen

Die TPC-H Specification unterscheidet zwei Werkzeuge für die Benchmark-Durchführung:

*DBGen* (Database Generator) generiert synthetische Testdaten für die 8 TPC-H Tabellen. Die Daten folgen definierten Verteilungen und Constraints (Clause 4.2.2: Zufallswerte, Formate; Clause 4.2.3: Tabellenspezifische Generierungsregeln).

*QGen* (Query Generator) generiert ausführbare SQL-Queries aus Templates. Jede Query hat Substitutionsparameter die zufällig gewählt werden (Clause 2.1.2: SQL-92 Syntax; Clause 2.1.3: Parameter und Output).

Beide Tools sind TPC-bereitgestellte Software deren Nutzung verpflichtend ist (TPC, 2022, S. 80):

> The test database and the qualification database must be populated with data that meets the requirements of Clause 4.2.2 and Clause 4.2.3. DBGen is a TPC provided software package that must be used to produce the data used to populate the database.

> Executable query text must be generated according to the requirements of Clause 2.1.2 and Clause 2.1.3. QGen is a TPC provided software package that must be used to generate the query text.

### A.4.2 Änderungen an dbgen-Dateien

Alle Änderungen dokumentiert in `Misc/Setup/Diff_TPCH/diff_output.md`

#### A.4.2.1 macOS malloc.h

*Bezug:* `TPC-H V3.0.1/dbgen/bm_utils.c`, `TPC-H V3.0.1/dbgen/varsub.c`

macOS (Darwin) hat `malloc.h` deprecated, die Funktionen sind stattdessen in `stdlib.h`. Die Änderung ermöglicht Conditional Compilation für Platform-Kompatibilität ohne Impact auf den generierten Output.

#### A.4.2.2 Build-Konfiguration

*Bezug:* `TPC-H V3.0.1/dbgen/makefile.suite`

Build-Konfiguration vervollständigt durch Setzen von 4 leeren Variablen:

- Compiler-Name
- Ziel-Datenbank
- Ziel-Betriebssystem
- Benchmark-Typ

Das sind notwendige Änderungen ohne welche dbgen nicht kompiliert.

#### A.4.2.3 PostgreSQL Syntax

*Bezug:* `TPC-H V3.0.1/dbgen/qgen.c`

*Problem 1: SQL-92 zu PostgreSQL Syntax-Konvertierung*

SQL-92 Standard (TPC-H Spec):
```sql
interval '90' day (3)
date '1998-12-01'
```

PostgreSQL erwartet:
```sql
INTERVAL '90 days'
DATE '1998-12-01'
```

*Lösung:* `postgresql_fix_intervals(line)` - String-Transformation während Query-Generierung

*Problem 2: LIMIT Clause Handling*

TPC-H Queries nutzen `:n` Directive für Row-Limit:
```sql
SELECT ... :n 100
```

Standard-Verhalten (andere Datenbanken):
```sql
SET ROWCOUNT 100;
SELECT ...
```

PostgreSQL braucht:
```sql
SELECT ...
LIMIT 100;
```

*Lösung:* Pre-Scan des Query-Templates nach `:n` Directive, Buffer komplette Query, Füge LIMIT vor Semicolon ein

*Problem 3: Buffer-Management System*

Query muss komplett gelesen werden BEVOR sie ausgegeben wird (für LIMIT-Platzierung am Ende):

- `buffer_init()` - Allokiert Query-Buffer
- `buffer_append()` - Fügt Text hinzu (mit automatischem Resize)
- `buffer_flush_with_limit()` - Schreibt Query mit LIMIT

Die `buffer_append()` Funktion nutzt variable Argumentlisten (C Standard Header `stdarg.h`) um beliebig viele Parameter wie bei `printf()` zu akzeptieren.

#### A.4.2.4 PostgreSQL-spezifische Makros

*Bezug:* `TPC-H V3.0.1/dbgen/tpcd.h`

TPC-H Query-Templates nutzen Platzhalter-Direktiven (z.B. `:x`, `:b`, `:n`) die zur Generierungszeit durch datenbankspezifischen SQL-Code ersetzt werden. Die Makros in `tpcd.h` definieren diese Ersetzungen für PostgreSQL:

- *GEN_QUERY_PLAN* = `explain` - Ersetzt `:x` Direktive, zeigt Query-Ausführungsplan
- *START_TRAN* = `start transaction` - Ersetzt `:b` Direktive, beginnt Transaktion
- *END_TRAN* = `commit;` - Ersetzt `:e` Direktive, beendet Transaktion
- *SET_ROWCOUNT* = `limit %d;` - Ersetzt `:n` Direktive, begrenzt Ergebnismenge
- *SET_OUTPUT* = (leer) - Output-Umleitung, von PostgreSQL nicht genutzt
- *SET_DBASE* = (leer) - Datenbankwechsel, von PostgreSQL nicht genutzt

Diese Makros sind notwendig da jede Datenbank eigene SQL-Dialekte hat. Beispiel: Ergebnisbegrenzung ist in PostgreSQL `LIMIT 100`, in anderen Systemen `SET ROWCOUNT 100`.

#### A.4.2.5 Hinweis zur TPC-H Specification-Konformität

TPC-H Konformität ist ein Zertifizierungsverfahren des Transaction Processing Performance Council für kommerzielle Datenbankanbieter. Es ermöglicht vergleichbare Ergebnisse zwischen Anbietern und erfordert unter anderem eine Prüfung durch einen TPC-zertifizierten Auditor sowie die Einreichung eines Full Disclosure Reports (TPC, 2022, S. 108 ff.). Diese Arbeit erhebt keinen Anspruch auf TPC-H Konformität, da die im Folgenden dokumentierten Änderungen teilweise nicht spezifikationskonform sind.

*Änderungen die spezifikationskonform sind:*

Die TPC-H Specification erlaubt explizit datenbankspezifische Anpassungen in bestimmten Bereichen:

- *Date/Interval-Syntax:* Vendor-spezifische Syntax für Datumsausdrücke ist erlaubt (Clause 2.2.3.c). Die Konvertierung von `interval '90' day (3)` zu `INTERVAL '90 days'` fällt unter diese Regelung.
- *LIMIT-Syntax:* Vendor-spezifische Befehle zur Begrenzung der Ergebnismenge sind erlaubt (Clause 2.1.3.1). Die Verwendung von `LIMIT n` anstelle von `SET ROWCOUNT n` ist damit abgedeckt.
- *macOS-Kompilierung:* Die Anpassung von `malloc.h` zu `stdlib.h` für macOS-Kompatibilität ist eine reine Compile-Zeit-Änderung ohne Auswirkung auf die generierten Daten oder Queries.

*Änderungen die nicht spezifikationskonform sind:*

- *PostgreSQL-Unterstützung:* Das TPC-H Kit unterstützt offiziell folgende Datenbanken: INFORMIX, DB2, Teradata, SQL Server, Sybase, Oracle, VectorWise (`TPC-H V3.0.1/dbgen/makefile.suite`, Zeile 27-28). PostgreSQL ist nicht in dieser Liste enthalten. Die Implementierung der PostgreSQL-spezifischen Makros in `tpcd.h` stellt eine Erweiterung des Kits dar, die über die in der Specification erlaubten "minor modifications" hinausgeht.
- *Kein Auditor:* Ein TPC-zertifizierter Auditor hat die Änderungen nicht geprüft (Clause 9.1.1).
- *Kein Full Disclosure Report:* Es wurde kein FDR gemäß Clause 8 erstellt oder eingereicht.

*Einordnung für diese Arbeit:*

Die fehlende TPC-H Konformität hat keine Auswirkungen auf die Validität der in dieser Arbeit durchgeführten ML-Experimente. TPC-H Konformität dient dem Vergleich kommerzieller Datenbankprodukte. Dieser Zweck ist für diese Forschungsarbeit nicht relevant. Stattdessen wird Transparenz und Reproduzierbarkeit durch das beigefügte Repository gewährleistet, welches alle Änderungen am TPC-H Kit sowie die vollständige Dokumentation des Setups enthält.
