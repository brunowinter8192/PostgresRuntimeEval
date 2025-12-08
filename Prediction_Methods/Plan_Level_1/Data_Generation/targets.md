# Plan-Level Targets and Metadata

## Target Variable

### runtime - Query Execution Time (ms)

Wall-clock execution time of the query in milliseconds.

**Extraction:** Python `time.perf_counter()` before and after query execution

**Measurement Method:**
```python
start_time = time.perf_counter()
cursor.execute(query)
cursor.fetchall()
end_time = time.perf_counter()
runtime = (end_time - start_time) * 1000
```

**Cold Cache Protocol:**
1. Completely shut down OrbStack
2. Purge system memory cache (`sudo purge`)
3. Restart OrbStack
4. Start Docker container
5. Wait for PostgreSQL connection
6. Execute query and measure time

**Example:** Query runs 1.234 seconds -> runtime = 1234.0

**Important:**
- Each query is executed with cold cache
- No warm-up queries
- Real wall-clock time, not EXPLAIN ANALYZE times

---

## Metadata

### query_file - Query Identifier

Unique identification of the query based on the SQL filename.

**Extraction:** `query_file.name` (filename with extension)

**Format:** `Q{template}_{variant}_seed_{seed}.sql`

**Example:**
- SQL file: `Q1_100_seed_812199069.sql`
- query_file = `"Q1_100_seed_812199069.sql"`

---

### template - Query Template

TPC-H template number of the query.

**Extraction:** Parent directory name of the SQL file

**Format:** `Q{number}` (1-22, excluding Q15)

**Example:**
- SQL file in `/queries/Q1/Q1_100_seed_812199069.sql`
- template = `"Q1"`

**TPC-H Templates:** Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q20, Q21, Q22

**Note:** Q15 is excluded (CREATE VIEW not supported)

---