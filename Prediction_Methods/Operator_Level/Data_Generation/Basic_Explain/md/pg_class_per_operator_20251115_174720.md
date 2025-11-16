# PG_CLASS Statistics - Per Operator

**Generated:** 2025-11-15 17:47:20

**Total Queries:** 19

---

## 1. Q1_100_seed_812199069.sql

**Template:** Q1

**Total Operators:** 5

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 6

**Plan Width:** 236

**Startup Cost:** 170311.11

**Total Cost:** 170315.88

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 2: Gather Merge

**Operator ID:** 2

**Plan Rows:** 30

**Plan Width:** 236

**Startup Cost:** 170311.11

**Total Cost:** 170314.74

**No table references found**

---

### Operator 3: Sort

**Operator ID:** 3

**Plan Rows:** 6

**Plan Width:** 236

**Startup Cost:** 169311.04

**Total Cost:** 169311.05

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 4: Aggregate

**Operator ID:** 4

**Plan Rows:** 6

**Plan Width:** 236

**Startup Cost:** 169310.82

**Total Cost:** 169310.96

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 5: Seq Scan

**Operator ID:** 5

**Plan Rows:** 1,191,651

**Plan Width:** 25

**Startup Cost:** 0.00

**Total Cost:** 127603.04

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

## 2. Q2_100_seed_812199069.sql

**Template:** Q2

**Total Operators:** 24

### Operator 1: Limit

**Operator ID:** 1

**Plan Rows:** 1

**Plan Width:** 270

**Startup Cost:** 45927.74

**Total Cost:** 45927.74

**Referenced Tables:** nation, part, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| part | 200,000 | 4,128 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 2: Sort

**Operator ID:** 2

**Plan Rows:** 1

**Plan Width:** 270

**Startup Cost:** 45927.74

**Total Cost:** 45927.74

**Referenced Tables:** nation, part, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| part | 200,000 | 4,128 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 3: Hash Join

**Operator ID:** 3

**Plan Rows:** 1

**Plan Width:** 270

**Startup Cost:** 33967.96

**Total Cost:** 45927.73

**Referenced Tables:** nation, part, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 4: Gather

**Operator ID:** 4

**Plan Rows:** 817

**Plan Width:** 30

**Startup Cost:** 1000.00

**Total Cost:** 6459.70

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 5: Seq Scan

**Operator ID:** 5

**Plan Rows:** 340

**Plan Width:** 30

**Startup Cost:** 0.00

**Total Cost:** 5378.00

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 6: Hash

**Operator ID:** 6

**Plan Rows:** 160,000

**Plan Width:** 250

**Startup Cost:** 30567.96

**Total Cost:** 30567.96

**Referenced Tables:** nation, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 7: Hash Join

**Operator ID:** 7

**Plan Rows:** 160,000

**Plan Width:** 250

**Startup Cost:** 407.96

**Total Cost:** 30567.96

**Referenced Tables:** nation, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 8: Seq Scan

**Operator ID:** 8

**Plan Rows:** 800,000

**Plan Width:** 14

**Startup Cost:** 0.00

**Total Cost:** 25560.00

**Referenced Tables:** partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 9: Hash

**Operator ID:** 9

**Plan Rows:** 2,000

**Plan Width:** 244

**Startup Cost:** 382.96

**Total Cost:** 382.96

**Referenced Tables:** nation, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 10: Hash Join

**Operator ID:** 10

**Plan Rows:** 2,000

**Plan Width:** 244

**Startup Cost:** 2.46

**Total Cost:** 382.96

**Referenced Tables:** nation, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 11: Seq Scan

**Operator ID:** 11

**Plan Rows:** 10,000

**Plan Width:** 144

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 12: Hash

**Operator ID:** 12

**Plan Rows:** 5

**Plan Width:** 108

**Startup Cost:** 2.40

**Total Cost:** 2.40

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 13: Hash Join

**Operator ID:** 13

**Plan Rows:** 5

**Plan Width:** 108

**Startup Cost:** 1.07

**Total Cost:** 2.40

**Referenced Tables:** nation, region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| region | 5 | 1 | table |

---

### Operator 14: Seq Scan

**Operator ID:** 14

**Plan Rows:** 25

**Plan Width:** 112

**Startup Cost:** 0.00

**Total Cost:** 1.25

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 15: Hash

**Operator ID:** 15

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 1.06

**Total Cost:** 1.06

**Referenced Tables:** region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 16: Seq Scan

**Operator ID:** 16

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.06

**Referenced Tables:** region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 17: Aggregate

**Operator ID:** 17

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 15.89

**Total Cost:** 15.90

**Referenced Tables:** min(partsupp_1

---

### Operator 18: Nested Loop

**Operator ID:** 18

**Plan Rows:** 1

**Plan Width:** 6

**Startup Cost:** 0.85

**Total Cost:** 15.88

**Referenced Tables:** partsupp_1

---

### Operator 19: Seq Scan

**Operator ID:** 19

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.06

**Referenced Tables:** region, region_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 20: Nested Loop

**Operator ID:** 20

**Plan Rows:** 4

**Plan Width:** 10

**Startup Cost:** 0.85

**Total Cost:** 14.77

**Referenced Tables:** nation_1, partsupp_1

---

### Operator 21: Nested Loop

**Operator ID:** 21

**Plan Rows:** 4

**Plan Width:** 10

**Startup Cost:** 0.71

**Total Cost:** 14.15

**Referenced Tables:** partsupp_1, supplier_1

---

### Operator 22: Index Scan

**Operator ID:** 22

**Plan Rows:** 4

**Plan Width:** 10

**Startup Cost:** 0.42

**Total Cost:** 4.14

**Referenced Tables:** partsupp, partsupp_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 23: Index Scan

**Operator ID:** 23

**Plan Rows:** 1

**Plan Width:** 8

**Startup Cost:** 0.29

**Total Cost:** 2.50

**Referenced Tables:** supplier, supplier_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 24: Index Scan

**Operator ID:** 24

**Plan Rows:** 1

**Plan Width:** 8

**Startup Cost:** 0.14

**Total Cost:** 0.16

**Referenced Tables:** nation, nation_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

## 3. Q3_100_seed_812199069.sql

**Template:** Q3

**Total Operators:** 10

### Operator 1: Limit

**Operator ID:** 1

**Plan Rows:** 10

**Plan Width:** 44

**Startup Cost:** 119771.80

**Total Cost:** 119771.83

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 2: Sort

**Operator ID:** 2

**Plan Rows:** 311,016

**Plan Width:** 44

**Startup Cost:** 119771.80

**Total Cost:** 120549.34

**Referenced Tables:** (sum((lineitem, lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 311,016

**Plan Width:** 44

**Startup Cost:** 109163.16

**Total Cost:** 113050.86

**Referenced Tables:** lineitem, orders, sum((lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 4: Gather

**Operator ID:** 4

**Plan Rows:** 311,016

**Plan Width:** 24

**Startup Cost:** 5536.64

**Total Cost:** 104497.92

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 5: Nested Loop

**Operator ID:** 5

**Plan Rows:** 100,328

**Plan Width:** 24

**Startup Cost:** 4536.64

**Total Cost:** 72396.32

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 6: Hash Join

**Operator ID:** 6

**Plan Rows:** 46,189

**Plan Width:** 12

**Startup Cost:** 4536.21

**Total Cost:** 37331.91

**Referenced Tables:** customer, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 7: Seq Scan

**Operator ID:** 7

**Plan Rows:** 232,872

**Plan Width:** 16

**Startup Cost:** 0.00

**Total Cost:** 32184.39

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 8: Hash

**Operator ID:** 8

**Plan Rows:** 12,397

**Plan Width:** 4

**Startup Cost:** 4381.25

**Total Cost:** 4381.25

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 12,397

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 4381.25

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 10: Index Scan

**Operator ID:** 10

**Plan Rows:** 3

**Plan Width:** 16

**Startup Cost:** 0.43

**Total Cost:** 0.73

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

## 4. Q4_100_seed_812199069.sql

**Template:** Q4

**Total Operators:** 7

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 5

**Plan Width:** 24

**Startup Cost:** 66871.03

**Total Cost:** 66872.93

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 2: Gather Merge

**Operator ID:** 2

**Plan Rows:** 15

**Plan Width:** 24

**Startup Cost:** 66871.03

**Total Cost:** 66872.80

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 3: Sort

**Operator ID:** 3

**Plan Rows:** 5

**Plan Width:** 24

**Startup Cost:** 65870.99

**Total Cost:** 65871.00

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 4: Aggregate

**Operator ID:** 4

**Plan Rows:** 5

**Plan Width:** 24

**Startup Cost:** 65870.88

**Total Cost:** 65870.93

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 5: Nested Loop

**Operator ID:** 5

**Plan Rows:** 14,866

**Plan Width:** 16

**Startup Cost:** 0.43

**Total Cost:** 65796.55

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 6: Seq Scan

**Operator ID:** 6

**Plan Rows:** 18,230

**Plan Width:** 20

**Startup Cost:** 0.00

**Total Cost:** 33394.06

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 7: Index Scan

**Operator ID:** 7

**Plan Rows:** 2

**Plan Width:** 4

**Startup Cost:** 0.43

**Total Cost:** 2.31

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

## 5. Q5_100_seed_812199069.sql

**Template:** Q5

**Total Operators:** 20

### Operator 1: Sort

**Operator ID:** 1

**Plan Rows:** 25

**Plan Width:** 136

**Startup Cost:** 57910.47

**Total Cost:** 57910.53

**Referenced Tables:** (sum((lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 2: Aggregate

**Operator ID:** 2

**Plan Rows:** 25

**Plan Width:** 136

**Startup Cost:** 57870.66

**Total Cost:** 57909.89

**Referenced Tables:** nation, sum((lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 3: Gather Merge

**Operator ID:** 3

**Plan Rows:** 75

**Plan Width:** 136

**Startup Cost:** 57870.66

**Total Cost:** 57909.01

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 4: Aggregate

**Operator ID:** 4

**Plan Rows:** 25

**Plan Width:** 136

**Startup Cost:** 56870.62

**Total Cost:** 56900.16

**Referenced Tables:** PARTIAL sum((lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 5: Sort

**Operator ID:** 5

**Plan Rows:** 2,338

**Plan Width:** 116

**Startup Cost:** 56870.62

**Total Cost:** 56876.47

**Referenced Tables:** lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |

---

### Operator 6: Hash Join

**Operator ID:** 6

**Plan Rows:** 2,338

**Plan Width:** 116

**Startup Cost:** 5216.52

**Total Cost:** 56739.80

**Referenced Tables:** customer, lineitem, nation, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 7: Nested Loop

**Operator ID:** 7

**Plan Rows:** 58,459

**Plan Width:** 128

**Startup Cost:** 4743.52

**Total Cost:** 55959.89

**Referenced Tables:** customer, lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |

---

### Operator 8: Hash Join

**Operator ID:** 8

**Plan Rows:** 14,612

**Plan Width:** 116

**Startup Cost:** 4743.09

**Total Cost:** 38472.01

**Referenced Tables:** customer, nation, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| nation | 25 | 1 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 73,059

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 33394.06

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 10: Hash

**Operator ID:** 10

**Plan Rows:** 12,500

**Plan Width:** 116

**Startup Cost:** 4586.84

**Total Cost:** 4586.84

**Referenced Tables:** customer, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| nation | 25 | 1 | table |

---

### Operator 11: Hash Join

**Operator ID:** 11

**Plan Rows:** 12,500

**Plan Width:** 116

**Startup Cost:** 2.46

**Total Cost:** 4586.84

**Referenced Tables:** customer, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| nation | 25 | 1 | table |

---

### Operator 12: Seq Scan

**Operator ID:** 12

**Plan Rows:** 62,500

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 4225.00

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 13: Hash

**Operator ID:** 13

**Plan Rows:** 5

**Plan Width:** 108

**Startup Cost:** 2.40

**Total Cost:** 2.40

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 14: Hash Join

**Operator ID:** 14

**Plan Rows:** 5

**Plan Width:** 108

**Startup Cost:** 1.07

**Total Cost:** 2.40

**Referenced Tables:** nation, region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| region | 5 | 1 | table |

---

### Operator 15: Seq Scan

**Operator ID:** 15

**Plan Rows:** 25

**Plan Width:** 112

**Startup Cost:** 0.00

**Total Cost:** 1.25

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 16: Hash

**Operator ID:** 16

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 1.06

**Total Cost:** 1.06

**Referenced Tables:** region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 17: Seq Scan

**Operator ID:** 17

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.06

**Referenced Tables:** region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 18: Index Scan

**Operator ID:** 18

**Plan Rows:** 5

**Plan Width:** 20

**Startup Cost:** 0.43

**Total Cost:** 1.15

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 19: Hash

**Operator ID:** 19

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 323.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 20: Seq Scan

**Operator ID:** 20

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

## 6. Q6_100_seed_812199069.sql

**Template:** Q6

**Total Operators:** 4

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 140720.25

**Total Cost:** 140720.26

**No table references found**

---

### Operator 2: Gather

**Operator ID:** 2

**Plan Rows:** 5

**Plan Width:** 32

**Startup Cost:** 140719.71

**Total Cost:** 140720.22

**No table references found**

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 139719.71

**Total Cost:** 139719.72

**No table references found**

---

### Operator 4: Seq Scan

**Operator ID:** 4

**Plan Rows:** 22,848

**Plan Width:** 12

**Startup Cost:** 0.00

**Total Cost:** 139605.47

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

## 7. Q7_100_seed_812199069.sql

**Template:** Q7

**Total Operators:** 18

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 6,078

**Plan Width:** 272

**Startup Cost:** 64308.27

**Total Cost:** 65209.68

**Referenced Tables:** (EXTRACT(year FROM lineitem, n1, n2, sum((lineitem

---

### Operator 2: Gather Merge

**Operator ID:** 2

**Plan Rows:** 6,078

**Plan Width:** 252

**Startup Cost:** 64308.27

**Total Cost:** 65027.34

**Referenced Tables:** lineitem, n1, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 3: Sort

**Operator ID:** 3

**Plan Rows:** 1,961

**Plan Width:** 252

**Startup Cost:** 63308.23

**Total Cost:** 63313.13

**Referenced Tables:** (EXTRACT(year FROM lineitem, lineitem, n1, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 4: Hash Join

**Operator ID:** 4

**Plan Rows:** 1,961

**Plan Width:** 252

**Startup Cost:** 4846.31

**Total Cost:** 63200.99

**Referenced Tables:** EXTRACT(year FROM lineitem, lineitem, n1, n2, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 5: Nested Loop

**Operator ID:** 5

**Plan Rows:** 47,115

**Plan Width:** 124

**Startup Cost:** 4481.21

**Total Cost:** 62578.93

**Referenced Tables:** lineitem, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 6: Hash Join

**Operator ID:** 6

**Plan Rows:** 38,710

**Plan Width:** 108

**Startup Cost:** 4480.77

**Total Cost:** 37431.29

**Referenced Tables:** customer, n2, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 7: Seq Scan

**Operator ID:** 7

**Plan Rows:** 483,871

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 30974.71

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 8: Hash

**Operator ID:** 8

**Plan Rows:** 5,000

**Plan Width:** 108

**Startup Cost:** 4418.27

**Total Cost:** 4418.27

**Referenced Tables:** customer, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 9: Hash Join

**Operator ID:** 9

**Plan Rows:** 5,000

**Plan Width:** 108

**Startup Cost:** 1.40

**Total Cost:** 4418.27

**Referenced Tables:** customer, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 10: Seq Scan

**Operator ID:** 10

**Plan Rows:** 62,500

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 4225.00

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 11: Hash

**Operator ID:** 11

**Plan Rows:** 2

**Plan Width:** 108

**Startup Cost:** 1.38

**Total Cost:** 1.38

**Referenced Tables:** n2

---

### Operator 12: Seq Scan

**Operator ID:** 12

**Plan Rows:** 2

**Plan Width:** 108

**Startup Cost:** 0.00

**Total Cost:** 1.38

**Referenced Tables:** n2, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 13: Index Scan

**Operator ID:** 13

**Plan Rows:** 1

**Plan Width:** 24

**Startup Cost:** 0.43

**Total Cost:** 0.64

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 14: Hash

**Operator ID:** 14

**Plan Rows:** 800

**Plan Width:** 108

**Startup Cost:** 355.10

**Total Cost:** 355.10

**Referenced Tables:** n1, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 15: Hash Join

**Operator ID:** 15

**Plan Rows:** 800

**Plan Width:** 108

**Startup Cost:** 1.40

**Total Cost:** 355.10

**Referenced Tables:** n1, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 16: Seq Scan

**Operator ID:** 16

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 17: Hash

**Operator ID:** 17

**Plan Rows:** 2

**Plan Width:** 108

**Startup Cost:** 1.38

**Total Cost:** 1.38

**Referenced Tables:** n1

---

### Operator 18: Seq Scan

**Operator ID:** 18

**Plan Rows:** 2

**Plan Width:** 108

**Startup Cost:** 0.00

**Total Cost:** 1.38

**Referenced Tables:** n1, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

## 8. Q8_100_seed_812199069.sql

**Template:** Q8

**Total Operators:** 23

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 2,372

**Plan Width:** 64

**Startup Cost:** 71545.37

**Total Cost:** 71920.87

**Referenced Tables:** (EXTRACT(year FROM orders

---

### Operator 2: Gather Merge

**Operator ID:** 2

**Plan Rows:** 2,372

**Plan Width:** 148

**Startup Cost:** 71545.37

**Total Cost:** 71825.99

**Referenced Tables:** lineitem, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 3: Sort

**Operator ID:** 3

**Plan Rows:** 765

**Plan Width:** 148

**Startup Cost:** 70545.33

**Total Cost:** 70547.24

**Referenced Tables:** (EXTRACT(year FROM orders, lineitem, n2

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 4: Hash Join

**Operator ID:** 4

**Plan Rows:** 765

**Plan Width:** 148

**Startup Cost:** 9921.79

**Total Cost:** 70508.69

**Referenced Tables:** EXTRACT(year FROM orders, lineitem, n2, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 5: Nested Loop

**Operator ID:** 5

**Plan Rows:** 765

**Plan Width:** 20

**Startup Cost:** 9920.22

**Total Cost:** 70502.86

**Referenced Tables:** lineitem, orders, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 6: Hash Join

**Operator ID:** 6

**Plan Rows:** 765

**Plan Width:** 20

**Startup Cost:** 9919.94

**Total Cost:** 70271.42

**Referenced Tables:** lineitem, orders, part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |
| part | 200,000 | 4,128 | table |

---

### Operator 7: Nested Loop

**Operator ID:** 7

**Plan Rows:** 118,013

**Plan Width:** 24

**Startup Cost:** 4743.52

**Total Cost:** 64785.20

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 8: Hash Join

**Operator ID:** 8

**Plan Rows:** 29,497

**Plan Width:** 8

**Startup Cost:** 4743.09

**Total Cost:** 38813.14

**Referenced Tables:** customer, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 147,487

**Plan Width:** 12

**Startup Cost:** 0.00

**Total Cost:** 33394.06

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 10: Hash

**Operator ID:** 10

**Plan Rows:** 12,500

**Plan Width:** 4

**Startup Cost:** 4586.84

**Total Cost:** 4586.84

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 11: Hash Join

**Operator ID:** 11

**Plan Rows:** 12,500

**Plan Width:** 4

**Startup Cost:** 2.46

**Total Cost:** 4586.84

**Referenced Tables:** customer, n1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 12: Seq Scan

**Operator ID:** 12

**Plan Rows:** 62,500

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 4225.00

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 13: Hash

**Operator ID:** 13

**Plan Rows:** 5

**Plan Width:** 4

**Startup Cost:** 2.40

**Total Cost:** 2.40

**Referenced Tables:** n1

---

### Operator 14: Hash Join

**Operator ID:** 14

**Plan Rows:** 5

**Plan Width:** 4

**Startup Cost:** 1.07

**Total Cost:** 2.40

**Referenced Tables:** n1, region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 15: Seq Scan

**Operator ID:** 15

**Plan Rows:** 25

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 1.25

**Referenced Tables:** n1, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 16: Hash

**Operator ID:** 16

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 1.06

**Total Cost:** 1.06

**Referenced Tables:** region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 17: Seq Scan

**Operator ID:** 17

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.06

**Referenced Tables:** region

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| region | 5 | 1 | table |

---

### Operator 18: Index Scan

**Operator ID:** 18

**Plan Rows:** 5

**Plan Width:** 24

**Startup Cost:** 0.43

**Total Cost:** 0.83

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 19: Hash

**Operator ID:** 19

**Plan Rows:** 540

**Plan Width:** 4

**Startup Cost:** 5169.67

**Total Cost:** 5169.67

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 20: Seq Scan

**Operator ID:** 20

**Plan Rows:** 540

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 5169.67

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 21: Index Scan

**Operator ID:** 21

**Plan Rows:** 1

**Plan Width:** 8

**Startup Cost:** 0.29

**Total Cost:** 0.30

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 22: Hash

**Operator ID:** 22

**Plan Rows:** 25

**Plan Width:** 108

**Startup Cost:** 1.25

**Total Cost:** 1.25

**Referenced Tables:** n2

---

### Operator 23: Seq Scan

**Operator ID:** 23

**Plan Rows:** 25

**Plan Width:** 108

**Startup Cost:** 0.00

**Total Cost:** 1.25

**Referenced Tables:** n2, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

## 9. Q9_100_seed_812199069.sql

**Template:** Q9

**Total Operators:** 19

### Operator 1: Sort

**Operator ID:** 1

**Plan Rows:** 60,150

**Plan Width:** 168

**Startup Cost:** 215550.82

**Total Cost:** 215701.20

**Referenced Tables:** (EXTRACT(year FROM orders, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 2: Aggregate

**Operator ID:** 2

**Plan Rows:** 60,150

**Plan Width:** 168

**Startup Cost:** 209873.78

**Total Cost:** 210776.03

**Referenced Tables:** (EXTRACT(year FROM orders, nation, sum(((lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 3: Gather

**Operator ID:** 3

**Plan Rows:** 180,450

**Plan Width:** 168

**Startup Cost:** 189122.03

**Total Cost:** 208069.28

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 4: Aggregate

**Operator ID:** 4

**Plan Rows:** 60,150

**Plan Width:** 168

**Startup Cost:** 188122.03

**Total Cost:** 189024.28

**Referenced Tables:** EXTRACT(year FROM orders, PARTIAL sum(((lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 5: Hash Join

**Operator ID:** 5

**Plan Rows:** 155,180

**Plan Width:** 159

**Startup Cost:** 151918.84

**Total Cost:** 185406.38

**Referenced Tables:** EXTRACT(year FROM orders, lineitem, nation, orders, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |
| orders | 1,500,000 | 26,136 | table |
| partsupp | 800,000 | 17,560 | table |

---

### Operator 6: Seq Scan

**Operator ID:** 6

**Plan Rows:** 483,871

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 30974.71

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 7: Hash

**Operator ID:** 7

**Plan Rows:** 96,211

**Plan Width:** 131

**Startup Cost:** 150716.21

**Total Cost:** 150716.21

**Referenced Tables:** lineitem, nation, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |
| partsupp | 800,000 | 17,560 | table |

---

### Operator 8: Hash Join

**Operator ID:** 8

**Plan Rows:** 96,211

**Plan Width:** 131

**Startup Cost:** 17111.79

**Total Cost:** 150716.21

**Referenced Tables:** lineitem, nation, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 1,200,243

**Plan Width:** 29

**Startup Cost:** 0.00

**Total Cost:** 124602.43

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 10: Hash

**Operator ID:** 10

**Plan Rows:** 26,720

**Plan Width:** 126

**Startup Cost:** 16710.99

**Total Cost:** 16710.99

**Referenced Tables:** nation, part, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 11: Hash Join

**Operator ID:** 11

**Plan Rows:** 26,720

**Plan Width:** 126

**Startup Cost:** 449.99

**Total Cost:** 16710.99

**Referenced Tables:** nation, part, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 12: Hash Join

**Operator ID:** 12

**Plan Rows:** 26,720

**Plan Width:** 26

**Startup Cost:** 448.43

**Total Cost:** 16627.40

**Referenced Tables:** part, partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 13: Nested Loop

**Operator ID:** 13

**Plan Rows:** 26,720

**Plan Width:** 18

**Startup Cost:** 0.42

**Total Cost:** 16109.23

**Referenced Tables:** part, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |

---

### Operator 14: Seq Scan

**Operator ID:** 14

**Plan Rows:** 6,680

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 5169.67

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 15: Index Scan

**Operator ID:** 15

**Plan Rows:** 4

**Plan Width:** 14

**Startup Cost:** 0.42

**Total Cost:** 1.60

**Referenced Tables:** partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 16: Hash

**Operator ID:** 16

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 323.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 17: Seq Scan

**Operator ID:** 17

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 18: Hash

**Operator ID:** 18

**Plan Rows:** 25

**Plan Width:** 108

**Startup Cost:** 1.25

**Total Cost:** 1.25

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 19: Seq Scan

**Operator ID:** 19

**Plan Rows:** 25

**Plan Width:** 108

**Startup Cost:** 0.00

**Total Cost:** 1.25

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

## 10. Q10_100_seed_812199069.sql

**Template:** Q10

**Total Operators:** 13

### Operator 1: Limit

**Operator ID:** 1

**Plan Rows:** 20

**Plan Width:** 280

**Startup Cost:** 90477.26

**Total Cost:** 90477.31

**Referenced Tables:** customer, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| nation | 25 | 1 | table |

---

### Operator 2: Sort

**Operator ID:** 2

**Plan Rows:** 56,515

**Plan Width:** 280

**Startup Cost:** 90477.26

**Total Cost:** 90618.54

**Referenced Tables:** (sum((lineitem, customer, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| nation | 25 | 1 | table |

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 56,515

**Plan Width:** 280

**Startup Cost:** 88266.98

**Total Cost:** 88973.41

**Referenced Tables:** customer, nation, sum((lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| nation | 25 | 1 | table |

---

### Operator 4: Gather

**Operator ID:** 4

**Plan Rows:** 56,515

**Plan Width:** 260

**Startup Cost:** 6008.24

**Total Cost:** 87560.54

**Referenced Tables:** customer, lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |

---

### Operator 5: Hash Join

**Operator ID:** 5

**Plan Rows:** 18,231

**Plan Width:** 260

**Startup Cost:** 5008.24

**Total Cost:** 80909.04

**Referenced Tables:** customer, lineitem, nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| nation | 25 | 1 | table |

---

### Operator 6: Hash Join

**Operator ID:** 6

**Plan Rows:** 18,231

**Plan Width:** 160

**Startup Cost:** 5006.68

**Total Cost:** 80851.51

**Referenced Tables:** customer, lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 7: Nested Loop

**Operator ID:** 7

**Plan Rows:** 18,231

**Plan Width:** 16

**Startup Cost:** 0.43

**Total Cost:** 75797.40

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 8: Seq Scan

**Operator ID:** 8

**Plan Rows:** 18,419

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 33394.06

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 9: Index Scan

**Operator ID:** 9

**Plan Rows:** 1

**Plan Width:** 16

**Startup Cost:** 0.43

**Total Cost:** 2.29

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 10: Hash

**Operator ID:** 10

**Plan Rows:** 62,500

**Plan Width:** 148

**Startup Cost:** 4225.00

**Total Cost:** 4225.00

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 11: Seq Scan

**Operator ID:** 11

**Plan Rows:** 62,500

**Plan Width:** 148

**Startup Cost:** 0.00

**Total Cost:** 4225.00

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 12: Hash

**Operator ID:** 12

**Plan Rows:** 25

**Plan Width:** 108

**Startup Cost:** 1.25

**Total Cost:** 1.25

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 13: Seq Scan

**Operator ID:** 13

**Plan Rows:** 25

**Plan Width:** 108

**Startup Cost:** 0.00

**Total Cost:** 1.25

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

## 11. Q11_100_seed_812199069.sql

**Template:** Q11

**Total Operators:** 20

### Operator 1: Sort

**Operator ID:** 1

**Plan Rows:** 10,667

**Plan Width:** 36

**Startup Cost:** 49934.72

**Total Cost:** 49961.39

**Referenced Tables:** (sum((partsupp, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 2: Aggregate

**Operator ID:** 2

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 22649.40

**Total Cost:** 22649.41

**No table references found**

---

### Operator 3: Gather

**Operator ID:** 3

**Plan Rows:** 3

**Plan Width:** 32

**Startup Cost:** 22649.07

**Total Cost:** 22649.38

**No table references found**

---

### Operator 4: Aggregate

**Operator ID:** 4

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 21649.07

**Total Cost:** 21649.08

**Referenced Tables:** PARTIAL sum((partsupp_1

---

### Operator 5: Hash Join

**Operator ID:** 5

**Plan Rows:** 10,323

**Plan Width:** 10

**Startup Cost:** 360.02

**Total Cost:** 21571.64

**Referenced Tables:** partsupp_1, supplier_1

---

### Operator 6: Seq Scan

**Operator ID:** 6

**Plan Rows:** 258,065

**Plan Width:** 14

**Startup Cost:** 0.00

**Total Cost:** 20140.65

**Referenced Tables:** partsupp, partsupp_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 7: Hash

**Operator ID:** 7

**Plan Rows:** 400

**Plan Width:** 4

**Startup Cost:** 355.02

**Total Cost:** 355.02

**Referenced Tables:** supplier_1

---

### Operator 8: Hash Join

**Operator ID:** 8

**Plan Rows:** 400

**Plan Width:** 4

**Startup Cost:** 1.32

**Total Cost:** 355.02

**Referenced Tables:** nation_1, supplier_1

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier, supplier_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 10: Hash

**Operator ID:** 10

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 1.31

**Total Cost:** 1.31

**Referenced Tables:** nation_1

---

### Operator 11: Seq Scan

**Operator ID:** 11

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.31

**Referenced Tables:** nation, nation_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 12: Aggregate

**Operator ID:** 12

**Plan Rows:** 10,667

**Plan Width:** 36

**Startup Cost:** 26091.64

**Total Cost:** 26571.64

**Referenced Tables:** partsupp, sum((partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 13: Gather

**Operator ID:** 13

**Plan Rows:** 32,000

**Plan Width:** 14

**Startup Cost:** 1360.03

**Total Cost:** 25771.64

**Referenced Tables:** partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 14: Hash Join

**Operator ID:** 14

**Plan Rows:** 10,323

**Plan Width:** 14

**Startup Cost:** 360.02

**Total Cost:** 21571.64

**Referenced Tables:** partsupp, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 15: Seq Scan

**Operator ID:** 15

**Plan Rows:** 258,065

**Plan Width:** 18

**Startup Cost:** 0.00

**Total Cost:** 20140.65

**Referenced Tables:** partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 16: Hash

**Operator ID:** 16

**Plan Rows:** 400

**Plan Width:** 4

**Startup Cost:** 355.02

**Total Cost:** 355.02

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 17: Hash Join

**Operator ID:** 17

**Plan Rows:** 400

**Plan Width:** 4

**Startup Cost:** 1.32

**Total Cost:** 355.02

**Referenced Tables:** nation, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 18: Seq Scan

**Operator ID:** 18

**Plan Rows:** 10,000

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 19: Hash

**Operator ID:** 19

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 1.31

**Total Cost:** 1.31

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 20: Seq Scan

**Operator ID:** 20

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.31

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

## 12. Q12_100_seed_812199069.sql

**Template:** Q12

**Total Operators:** 7

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 7

**Plan Width:** 27

**Startup Cost:** 148539.70

**Total Cost:** 148659.94

**Referenced Tables:** lineitem, sum(CASE WHEN ((orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 2: Gather Merge

**Operator ID:** 2

**Plan Rows:** 35

**Plan Width:** 27

**Startup Cost:** 148539.70

**Total Cost:** 148659.60

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 7

**Plan Width:** 27

**Startup Cost:** 147539.62

**Total Cost:** 147655.31

**Referenced Tables:** PARTIAL sum(CASE WHEN ((orders, lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 4: Sort

**Operator ID:** 4

**Plan Rows:** 5,781

**Plan Width:** 27

**Startup Cost:** 147539.62

**Total Cost:** 147554.07

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 5: Nested Loop

**Operator ID:** 5

**Plan Rows:** 5,781

**Plan Width:** 27

**Startup Cost:** 0.43

**Total Cost:** 147178.39

**Referenced Tables:** lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 6: Seq Scan

**Operator ID:** 6

**Plan Rows:** 5,781

**Plan Width:** 15

**Startup Cost:** 0.00

**Total Cost:** 139605.47

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 7: Index Scan

**Operator ID:** 7

**Plan Rows:** 1

**Plan Width:** 20

**Startup Cost:** 0.43

**Total Cost:** 1.31

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

## 13. Q13_100_seed_812199069.sql

**Template:** Q13

**Total Operators:** 7

### Operator 1: Sort

**Operator ID:** 1

**Plan Rows:** 200

**Plan Width:** 16

**Startup Cost:** 64579.49

**Total Cost:** 64579.99

**Referenced Tables:** (count(orders

---

### Operator 2: Aggregate

**Operator ID:** 2

**Plan Rows:** 200

**Plan Width:** 16

**Startup Cost:** 64569.85

**Total Cost:** 64571.85

**Referenced Tables:** count(orders

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 150,000

**Plan Width:** 12

**Startup Cost:** 60819.85

**Total Cost:** 62319.85

**Referenced Tables:** count(orders, customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 4: Hash Join

**Operator ID:** 4

**Plan Rows:** 1,487,976

**Plan Width:** 8

**Startup Cost:** 4587.92

**Total Cost:** 53379.97

**Referenced Tables:** customer, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 5: Seq Scan

**Operator ID:** 5

**Plan Rows:** 1,487,976

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 44886.00

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 6: Hash

**Operator ID:** 6

**Plan Rows:** 150,000

**Plan Width:** 4

**Startup Cost:** 2712.92

**Total Cost:** 2712.92

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 7: Index Only Scan

**Operator ID:** 7

**Plan Rows:** 150,000

**Plan Width:** 4

**Startup Cost:** 0.42

**Total Cost:** 2712.92

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

## 14. Q14_100_seed_812199069.sql

**Template:** Q14

**Total Operators:** 7

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 137921.76

**Total Cost:** 137921.78

**No table references found**

---

### Operator 2: Gather

**Operator ID:** 2

**Plan Rows:** 5

**Plan Width:** 64

**Startup Cost:** 137921.20

**Total Cost:** 137921.71

**No table references found**

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 1

**Plan Width:** 64

**Startup Cost:** 136921.20

**Total Cost:** 136921.21

**Referenced Tables:** PARTIAL sum((lineitem, PARTIAL sum(CASE WHEN ((part

---

### Operator 4: Hash Join

**Operator ID:** 4

**Plan Rows:** 15,630

**Plan Width:** 33

**Startup Cost:** 6003.00

**Total Cost:** 136647.67

**Referenced Tables:** lineitem, part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| part | 200,000 | 4,128 | table |

---

### Operator 5: Seq Scan

**Operator ID:** 5

**Plan Rows:** 15,630

**Plan Width:** 16

**Startup Cost:** 0.00

**Total Cost:** 130603.64

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 6: Hash

**Operator ID:** 6

**Plan Rows:** 83,333

**Plan Width:** 25

**Startup Cost:** 4961.33

**Total Cost:** 4961.33

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 7: Seq Scan

**Operator ID:** 7

**Plan Rows:** 83,333

**Plan Width:** 25

**Startup Cost:** 0.00

**Total Cost:** 4961.33

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

## 15. Q16_100_seed_812199069.sql

**Template:** Q16

**Total Operators:** 9

### Operator 1: Sort

**Operator ID:** 1

**Plan Rows:** 15,945

**Plan Width:** 44

**Startup Cost:** 26886.13

**Total Cost:** 26925.99

**Referenced Tables:** (count(DISTINCT partsupp, part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 2: Aggregate

**Operator ID:** 2

**Plan Rows:** 15,945

**Plan Width:** 44

**Startup Cost:** 17959.83

**Total Cost:** 25773.10

**Referenced Tables:** count(DISTINCT partsupp, part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 3: Gather Merge

**Operator ID:** 3

**Plan Rows:** 58,996

**Plan Width:** 40

**Startup Cost:** 17959.83

**Total Cost:** 25023.69

**Referenced Tables:** part, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |

---

### Operator 4: Sort

**Operator ID:** 4

**Plan Rows:** 14,749

**Plan Width:** 40

**Startup Cost:** 16959.77

**Total Cost:** 16996.64

**Referenced Tables:** part, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |

---

### Operator 5: Hash Join

**Operator ID:** 5

**Plan Rows:** 14,749

**Plan Width:** 40

**Startup Cost:** 6713.40

**Total Cost:** 15938.52

**Referenced Tables:** part, partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |
| partsupp | 800,000 | 17,560 | table |

---

### Operator 6: Index Only Scan

**Operator ID:** 6

**Plan Rows:** 100,000

**Plan Width:** 8

**Startup Cost:** 348.43

**Total Cost:** 9311.05

**Referenced Tables:** partsupp

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| partsupp | 800,000 | 17,560 | table |

---

### Operator 7: Seq Scan

**Operator ID:** 7

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 348.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 8: Hash

**Operator ID:** 8

**Plan Rows:** 12,291

**Plan Width:** 40

**Startup Cost:** 6211.33

**Total Cost:** 6211.33

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 12,291

**Plan Width:** 40

**Startup Cost:** 0.00

**Total Cost:** 6211.33

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

## 16. Q18_100_seed_812199069.sql

**Template:** Q18

**Total Operators:** 16

### Operator 1: Limit

**Operator ID:** 1

**Plan Rows:** 100

**Plan Width:** 71

**Startup Cost:** 732650.26

**Total Cost:** 732650.51

**Referenced Tables:** customer, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 2: Sort

**Operator ID:** 2

**Plan Rows:** 1,631,266

**Plan Width:** 71

**Startup Cost:** 732650.26

**Total Cost:** 736728.42

**Referenced Tables:** customer, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 1,631,266

**Plan Width:** 71

**Startup Cost:** 341523.47

**Total Cost:** 670304.45

**Referenced Tables:** customer, orders, sum(lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 4: Gather Merge

**Operator ID:** 4

**Plan Rows:** 1,631,266

**Plan Width:** 44

**Startup Cost:** 341523.47

**Total Cost:** 637679.13

**Referenced Tables:** customer, lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 5: Incremental Sort

**Operator ID:** 5

**Plan Rows:** 526,215

**Plan Width:** 44

**Startup Cost:** 340523.43

**Total Cost:** 445005.33

**Referenced Tables:** customer, lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 6: Nested Loop

**Operator ID:** 6

**Plan Rows:** 526,215

**Plan Width:** 44

**Startup Cost:** 340522.80

**Total Cost:** 430663.58

**Referenced Tables:** customer, lineitem, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| lineitem | 6,001,215 | 112,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 7: Merge Join

**Operator ID:** 7

**Plan Rows:** 131,527

**Plan Width:** 43

**Startup Cost:** 340522.36

**Total Cost:** 343245.24

**Referenced Tables:** customer, lineitem_1, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 8: Sort

**Operator ID:** 8

**Plan Rows:** 131,527

**Plan Width:** 24

**Startup Cost:** 322526.40

**Total Cost:** 322855.22

**Referenced Tables:** lineitem_1, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 9: Hash Join

**Operator ID:** 9

**Plan Rows:** 131,527

**Plan Width:** 24

**Startup Cost:** 279098.44

**Total Cost:** 311343.31

**Referenced Tables:** lineitem_1, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 10: Seq Scan

**Operator ID:** 10

**Plan Rows:** 483,871

**Plan Width:** 20

**Startup Cost:** 0.00

**Total Cost:** 30974.71

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 11: Hash

**Operator ID:** 11

**Plan Rows:** 407,734

**Plan Width:** 4

**Startup Cost:** 274001.77

**Total Cost:** 274001.77

**Referenced Tables:** lineitem_1

---

### Operator 12: Aggregate

**Operator ID:** 12

**Plan Rows:** 407,734

**Plan Width:** 4

**Startup Cost:** 0.43

**Total Cost:** 274001.77

**Referenced Tables:** lineitem_1

---

### Operator 13: Index Scan

**Operator ID:** 13

**Plan Rows:** 6,001,215

**Plan Width:** 9

**Startup Cost:** 0.43

**Total Cost:** 225647.66

**Referenced Tables:** lineitem, lineitem_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 14: Sort

**Operator ID:** 14

**Plan Rows:** 150,000

**Plan Width:** 23

**Startup Cost:** 17995.95

**Total Cost:** 18370.95

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 15: Seq Scan

**Operator ID:** 15

**Plan Rows:** 150,000

**Plan Width:** 23

**Startup Cost:** 0.00

**Total Cost:** 5100.00

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 16: Index Scan

**Operator ID:** 16

**Plan Rows:** 5

**Plan Width:** 9

**Startup Cost:** 0.43

**Total Cost:** 0.61

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

## 17. Q19_100_seed_812199069.sql

**Template:** Q19

**Total Operators:** 7

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 157339.26

**Total Cost:** 157339.27

**Referenced Tables:** sum((lineitem

---

### Operator 2: Gather

**Operator ID:** 2

**Plan Rows:** 5

**Plan Width:** 32

**Startup Cost:** 157338.73

**Total Cost:** 157339.24

**No table references found**

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 156338.73

**Total Cost:** 156338.74

**Referenced Tables:** PARTIAL sum((lineitem

---

### Operator 4: Hash Join

**Operator ID:** 4

**Plan Rows:** 23

**Plan Width:** 12

**Startup Cost:** 7672.22

**Total Cost:** 156338.55

**Referenced Tables:** lineitem, part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |
| part | 200,000 | 4,128 | table |

---

### Operator 5: Seq Scan

**Operator ID:** 5

**Plan Rows:** 22,493

**Plan Width:** 21

**Startup Cost:** 0.00

**Total Cost:** 148607.29

**Referenced Tables:** lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 6: Hash

**Operator ID:** 6

**Plan Rows:** 204

**Plan Width:** 30

**Startup Cost:** 7669.67

**Total Cost:** 7669.67

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

### Operator 7: Seq Scan

**Operator ID:** 7

**Plan Rows:** 204

**Plan Width:** 30

**Startup Cost:** 0.00

**Total Cost:** 7669.67

**Referenced Tables:** part

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| part | 200,000 | 4,128 | table |

---

## 18. Q21_100_seed_812199069.sql

**Template:** Q21

**Total Operators:** 18

### Operator 1: Limit

**Operator ID:** 1

**Plan Rows:** 1

**Plan Width:** 34

**Startup Cost:** 140017.17

**Total Cost:** 140017.17

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 2: Sort

**Operator ID:** 2

**Plan Rows:** 1

**Plan Width:** 34

**Startup Cost:** 140017.17

**Total Cost:** 140017.17

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 3: Aggregate

**Operator ID:** 3

**Plan Rows:** 1

**Plan Width:** 34

**Startup Cost:** 140017.14

**Total Cost:** 140017.16

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 4: Sort

**Operator ID:** 4

**Plan Rows:** 1

**Plan Width:** 26

**Startup Cost:** 140017.14

**Total Cost:** 140017.14

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 5: Nested Loop

**Operator ID:** 5

**Plan Rows:** 1

**Plan Width:** 26

**Startup Cost:** 1361.32

**Total Cost:** 140017.13

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 6: Nested Loop

**Operator ID:** 6

**Plan Rows:** 1

**Plan Width:** 34

**Startup Cost:** 1360.89

**Total Cost:** 140016.66

**Referenced Tables:** l1, l2, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 7: Gather

**Operator ID:** 7

**Plan Rows:** 1

**Plan Width:** 34

**Startup Cost:** 1360.46

**Total Cost:** 140016.04

**Referenced Tables:** l1, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 8: Nested Loop

**Operator ID:** 8

**Plan Rows:** 1

**Plan Width:** 34

**Startup Cost:** 360.46

**Total Cost:** 139015.94

**Referenced Tables:** l1, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 9: Hash Join

**Operator ID:** 9

**Plan Rows:** 16,003

**Plan Width:** 34

**Startup Cost:** 360.02

**Total Cost:** 129623.40

**Referenced Tables:** l1, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 10: Seq Scan

**Operator ID:** 10

**Plan Rows:** 400,081

**Plan Width:** 8

**Startup Cost:** 0.00

**Total Cost:** 127603.04

**Referenced Tables:** l1, lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 11: Hash

**Operator ID:** 11

**Plan Rows:** 400

**Plan Width:** 30

**Startup Cost:** 355.02

**Total Cost:** 355.02

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 12: Hash Join

**Operator ID:** 12

**Plan Rows:** 400

**Plan Width:** 30

**Startup Cost:** 1.32

**Total Cost:** 355.02

**Referenced Tables:** nation, supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |
| supplier | 10,000 | 223 | table |

---

### Operator 13: Seq Scan

**Operator ID:** 13

**Plan Rows:** 10,000

**Plan Width:** 34

**Startup Cost:** 0.00

**Total Cost:** 323.00

**Referenced Tables:** supplier

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| supplier | 10,000 | 223 | table |

---

### Operator 14: Hash

**Operator ID:** 14

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 1.31

**Total Cost:** 1.31

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 15: Seq Scan

**Operator ID:** 15

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 1.31

**Referenced Tables:** nation

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| nation | 25 | 1 | table |

---

### Operator 16: Index Scan

**Operator ID:** 16

**Plan Rows:** 2

**Plan Width:** 8

**Startup Cost:** 0.43

**Total Cost:** 0.62

**Referenced Tables:** l3, lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 17: Index Scan

**Operator ID:** 17

**Plan Rows:** 5

**Plan Width:** 8

**Startup Cost:** 0.43

**Total Cost:** 0.60

**Referenced Tables:** l2, lineitem

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| lineitem | 6,001,215 | 112,600 | table |

---

### Operator 18: Index Scan

**Operator ID:** 18

**Plan Rows:** 1

**Plan Width:** 4

**Startup Cost:** 0.43

**Total Cost:** 0.46

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

## 19. Q22_100_seed_812199069.sql

**Template:** Q22

**Total Operators:** 11

### Operator 1: Aggregate

**Operator ID:** 1

**Plan Rows:** 668

**Plan Width:** 72

**Startup Cost:** 48079.63

**Total Cost:** 48175.36

**Referenced Tables:** (SUBSTRING(customer, sum(customer

---

### Operator 2: Aggregate

**Operator ID:** 2

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 6245.82

**Total Cost:** 6245.83

**Referenced Tables:** avg(customer_1

---

### Operator 3: Gather

**Operator ID:** 3

**Plan Rows:** 2

**Plan Width:** 32

**Startup Cost:** 6245.60

**Total Cost:** 6245.81

**No table references found**

---

### Operator 4: Aggregate

**Operator ID:** 4

**Plan Rows:** 1

**Plan Width:** 32

**Startup Cost:** 5245.60

**Total Cost:** 5245.61

**Referenced Tables:** PARTIAL avg(customer_1

---

### Operator 5: Seq Scan

**Operator ID:** 5

**Plan Rows:** 1,988

**Plan Width:** 6

**Startup Cost:** 0.00

**Total Cost:** 5240.62

**Referenced Tables:** customer, customer_1

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 6: Gather Merge

**Operator ID:** 6

**Plan Rows:** 668

**Plan Width:** 38

**Startup Cost:** 41833.80

**Total Cost:** 41912.83

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 7: Sort

**Operator ID:** 7

**Plan Rows:** 215

**Plan Width:** 38

**Startup Cost:** 40833.76

**Total Cost:** 40834.30

**Referenced Tables:** (SUBSTRING(customer, customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 8: Hash Join

**Operator ID:** 8

**Plan Rows:** 215

**Plan Width:** 38

**Startup Cost:** 5249.74

**Total Cost:** 40825.43

**Referenced Tables:** SUBSTRING(customer, customer, orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |
| orders | 1,500,000 | 26,136 | table |

---

### Operator 9: Seq Scan

**Operator ID:** 9

**Plan Rows:** 483,871

**Plan Width:** 4

**Startup Cost:** 0.00

**Total Cost:** 30974.71

**Referenced Tables:** orders

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| orders | 1,500,000 | 26,136 | table |

---

### Operator 10: Hash

**Operator ID:** 10

**Plan Rows:** 729

**Plan Width:** 26

**Startup Cost:** 5240.62

**Total Cost:** 5240.62

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

### Operator 11: Seq Scan

**Operator ID:** 11

**Plan Rows:** 729

**Plan Width:** 26

**Startup Cost:** 0.00

**Total Cost:** 5240.62

**Referenced Tables:** customer

#### PG_CLASS Statistics

| Table Name | reltuples | relpages | Kind |
|------------|-----------|----------|------|
| customer | 150,000 | 3,600 | table |

---

