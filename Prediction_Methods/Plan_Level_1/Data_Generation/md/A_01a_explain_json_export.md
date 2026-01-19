# EXPLAIN JSON Export - Plan Level Features

**Generated:** 2026-01-12 23:24:59

**Total Templates:** 21

**Purpose:** Raw EXPLAIN JSON output for feature exploration.

**EXPLAIN Options:** `ANALYZE false, VERBOSE true, COSTS true, SUMMARY true, FORMAT JSON`

---

## 1. Q1 - Q1_100_seed_812199069.sql

**Template:** Q1

**File:** `Q1_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Partial Mode": "Finalize",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 170311.11,
      "Total Cost": 170315.88,
      "Plan Rows": 6,
      "Plan Width": 236,
      "Output": [
        "l_returnflag",
        "l_linestatus",
        "sum(l_quantity)",
        "sum(l_extendedprice)",
        "sum((l_extendedprice * ('1'::numeric - l_discount)))",
        "sum(((l_extendedprice * ('1'::numeric - l_discount)) * ('1'::numeric + l_tax)))",
        "avg(l_quantity)",
        "avg(l_extendedprice)",
        "avg(l_discount)",
        "count(*)"
      ],
      "Group Key": [
        "lineitem.l_returnflag",
        "lineitem.l_linestatus"
      ],
      "Plans": [
        {
          "Node Type": "Gather Merge",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 170311.11,
          "Total Cost": 170314.74,
          "Plan Rows": 30,
          "Plan Width": 236,
          "Output": [
            "l_returnflag",
            "l_linestatus",
            "(PARTIAL sum(l_quantity))",
            "(PARTIAL sum(l_extendedprice))",
            "(PARTIAL sum((l_extendedprice * ('1'::numeric - l_discount))))",
            "(PARTIAL sum(((l_extendedprice * ('1'::numeric - l_discount)) * ('1'::numeric + l_tax))))",
            "(PARTIAL avg(l_quantity))",
            "(PARTIAL avg(l_extendedprice))",
            "(PARTIAL avg(l_discount))",
            "(PARTIAL count(*))"
          ],
          "Workers Planned": 5,
          "Plans": [
            {
              "Node Type": "Sort",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 169311.04,
              "Total Cost": 169311.05,
              "Plan Rows": 6,
              "Plan Width": 236,
              "Output": [
                "l_returnflag",
                "l_linestatus",
                "(PARTIAL sum(l_quantity))",
                "(PARTIAL sum(l_extendedprice))",
                "(PARTIAL sum((l_extendedprice * ('1'::numeric - l_discount))))",
                "(PARTIAL sum(((l_extendedprice * ('1'::numeric - l_discount)) * ('1'::numeric + l_tax))))",
                "(PARTIAL avg(l_quantity))",
                "(PARTIAL avg(l_extendedprice))",
                "(PARTIAL avg(l_discount))",
                "(PARTIAL count(*))"
              ],
              "Sort Key": [
                "lineitem.l_returnflag",
                "lineitem.l_linestatus"
              ],
              "Plans": [
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Hashed",
                  "Partial Mode": "Partial",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 169310.82,
                  "Total Cost": 169310.96,
                  "Plan Rows": 6,
                  "Plan Width": 236,
                  "Output": [
                    "l_returnflag",
                    "l_linestatus",
                    "PARTIAL sum(l_quantity)",
                    "PARTIAL sum(l_extendedprice)",
                    "PARTIAL sum((l_extendedprice * ('1'::numeric - l_discount)))",
                    "PARTIAL sum(((l_extendedprice * ('1'::numeric - l_discount)) * ('1'::numeric + l_tax)))",
                    "PARTIAL avg(l_quantity)",
                    "PARTIAL avg(l_extendedprice)",
                    "PARTIAL avg(l_discount)",
                    "PARTIAL count(*)"
                  ],
                  "Group Key": [
                    "lineitem.l_returnflag",
                    "lineitem.l_linestatus"
                  ],
                  "Planned Partitions": 0,
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "lineitem",
                      "Schema": "public",
                      "Alias": "lineitem",
                      "Startup Cost": 0.0,
                      "Total Cost": 127603.04,
                      "Plan Rows": 1191651,
                      "Plan Width": 25,
                      "Output": [
                        "l_orderkey",
                        "l_partkey",
                        "l_suppkey",
                        "l_linenumber",
                        "l_quantity",
                        "l_extendedprice",
                        "l_discount",
                        "l_tax",
                        "l_returnflag",
                        "l_linestatus",
                        "l_shipdate",
                        "l_commitdate",
                        "l_receiptdate",
                        "l_shipinstruct",
                        "l_shipmode",
                        "l_comment"
                      ],
                      "Filter": "(lineitem.l_shipdate <= '1998-09-28 00:00:00'::timestamp without time zone)"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 4.029,
    "JIT": {
      "Functions": 9,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 2. Q2 - Q2_100_seed_812199069.sql

**Template:** Q2

**File:** `Q2_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Limit",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 45927.74,
      "Total Cost": 45927.74,
      "Plan Rows": 1,
      "Plan Width": 270,
      "Output": [
        "supplier.s_acctbal",
        "supplier.s_name",
        "nation.n_name",
        "part.p_partkey",
        "part.p_mfgr",
        "supplier.s_address",
        "supplier.s_phone",
        "supplier.s_comment"
      ],
      "Plans": [
        {
          "Node Type": "Sort",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 45927.74,
          "Total Cost": 45927.74,
          "Plan Rows": 1,
          "Plan Width": 270,
          "Output": [
            "supplier.s_acctbal",
            "supplier.s_name",
            "nation.n_name",
            "part.p_partkey",
            "part.p_mfgr",
            "supplier.s_address",
            "supplier.s_phone",
            "supplier.s_comment"
          ],
          "Sort Key": [
            "supplier.s_acctbal DESC",
            "nation.n_name",
            "supplier.s_name",
            "part.p_partkey"
          ],
          "Plans": [
            {
              "Node Type": "Hash Join",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Join Type": "Inner",
              "Startup Cost": 33967.96,
              "Total Cost": 45927.73,
              "Plan Rows": 1,
              "Plan Width": 270,
              "Output": [
                "supplier.s_acctbal",
                "supplier.s_name",
                "nation.n_name",
                "part.p_partkey",
                "part.p_mfgr",
                "supplier.s_address",
                "supplier.s_phone",
                "supplier.s_comment"
              ],
              "Inner Unique": false,
              "Hash Cond": "((part.p_partkey = partsupp.ps_partkey) AND ((SubPlan 1) = partsupp.ps_supplycost))",
              "Plans": [
                {
                  "Node Type": "Gather",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 1000.0,
                  "Total Cost": 6459.7,
                  "Plan Rows": 817,
                  "Plan Width": 30,
                  "Output": [
                    "part.p_partkey",
                    "part.p_mfgr"
                  ],
                  "Workers Planned": 2,
                  "Single Copy": false,
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "part",
                      "Schema": "public",
                      "Alias": "part",
                      "Startup Cost": 0.0,
                      "Total Cost": 5378.0,
                      "Plan Rows": 340,
                      "Plan Width": 30,
                      "Output": [
                        "part.p_partkey",
                        "part.p_mfgr"
                      ],
                      "Filter": "(((part.p_type)::text ~~ '%NICKEL'::text) AND (part.p_size = 11))"
                    }
                  ]
                },
                {
                  "Node Type": "Hash",
                  "Parent Relationship": "Inner",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 30567.96,
                  "Total Cost": 30567.96,
                  "Plan Rows": 160000,
                  "Plan Width": 250,
                  "Output": [
                    "supplier.s_acctbal",
                    "supplier.s_name",
                    "supplier.s_address",
                    "supplier.s_phone",
                    "supplier.s_comment",
                    "partsupp.ps_partkey",
                    "partsupp.ps_supplycost",
                    "nation.n_name"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Hash Join",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 407.96,
                      "Total Cost": 30567.96,
                      "Plan Rows": 160000,
                      "Plan Width": 250,
                      "Output": [
                        "supplier.s_acctbal",
                        "supplier.s_name",
                        "supplier.s_address",
                        "supplier.s_phone",
                        "supplier.s_comment",
                        "partsupp.ps_partkey",
                        "partsupp.ps_supplycost",
                        "nation.n_name"
                      ],
                      "Inner Unique": false,
                      "Hash Cond": "(partsupp.ps_suppkey = supplier.s_suppkey)",
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Relation Name": "partsupp",
                          "Schema": "public",
                          "Alias": "partsupp",
                          "Startup Cost": 0.0,
                          "Total Cost": 25560.0,
                          "Plan Rows": 800000,
                          "Plan Width": 14,
                          "Output": [
                            "partsupp.ps_partkey",
                            "partsupp.ps_suppkey",
                            "partsupp.ps_availqty",
                            "partsupp.ps_supplycost",
                            "partsupp.ps_comment"
                          ]
                        },
                        {
                          "Node Type": "Hash",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Startup Cost": 382.96,
                          "Total Cost": 382.96,
                          "Plan Rows": 2000,
                          "Plan Width": 244,
                          "Output": [
                            "supplier.s_acctbal",
                            "supplier.s_name",
                            "supplier.s_address",
                            "supplier.s_phone",
                            "supplier.s_comment",
                            "supplier.s_suppkey",
                            "nation.n_name"
                          ],
                          "Plans": [
                            {
                              "Node Type": "Hash Join",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 2.46,
                              "Total Cost": 382.96,
                              "Plan Rows": 2000,
                              "Plan Width": 244,
                              "Output": [
                                "supplier.s_acctbal",
                                "supplier.s_name",
                                "supplier.s_address",
                                "supplier.s_phone",
                                "supplier.s_comment",
                                "supplier.s_suppkey",
                                "nation.n_name"
                              ],
                              "Inner Unique": false,
                              "Hash Cond": "(supplier.s_nationkey = nation.n_nationkey)",
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Relation Name": "supplier",
                                  "Schema": "public",
                                  "Alias": "supplier",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 323.0,
                                  "Plan Rows": 10000,
                                  "Plan Width": 144,
                                  "Output": [
                                    "supplier.s_suppkey",
                                    "supplier.s_name",
                                    "supplier.s_address",
                                    "supplier.s_nationkey",
                                    "supplier.s_phone",
                                    "supplier.s_acctbal",
                                    "supplier.s_comment"
                                  ]
                                },
                                {
                                  "Node Type": "Hash",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Startup Cost": 2.4,
                                  "Total Cost": 2.4,
                                  "Plan Rows": 5,
                                  "Plan Width": 108,
                                  "Output": [
                                    "nation.n_name",
                                    "nation.n_nationkey"
                                  ],
                                  "Plans": [
                                    {
                                      "Node Type": "Hash Join",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Join Type": "Inner",
                                      "Startup Cost": 1.07,
                                      "Total Cost": 2.4,
                                      "Plan Rows": 5,
                                      "Plan Width": 108,
                                      "Output": [
                                        "nation.n_name",
                                        "nation.n_nationkey"
                                      ],
                                      "Inner Unique": true,
                                      "Hash Cond": "(nation.n_regionkey = region.r_regionkey)",
                                      "Plans": [
                                        {
                                          "Node Type": "Seq Scan",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Relation Name": "nation",
                                          "Schema": "public",
                                          "Alias": "nation",
                                          "Startup Cost": 0.0,
                                          "Total Cost": 1.25,
                                          "Plan Rows": 25,
                                          "Plan Width": 112,
                                          "Output": [
                                            "nation.n_nationkey",
                                            "nation.n_name",
                                            "nation.n_regionkey",
                                            "nation.n_comment"
                                          ]
                                        },
                                        {
                                          "Node Type": "Hash",
                                          "Parent Relationship": "Inner",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Startup Cost": 1.06,
                                          "Total Cost": 1.06,
                                          "Plan Rows": 1,
                                          "Plan Width": 4,
                                          "Output": [
                                            "region.r_regionkey"
                                          ],
                                          "Plans": [
                                            {
                                              "Node Type": "Seq Scan",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Relation Name": "region",
                                              "Schema": "public",
                                              "Alias": "region",
                                              "Startup Cost": 0.0,
                                              "Total Cost": 1.06,
                                              "Plan Rows": 1,
                                              "Plan Width": 4,
                                              "Output": [
                                                "region.r_regionkey"
                                              ],
                                              "Filter": "(region.r_name = 'AMERICA'::bpchar)"
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Plain",
                  "Partial Mode": "Simple",
                  "Parent Relationship": "SubPlan",
                  "Subplan Name": "SubPlan 1",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 15.89,
                  "Total Cost": 15.9,
                  "Plan Rows": 1,
                  "Plan Width": 32,
                  "Output": [
                    "min(partsupp_1.ps_supplycost)"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 0.85,
                      "Total Cost": 15.88,
                      "Plan Rows": 1,
                      "Plan Width": 6,
                      "Output": [
                        "partsupp_1.ps_supplycost"
                      ],
                      "Inner Unique": false,
                      "Join Filter": "(region_1.r_regionkey = nation_1.n_regionkey)",
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Relation Name": "region",
                          "Schema": "public",
                          "Alias": "region_1",
                          "Startup Cost": 0.0,
                          "Total Cost": 1.06,
                          "Plan Rows": 1,
                          "Plan Width": 4,
                          "Output": [
                            "region_1.r_regionkey",
                            "region_1.r_name",
                            "region_1.r_comment"
                          ],
                          "Filter": "(region_1.r_name = 'AMERICA'::bpchar)"
                        },
                        {
                          "Node Type": "Nested Loop",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 0.85,
                          "Total Cost": 14.77,
                          "Plan Rows": 4,
                          "Plan Width": 10,
                          "Output": [
                            "partsupp_1.ps_supplycost",
                            "nation_1.n_regionkey"
                          ],
                          "Inner Unique": true,
                          "Plans": [
                            {
                              "Node Type": "Nested Loop",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 0.71,
                              "Total Cost": 14.15,
                              "Plan Rows": 4,
                              "Plan Width": 10,
                              "Output": [
                                "partsupp_1.ps_supplycost",
                                "supplier_1.s_nationkey"
                              ],
                              "Inner Unique": true,
                              "Plans": [
                                {
                                  "Node Type": "Index Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Scan Direction": "Forward",
                                  "Index Name": "partsupp_pkey",
                                  "Relation Name": "partsupp",
                                  "Schema": "public",
                                  "Alias": "partsupp_1",
                                  "Startup Cost": 0.42,
                                  "Total Cost": 4.14,
                                  "Plan Rows": 4,
                                  "Plan Width": 10,
                                  "Output": [
                                    "partsupp_1.ps_partkey",
                                    "partsupp_1.ps_suppkey",
                                    "partsupp_1.ps_availqty",
                                    "partsupp_1.ps_supplycost",
                                    "partsupp_1.ps_comment"
                                  ],
                                  "Index Cond": "(partsupp_1.ps_partkey = part.p_partkey)"
                                },
                                {
                                  "Node Type": "Index Scan",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Scan Direction": "Forward",
                                  "Index Name": "supplier_pkey",
                                  "Relation Name": "supplier",
                                  "Schema": "public",
                                  "Alias": "supplier_1",
                                  "Startup Cost": 0.29,
                                  "Total Cost": 2.5,
                                  "Plan Rows": 1,
                                  "Plan Width": 8,
                                  "Output": [
                                    "supplier_1.s_suppkey",
                                    "supplier_1.s_name",
                                    "supplier_1.s_address",
                                    "supplier_1.s_nationkey",
                                    "supplier_1.s_phone",
                                    "supplier_1.s_acctbal",
                                    "supplier_1.s_comment"
                                  ],
                                  "Index Cond": "(supplier_1.s_suppkey = partsupp_1.ps_suppkey)"
                                }
                              ]
                            },
                            {
                              "Node Type": "Index Scan",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Scan Direction": "Forward",
                              "Index Name": "nation_pkey",
                              "Relation Name": "nation",
                              "Schema": "public",
                              "Alias": "nation_1",
                              "Startup Cost": 0.14,
                              "Total Cost": 0.16,
                              "Plan Rows": 1,
                              "Plan Width": 8,
                              "Output": [
                                "nation_1.n_nationkey",
                                "nation_1.n_name",
                                "nation_1.n_regionkey",
                                "nation_1.n_comment"
                              ],
                              "Index Cond": "(nation_1.n_nationkey = supplier_1.s_nationkey)"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 5.352
  }
]
```

---

## 3. Q3 - Q3_100_seed_812199069.sql

**Template:** Q3

**File:** `Q3_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Limit",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 119771.8,
      "Total Cost": 119771.83,
      "Plan Rows": 10,
      "Plan Width": 44,
      "Output": [
        "lineitem.l_orderkey",
        "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))",
        "orders.o_orderdate",
        "orders.o_shippriority"
      ],
      "Plans": [
        {
          "Node Type": "Sort",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 119771.8,
          "Total Cost": 120549.34,
          "Plan Rows": 311016,
          "Plan Width": 44,
          "Output": [
            "lineitem.l_orderkey",
            "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))",
            "orders.o_orderdate",
            "orders.o_shippriority"
          ],
          "Sort Key": [
            "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))) DESC",
            "orders.o_orderdate"
          ],
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Hashed",
              "Partial Mode": "Simple",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 109163.16,
              "Total Cost": 113050.86,
              "Plan Rows": 311016,
              "Plan Width": 44,
              "Output": [
                "lineitem.l_orderkey",
                "sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))",
                "orders.o_orderdate",
                "orders.o_shippriority"
              ],
              "Group Key": [
                "lineitem.l_orderkey",
                "orders.o_orderdate",
                "orders.o_shippriority"
              ],
              "Planned Partitions": 0,
              "Plans": [
                {
                  "Node Type": "Gather",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 5536.64,
                  "Total Cost": 104497.92,
                  "Plan Rows": 311016,
                  "Plan Width": 24,
                  "Output": [
                    "lineitem.l_orderkey",
                    "orders.o_orderdate",
                    "orders.o_shippriority",
                    "lineitem.l_extendedprice",
                    "lineitem.l_discount"
                  ],
                  "Workers Planned": 3,
                  "Single Copy": false,
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 4536.64,
                      "Total Cost": 72396.32,
                      "Plan Rows": 100328,
                      "Plan Width": 24,
                      "Output": [
                        "lineitem.l_orderkey",
                        "orders.o_orderdate",
                        "orders.o_shippriority",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount"
                      ],
                      "Inner Unique": false,
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 4536.21,
                          "Total Cost": 37331.91,
                          "Plan Rows": 46189,
                          "Plan Width": 12,
                          "Output": [
                            "orders.o_orderdate",
                            "orders.o_shippriority",
                            "orders.o_orderkey"
                          ],
                          "Inner Unique": true,
                          "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Relation Name": "orders",
                              "Schema": "public",
                              "Alias": "orders",
                              "Startup Cost": 0.0,
                              "Total Cost": 32184.39,
                              "Plan Rows": 232872,
                              "Plan Width": 16,
                              "Output": [
                                "orders.o_orderkey",
                                "orders.o_custkey",
                                "orders.o_orderstatus",
                                "orders.o_totalprice",
                                "orders.o_orderdate",
                                "orders.o_orderpriority",
                                "orders.o_clerk",
                                "orders.o_shippriority",
                                "orders.o_comment"
                              ],
                              "Filter": "(orders.o_orderdate < '1995-03-07'::date)"
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Startup Cost": 4381.25,
                              "Total Cost": 4381.25,
                              "Plan Rows": 12397,
                              "Plan Width": 4,
                              "Output": [
                                "customer.c_custkey"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Relation Name": "customer",
                                  "Schema": "public",
                                  "Alias": "customer",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 4381.25,
                                  "Plan Rows": 12397,
                                  "Plan Width": 4,
                                  "Output": [
                                    "customer.c_custkey"
                                  ],
                                  "Filter": "(customer.c_mktsegment = 'AUTOMOBILE'::bpchar)"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "lineitem_pkey",
                          "Relation Name": "lineitem",
                          "Schema": "public",
                          "Alias": "lineitem",
                          "Startup Cost": 0.43,
                          "Total Cost": 0.73,
                          "Plan Rows": 3,
                          "Plan Width": 16,
                          "Output": [
                            "lineitem.l_orderkey",
                            "lineitem.l_partkey",
                            "lineitem.l_suppkey",
                            "lineitem.l_linenumber",
                            "lineitem.l_quantity",
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount",
                            "lineitem.l_tax",
                            "lineitem.l_returnflag",
                            "lineitem.l_linestatus",
                            "lineitem.l_shipdate",
                            "lineitem.l_commitdate",
                            "lineitem.l_receiptdate",
                            "lineitem.l_shipinstruct",
                            "lineitem.l_shipmode",
                            "lineitem.l_comment"
                          ],
                          "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)",
                          "Filter": "(lineitem.l_shipdate > '1995-03-07'::date)"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 2.975,
    "JIT": {
      "Functions": 23,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 4. Q4 - Q4_100_seed_812199069.sql

**Template:** Q4

**File:** `Q4_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Partial Mode": "Finalize",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 66871.03,
      "Total Cost": 66872.93,
      "Plan Rows": 5,
      "Plan Width": 24,
      "Output": [
        "orders.o_orderpriority",
        "count(*)"
      ],
      "Group Key": [
        "orders.o_orderpriority"
      ],
      "Plans": [
        {
          "Node Type": "Gather Merge",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 66871.03,
          "Total Cost": 66872.8,
          "Plan Rows": 15,
          "Plan Width": 24,
          "Output": [
            "orders.o_orderpriority",
            "(PARTIAL count(*))"
          ],
          "Workers Planned": 3,
          "Plans": [
            {
              "Node Type": "Sort",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 65870.99,
              "Total Cost": 65871.0,
              "Plan Rows": 5,
              "Plan Width": 24,
              "Output": [
                "orders.o_orderpriority",
                "(PARTIAL count(*))"
              ],
              "Sort Key": [
                "orders.o_orderpriority"
              ],
              "Plans": [
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Hashed",
                  "Partial Mode": "Partial",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 65870.88,
                  "Total Cost": 65870.93,
                  "Plan Rows": 5,
                  "Plan Width": 24,
                  "Output": [
                    "orders.o_orderpriority",
                    "PARTIAL count(*)"
                  ],
                  "Group Key": [
                    "orders.o_orderpriority"
                  ],
                  "Planned Partitions": 0,
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Semi",
                      "Startup Cost": 0.43,
                      "Total Cost": 65796.55,
                      "Plan Rows": 14866,
                      "Plan Width": 16,
                      "Output": [
                        "orders.o_orderpriority"
                      ],
                      "Inner Unique": false,
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "orders",
                          "Schema": "public",
                          "Alias": "orders",
                          "Startup Cost": 0.0,
                          "Total Cost": 33394.06,
                          "Plan Rows": 18230,
                          "Plan Width": 20,
                          "Output": [
                            "orders.o_orderkey",
                            "orders.o_custkey",
                            "orders.o_orderstatus",
                            "orders.o_totalprice",
                            "orders.o_orderdate",
                            "orders.o_orderpriority",
                            "orders.o_clerk",
                            "orders.o_shippriority",
                            "orders.o_comment"
                          ],
                          "Filter": "((orders.o_orderdate >= '1994-01-01'::date) AND (orders.o_orderdate < '1994-04-01 00:00:00'::timestamp without time zone))"
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "lineitem_pkey",
                          "Relation Name": "lineitem",
                          "Schema": "public",
                          "Alias": "lineitem",
                          "Startup Cost": 0.43,
                          "Total Cost": 2.31,
                          "Plan Rows": 2,
                          "Plan Width": 4,
                          "Output": [
                            "lineitem.l_orderkey",
                            "lineitem.l_partkey",
                            "lineitem.l_suppkey",
                            "lineitem.l_linenumber",
                            "lineitem.l_quantity",
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount",
                            "lineitem.l_tax",
                            "lineitem.l_returnflag",
                            "lineitem.l_linestatus",
                            "lineitem.l_shipdate",
                            "lineitem.l_commitdate",
                            "lineitem.l_receiptdate",
                            "lineitem.l_shipinstruct",
                            "lineitem.l_shipmode",
                            "lineitem.l_comment"
                          ],
                          "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)",
                          "Filter": "(lineitem.l_commitdate < lineitem.l_receiptdate)"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.132
  }
]
```

---

## 5. Q5 - Q5_100_seed_812199069.sql

**Template:** Q5

**File:** `Q5_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 57910.47,
      "Total Cost": 57910.53,
      "Plan Rows": 25,
      "Plan Width": 136,
      "Output": [
        "nation.n_name",
        "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))"
      ],
      "Sort Key": [
        "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))) DESC"
      ],
      "Plans": [
        {
          "Node Type": "Aggregate",
          "Strategy": "Sorted",
          "Partial Mode": "Finalize",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 57870.66,
          "Total Cost": 57909.89,
          "Plan Rows": 25,
          "Plan Width": 136,
          "Output": [
            "nation.n_name",
            "sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))"
          ],
          "Group Key": [
            "nation.n_name"
          ],
          "Plans": [
            {
              "Node Type": "Gather Merge",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 57870.66,
              "Total Cost": 57909.01,
              "Plan Rows": 75,
              "Plan Width": 136,
              "Output": [
                "nation.n_name",
                "(PARTIAL sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))"
              ],
              "Workers Planned": 3,
              "Plans": [
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Sorted",
                  "Partial Mode": "Partial",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 56870.62,
                  "Total Cost": 56900.16,
                  "Plan Rows": 25,
                  "Plan Width": 136,
                  "Output": [
                    "nation.n_name",
                    "PARTIAL sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))"
                  ],
                  "Group Key": [
                    "nation.n_name"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Sort",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Startup Cost": 56870.62,
                      "Total Cost": 56876.47,
                      "Plan Rows": 2338,
                      "Plan Width": 116,
                      "Output": [
                        "nation.n_name",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount"
                      ],
                      "Sort Key": [
                        "nation.n_name"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 5216.52,
                          "Total Cost": 56739.8,
                          "Plan Rows": 2338,
                          "Plan Width": 116,
                          "Output": [
                            "nation.n_name",
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount"
                          ],
                          "Inner Unique": true,
                          "Hash Cond": "((lineitem.l_suppkey = supplier.s_suppkey) AND (customer.c_nationkey = supplier.s_nationkey))",
                          "Plans": [
                            {
                              "Node Type": "Nested Loop",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 4743.52,
                              "Total Cost": 55959.89,
                              "Plan Rows": 58459,
                              "Plan Width": 128,
                              "Output": [
                                "customer.c_nationkey",
                                "lineitem.l_extendedprice",
                                "lineitem.l_discount",
                                "lineitem.l_suppkey",
                                "nation.n_name",
                                "nation.n_nationkey"
                              ],
                              "Inner Unique": false,
                              "Plans": [
                                {
                                  "Node Type": "Hash Join",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Join Type": "Inner",
                                  "Startup Cost": 4743.09,
                                  "Total Cost": 38472.01,
                                  "Plan Rows": 14612,
                                  "Plan Width": 116,
                                  "Output": [
                                    "customer.c_nationkey",
                                    "orders.o_orderkey",
                                    "nation.n_name",
                                    "nation.n_nationkey"
                                  ],
                                  "Inner Unique": false,
                                  "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                                  "Plans": [
                                    {
                                      "Node Type": "Seq Scan",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": true,
                                      "Async Capable": false,
                                      "Relation Name": "orders",
                                      "Schema": "public",
                                      "Alias": "orders",
                                      "Startup Cost": 0.0,
                                      "Total Cost": 33394.06,
                                      "Plan Rows": 73059,
                                      "Plan Width": 8,
                                      "Output": [
                                        "orders.o_orderkey",
                                        "orders.o_custkey",
                                        "orders.o_orderstatus",
                                        "orders.o_totalprice",
                                        "orders.o_orderdate",
                                        "orders.o_orderpriority",
                                        "orders.o_clerk",
                                        "orders.o_shippriority",
                                        "orders.o_comment"
                                      ],
                                      "Filter": "((orders.o_orderdate >= '1995-01-01'::date) AND (orders.o_orderdate < '1996-01-01 00:00:00'::timestamp without time zone))"
                                    },
                                    {
                                      "Node Type": "Hash",
                                      "Parent Relationship": "Inner",
                                      "Parallel Aware": true,
                                      "Async Capable": false,
                                      "Startup Cost": 4586.84,
                                      "Total Cost": 4586.84,
                                      "Plan Rows": 12500,
                                      "Plan Width": 116,
                                      "Output": [
                                        "customer.c_custkey",
                                        "customer.c_nationkey",
                                        "nation.n_name",
                                        "nation.n_nationkey"
                                      ],
                                      "Plans": [
                                        {
                                          "Node Type": "Hash Join",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Join Type": "Inner",
                                          "Startup Cost": 2.46,
                                          "Total Cost": 4586.84,
                                          "Plan Rows": 12500,
                                          "Plan Width": 116,
                                          "Output": [
                                            "customer.c_custkey",
                                            "customer.c_nationkey",
                                            "nation.n_name",
                                            "nation.n_nationkey"
                                          ],
                                          "Inner Unique": false,
                                          "Hash Cond": "(customer.c_nationkey = nation.n_nationkey)",
                                          "Plans": [
                                            {
                                              "Node Type": "Seq Scan",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": true,
                                              "Async Capable": false,
                                              "Relation Name": "customer",
                                              "Schema": "public",
                                              "Alias": "customer",
                                              "Startup Cost": 0.0,
                                              "Total Cost": 4225.0,
                                              "Plan Rows": 62500,
                                              "Plan Width": 8,
                                              "Output": [
                                                "customer.c_custkey",
                                                "customer.c_name",
                                                "customer.c_address",
                                                "customer.c_nationkey",
                                                "customer.c_phone",
                                                "customer.c_acctbal",
                                                "customer.c_mktsegment",
                                                "customer.c_comment"
                                              ]
                                            },
                                            {
                                              "Node Type": "Hash",
                                              "Parent Relationship": "Inner",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Startup Cost": 2.4,
                                              "Total Cost": 2.4,
                                              "Plan Rows": 5,
                                              "Plan Width": 108,
                                              "Output": [
                                                "nation.n_name",
                                                "nation.n_nationkey"
                                              ],
                                              "Plans": [
                                                {
                                                  "Node Type": "Hash Join",
                                                  "Parent Relationship": "Outer",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Join Type": "Inner",
                                                  "Startup Cost": 1.07,
                                                  "Total Cost": 2.4,
                                                  "Plan Rows": 5,
                                                  "Plan Width": 108,
                                                  "Output": [
                                                    "nation.n_name",
                                                    "nation.n_nationkey"
                                                  ],
                                                  "Inner Unique": true,
                                                  "Hash Cond": "(nation.n_regionkey = region.r_regionkey)",
                                                  "Plans": [
                                                    {
                                                      "Node Type": "Seq Scan",
                                                      "Parent Relationship": "Outer",
                                                      "Parallel Aware": false,
                                                      "Async Capable": false,
                                                      "Relation Name": "nation",
                                                      "Schema": "public",
                                                      "Alias": "nation",
                                                      "Startup Cost": 0.0,
                                                      "Total Cost": 1.25,
                                                      "Plan Rows": 25,
                                                      "Plan Width": 112,
                                                      "Output": [
                                                        "nation.n_nationkey",
                                                        "nation.n_name",
                                                        "nation.n_regionkey",
                                                        "nation.n_comment"
                                                      ]
                                                    },
                                                    {
                                                      "Node Type": "Hash",
                                                      "Parent Relationship": "Inner",
                                                      "Parallel Aware": false,
                                                      "Async Capable": false,
                                                      "Startup Cost": 1.06,
                                                      "Total Cost": 1.06,
                                                      "Plan Rows": 1,
                                                      "Plan Width": 4,
                                                      "Output": [
                                                        "region.r_regionkey"
                                                      ],
                                                      "Plans": [
                                                        {
                                                          "Node Type": "Seq Scan",
                                                          "Parent Relationship": "Outer",
                                                          "Parallel Aware": false,
                                                          "Async Capable": false,
                                                          "Relation Name": "region",
                                                          "Schema": "public",
                                                          "Alias": "region",
                                                          "Startup Cost": 0.0,
                                                          "Total Cost": 1.06,
                                                          "Plan Rows": 1,
                                                          "Plan Width": 4,
                                                          "Output": [
                                                            "region.r_regionkey"
                                                          ],
                                                          "Filter": "(region.r_name = 'AMERICA'::bpchar)"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "Node Type": "Index Scan",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Scan Direction": "Forward",
                                  "Index Name": "lineitem_pkey",
                                  "Relation Name": "lineitem",
                                  "Schema": "public",
                                  "Alias": "lineitem",
                                  "Startup Cost": 0.43,
                                  "Total Cost": 1.15,
                                  "Plan Rows": 5,
                                  "Plan Width": 20,
                                  "Output": [
                                    "lineitem.l_orderkey",
                                    "lineitem.l_partkey",
                                    "lineitem.l_suppkey",
                                    "lineitem.l_linenumber",
                                    "lineitem.l_quantity",
                                    "lineitem.l_extendedprice",
                                    "lineitem.l_discount",
                                    "lineitem.l_tax",
                                    "lineitem.l_returnflag",
                                    "lineitem.l_linestatus",
                                    "lineitem.l_shipdate",
                                    "lineitem.l_commitdate",
                                    "lineitem.l_receiptdate",
                                    "lineitem.l_shipinstruct",
                                    "lineitem.l_shipmode",
                                    "lineitem.l_comment"
                                  ],
                                  "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)"
                                }
                              ]
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Startup Cost": 323.0,
                              "Total Cost": 323.0,
                              "Plan Rows": 10000,
                              "Plan Width": 8,
                              "Output": [
                                "supplier.s_suppkey",
                                "supplier.s_nationkey"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Relation Name": "supplier",
                                  "Schema": "public",
                                  "Alias": "supplier",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 323.0,
                                  "Plan Rows": 10000,
                                  "Plan Width": 8,
                                  "Output": [
                                    "supplier.s_suppkey",
                                    "supplier.s_nationkey"
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.479
  }
]
```

---

## 6. Q6 - Q6_100_seed_812199069.sql

**Template:** Q6

**File:** `Q6_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Plain",
      "Partial Mode": "Finalize",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 140720.25,
      "Total Cost": 140720.26,
      "Plan Rows": 1,
      "Plan Width": 32,
      "Output": [
        "sum((l_extendedprice * l_discount))"
      ],
      "Plans": [
        {
          "Node Type": "Gather",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 140719.71,
          "Total Cost": 140720.22,
          "Plan Rows": 5,
          "Plan Width": 32,
          "Output": [
            "(PARTIAL sum((l_extendedprice * l_discount)))"
          ],
          "Workers Planned": 5,
          "Single Copy": false,
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Plain",
              "Partial Mode": "Partial",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 139719.71,
              "Total Cost": 139719.72,
              "Plan Rows": 1,
              "Plan Width": 32,
              "Output": [
                "PARTIAL sum((l_extendedprice * l_discount))"
              ],
              "Plans": [
                {
                  "Node Type": "Seq Scan",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": true,
                  "Async Capable": false,
                  "Relation Name": "lineitem",
                  "Schema": "public",
                  "Alias": "lineitem",
                  "Startup Cost": 0.0,
                  "Total Cost": 139605.47,
                  "Plan Rows": 22848,
                  "Plan Width": 12,
                  "Output": [
                    "l_orderkey",
                    "l_partkey",
                    "l_suppkey",
                    "l_linenumber",
                    "l_quantity",
                    "l_extendedprice",
                    "l_discount",
                    "l_tax",
                    "l_returnflag",
                    "l_linestatus",
                    "l_shipdate",
                    "l_commitdate",
                    "l_receiptdate",
                    "l_shipinstruct",
                    "l_shipmode",
                    "l_comment"
                  ],
                  "Filter": "((lineitem.l_shipdate >= '1995-01-01'::date) AND (lineitem.l_shipdate < '1996-01-01 00:00:00'::timestamp without time zone) AND (lineitem.l_discount >= 0.01) AND (lineitem.l_discount <= 0.03) AND (lineitem.l_quantity < '24'::numeric))"
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.03,
    "JIT": {
      "Functions": 7,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 7. Q7 - Q7_100_seed_812199069.sql

**Template:** Q7

**File:** `Q7_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Partial Mode": "Simple",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 64308.27,
      "Total Cost": 65209.68,
      "Plan Rows": 6078,
      "Plan Width": 272,
      "Output": [
        "n1.n_name",
        "n2.n_name",
        "(EXTRACT(year FROM lineitem.l_shipdate))",
        "sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))"
      ],
      "Group Key": [
        "n1.n_name",
        "n2.n_name",
        "(EXTRACT(year FROM lineitem.l_shipdate))"
      ],
      "Plans": [
        {
          "Node Type": "Gather Merge",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 64308.27,
          "Total Cost": 65027.34,
          "Plan Rows": 6078,
          "Plan Width": 252,
          "Output": [
            "n1.n_name",
            "n2.n_name",
            "(EXTRACT(year FROM lineitem.l_shipdate))",
            "lineitem.l_extendedprice",
            "lineitem.l_discount"
          ],
          "Workers Planned": 3,
          "Plans": [
            {
              "Node Type": "Sort",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 63308.23,
              "Total Cost": 63313.13,
              "Plan Rows": 1961,
              "Plan Width": 252,
              "Output": [
                "n1.n_name",
                "n2.n_name",
                "(EXTRACT(year FROM lineitem.l_shipdate))",
                "lineitem.l_extendedprice",
                "lineitem.l_discount"
              ],
              "Sort Key": [
                "n1.n_name",
                "n2.n_name",
                "(EXTRACT(year FROM lineitem.l_shipdate))"
              ],
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Join Type": "Inner",
                  "Startup Cost": 4846.31,
                  "Total Cost": 63200.99,
                  "Plan Rows": 1961,
                  "Plan Width": 252,
                  "Output": [
                    "n1.n_name",
                    "n2.n_name",
                    "EXTRACT(year FROM lineitem.l_shipdate)",
                    "lineitem.l_extendedprice",
                    "lineitem.l_discount"
                  ],
                  "Inner Unique": false,
                  "Hash Cond": "(lineitem.l_suppkey = supplier.s_suppkey)",
                  "Join Filter": "(((n1.n_name = 'ALGERIA'::bpchar) AND (n2.n_name = 'INDONESIA'::bpchar)) OR ((n1.n_name = 'INDONESIA'::bpchar) AND (n2.n_name = 'ALGERIA'::bpchar)))",
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 4481.21,
                      "Total Cost": 62578.93,
                      "Plan Rows": 47115,
                      "Plan Width": 124,
                      "Output": [
                        "lineitem.l_shipdate",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount",
                        "lineitem.l_suppkey",
                        "n2.n_name"
                      ],
                      "Inner Unique": false,
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 4480.77,
                          "Total Cost": 37431.29,
                          "Plan Rows": 38710,
                          "Plan Width": 108,
                          "Output": [
                            "orders.o_orderkey",
                            "n2.n_name"
                          ],
                          "Inner Unique": false,
                          "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Relation Name": "orders",
                              "Schema": "public",
                              "Alias": "orders",
                              "Startup Cost": 0.0,
                              "Total Cost": 30974.71,
                              "Plan Rows": 483871,
                              "Plan Width": 8,
                              "Output": [
                                "orders.o_orderkey",
                                "orders.o_custkey",
                                "orders.o_orderstatus",
                                "orders.o_totalprice",
                                "orders.o_orderdate",
                                "orders.o_orderpriority",
                                "orders.o_clerk",
                                "orders.o_shippriority",
                                "orders.o_comment"
                              ]
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Startup Cost": 4418.27,
                              "Total Cost": 4418.27,
                              "Plan Rows": 5000,
                              "Plan Width": 108,
                              "Output": [
                                "customer.c_custkey",
                                "n2.n_name"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Hash Join",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Join Type": "Inner",
                                  "Startup Cost": 1.4,
                                  "Total Cost": 4418.27,
                                  "Plan Rows": 5000,
                                  "Plan Width": 108,
                                  "Output": [
                                    "customer.c_custkey",
                                    "n2.n_name"
                                  ],
                                  "Inner Unique": true,
                                  "Hash Cond": "(customer.c_nationkey = n2.n_nationkey)",
                                  "Plans": [
                                    {
                                      "Node Type": "Seq Scan",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": true,
                                      "Async Capable": false,
                                      "Relation Name": "customer",
                                      "Schema": "public",
                                      "Alias": "customer",
                                      "Startup Cost": 0.0,
                                      "Total Cost": 4225.0,
                                      "Plan Rows": 62500,
                                      "Plan Width": 8,
                                      "Output": [
                                        "customer.c_custkey",
                                        "customer.c_name",
                                        "customer.c_address",
                                        "customer.c_nationkey",
                                        "customer.c_phone",
                                        "customer.c_acctbal",
                                        "customer.c_mktsegment",
                                        "customer.c_comment"
                                      ]
                                    },
                                    {
                                      "Node Type": "Hash",
                                      "Parent Relationship": "Inner",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Startup Cost": 1.38,
                                      "Total Cost": 1.38,
                                      "Plan Rows": 2,
                                      "Plan Width": 108,
                                      "Output": [
                                        "n2.n_name",
                                        "n2.n_nationkey"
                                      ],
                                      "Plans": [
                                        {
                                          "Node Type": "Seq Scan",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Relation Name": "nation",
                                          "Schema": "public",
                                          "Alias": "n2",
                                          "Startup Cost": 0.0,
                                          "Total Cost": 1.38,
                                          "Plan Rows": 2,
                                          "Plan Width": 108,
                                          "Output": [
                                            "n2.n_name",
                                            "n2.n_nationkey"
                                          ],
                                          "Filter": "((n2.n_name = 'INDONESIA'::bpchar) OR (n2.n_name = 'ALGERIA'::bpchar))"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "lineitem_pkey",
                          "Relation Name": "lineitem",
                          "Schema": "public",
                          "Alias": "lineitem",
                          "Startup Cost": 0.43,
                          "Total Cost": 0.64,
                          "Plan Rows": 1,
                          "Plan Width": 24,
                          "Output": [
                            "lineitem.l_orderkey",
                            "lineitem.l_partkey",
                            "lineitem.l_suppkey",
                            "lineitem.l_linenumber",
                            "lineitem.l_quantity",
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount",
                            "lineitem.l_tax",
                            "lineitem.l_returnflag",
                            "lineitem.l_linestatus",
                            "lineitem.l_shipdate",
                            "lineitem.l_commitdate",
                            "lineitem.l_receiptdate",
                            "lineitem.l_shipinstruct",
                            "lineitem.l_shipmode",
                            "lineitem.l_comment"
                          ],
                          "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)",
                          "Filter": "((lineitem.l_shipdate >= '1995-01-01'::date) AND (lineitem.l_shipdate <= '1996-12-31'::date))"
                        }
                      ]
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Startup Cost": 355.1,
                      "Total Cost": 355.1,
                      "Plan Rows": 800,
                      "Plan Width": 108,
                      "Output": [
                        "supplier.s_suppkey",
                        "n1.n_name"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 1.4,
                          "Total Cost": 355.1,
                          "Plan Rows": 800,
                          "Plan Width": 108,
                          "Output": [
                            "supplier.s_suppkey",
                            "n1.n_name"
                          ],
                          "Inner Unique": true,
                          "Hash Cond": "(supplier.s_nationkey = n1.n_nationkey)",
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Relation Name": "supplier",
                              "Schema": "public",
                              "Alias": "supplier",
                              "Startup Cost": 0.0,
                              "Total Cost": 323.0,
                              "Plan Rows": 10000,
                              "Plan Width": 8,
                              "Output": [
                                "supplier.s_suppkey",
                                "supplier.s_name",
                                "supplier.s_address",
                                "supplier.s_nationkey",
                                "supplier.s_phone",
                                "supplier.s_acctbal",
                                "supplier.s_comment"
                              ]
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Startup Cost": 1.38,
                              "Total Cost": 1.38,
                              "Plan Rows": 2,
                              "Plan Width": 108,
                              "Output": [
                                "n1.n_name",
                                "n1.n_nationkey"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Relation Name": "nation",
                                  "Schema": "public",
                                  "Alias": "n1",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 1.38,
                                  "Plan Rows": 2,
                                  "Plan Width": 108,
                                  "Output": [
                                    "n1.n_name",
                                    "n1.n_nationkey"
                                  ],
                                  "Filter": "((n1.n_name = 'ALGERIA'::bpchar) OR (n1.n_name = 'INDONESIA'::bpchar))"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.319
  }
]
```

---

## 8. Q8 - Q8_100_seed_812199069.sql

**Template:** Q8

**File:** `Q8_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Partial Mode": "Simple",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 71545.37,
      "Total Cost": 71920.87,
      "Plan Rows": 2372,
      "Plan Width": 64,
      "Output": [
        "(EXTRACT(year FROM orders.o_orderdate))",
        "(sum(CASE WHEN (n2.n_name = 'INDONESIA'::bpchar) THEN (lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) ELSE '0'::numeric END) / sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))"
      ],
      "Group Key": [
        "(EXTRACT(year FROM orders.o_orderdate))"
      ],
      "Plans": [
        {
          "Node Type": "Gather Merge",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 71545.37,
          "Total Cost": 71825.99,
          "Plan Rows": 2372,
          "Plan Width": 148,
          "Output": [
            "(EXTRACT(year FROM orders.o_orderdate))",
            "n2.n_name",
            "lineitem.l_extendedprice",
            "lineitem.l_discount"
          ],
          "Workers Planned": 3,
          "Plans": [
            {
              "Node Type": "Sort",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 70545.33,
              "Total Cost": 70547.24,
              "Plan Rows": 765,
              "Plan Width": 148,
              "Output": [
                "(EXTRACT(year FROM orders.o_orderdate))",
                "n2.n_name",
                "lineitem.l_extendedprice",
                "lineitem.l_discount"
              ],
              "Sort Key": [
                "(EXTRACT(year FROM orders.o_orderdate))"
              ],
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Join Type": "Inner",
                  "Startup Cost": 9921.79,
                  "Total Cost": 70508.69,
                  "Plan Rows": 765,
                  "Plan Width": 148,
                  "Output": [
                    "EXTRACT(year FROM orders.o_orderdate)",
                    "n2.n_name",
                    "lineitem.l_extendedprice",
                    "lineitem.l_discount"
                  ],
                  "Inner Unique": true,
                  "Hash Cond": "(supplier.s_nationkey = n2.n_nationkey)",
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 9920.22,
                      "Total Cost": 70502.86,
                      "Plan Rows": 765,
                      "Plan Width": 20,
                      "Output": [
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount",
                        "supplier.s_nationkey",
                        "orders.o_orderdate"
                      ],
                      "Inner Unique": true,
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 9919.94,
                          "Total Cost": 70271.42,
                          "Plan Rows": 765,
                          "Plan Width": 20,
                          "Output": [
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount",
                            "lineitem.l_suppkey",
                            "orders.o_orderdate"
                          ],
                          "Inner Unique": true,
                          "Hash Cond": "(lineitem.l_partkey = part.p_partkey)",
                          "Plans": [
                            {
                              "Node Type": "Nested Loop",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 4743.52,
                              "Total Cost": 64785.2,
                              "Plan Rows": 118013,
                              "Plan Width": 24,
                              "Output": [
                                "lineitem.l_extendedprice",
                                "lineitem.l_discount",
                                "lineitem.l_partkey",
                                "lineitem.l_suppkey",
                                "orders.o_orderdate"
                              ],
                              "Inner Unique": false,
                              "Plans": [
                                {
                                  "Node Type": "Hash Join",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Join Type": "Inner",
                                  "Startup Cost": 4743.09,
                                  "Total Cost": 38813.14,
                                  "Plan Rows": 29497,
                                  "Plan Width": 8,
                                  "Output": [
                                    "orders.o_orderdate",
                                    "orders.o_orderkey"
                                  ],
                                  "Inner Unique": false,
                                  "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                                  "Plans": [
                                    {
                                      "Node Type": "Seq Scan",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": true,
                                      "Async Capable": false,
                                      "Relation Name": "orders",
                                      "Schema": "public",
                                      "Alias": "orders",
                                      "Startup Cost": 0.0,
                                      "Total Cost": 33394.06,
                                      "Plan Rows": 147487,
                                      "Plan Width": 12,
                                      "Output": [
                                        "orders.o_orderkey",
                                        "orders.o_custkey",
                                        "orders.o_orderstatus",
                                        "orders.o_totalprice",
                                        "orders.o_orderdate",
                                        "orders.o_orderpriority",
                                        "orders.o_clerk",
                                        "orders.o_shippriority",
                                        "orders.o_comment"
                                      ],
                                      "Filter": "((orders.o_orderdate >= '1995-01-01'::date) AND (orders.o_orderdate <= '1996-12-31'::date))"
                                    },
                                    {
                                      "Node Type": "Hash",
                                      "Parent Relationship": "Inner",
                                      "Parallel Aware": true,
                                      "Async Capable": false,
                                      "Startup Cost": 4586.84,
                                      "Total Cost": 4586.84,
                                      "Plan Rows": 12500,
                                      "Plan Width": 4,
                                      "Output": [
                                        "customer.c_custkey"
                                      ],
                                      "Plans": [
                                        {
                                          "Node Type": "Hash Join",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Join Type": "Inner",
                                          "Startup Cost": 2.46,
                                          "Total Cost": 4586.84,
                                          "Plan Rows": 12500,
                                          "Plan Width": 4,
                                          "Output": [
                                            "customer.c_custkey"
                                          ],
                                          "Inner Unique": false,
                                          "Hash Cond": "(customer.c_nationkey = n1.n_nationkey)",
                                          "Plans": [
                                            {
                                              "Node Type": "Seq Scan",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": true,
                                              "Async Capable": false,
                                              "Relation Name": "customer",
                                              "Schema": "public",
                                              "Alias": "customer",
                                              "Startup Cost": 0.0,
                                              "Total Cost": 4225.0,
                                              "Plan Rows": 62500,
                                              "Plan Width": 8,
                                              "Output": [
                                                "customer.c_custkey",
                                                "customer.c_name",
                                                "customer.c_address",
                                                "customer.c_nationkey",
                                                "customer.c_phone",
                                                "customer.c_acctbal",
                                                "customer.c_mktsegment",
                                                "customer.c_comment"
                                              ]
                                            },
                                            {
                                              "Node Type": "Hash",
                                              "Parent Relationship": "Inner",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Startup Cost": 2.4,
                                              "Total Cost": 2.4,
                                              "Plan Rows": 5,
                                              "Plan Width": 4,
                                              "Output": [
                                                "n1.n_nationkey"
                                              ],
                                              "Plans": [
                                                {
                                                  "Node Type": "Hash Join",
                                                  "Parent Relationship": "Outer",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Join Type": "Inner",
                                                  "Startup Cost": 1.07,
                                                  "Total Cost": 2.4,
                                                  "Plan Rows": 5,
                                                  "Plan Width": 4,
                                                  "Output": [
                                                    "n1.n_nationkey"
                                                  ],
                                                  "Inner Unique": true,
                                                  "Hash Cond": "(n1.n_regionkey = region.r_regionkey)",
                                                  "Plans": [
                                                    {
                                                      "Node Type": "Seq Scan",
                                                      "Parent Relationship": "Outer",
                                                      "Parallel Aware": false,
                                                      "Async Capable": false,
                                                      "Relation Name": "nation",
                                                      "Schema": "public",
                                                      "Alias": "n1",
                                                      "Startup Cost": 0.0,
                                                      "Total Cost": 1.25,
                                                      "Plan Rows": 25,
                                                      "Plan Width": 8,
                                                      "Output": [
                                                        "n1.n_nationkey",
                                                        "n1.n_name",
                                                        "n1.n_regionkey",
                                                        "n1.n_comment"
                                                      ]
                                                    },
                                                    {
                                                      "Node Type": "Hash",
                                                      "Parent Relationship": "Inner",
                                                      "Parallel Aware": false,
                                                      "Async Capable": false,
                                                      "Startup Cost": 1.06,
                                                      "Total Cost": 1.06,
                                                      "Plan Rows": 1,
                                                      "Plan Width": 4,
                                                      "Output": [
                                                        "region.r_regionkey"
                                                      ],
                                                      "Plans": [
                                                        {
                                                          "Node Type": "Seq Scan",
                                                          "Parent Relationship": "Outer",
                                                          "Parallel Aware": false,
                                                          "Async Capable": false,
                                                          "Relation Name": "region",
                                                          "Schema": "public",
                                                          "Alias": "region",
                                                          "Startup Cost": 0.0,
                                                          "Total Cost": 1.06,
                                                          "Plan Rows": 1,
                                                          "Plan Width": 4,
                                                          "Output": [
                                                            "region.r_regionkey"
                                                          ],
                                                          "Filter": "(region.r_name = 'ASIA'::bpchar)"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "Node Type": "Index Scan",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Scan Direction": "Forward",
                                  "Index Name": "lineitem_pkey",
                                  "Relation Name": "lineitem",
                                  "Schema": "public",
                                  "Alias": "lineitem",
                                  "Startup Cost": 0.43,
                                  "Total Cost": 0.83,
                                  "Plan Rows": 5,
                                  "Plan Width": 24,
                                  "Output": [
                                    "lineitem.l_orderkey",
                                    "lineitem.l_partkey",
                                    "lineitem.l_suppkey",
                                    "lineitem.l_linenumber",
                                    "lineitem.l_quantity",
                                    "lineitem.l_extendedprice",
                                    "lineitem.l_discount",
                                    "lineitem.l_tax",
                                    "lineitem.l_returnflag",
                                    "lineitem.l_linestatus",
                                    "lineitem.l_shipdate",
                                    "lineitem.l_commitdate",
                                    "lineitem.l_receiptdate",
                                    "lineitem.l_shipinstruct",
                                    "lineitem.l_shipmode",
                                    "lineitem.l_comment"
                                  ],
                                  "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)"
                                }
                              ]
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Startup Cost": 5169.67,
                              "Total Cost": 5169.67,
                              "Plan Rows": 540,
                              "Plan Width": 4,
                              "Output": [
                                "part.p_partkey"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Relation Name": "part",
                                  "Schema": "public",
                                  "Alias": "part",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 5169.67,
                                  "Plan Rows": 540,
                                  "Plan Width": 4,
                                  "Output": [
                                    "part.p_partkey"
                                  ],
                                  "Filter": "((part.p_type)::text = 'PROMO BURNISHED BRASS'::text)"
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "supplier_pkey",
                          "Relation Name": "supplier",
                          "Schema": "public",
                          "Alias": "supplier",
                          "Startup Cost": 0.29,
                          "Total Cost": 0.3,
                          "Plan Rows": 1,
                          "Plan Width": 8,
                          "Output": [
                            "supplier.s_suppkey",
                            "supplier.s_name",
                            "supplier.s_address",
                            "supplier.s_nationkey",
                            "supplier.s_phone",
                            "supplier.s_acctbal",
                            "supplier.s_comment"
                          ],
                          "Index Cond": "(supplier.s_suppkey = lineitem.l_suppkey)"
                        }
                      ]
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Startup Cost": 1.25,
                      "Total Cost": 1.25,
                      "Plan Rows": 25,
                      "Plan Width": 108,
                      "Output": [
                        "n2.n_name",
                        "n2.n_nationkey"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Relation Name": "nation",
                          "Schema": "public",
                          "Alias": "n2",
                          "Startup Cost": 0.0,
                          "Total Cost": 1.25,
                          "Plan Rows": 25,
                          "Plan Width": 108,
                          "Output": [
                            "n2.n_name",
                            "n2.n_nationkey"
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.5
  }
]
```

---

## 9. Q9 - Q9_100_seed_812199069.sql

**Template:** Q9

**File:** `Q9_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 215550.82,
      "Total Cost": 215701.2,
      "Plan Rows": 60150,
      "Plan Width": 168,
      "Output": [
        "nation.n_name",
        "(EXTRACT(year FROM orders.o_orderdate))",
        "(sum(((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) - (partsupp.ps_supplycost * lineitem.l_quantity))))"
      ],
      "Sort Key": [
        "nation.n_name",
        "(EXTRACT(year FROM orders.o_orderdate)) DESC"
      ],
      "Plans": [
        {
          "Node Type": "Aggregate",
          "Strategy": "Hashed",
          "Partial Mode": "Finalize",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 209873.78,
          "Total Cost": 210776.03,
          "Plan Rows": 60150,
          "Plan Width": 168,
          "Output": [
            "nation.n_name",
            "(EXTRACT(year FROM orders.o_orderdate))",
            "sum(((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) - (partsupp.ps_supplycost * lineitem.l_quantity)))"
          ],
          "Group Key": [
            "nation.n_name",
            "(EXTRACT(year FROM orders.o_orderdate))"
          ],
          "Planned Partitions": 0,
          "Plans": [
            {
              "Node Type": "Gather",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 189122.03,
              "Total Cost": 208069.28,
              "Plan Rows": 180450,
              "Plan Width": 168,
              "Output": [
                "nation.n_name",
                "(EXTRACT(year FROM orders.o_orderdate))",
                "(PARTIAL sum(((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) - (partsupp.ps_supplycost * lineitem.l_quantity))))"
              ],
              "Workers Planned": 3,
              "Single Copy": false,
              "Plans": [
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Hashed",
                  "Partial Mode": "Partial",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 188122.03,
                  "Total Cost": 189024.28,
                  "Plan Rows": 60150,
                  "Plan Width": 168,
                  "Output": [
                    "nation.n_name",
                    "(EXTRACT(year FROM orders.o_orderdate))",
                    "PARTIAL sum(((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) - (partsupp.ps_supplycost * lineitem.l_quantity)))"
                  ],
                  "Group Key": [
                    "nation.n_name",
                    "EXTRACT(year FROM orders.o_orderdate)"
                  ],
                  "Planned Partitions": 0,
                  "Plans": [
                    {
                      "Node Type": "Hash Join",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 151918.84,
                      "Total Cost": 185406.38,
                      "Plan Rows": 155180,
                      "Plan Width": 159,
                      "Output": [
                        "nation.n_name",
                        "EXTRACT(year FROM orders.o_orderdate)",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount",
                        "partsupp.ps_supplycost",
                        "lineitem.l_quantity"
                      ],
                      "Inner Unique": false,
                      "Hash Cond": "(orders.o_orderkey = lineitem.l_orderkey)",
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "orders",
                          "Schema": "public",
                          "Alias": "orders",
                          "Startup Cost": 0.0,
                          "Total Cost": 30974.71,
                          "Plan Rows": 483871,
                          "Plan Width": 8,
                          "Output": [
                            "orders.o_orderkey",
                            "orders.o_custkey",
                            "orders.o_orderstatus",
                            "orders.o_totalprice",
                            "orders.o_orderdate",
                            "orders.o_orderpriority",
                            "orders.o_clerk",
                            "orders.o_shippriority",
                            "orders.o_comment"
                          ]
                        },
                        {
                          "Node Type": "Hash",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Startup Cost": 150716.21,
                          "Total Cost": 150716.21,
                          "Plan Rows": 96211,
                          "Plan Width": 131,
                          "Output": [
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount",
                            "lineitem.l_quantity",
                            "lineitem.l_orderkey",
                            "partsupp.ps_supplycost",
                            "nation.n_name"
                          ],
                          "Plans": [
                            {
                              "Node Type": "Hash Join",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 17111.79,
                              "Total Cost": 150716.21,
                              "Plan Rows": 96211,
                              "Plan Width": 131,
                              "Output": [
                                "lineitem.l_extendedprice",
                                "lineitem.l_discount",
                                "lineitem.l_quantity",
                                "lineitem.l_orderkey",
                                "partsupp.ps_supplycost",
                                "nation.n_name"
                              ],
                              "Inner Unique": false,
                              "Hash Cond": "((lineitem.l_suppkey = supplier.s_suppkey) AND (lineitem.l_partkey = partsupp.ps_partkey))",
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Relation Name": "lineitem",
                                  "Schema": "public",
                                  "Alias": "lineitem",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 124602.43,
                                  "Plan Rows": 1200243,
                                  "Plan Width": 29,
                                  "Output": [
                                    "lineitem.l_orderkey",
                                    "lineitem.l_partkey",
                                    "lineitem.l_suppkey",
                                    "lineitem.l_linenumber",
                                    "lineitem.l_quantity",
                                    "lineitem.l_extendedprice",
                                    "lineitem.l_discount",
                                    "lineitem.l_tax",
                                    "lineitem.l_returnflag",
                                    "lineitem.l_linestatus",
                                    "lineitem.l_shipdate",
                                    "lineitem.l_commitdate",
                                    "lineitem.l_receiptdate",
                                    "lineitem.l_shipinstruct",
                                    "lineitem.l_shipmode",
                                    "lineitem.l_comment"
                                  ]
                                },
                                {
                                  "Node Type": "Hash",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Startup Cost": 16710.99,
                                  "Total Cost": 16710.99,
                                  "Plan Rows": 26720,
                                  "Plan Width": 126,
                                  "Output": [
                                    "part.p_partkey",
                                    "partsupp.ps_supplycost",
                                    "partsupp.ps_suppkey",
                                    "partsupp.ps_partkey",
                                    "supplier.s_suppkey",
                                    "nation.n_name"
                                  ],
                                  "Plans": [
                                    {
                                      "Node Type": "Hash Join",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Join Type": "Inner",
                                      "Startup Cost": 449.99,
                                      "Total Cost": 16710.99,
                                      "Plan Rows": 26720,
                                      "Plan Width": 126,
                                      "Output": [
                                        "part.p_partkey",
                                        "partsupp.ps_supplycost",
                                        "partsupp.ps_suppkey",
                                        "partsupp.ps_partkey",
                                        "supplier.s_suppkey",
                                        "nation.n_name"
                                      ],
                                      "Inner Unique": true,
                                      "Hash Cond": "(supplier.s_nationkey = nation.n_nationkey)",
                                      "Plans": [
                                        {
                                          "Node Type": "Hash Join",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Join Type": "Inner",
                                          "Startup Cost": 448.43,
                                          "Total Cost": 16627.4,
                                          "Plan Rows": 26720,
                                          "Plan Width": 26,
                                          "Output": [
                                            "part.p_partkey",
                                            "partsupp.ps_supplycost",
                                            "partsupp.ps_suppkey",
                                            "partsupp.ps_partkey",
                                            "supplier.s_suppkey",
                                            "supplier.s_nationkey"
                                          ],
                                          "Inner Unique": true,
                                          "Hash Cond": "(partsupp.ps_suppkey = supplier.s_suppkey)",
                                          "Plans": [
                                            {
                                              "Node Type": "Nested Loop",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Join Type": "Inner",
                                              "Startup Cost": 0.42,
                                              "Total Cost": 16109.23,
                                              "Plan Rows": 26720,
                                              "Plan Width": 18,
                                              "Output": [
                                                "part.p_partkey",
                                                "partsupp.ps_supplycost",
                                                "partsupp.ps_suppkey",
                                                "partsupp.ps_partkey"
                                              ],
                                              "Inner Unique": false,
                                              "Plans": [
                                                {
                                                  "Node Type": "Seq Scan",
                                                  "Parent Relationship": "Outer",
                                                  "Parallel Aware": true,
                                                  "Async Capable": false,
                                                  "Relation Name": "part",
                                                  "Schema": "public",
                                                  "Alias": "part",
                                                  "Startup Cost": 0.0,
                                                  "Total Cost": 5169.67,
                                                  "Plan Rows": 6680,
                                                  "Plan Width": 4,
                                                  "Output": [
                                                    "part.p_partkey",
                                                    "part.p_name",
                                                    "part.p_mfgr",
                                                    "part.p_brand",
                                                    "part.p_type",
                                                    "part.p_size",
                                                    "part.p_container",
                                                    "part.p_retailprice",
                                                    "part.p_comment"
                                                  ],
                                                  "Filter": "((part.p_name)::text ~~ '%snow%'::text)"
                                                },
                                                {
                                                  "Node Type": "Index Scan",
                                                  "Parent Relationship": "Inner",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Scan Direction": "Forward",
                                                  "Index Name": "partsupp_pkey",
                                                  "Relation Name": "partsupp",
                                                  "Schema": "public",
                                                  "Alias": "partsupp",
                                                  "Startup Cost": 0.42,
                                                  "Total Cost": 1.6,
                                                  "Plan Rows": 4,
                                                  "Plan Width": 14,
                                                  "Output": [
                                                    "partsupp.ps_partkey",
                                                    "partsupp.ps_suppkey",
                                                    "partsupp.ps_availqty",
                                                    "partsupp.ps_supplycost",
                                                    "partsupp.ps_comment"
                                                  ],
                                                  "Index Cond": "(partsupp.ps_partkey = part.p_partkey)"
                                                }
                                              ]
                                            },
                                            {
                                              "Node Type": "Hash",
                                              "Parent Relationship": "Inner",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Startup Cost": 323.0,
                                              "Total Cost": 323.0,
                                              "Plan Rows": 10000,
                                              "Plan Width": 8,
                                              "Output": [
                                                "supplier.s_suppkey",
                                                "supplier.s_nationkey"
                                              ],
                                              "Plans": [
                                                {
                                                  "Node Type": "Seq Scan",
                                                  "Parent Relationship": "Outer",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Relation Name": "supplier",
                                                  "Schema": "public",
                                                  "Alias": "supplier",
                                                  "Startup Cost": 0.0,
                                                  "Total Cost": 323.0,
                                                  "Plan Rows": 10000,
                                                  "Plan Width": 8,
                                                  "Output": [
                                                    "supplier.s_suppkey",
                                                    "supplier.s_nationkey"
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "Node Type": "Hash",
                                          "Parent Relationship": "Inner",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Startup Cost": 1.25,
                                          "Total Cost": 1.25,
                                          "Plan Rows": 25,
                                          "Plan Width": 108,
                                          "Output": [
                                            "nation.n_name",
                                            "nation.n_nationkey"
                                          ],
                                          "Plans": [
                                            {
                                              "Node Type": "Seq Scan",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Relation Name": "nation",
                                              "Schema": "public",
                                              "Alias": "nation",
                                              "Startup Cost": 0.0,
                                              "Total Cost": 1.25,
                                              "Plan Rows": 25,
                                              "Plan Width": 108,
                                              "Output": [
                                                "nation.n_name",
                                                "nation.n_nationkey"
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.73,
    "JIT": {
      "Functions": 48,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 10. Q10 - Q10_100_seed_812199069.sql

**Template:** Q10

**File:** `Q10_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Limit",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 90477.26,
      "Total Cost": 90477.31,
      "Plan Rows": 20,
      "Plan Width": 280,
      "Output": [
        "customer.c_custkey",
        "customer.c_name",
        "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))",
        "customer.c_acctbal",
        "nation.n_name",
        "customer.c_address",
        "customer.c_phone",
        "customer.c_comment"
      ],
      "Plans": [
        {
          "Node Type": "Sort",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 90477.26,
          "Total Cost": 90618.54,
          "Plan Rows": 56515,
          "Plan Width": 280,
          "Output": [
            "customer.c_custkey",
            "customer.c_name",
            "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))",
            "customer.c_acctbal",
            "nation.n_name",
            "customer.c_address",
            "customer.c_phone",
            "customer.c_comment"
          ],
          "Sort Key": [
            "(sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))) DESC"
          ],
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Hashed",
              "Partial Mode": "Simple",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 88266.98,
              "Total Cost": 88973.41,
              "Plan Rows": 56515,
              "Plan Width": 280,
              "Output": [
                "customer.c_custkey",
                "customer.c_name",
                "sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))",
                "customer.c_acctbal",
                "nation.n_name",
                "customer.c_address",
                "customer.c_phone",
                "customer.c_comment"
              ],
              "Group Key": [
                "customer.c_custkey",
                "nation.n_name"
              ],
              "Planned Partitions": 0,
              "Plans": [
                {
                  "Node Type": "Gather",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 6008.24,
                  "Total Cost": 87560.54,
                  "Plan Rows": 56515,
                  "Plan Width": 260,
                  "Output": [
                    "customer.c_custkey",
                    "nation.n_name",
                    "customer.c_name",
                    "lineitem.l_extendedprice",
                    "lineitem.l_discount",
                    "customer.c_acctbal",
                    "customer.c_address",
                    "customer.c_phone",
                    "customer.c_comment"
                  ],
                  "Workers Planned": 3,
                  "Single Copy": false,
                  "Plans": [
                    {
                      "Node Type": "Hash Join",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 5008.24,
                      "Total Cost": 80909.04,
                      "Plan Rows": 18231,
                      "Plan Width": 260,
                      "Output": [
                        "customer.c_custkey",
                        "nation.n_name",
                        "customer.c_name",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount",
                        "customer.c_acctbal",
                        "customer.c_address",
                        "customer.c_phone",
                        "customer.c_comment"
                      ],
                      "Inner Unique": true,
                      "Hash Cond": "(customer.c_nationkey = nation.n_nationkey)",
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 5006.68,
                          "Total Cost": 80851.51,
                          "Plan Rows": 18231,
                          "Plan Width": 160,
                          "Output": [
                            "customer.c_custkey",
                            "customer.c_name",
                            "customer.c_acctbal",
                            "customer.c_address",
                            "customer.c_phone",
                            "customer.c_comment",
                            "customer.c_nationkey",
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount"
                          ],
                          "Inner Unique": true,
                          "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                          "Plans": [
                            {
                              "Node Type": "Nested Loop",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 0.43,
                              "Total Cost": 75797.4,
                              "Plan Rows": 18231,
                              "Plan Width": 16,
                              "Output": [
                                "orders.o_custkey",
                                "lineitem.l_extendedprice",
                                "lineitem.l_discount"
                              ],
                              "Inner Unique": false,
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Relation Name": "orders",
                                  "Schema": "public",
                                  "Alias": "orders",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 33394.06,
                                  "Plan Rows": 18419,
                                  "Plan Width": 8,
                                  "Output": [
                                    "orders.o_orderkey",
                                    "orders.o_custkey",
                                    "orders.o_orderstatus",
                                    "orders.o_totalprice",
                                    "orders.o_orderdate",
                                    "orders.o_orderpriority",
                                    "orders.o_clerk",
                                    "orders.o_shippriority",
                                    "orders.o_comment"
                                  ],
                                  "Filter": "((orders.o_orderdate >= '1993-09-01'::date) AND (orders.o_orderdate < '1993-12-01 00:00:00'::timestamp without time zone))"
                                },
                                {
                                  "Node Type": "Index Scan",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Scan Direction": "Forward",
                                  "Index Name": "lineitem_pkey",
                                  "Relation Name": "lineitem",
                                  "Schema": "public",
                                  "Alias": "lineitem",
                                  "Startup Cost": 0.43,
                                  "Total Cost": 2.29,
                                  "Plan Rows": 1,
                                  "Plan Width": 16,
                                  "Output": [
                                    "lineitem.l_orderkey",
                                    "lineitem.l_partkey",
                                    "lineitem.l_suppkey",
                                    "lineitem.l_linenumber",
                                    "lineitem.l_quantity",
                                    "lineitem.l_extendedprice",
                                    "lineitem.l_discount",
                                    "lineitem.l_tax",
                                    "lineitem.l_returnflag",
                                    "lineitem.l_linestatus",
                                    "lineitem.l_shipdate",
                                    "lineitem.l_commitdate",
                                    "lineitem.l_receiptdate",
                                    "lineitem.l_shipinstruct",
                                    "lineitem.l_shipmode",
                                    "lineitem.l_comment"
                                  ],
                                  "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)",
                                  "Filter": "(lineitem.l_returnflag = 'R'::bpchar)"
                                }
                              ]
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Startup Cost": 4225.0,
                              "Total Cost": 4225.0,
                              "Plan Rows": 62500,
                              "Plan Width": 148,
                              "Output": [
                                "customer.c_custkey",
                                "customer.c_name",
                                "customer.c_acctbal",
                                "customer.c_address",
                                "customer.c_phone",
                                "customer.c_comment",
                                "customer.c_nationkey"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": true,
                                  "Async Capable": false,
                                  "Relation Name": "customer",
                                  "Schema": "public",
                                  "Alias": "customer",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 4225.0,
                                  "Plan Rows": 62500,
                                  "Plan Width": 148,
                                  "Output": [
                                    "customer.c_custkey",
                                    "customer.c_name",
                                    "customer.c_acctbal",
                                    "customer.c_address",
                                    "customer.c_phone",
                                    "customer.c_comment",
                                    "customer.c_nationkey"
                                  ]
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "Node Type": "Hash",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Startup Cost": 1.25,
                          "Total Cost": 1.25,
                          "Plan Rows": 25,
                          "Plan Width": 108,
                          "Output": [
                            "nation.n_name",
                            "nation.n_nationkey"
                          ],
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Relation Name": "nation",
                              "Schema": "public",
                              "Alias": "nation",
                              "Startup Cost": 0.0,
                              "Total Cost": 1.25,
                              "Plan Rows": 25,
                              "Plan Width": 108,
                              "Output": [
                                "nation.n_name",
                                "nation.n_nationkey"
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.284
  }
]
```

---

## 11. Q11 - Q11_100_seed_812199069.sql

**Template:** Q11

**File:** `Q11_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 49934.72,
      "Total Cost": 49961.39,
      "Plan Rows": 10667,
      "Plan Width": 36,
      "Output": [
        "partsupp.ps_partkey",
        "(sum((partsupp.ps_supplycost * (partsupp.ps_availqty)::numeric)))"
      ],
      "Sort Key": [
        "(sum((partsupp.ps_supplycost * (partsupp.ps_availqty)::numeric))) DESC"
      ],
      "Plans": [
        {
          "Node Type": "Aggregate",
          "Strategy": "Plain",
          "Partial Mode": "Finalize",
          "Parent Relationship": "InitPlan",
          "Subplan Name": "InitPlan 1",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 22649.4,
          "Total Cost": 22649.41,
          "Plan Rows": 1,
          "Plan Width": 32,
          "Output": [
            "(sum((partsupp_1.ps_supplycost * (partsupp_1.ps_availqty)::numeric)) * 0.0001000000)"
          ],
          "Plans": [
            {
              "Node Type": "Gather",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 22649.07,
              "Total Cost": 22649.38,
              "Plan Rows": 3,
              "Plan Width": 32,
              "Output": [
                "(PARTIAL sum((partsupp_1.ps_supplycost * (partsupp_1.ps_availqty)::numeric)))"
              ],
              "Workers Planned": 3,
              "Single Copy": false,
              "Plans": [
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Plain",
                  "Partial Mode": "Partial",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 21649.07,
                  "Total Cost": 21649.08,
                  "Plan Rows": 1,
                  "Plan Width": 32,
                  "Output": [
                    "PARTIAL sum((partsupp_1.ps_supplycost * (partsupp_1.ps_availqty)::numeric))"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Hash Join",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 360.02,
                      "Total Cost": 21571.64,
                      "Plan Rows": 10323,
                      "Plan Width": 10,
                      "Output": [
                        "partsupp_1.ps_supplycost",
                        "partsupp_1.ps_availqty"
                      ],
                      "Inner Unique": false,
                      "Hash Cond": "(partsupp_1.ps_suppkey = supplier_1.s_suppkey)",
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "partsupp",
                          "Schema": "public",
                          "Alias": "partsupp_1",
                          "Startup Cost": 0.0,
                          "Total Cost": 20140.65,
                          "Plan Rows": 258065,
                          "Plan Width": 14,
                          "Output": [
                            "partsupp_1.ps_partkey",
                            "partsupp_1.ps_suppkey",
                            "partsupp_1.ps_availqty",
                            "partsupp_1.ps_supplycost",
                            "partsupp_1.ps_comment"
                          ]
                        },
                        {
                          "Node Type": "Hash",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Startup Cost": 355.02,
                          "Total Cost": 355.02,
                          "Plan Rows": 400,
                          "Plan Width": 4,
                          "Output": [
                            "supplier_1.s_suppkey"
                          ],
                          "Plans": [
                            {
                              "Node Type": "Hash Join",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 1.32,
                              "Total Cost": 355.02,
                              "Plan Rows": 400,
                              "Plan Width": 4,
                              "Output": [
                                "supplier_1.s_suppkey"
                              ],
                              "Inner Unique": true,
                              "Hash Cond": "(supplier_1.s_nationkey = nation_1.n_nationkey)",
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Relation Name": "supplier",
                                  "Schema": "public",
                                  "Alias": "supplier_1",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 323.0,
                                  "Plan Rows": 10000,
                                  "Plan Width": 8,
                                  "Output": [
                                    "supplier_1.s_suppkey",
                                    "supplier_1.s_name",
                                    "supplier_1.s_address",
                                    "supplier_1.s_nationkey",
                                    "supplier_1.s_phone",
                                    "supplier_1.s_acctbal",
                                    "supplier_1.s_comment"
                                  ]
                                },
                                {
                                  "Node Type": "Hash",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Startup Cost": 1.31,
                                  "Total Cost": 1.31,
                                  "Plan Rows": 1,
                                  "Plan Width": 4,
                                  "Output": [
                                    "nation_1.n_nationkey"
                                  ],
                                  "Plans": [
                                    {
                                      "Node Type": "Seq Scan",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Relation Name": "nation",
                                      "Schema": "public",
                                      "Alias": "nation_1",
                                      "Startup Cost": 0.0,
                                      "Total Cost": 1.31,
                                      "Plan Rows": 1,
                                      "Plan Width": 4,
                                      "Output": [
                                        "nation_1.n_nationkey"
                                      ],
                                      "Filter": "(nation_1.n_name = 'SAUDI ARABIA'::bpchar)"
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "Node Type": "Aggregate",
          "Strategy": "Hashed",
          "Partial Mode": "Simple",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 26091.64,
          "Total Cost": 26571.64,
          "Plan Rows": 10667,
          "Plan Width": 36,
          "Output": [
            "partsupp.ps_partkey",
            "sum((partsupp.ps_supplycost * (partsupp.ps_availqty)::numeric))"
          ],
          "Group Key": [
            "partsupp.ps_partkey"
          ],
          "Filter": "(sum((partsupp.ps_supplycost * (partsupp.ps_availqty)::numeric)) > (InitPlan 1).col1)",
          "Planned Partitions": 0,
          "Plans": [
            {
              "Node Type": "Gather",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 1360.03,
              "Total Cost": 25771.64,
              "Plan Rows": 32000,
              "Plan Width": 14,
              "Output": [
                "partsupp.ps_partkey",
                "partsupp.ps_supplycost",
                "partsupp.ps_availqty"
              ],
              "Workers Planned": 3,
              "Single Copy": false,
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Join Type": "Inner",
                  "Startup Cost": 360.02,
                  "Total Cost": 21571.64,
                  "Plan Rows": 10323,
                  "Plan Width": 14,
                  "Output": [
                    "partsupp.ps_partkey",
                    "partsupp.ps_supplycost",
                    "partsupp.ps_availqty"
                  ],
                  "Inner Unique": false,
                  "Hash Cond": "(partsupp.ps_suppkey = supplier.s_suppkey)",
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "partsupp",
                      "Schema": "public",
                      "Alias": "partsupp",
                      "Startup Cost": 0.0,
                      "Total Cost": 20140.65,
                      "Plan Rows": 258065,
                      "Plan Width": 18,
                      "Output": [
                        "partsupp.ps_partkey",
                        "partsupp.ps_suppkey",
                        "partsupp.ps_availqty",
                        "partsupp.ps_supplycost",
                        "partsupp.ps_comment"
                      ]
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Startup Cost": 355.02,
                      "Total Cost": 355.02,
                      "Plan Rows": 400,
                      "Plan Width": 4,
                      "Output": [
                        "supplier.s_suppkey"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Hash Join",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 1.32,
                          "Total Cost": 355.02,
                          "Plan Rows": 400,
                          "Plan Width": 4,
                          "Output": [
                            "supplier.s_suppkey"
                          ],
                          "Inner Unique": true,
                          "Hash Cond": "(supplier.s_nationkey = nation.n_nationkey)",
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Relation Name": "supplier",
                              "Schema": "public",
                              "Alias": "supplier",
                              "Startup Cost": 0.0,
                              "Total Cost": 323.0,
                              "Plan Rows": 10000,
                              "Plan Width": 8,
                              "Output": [
                                "supplier.s_suppkey",
                                "supplier.s_name",
                                "supplier.s_address",
                                "supplier.s_nationkey",
                                "supplier.s_phone",
                                "supplier.s_acctbal",
                                "supplier.s_comment"
                              ]
                            },
                            {
                              "Node Type": "Hash",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Startup Cost": 1.31,
                              "Total Cost": 1.31,
                              "Plan Rows": 1,
                              "Plan Width": 4,
                              "Output": [
                                "nation.n_nationkey"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Relation Name": "nation",
                                  "Schema": "public",
                                  "Alias": "nation",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 1.31,
                                  "Plan Rows": 1,
                                  "Plan Width": 4,
                                  "Output": [
                                    "nation.n_nationkey"
                                  ],
                                  "Filter": "(nation.n_name = 'SAUDI ARABIA'::bpchar)"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.124
  }
]
```

---

## 12. Q12 - Q12_100_seed_812199069.sql

**Template:** Q12

**File:** `Q12_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Partial Mode": "Finalize",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 148539.7,
      "Total Cost": 148659.94,
      "Plan Rows": 7,
      "Plan Width": 27,
      "Output": [
        "lineitem.l_shipmode",
        "sum(CASE WHEN ((orders.o_orderpriority = '1-URGENT'::bpchar) OR (orders.o_orderpriority = '2-HIGH'::bpchar)) THEN 1 ELSE 0 END)",
        "sum(CASE WHEN ((orders.o_orderpriority <> '1-URGENT'::bpchar) AND (orders.o_orderpriority <> '2-HIGH'::bpchar)) THEN 1 ELSE 0 END)"
      ],
      "Group Key": [
        "lineitem.l_shipmode"
      ],
      "Plans": [
        {
          "Node Type": "Gather Merge",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 148539.7,
          "Total Cost": 148659.6,
          "Plan Rows": 35,
          "Plan Width": 27,
          "Output": [
            "lineitem.l_shipmode",
            "(PARTIAL sum(CASE WHEN ((orders.o_orderpriority = '1-URGENT'::bpchar) OR (orders.o_orderpriority = '2-HIGH'::bpchar)) THEN 1 ELSE 0 END))",
            "(PARTIAL sum(CASE WHEN ((orders.o_orderpriority <> '1-URGENT'::bpchar) AND (orders.o_orderpriority <> '2-HIGH'::bpchar)) THEN 1 ELSE 0 END))"
          ],
          "Workers Planned": 5,
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Sorted",
              "Partial Mode": "Partial",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 147539.62,
              "Total Cost": 147655.31,
              "Plan Rows": 7,
              "Plan Width": 27,
              "Output": [
                "lineitem.l_shipmode",
                "PARTIAL sum(CASE WHEN ((orders.o_orderpriority = '1-URGENT'::bpchar) OR (orders.o_orderpriority = '2-HIGH'::bpchar)) THEN 1 ELSE 0 END)",
                "PARTIAL sum(CASE WHEN ((orders.o_orderpriority <> '1-URGENT'::bpchar) AND (orders.o_orderpriority <> '2-HIGH'::bpchar)) THEN 1 ELSE 0 END)"
              ],
              "Group Key": [
                "lineitem.l_shipmode"
              ],
              "Plans": [
                {
                  "Node Type": "Sort",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 147539.62,
                  "Total Cost": 147554.07,
                  "Plan Rows": 5781,
                  "Plan Width": 27,
                  "Output": [
                    "lineitem.l_shipmode",
                    "orders.o_orderpriority"
                  ],
                  "Sort Key": [
                    "lineitem.l_shipmode"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 0.43,
                      "Total Cost": 147178.39,
                      "Plan Rows": 5781,
                      "Plan Width": 27,
                      "Output": [
                        "lineitem.l_shipmode",
                        "orders.o_orderpriority"
                      ],
                      "Inner Unique": true,
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "lineitem",
                          "Schema": "public",
                          "Alias": "lineitem",
                          "Startup Cost": 0.0,
                          "Total Cost": 139605.47,
                          "Plan Rows": 5781,
                          "Plan Width": 15,
                          "Output": [
                            "lineitem.l_orderkey",
                            "lineitem.l_partkey",
                            "lineitem.l_suppkey",
                            "lineitem.l_linenumber",
                            "lineitem.l_quantity",
                            "lineitem.l_extendedprice",
                            "lineitem.l_discount",
                            "lineitem.l_tax",
                            "lineitem.l_returnflag",
                            "lineitem.l_linestatus",
                            "lineitem.l_shipdate",
                            "lineitem.l_commitdate",
                            "lineitem.l_receiptdate",
                            "lineitem.l_shipinstruct",
                            "lineitem.l_shipmode",
                            "lineitem.l_comment"
                          ],
                          "Filter": "((lineitem.l_shipmode = ANY ('{TRUCK,SHIP}'::bpchar[])) AND (lineitem.l_commitdate < lineitem.l_receiptdate) AND (lineitem.l_shipdate < lineitem.l_commitdate) AND (lineitem.l_receiptdate >= '1994-01-01'::date) AND (lineitem.l_receiptdate < '1995-01-01 00:00:00'::timestamp without time zone))"
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "orders_pkey",
                          "Relation Name": "orders",
                          "Schema": "public",
                          "Alias": "orders",
                          "Startup Cost": 0.43,
                          "Total Cost": 1.31,
                          "Plan Rows": 1,
                          "Plan Width": 20,
                          "Output": [
                            "orders.o_orderkey",
                            "orders.o_custkey",
                            "orders.o_orderstatus",
                            "orders.o_totalprice",
                            "orders.o_orderdate",
                            "orders.o_orderpriority",
                            "orders.o_clerk",
                            "orders.o_shippriority",
                            "orders.o_comment"
                          ],
                          "Index Cond": "(orders.o_orderkey = lineitem.l_orderkey)"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.088,
    "JIT": {
      "Functions": 15,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 13. Q13 - Q13_100_seed_812199069.sql

**Template:** Q13

**File:** `Q13_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 64579.49,
      "Total Cost": 64579.99,
      "Plan Rows": 200,
      "Plan Width": 16,
      "Output": [
        "(count(orders.o_orderkey))",
        "(count(*))"
      ],
      "Sort Key": [
        "(count(*)) DESC",
        "(count(orders.o_orderkey)) DESC"
      ],
      "Plans": [
        {
          "Node Type": "Aggregate",
          "Strategy": "Hashed",
          "Partial Mode": "Simple",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 64569.85,
          "Total Cost": 64571.85,
          "Plan Rows": 200,
          "Plan Width": 16,
          "Output": [
            "(count(orders.o_orderkey))",
            "count(*)"
          ],
          "Group Key": [
            "count(orders.o_orderkey)"
          ],
          "Planned Partitions": 0,
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Hashed",
              "Partial Mode": "Simple",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 60819.85,
              "Total Cost": 62319.85,
              "Plan Rows": 150000,
              "Plan Width": 12,
              "Output": [
                "customer.c_custkey",
                "count(orders.o_orderkey)"
              ],
              "Group Key": [
                "customer.c_custkey"
              ],
              "Planned Partitions": 0,
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Join Type": "Right",
                  "Startup Cost": 4587.92,
                  "Total Cost": 53379.97,
                  "Plan Rows": 1487976,
                  "Plan Width": 8,
                  "Output": [
                    "customer.c_custkey",
                    "orders.o_orderkey"
                  ],
                  "Inner Unique": true,
                  "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Relation Name": "orders",
                      "Schema": "public",
                      "Alias": "orders",
                      "Startup Cost": 0.0,
                      "Total Cost": 44886.0,
                      "Plan Rows": 1487976,
                      "Plan Width": 8,
                      "Output": [
                        "orders.o_orderkey",
                        "orders.o_custkey",
                        "orders.o_orderstatus",
                        "orders.o_totalprice",
                        "orders.o_orderdate",
                        "orders.o_orderpriority",
                        "orders.o_clerk",
                        "orders.o_shippriority",
                        "orders.o_comment"
                      ],
                      "Filter": "((orders.o_comment)::text !~~ '%express%packages%'::text)"
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Startup Cost": 2712.92,
                      "Total Cost": 2712.92,
                      "Plan Rows": 150000,
                      "Plan Width": 4,
                      "Output": [
                        "customer.c_custkey"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Index Only Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "customer_pkey",
                          "Relation Name": "customer",
                          "Schema": "public",
                          "Alias": "customer",
                          "Startup Cost": 0.42,
                          "Total Cost": 2712.92,
                          "Plan Rows": 150000,
                          "Plan Width": 4,
                          "Output": [
                            "customer.c_custkey"
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.151
  }
]
```

---

## 14. Q14 - Q14_100_seed_812199069.sql

**Template:** Q14

**File:** `Q14_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Plain",
      "Partial Mode": "Finalize",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 137921.76,
      "Total Cost": 137921.78,
      "Plan Rows": 1,
      "Plan Width": 32,
      "Output": [
        "((100.00 * sum(CASE WHEN ((part.p_type)::text ~~ 'PROMO%'::text) THEN (lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) ELSE '0'::numeric END)) / sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))"
      ],
      "Plans": [
        {
          "Node Type": "Gather",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 137921.2,
          "Total Cost": 137921.71,
          "Plan Rows": 5,
          "Plan Width": 64,
          "Output": [
            "(PARTIAL sum(CASE WHEN ((part.p_type)::text ~~ 'PROMO%'::text) THEN (lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) ELSE '0'::numeric END))",
            "(PARTIAL sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))"
          ],
          "Workers Planned": 5,
          "Single Copy": false,
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Plain",
              "Partial Mode": "Partial",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 136921.2,
              "Total Cost": 136921.21,
              "Plan Rows": 1,
              "Plan Width": 64,
              "Output": [
                "PARTIAL sum(CASE WHEN ((part.p_type)::text ~~ 'PROMO%'::text) THEN (lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)) ELSE '0'::numeric END)",
                "PARTIAL sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))"
              ],
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": true,
                  "Async Capable": false,
                  "Join Type": "Inner",
                  "Startup Cost": 6003.0,
                  "Total Cost": 136647.67,
                  "Plan Rows": 15630,
                  "Plan Width": 33,
                  "Output": [
                    "part.p_type",
                    "lineitem.l_extendedprice",
                    "lineitem.l_discount"
                  ],
                  "Inner Unique": true,
                  "Hash Cond": "(lineitem.l_partkey = part.p_partkey)",
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "lineitem",
                      "Schema": "public",
                      "Alias": "lineitem",
                      "Startup Cost": 0.0,
                      "Total Cost": 130603.64,
                      "Plan Rows": 15630,
                      "Plan Width": 16,
                      "Output": [
                        "lineitem.l_orderkey",
                        "lineitem.l_partkey",
                        "lineitem.l_suppkey",
                        "lineitem.l_linenumber",
                        "lineitem.l_quantity",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount",
                        "lineitem.l_tax",
                        "lineitem.l_returnflag",
                        "lineitem.l_linestatus",
                        "lineitem.l_shipdate",
                        "lineitem.l_commitdate",
                        "lineitem.l_receiptdate",
                        "lineitem.l_shipinstruct",
                        "lineitem.l_shipmode",
                        "lineitem.l_comment"
                      ],
                      "Filter": "((lineitem.l_shipdate >= '1994-01-01'::date) AND (lineitem.l_shipdate < '1994-02-01 00:00:00'::timestamp without time zone))"
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Startup Cost": 4961.33,
                      "Total Cost": 4961.33,
                      "Plan Rows": 83333,
                      "Plan Width": 25,
                      "Output": [
                        "part.p_type",
                        "part.p_partkey"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "part",
                          "Schema": "public",
                          "Alias": "part",
                          "Startup Cost": 0.0,
                          "Total Cost": 4961.33,
                          "Plan Rows": 83333,
                          "Plan Width": 25,
                          "Output": [
                            "part.p_type",
                            "part.p_partkey"
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.056,
    "JIT": {
      "Functions": 17,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 15. Q16 - Q16_100_seed_812199069.sql

**Template:** Q16

**File:** `Q16_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 26886.13,
      "Total Cost": 26925.99,
      "Plan Rows": 15945,
      "Plan Width": 44,
      "Output": [
        "part.p_brand",
        "part.p_type",
        "part.p_size",
        "(count(DISTINCT partsupp.ps_suppkey))"
      ],
      "Sort Key": [
        "(count(DISTINCT partsupp.ps_suppkey)) DESC",
        "part.p_brand",
        "part.p_type",
        "part.p_size"
      ],
      "Plans": [
        {
          "Node Type": "Aggregate",
          "Strategy": "Sorted",
          "Partial Mode": "Simple",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 17959.83,
          "Total Cost": 25773.1,
          "Plan Rows": 15945,
          "Plan Width": 44,
          "Output": [
            "part.p_brand",
            "part.p_type",
            "part.p_size",
            "count(DISTINCT partsupp.ps_suppkey)"
          ],
          "Group Key": [
            "part.p_brand",
            "part.p_type",
            "part.p_size"
          ],
          "Plans": [
            {
              "Node Type": "Gather Merge",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 17959.83,
              "Total Cost": 25023.69,
              "Plan Rows": 58996,
              "Plan Width": 40,
              "Output": [
                "part.p_brand",
                "part.p_type",
                "part.p_size",
                "partsupp.ps_suppkey"
              ],
              "Workers Planned": 4,
              "Plans": [
                {
                  "Node Type": "Sort",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 16959.77,
                  "Total Cost": 16996.64,
                  "Plan Rows": 14749,
                  "Plan Width": 40,
                  "Output": [
                    "part.p_brand",
                    "part.p_type",
                    "part.p_size",
                    "partsupp.ps_suppkey"
                  ],
                  "Sort Key": [
                    "part.p_brand",
                    "part.p_type",
                    "part.p_size",
                    "partsupp.ps_suppkey"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Hash Join",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 6713.4,
                      "Total Cost": 15938.52,
                      "Plan Rows": 14749,
                      "Plan Width": 40,
                      "Output": [
                        "part.p_brand",
                        "part.p_type",
                        "part.p_size",
                        "partsupp.ps_suppkey"
                      ],
                      "Inner Unique": true,
                      "Hash Cond": "(partsupp.ps_partkey = part.p_partkey)",
                      "Plans": [
                        {
                          "Node Type": "Index Only Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "partsupp_pkey",
                          "Relation Name": "partsupp",
                          "Schema": "public",
                          "Alias": "partsupp",
                          "Startup Cost": 348.43,
                          "Total Cost": 9311.05,
                          "Plan Rows": 100000,
                          "Plan Width": 8,
                          "Output": [
                            "partsupp.ps_partkey",
                            "partsupp.ps_suppkey"
                          ],
                          "Filter": "(NOT (ANY (partsupp.ps_suppkey = (hashed SubPlan 1).col1)))",
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "SubPlan",
                              "Subplan Name": "SubPlan 1",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Relation Name": "supplier",
                              "Schema": "public",
                              "Alias": "supplier",
                              "Startup Cost": 0.0,
                              "Total Cost": 348.0,
                              "Plan Rows": 1,
                              "Plan Width": 4,
                              "Output": [
                                "supplier.s_suppkey"
                              ],
                              "Filter": "((supplier.s_comment)::text ~~ '%Customer%Complaints%'::text)"
                            }
                          ]
                        },
                        {
                          "Node Type": "Hash",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Startup Cost": 6211.33,
                          "Total Cost": 6211.33,
                          "Plan Rows": 12291,
                          "Plan Width": 40,
                          "Output": [
                            "part.p_brand",
                            "part.p_type",
                            "part.p_size",
                            "part.p_partkey"
                          ],
                          "Plans": [
                            {
                              "Node Type": "Seq Scan",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": true,
                              "Async Capable": false,
                              "Relation Name": "part",
                              "Schema": "public",
                              "Alias": "part",
                              "Startup Cost": 0.0,
                              "Total Cost": 6211.33,
                              "Plan Rows": 12291,
                              "Plan Width": 40,
                              "Output": [
                                "part.p_brand",
                                "part.p_type",
                                "part.p_size",
                                "part.p_partkey"
                              ],
                              "Filter": "((part.p_brand <> 'Brand#54'::bpchar) AND ((part.p_type)::text !~~ 'LARGE PLATED%'::text) AND (part.p_size = ANY ('{5,39,31,50,40,37,32,36}'::integer[])))"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.175
  }
]
```

---

## 16. Q17 - Q17_100_seed_812199069.sql

**Template:** Q17

**File:** `Q17_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Plain",
      "Partial Mode": "Simple",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 2070923.5,
      "Total Cost": 2070923.52,
      "Plan Rows": 1,
      "Plan Width": 32,
      "Output": [
        "(sum(lineitem.l_extendedprice) / 7.0)"
      ],
      "Plans": [
        {
          "Node Type": "Hash Join",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Join Type": "Inner",
          "Startup Cost": 6400.28,
          "Total Cost": 2070918.55,
          "Plan Rows": 1980,
          "Plan Width": 8,
          "Output": [
            "lineitem.l_extendedprice"
          ],
          "Inner Unique": true,
          "Hash Cond": "(lineitem.l_partkey = part.p_partkey)",
          "Join Filter": "(lineitem.l_quantity < (SubPlan 1))",
          "Plans": [
            {
              "Node Type": "Seq Scan",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Relation Name": "lineitem",
              "Schema": "public",
              "Alias": "lineitem",
              "Startup Cost": 0.0,
              "Total Cost": 172612.15,
              "Plan Rows": 6001215,
              "Plan Width": 17,
              "Output": [
                "lineitem.l_orderkey",
                "lineitem.l_partkey",
                "lineitem.l_suppkey",
                "lineitem.l_linenumber",
                "lineitem.l_quantity",
                "lineitem.l_extendedprice",
                "lineitem.l_discount",
                "lineitem.l_tax",
                "lineitem.l_returnflag",
                "lineitem.l_linestatus",
                "lineitem.l_shipdate",
                "lineitem.l_commitdate",
                "lineitem.l_receiptdate",
                "lineitem.l_shipinstruct",
                "lineitem.l_shipmode",
                "lineitem.l_comment"
              ]
            },
            {
              "Node Type": "Hash",
              "Parent Relationship": "Inner",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 6397.8,
              "Total Cost": 6397.8,
              "Plan Rows": 198,
              "Plan Width": 4,
              "Output": [
                "part.p_partkey"
              ],
              "Plans": [
                {
                  "Node Type": "Gather",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 1000.0,
                  "Total Cost": 6397.8,
                  "Plan Rows": 198,
                  "Plan Width": 4,
                  "Output": [
                    "part.p_partkey"
                  ],
                  "Workers Planned": 2,
                  "Single Copy": false,
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "part",
                      "Schema": "public",
                      "Alias": "part",
                      "Startup Cost": 0.0,
                      "Total Cost": 5378.0,
                      "Plan Rows": 82,
                      "Plan Width": 4,
                      "Output": [
                        "part.p_partkey"
                      ],
                      "Filter": "((part.p_brand = 'Brand#43'::bpchar) AND (part.p_container = 'SM JAR'::bpchar))"
                    }
                  ]
                }
              ]
            },
            {
              "Node Type": "Aggregate",
              "Strategy": "Plain",
              "Partial Mode": "Simple",
              "Parent Relationship": "SubPlan",
              "Subplan Name": "SubPlan 1",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 187615.27,
              "Total Cost": 187615.28,
              "Plan Rows": 1,
              "Plan Width": 32,
              "Output": [
                "(0.2 * avg(lineitem_1.l_quantity))"
              ],
              "Plans": [
                {
                  "Node Type": "Seq Scan",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Relation Name": "lineitem",
                  "Schema": "public",
                  "Alias": "lineitem_1",
                  "Startup Cost": 0.0,
                  "Total Cost": 187615.19,
                  "Plan Rows": 31,
                  "Plan Width": 5,
                  "Output": [
                    "lineitem_1.l_orderkey",
                    "lineitem_1.l_partkey",
                    "lineitem_1.l_suppkey",
                    "lineitem_1.l_linenumber",
                    "lineitem_1.l_quantity",
                    "lineitem_1.l_extendedprice",
                    "lineitem_1.l_discount",
                    "lineitem_1.l_tax",
                    "lineitem_1.l_returnflag",
                    "lineitem_1.l_linestatus",
                    "lineitem_1.l_shipdate",
                    "lineitem_1.l_commitdate",
                    "lineitem_1.l_receiptdate",
                    "lineitem_1.l_shipinstruct",
                    "lineitem_1.l_shipmode",
                    "lineitem_1.l_comment"
                  ],
                  "Filter": "(lineitem_1.l_partkey = part.p_partkey)"
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.059,
    "JIT": {
      "Functions": 24,
      "Options": {
        "Inlining": true,
        "Optimization": true,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 17. Q18 - Q18_100_seed_812199069.sql

**Template:** Q18

**File:** `Q18_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Limit",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 732650.26,
      "Total Cost": 732650.51,
      "Plan Rows": 100,
      "Plan Width": 71,
      "Output": [
        "customer.c_name",
        "customer.c_custkey",
        "orders.o_orderkey",
        "orders.o_orderdate",
        "orders.o_totalprice",
        "(sum(lineitem.l_quantity))"
      ],
      "Plans": [
        {
          "Node Type": "Sort",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 732650.26,
          "Total Cost": 736728.42,
          "Plan Rows": 1631266,
          "Plan Width": 71,
          "Output": [
            "customer.c_name",
            "customer.c_custkey",
            "orders.o_orderkey",
            "orders.o_orderdate",
            "orders.o_totalprice",
            "(sum(lineitem.l_quantity))"
          ],
          "Sort Key": [
            "orders.o_totalprice DESC",
            "orders.o_orderdate"
          ],
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Sorted",
              "Partial Mode": "Simple",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 341523.47,
              "Total Cost": 670304.45,
              "Plan Rows": 1631266,
              "Plan Width": 71,
              "Output": [
                "customer.c_name",
                "customer.c_custkey",
                "orders.o_orderkey",
                "orders.o_orderdate",
                "orders.o_totalprice",
                "sum(lineitem.l_quantity)"
              ],
              "Group Key": [
                "customer.c_custkey",
                "orders.o_orderkey"
              ],
              "Plans": [
                {
                  "Node Type": "Gather Merge",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 341523.47,
                  "Total Cost": 637679.13,
                  "Plan Rows": 1631266,
                  "Plan Width": 44,
                  "Output": [
                    "customer.c_custkey",
                    "orders.o_orderkey",
                    "customer.c_name",
                    "orders.o_orderdate",
                    "orders.o_totalprice",
                    "lineitem.l_quantity"
                  ],
                  "Workers Planned": 3,
                  "Plans": [
                    {
                      "Node Type": "Incremental Sort",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Startup Cost": 340523.43,
                      "Total Cost": 445005.33,
                      "Plan Rows": 526215,
                      "Plan Width": 44,
                      "Output": [
                        "customer.c_custkey",
                        "orders.o_orderkey",
                        "customer.c_name",
                        "orders.o_orderdate",
                        "orders.o_totalprice",
                        "lineitem.l_quantity"
                      ],
                      "Sort Key": [
                        "customer.c_custkey",
                        "orders.o_orderkey"
                      ],
                      "Presorted Key": [
                        "customer.c_custkey"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Nested Loop",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Join Type": "Inner",
                          "Startup Cost": 340522.8,
                          "Total Cost": 430663.58,
                          "Plan Rows": 526215,
                          "Plan Width": 44,
                          "Output": [
                            "customer.c_custkey",
                            "orders.o_orderkey",
                            "customer.c_name",
                            "orders.o_orderdate",
                            "orders.o_totalprice",
                            "lineitem.l_quantity"
                          ],
                          "Inner Unique": false,
                          "Plans": [
                            {
                              "Node Type": "Merge Join",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Join Type": "Inner",
                              "Startup Cost": 340522.36,
                              "Total Cost": 343245.24,
                              "Plan Rows": 131527,
                              "Plan Width": 43,
                              "Output": [
                                "customer.c_name",
                                "customer.c_custkey",
                                "orders.o_orderkey",
                                "orders.o_orderdate",
                                "orders.o_totalprice",
                                "lineitem_1.l_orderkey"
                              ],
                              "Inner Unique": true,
                              "Merge Cond": "(orders.o_custkey = customer.c_custkey)",
                              "Plans": [
                                {
                                  "Node Type": "Sort",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Startup Cost": 322526.4,
                                  "Total Cost": 322855.22,
                                  "Plan Rows": 131527,
                                  "Plan Width": 24,
                                  "Output": [
                                    "orders.o_orderkey",
                                    "orders.o_orderdate",
                                    "orders.o_totalprice",
                                    "orders.o_custkey",
                                    "lineitem_1.l_orderkey"
                                  ],
                                  "Sort Key": [
                                    "orders.o_custkey"
                                  ],
                                  "Plans": [
                                    {
                                      "Node Type": "Hash Join",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Join Type": "Inner",
                                      "Startup Cost": 279098.44,
                                      "Total Cost": 311343.31,
                                      "Plan Rows": 131527,
                                      "Plan Width": 24,
                                      "Output": [
                                        "orders.o_orderkey",
                                        "orders.o_orderdate",
                                        "orders.o_totalprice",
                                        "orders.o_custkey",
                                        "lineitem_1.l_orderkey"
                                      ],
                                      "Inner Unique": true,
                                      "Hash Cond": "(orders.o_orderkey = lineitem_1.l_orderkey)",
                                      "Plans": [
                                        {
                                          "Node Type": "Seq Scan",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": true,
                                          "Async Capable": false,
                                          "Relation Name": "orders",
                                          "Schema": "public",
                                          "Alias": "orders",
                                          "Startup Cost": 0.0,
                                          "Total Cost": 30974.71,
                                          "Plan Rows": 483871,
                                          "Plan Width": 20,
                                          "Output": [
                                            "orders.o_orderkey",
                                            "orders.o_custkey",
                                            "orders.o_orderstatus",
                                            "orders.o_totalprice",
                                            "orders.o_orderdate",
                                            "orders.o_orderpriority",
                                            "orders.o_clerk",
                                            "orders.o_shippriority",
                                            "orders.o_comment"
                                          ]
                                        },
                                        {
                                          "Node Type": "Hash",
                                          "Parent Relationship": "Inner",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Startup Cost": 274001.77,
                                          "Total Cost": 274001.77,
                                          "Plan Rows": 407734,
                                          "Plan Width": 4,
                                          "Output": [
                                            "lineitem_1.l_orderkey"
                                          ],
                                          "Plans": [
                                            {
                                              "Node Type": "Aggregate",
                                              "Strategy": "Sorted",
                                              "Partial Mode": "Simple",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Startup Cost": 0.43,
                                              "Total Cost": 274001.77,
                                              "Plan Rows": 407734,
                                              "Plan Width": 4,
                                              "Output": [
                                                "lineitem_1.l_orderkey"
                                              ],
                                              "Group Key": [
                                                "lineitem_1.l_orderkey"
                                              ],
                                              "Filter": "(sum(lineitem_1.l_quantity) > '314'::numeric)",
                                              "Plans": [
                                                {
                                                  "Node Type": "Index Scan",
                                                  "Parent Relationship": "Outer",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Scan Direction": "Forward",
                                                  "Index Name": "lineitem_pkey",
                                                  "Relation Name": "lineitem",
                                                  "Schema": "public",
                                                  "Alias": "lineitem_1",
                                                  "Startup Cost": 0.43,
                                                  "Total Cost": 225647.66,
                                                  "Plan Rows": 6001215,
                                                  "Plan Width": 9,
                                                  "Output": [
                                                    "lineitem_1.l_orderkey",
                                                    "lineitem_1.l_partkey",
                                                    "lineitem_1.l_suppkey",
                                                    "lineitem_1.l_linenumber",
                                                    "lineitem_1.l_quantity",
                                                    "lineitem_1.l_extendedprice",
                                                    "lineitem_1.l_discount",
                                                    "lineitem_1.l_tax",
                                                    "lineitem_1.l_returnflag",
                                                    "lineitem_1.l_linestatus",
                                                    "lineitem_1.l_shipdate",
                                                    "lineitem_1.l_commitdate",
                                                    "lineitem_1.l_receiptdate",
                                                    "lineitem_1.l_shipinstruct",
                                                    "lineitem_1.l_shipmode",
                                                    "lineitem_1.l_comment"
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                },
                                {
                                  "Node Type": "Sort",
                                  "Parent Relationship": "Inner",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Startup Cost": 17995.95,
                                  "Total Cost": 18370.95,
                                  "Plan Rows": 150000,
                                  "Plan Width": 23,
                                  "Output": [
                                    "customer.c_name",
                                    "customer.c_custkey"
                                  ],
                                  "Sort Key": [
                                    "customer.c_custkey"
                                  ],
                                  "Plans": [
                                    {
                                      "Node Type": "Seq Scan",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Relation Name": "customer",
                                      "Schema": "public",
                                      "Alias": "customer",
                                      "Startup Cost": 0.0,
                                      "Total Cost": 5100.0,
                                      "Plan Rows": 150000,
                                      "Plan Width": 23,
                                      "Output": [
                                        "customer.c_name",
                                        "customer.c_custkey"
                                      ]
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "Node Type": "Index Scan",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Scan Direction": "Forward",
                              "Index Name": "lineitem_pkey",
                              "Relation Name": "lineitem",
                              "Schema": "public",
                              "Alias": "lineitem",
                              "Startup Cost": 0.43,
                              "Total Cost": 0.61,
                              "Plan Rows": 5,
                              "Plan Width": 9,
                              "Output": [
                                "lineitem.l_orderkey",
                                "lineitem.l_partkey",
                                "lineitem.l_suppkey",
                                "lineitem.l_linenumber",
                                "lineitem.l_quantity",
                                "lineitem.l_extendedprice",
                                "lineitem.l_discount",
                                "lineitem.l_tax",
                                "lineitem.l_returnflag",
                                "lineitem.l_linestatus",
                                "lineitem.l_shipdate",
                                "lineitem.l_commitdate",
                                "lineitem.l_receiptdate",
                                "lineitem.l_shipinstruct",
                                "lineitem.l_shipmode",
                                "lineitem.l_comment"
                              ],
                              "Index Cond": "(lineitem.l_orderkey = orders.o_orderkey)"
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.281,
    "JIT": {
      "Functions": 32,
      "Options": {
        "Inlining": true,
        "Optimization": true,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 18. Q19 - Q19_100_seed_812199069.sql

**Template:** Q19

**File:** `Q19_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Plain",
      "Partial Mode": "Finalize",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 157339.26,
      "Total Cost": 157339.27,
      "Plan Rows": 1,
      "Plan Width": 32,
      "Output": [
        "sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))"
      ],
      "Plans": [
        {
          "Node Type": "Gather",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 157338.73,
          "Total Cost": 157339.24,
          "Plan Rows": 5,
          "Plan Width": 32,
          "Output": [
            "(PARTIAL sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount))))"
          ],
          "Workers Planned": 5,
          "Single Copy": false,
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Plain",
              "Partial Mode": "Partial",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 156338.73,
              "Total Cost": 156338.74,
              "Plan Rows": 1,
              "Plan Width": 32,
              "Output": [
                "PARTIAL sum((lineitem.l_extendedprice * ('1'::numeric - lineitem.l_discount)))"
              ],
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": true,
                  "Async Capable": false,
                  "Join Type": "Inner",
                  "Startup Cost": 7672.22,
                  "Total Cost": 156338.55,
                  "Plan Rows": 23,
                  "Plan Width": 12,
                  "Output": [
                    "lineitem.l_extendedprice",
                    "lineitem.l_discount"
                  ],
                  "Inner Unique": true,
                  "Hash Cond": "(lineitem.l_partkey = part.p_partkey)",
                  "Join Filter": "(((part.p_brand = 'Brand#14'::bpchar) AND (part.p_container = ANY ('{\"SM CASE\",\"SM BOX\",\"SM PACK\",\"SM PKG\"}'::bpchar[])) AND (lineitem.l_quantity >= '6'::numeric) AND (lineitem.l_quantity <= '16'::numeric) AND (part.p_size <= 5)) OR ((part.p_brand = 'Brand#35'::bpchar) AND (part.p_container = ANY ('{\"MED BAG\",\"MED BOX\",\"MED PKG\",\"MED PACK\"}'::bpchar[])) AND (lineitem.l_quantity >= '17'::numeric) AND (lineitem.l_quantity <= '27'::numeric) AND (part.p_size <= 10)) OR ((part.p_brand = 'Brand#44'::bpchar) AND (part.p_container = ANY ('{\"LG CASE\",\"LG BOX\",\"LG PACK\",\"LG PKG\"}'::bpchar[])) AND (lineitem.l_quantity >= '24'::numeric) AND (lineitem.l_quantity <= '34'::numeric) AND (part.p_size <= 15)))",
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "lineitem",
                      "Schema": "public",
                      "Alias": "lineitem",
                      "Startup Cost": 0.0,
                      "Total Cost": 148607.29,
                      "Plan Rows": 22493,
                      "Plan Width": 21,
                      "Output": [
                        "lineitem.l_orderkey",
                        "lineitem.l_partkey",
                        "lineitem.l_suppkey",
                        "lineitem.l_linenumber",
                        "lineitem.l_quantity",
                        "lineitem.l_extendedprice",
                        "lineitem.l_discount",
                        "lineitem.l_tax",
                        "lineitem.l_returnflag",
                        "lineitem.l_linestatus",
                        "lineitem.l_shipdate",
                        "lineitem.l_commitdate",
                        "lineitem.l_receiptdate",
                        "lineitem.l_shipinstruct",
                        "lineitem.l_shipmode",
                        "lineitem.l_comment"
                      ],
                      "Filter": "((lineitem.l_shipmode = ANY ('{AIR,\"AIR REG\"}'::bpchar[])) AND (lineitem.l_shipinstruct = 'DELIVER IN PERSON'::bpchar) AND (((lineitem.l_quantity >= '6'::numeric) AND (lineitem.l_quantity <= '16'::numeric)) OR ((lineitem.l_quantity >= '17'::numeric) AND (lineitem.l_quantity <= '27'::numeric)) OR ((lineitem.l_quantity >= '24'::numeric) AND (lineitem.l_quantity <= '34'::numeric))))"
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Startup Cost": 7669.67,
                      "Total Cost": 7669.67,
                      "Plan Rows": 204,
                      "Plan Width": 30,
                      "Output": [
                        "part.p_partkey",
                        "part.p_brand",
                        "part.p_container",
                        "part.p_size"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "part",
                          "Schema": "public",
                          "Alias": "part",
                          "Startup Cost": 0.0,
                          "Total Cost": 7669.67,
                          "Plan Rows": 204,
                          "Plan Width": 30,
                          "Output": [
                            "part.p_partkey",
                            "part.p_brand",
                            "part.p_container",
                            "part.p_size"
                          ],
                          "Filter": "((part.p_size >= 1) AND (((part.p_brand = 'Brand#14'::bpchar) AND (part.p_container = ANY ('{\"SM CASE\",\"SM BOX\",\"SM PACK\",\"SM PKG\"}'::bpchar[])) AND (part.p_size <= 5)) OR ((part.p_brand = 'Brand#35'::bpchar) AND (part.p_container = ANY ('{\"MED BAG\",\"MED BOX\",\"MED PKG\",\"MED PACK\"}'::bpchar[])) AND (part.p_size <= 10)) OR ((part.p_brand = 'Brand#44'::bpchar) AND (part.p_container = ANY ('{\"LG CASE\",\"LG BOX\",\"LG PACK\",\"LG PKG\"}'::bpchar[])) AND (part.p_size <= 15))))"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.112,
    "JIT": {
      "Functions": 21,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 19. Q20 - Q20_100_seed_812199069.sql

**Template:** Q20

**File:** `Q20_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Sort",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 2238341989.8,
      "Total Cost": 2238341990.12,
      "Plan Rows": 128,
      "Plan Width": 51,
      "Output": [
        "supplier.s_name",
        "supplier.s_address"
      ],
      "Sort Key": [
        "supplier.s_name"
      ],
      "Plans": [
        {
          "Node Type": "Nested Loop",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Join Type": "Inner",
          "Startup Cost": 0.42,
          "Total Cost": 2238341985.32,
          "Plan Rows": 128,
          "Plan Width": 51,
          "Output": [
            "supplier.s_name",
            "supplier.s_address"
          ],
          "Inner Unique": false,
          "Join Filter": "(nation.n_nationkey = supplier.s_nationkey)",
          "Plans": [
            {
              "Node Type": "Seq Scan",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Relation Name": "nation",
              "Schema": "public",
              "Alias": "nation",
              "Startup Cost": 0.0,
              "Total Cost": 1.31,
              "Plan Rows": 1,
              "Plan Width": 4,
              "Output": [
                "nation.n_nationkey",
                "nation.n_name",
                "nation.n_regionkey",
                "nation.n_comment"
              ],
              "Filter": "(nation.n_name = 'UNITED STATES'::bpchar)"
            },
            {
              "Node Type": "Nested Loop",
              "Parent Relationship": "Inner",
              "Parallel Aware": false,
              "Async Capable": false,
              "Join Type": "Semi",
              "Startup Cost": 0.42,
              "Total Cost": 2238341943.92,
              "Plan Rows": 3207,
              "Plan Width": 55,
              "Output": [
                "supplier.s_name",
                "supplier.s_address",
                "supplier.s_nationkey"
              ],
              "Inner Unique": false,
              "Join Filter": "(supplier.s_suppkey = partsupp.ps_suppkey)",
              "Plans": [
                {
                  "Node Type": "Seq Scan",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Relation Name": "supplier",
                  "Schema": "public",
                  "Alias": "supplier",
                  "Startup Cost": 0.0,
                  "Total Cost": 323.0,
                  "Plan Rows": 10000,
                  "Plan Width": 59,
                  "Output": [
                    "supplier.s_suppkey",
                    "supplier.s_name",
                    "supplier.s_address",
                    "supplier.s_nationkey",
                    "supplier.s_phone",
                    "supplier.s_acctbal",
                    "supplier.s_comment"
                  ]
                },
                {
                  "Node Type": "Materialize",
                  "Parent Relationship": "Inner",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 0.42,
                  "Total Cost": 2237860578.94,
                  "Plan Rows": 3207,
                  "Plan Width": 4,
                  "Output": [
                    "partsupp.ps_suppkey"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 0.42,
                      "Total Cost": 2237860562.9,
                      "Plan Rows": 3207,
                      "Plan Width": 4,
                      "Output": [
                        "partsupp.ps_suppkey"
                      ],
                      "Inner Unique": false,
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Relation Name": "part",
                          "Schema": "public",
                          "Alias": "part",
                          "Startup Cost": 0.0,
                          "Total Cost": 6628.0,
                          "Plan Rows": 2405,
                          "Plan Width": 4,
                          "Output": [
                            "part.p_partkey",
                            "part.p_name",
                            "part.p_mfgr",
                            "part.p_brand",
                            "part.p_type",
                            "part.p_size",
                            "part.p_container",
                            "part.p_retailprice",
                            "part.p_comment"
                          ],
                          "Filter": "((part.p_name)::text ~~ 'rosy%'::text)"
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "partsupp_pkey",
                          "Relation Name": "partsupp",
                          "Schema": "public",
                          "Alias": "partsupp",
                          "Startup Cost": 0.42,
                          "Total Cost": 930500.59,
                          "Plan Rows": 1,
                          "Plan Width": 8,
                          "Output": [
                            "partsupp.ps_partkey",
                            "partsupp.ps_suppkey",
                            "partsupp.ps_availqty",
                            "partsupp.ps_supplycost",
                            "partsupp.ps_comment"
                          ],
                          "Index Cond": "(partsupp.ps_partkey = part.p_partkey)",
                          "Filter": "((partsupp.ps_availqty)::numeric > (SubPlan 1))",
                          "Plans": [
                            {
                              "Node Type": "Aggregate",
                              "Strategy": "Plain",
                              "Partial Mode": "Simple",
                              "Parent Relationship": "SubPlan",
                              "Subplan Name": "SubPlan 1",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Startup Cost": 232624.3,
                              "Total Cost": 232624.32,
                              "Plan Rows": 1,
                              "Plan Width": 32,
                              "Output": [
                                "(0.5 * sum(lineitem.l_quantity))"
                              ],
                              "Plans": [
                                {
                                  "Node Type": "Seq Scan",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Relation Name": "lineitem",
                                  "Schema": "public",
                                  "Alias": "lineitem",
                                  "Startup Cost": 0.0,
                                  "Total Cost": 232624.3,
                                  "Plan Rows": 1,
                                  "Plan Width": 5,
                                  "Output": [
                                    "lineitem.l_orderkey",
                                    "lineitem.l_partkey",
                                    "lineitem.l_suppkey",
                                    "lineitem.l_linenumber",
                                    "lineitem.l_quantity",
                                    "lineitem.l_extendedprice",
                                    "lineitem.l_discount",
                                    "lineitem.l_tax",
                                    "lineitem.l_returnflag",
                                    "lineitem.l_linestatus",
                                    "lineitem.l_shipdate",
                                    "lineitem.l_commitdate",
                                    "lineitem.l_receiptdate",
                                    "lineitem.l_shipinstruct",
                                    "lineitem.l_shipmode",
                                    "lineitem.l_comment"
                                  ],
                                  "Filter": "((lineitem.l_shipdate >= '1995-01-01'::date) AND (lineitem.l_shipdate < '1996-01-01 00:00:00'::timestamp without time zone) AND (lineitem.l_partkey = partsupp.ps_partkey) AND (lineitem.l_suppkey = partsupp.ps_suppkey))"
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.156,
    "JIT": {
      "Functions": 27,
      "Options": {
        "Inlining": true,
        "Optimization": true,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 20. Q21 - Q21_100_seed_812199069.sql

**Template:** Q21

**File:** `Q21_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Limit",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 140017.17,
      "Total Cost": 140017.17,
      "Plan Rows": 1,
      "Plan Width": 34,
      "Output": [
        "supplier.s_name",
        "(count(*))"
      ],
      "Plans": [
        {
          "Node Type": "Sort",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 140017.17,
          "Total Cost": 140017.17,
          "Plan Rows": 1,
          "Plan Width": 34,
          "Output": [
            "supplier.s_name",
            "(count(*))"
          ],
          "Sort Key": [
            "(count(*)) DESC",
            "supplier.s_name"
          ],
          "Plans": [
            {
              "Node Type": "Aggregate",
              "Strategy": "Sorted",
              "Partial Mode": "Simple",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 140017.14,
              "Total Cost": 140017.16,
              "Plan Rows": 1,
              "Plan Width": 34,
              "Output": [
                "supplier.s_name",
                "count(*)"
              ],
              "Group Key": [
                "supplier.s_name"
              ],
              "Plans": [
                {
                  "Node Type": "Sort",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 140017.14,
                  "Total Cost": 140017.14,
                  "Plan Rows": 1,
                  "Plan Width": 26,
                  "Output": [
                    "supplier.s_name"
                  ],
                  "Sort Key": [
                    "supplier.s_name"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Nested Loop",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": false,
                      "Async Capable": false,
                      "Join Type": "Inner",
                      "Startup Cost": 1361.32,
                      "Total Cost": 140017.13,
                      "Plan Rows": 1,
                      "Plan Width": 26,
                      "Output": [
                        "supplier.s_name"
                      ],
                      "Inner Unique": true,
                      "Plans": [
                        {
                          "Node Type": "Nested Loop",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Join Type": "Semi",
                          "Startup Cost": 1360.89,
                          "Total Cost": 140016.66,
                          "Plan Rows": 1,
                          "Plan Width": 34,
                          "Output": [
                            "supplier.s_name",
                            "l1.l_orderkey",
                            "l2.l_orderkey"
                          ],
                          "Inner Unique": false,
                          "Plans": [
                            {
                              "Node Type": "Gather",
                              "Parent Relationship": "Outer",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Startup Cost": 1360.46,
                              "Total Cost": 140016.04,
                              "Plan Rows": 1,
                              "Plan Width": 34,
                              "Output": [
                                "supplier.s_name",
                                "l1.l_suppkey",
                                "l1.l_orderkey"
                              ],
                              "Workers Planned": 5,
                              "Single Copy": false,
                              "Plans": [
                                {
                                  "Node Type": "Nested Loop",
                                  "Parent Relationship": "Outer",
                                  "Parallel Aware": false,
                                  "Async Capable": false,
                                  "Join Type": "Anti",
                                  "Startup Cost": 360.46,
                                  "Total Cost": 139015.94,
                                  "Plan Rows": 1,
                                  "Plan Width": 34,
                                  "Output": [
                                    "supplier.s_name",
                                    "l1.l_suppkey",
                                    "l1.l_orderkey"
                                  ],
                                  "Inner Unique": false,
                                  "Plans": [
                                    {
                                      "Node Type": "Hash Join",
                                      "Parent Relationship": "Outer",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Join Type": "Inner",
                                      "Startup Cost": 360.02,
                                      "Total Cost": 129623.4,
                                      "Plan Rows": 16003,
                                      "Plan Width": 34,
                                      "Output": [
                                        "supplier.s_name",
                                        "l1.l_suppkey",
                                        "l1.l_orderkey"
                                      ],
                                      "Inner Unique": false,
                                      "Hash Cond": "(l1.l_suppkey = supplier.s_suppkey)",
                                      "Plans": [
                                        {
                                          "Node Type": "Seq Scan",
                                          "Parent Relationship": "Outer",
                                          "Parallel Aware": true,
                                          "Async Capable": false,
                                          "Relation Name": "lineitem",
                                          "Schema": "public",
                                          "Alias": "l1",
                                          "Startup Cost": 0.0,
                                          "Total Cost": 127603.04,
                                          "Plan Rows": 400081,
                                          "Plan Width": 8,
                                          "Output": [
                                            "l1.l_orderkey",
                                            "l1.l_partkey",
                                            "l1.l_suppkey",
                                            "l1.l_linenumber",
                                            "l1.l_quantity",
                                            "l1.l_extendedprice",
                                            "l1.l_discount",
                                            "l1.l_tax",
                                            "l1.l_returnflag",
                                            "l1.l_linestatus",
                                            "l1.l_shipdate",
                                            "l1.l_commitdate",
                                            "l1.l_receiptdate",
                                            "l1.l_shipinstruct",
                                            "l1.l_shipmode",
                                            "l1.l_comment"
                                          ],
                                          "Filter": "(l1.l_receiptdate > l1.l_commitdate)"
                                        },
                                        {
                                          "Node Type": "Hash",
                                          "Parent Relationship": "Inner",
                                          "Parallel Aware": false,
                                          "Async Capable": false,
                                          "Startup Cost": 355.02,
                                          "Total Cost": 355.02,
                                          "Plan Rows": 400,
                                          "Plan Width": 30,
                                          "Output": [
                                            "supplier.s_name",
                                            "supplier.s_suppkey"
                                          ],
                                          "Plans": [
                                            {
                                              "Node Type": "Hash Join",
                                              "Parent Relationship": "Outer",
                                              "Parallel Aware": false,
                                              "Async Capable": false,
                                              "Join Type": "Inner",
                                              "Startup Cost": 1.32,
                                              "Total Cost": 355.02,
                                              "Plan Rows": 400,
                                              "Plan Width": 30,
                                              "Output": [
                                                "supplier.s_name",
                                                "supplier.s_suppkey"
                                              ],
                                              "Inner Unique": true,
                                              "Hash Cond": "(supplier.s_nationkey = nation.n_nationkey)",
                                              "Plans": [
                                                {
                                                  "Node Type": "Seq Scan",
                                                  "Parent Relationship": "Outer",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Relation Name": "supplier",
                                                  "Schema": "public",
                                                  "Alias": "supplier",
                                                  "Startup Cost": 0.0,
                                                  "Total Cost": 323.0,
                                                  "Plan Rows": 10000,
                                                  "Plan Width": 34,
                                                  "Output": [
                                                    "supplier.s_suppkey",
                                                    "supplier.s_name",
                                                    "supplier.s_address",
                                                    "supplier.s_nationkey",
                                                    "supplier.s_phone",
                                                    "supplier.s_acctbal",
                                                    "supplier.s_comment"
                                                  ]
                                                },
                                                {
                                                  "Node Type": "Hash",
                                                  "Parent Relationship": "Inner",
                                                  "Parallel Aware": false,
                                                  "Async Capable": false,
                                                  "Startup Cost": 1.31,
                                                  "Total Cost": 1.31,
                                                  "Plan Rows": 1,
                                                  "Plan Width": 4,
                                                  "Output": [
                                                    "nation.n_nationkey"
                                                  ],
                                                  "Plans": [
                                                    {
                                                      "Node Type": "Seq Scan",
                                                      "Parent Relationship": "Outer",
                                                      "Parallel Aware": false,
                                                      "Async Capable": false,
                                                      "Relation Name": "nation",
                                                      "Schema": "public",
                                                      "Alias": "nation",
                                                      "Startup Cost": 0.0,
                                                      "Total Cost": 1.31,
                                                      "Plan Rows": 1,
                                                      "Plan Width": 4,
                                                      "Output": [
                                                        "nation.n_nationkey"
                                                      ],
                                                      "Filter": "(nation.n_name = 'KENYA'::bpchar)"
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    },
                                    {
                                      "Node Type": "Index Scan",
                                      "Parent Relationship": "Inner",
                                      "Parallel Aware": false,
                                      "Async Capable": false,
                                      "Scan Direction": "Forward",
                                      "Index Name": "lineitem_pkey",
                                      "Relation Name": "lineitem",
                                      "Schema": "public",
                                      "Alias": "l3",
                                      "Startup Cost": 0.43,
                                      "Total Cost": 0.62,
                                      "Plan Rows": 2,
                                      "Plan Width": 8,
                                      "Output": [
                                        "l3.l_orderkey",
                                        "l3.l_partkey",
                                        "l3.l_suppkey",
                                        "l3.l_linenumber",
                                        "l3.l_quantity",
                                        "l3.l_extendedprice",
                                        "l3.l_discount",
                                        "l3.l_tax",
                                        "l3.l_returnflag",
                                        "l3.l_linestatus",
                                        "l3.l_shipdate",
                                        "l3.l_commitdate",
                                        "l3.l_receiptdate",
                                        "l3.l_shipinstruct",
                                        "l3.l_shipmode",
                                        "l3.l_comment"
                                      ],
                                      "Index Cond": "(l3.l_orderkey = l1.l_orderkey)",
                                      "Filter": "((l3.l_receiptdate > l3.l_commitdate) AND (l3.l_suppkey <> l1.l_suppkey))"
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "Node Type": "Index Scan",
                              "Parent Relationship": "Inner",
                              "Parallel Aware": false,
                              "Async Capable": false,
                              "Scan Direction": "Forward",
                              "Index Name": "lineitem_pkey",
                              "Relation Name": "lineitem",
                              "Schema": "public",
                              "Alias": "l2",
                              "Startup Cost": 0.43,
                              "Total Cost": 0.6,
                              "Plan Rows": 5,
                              "Plan Width": 8,
                              "Output": [
                                "l2.l_orderkey",
                                "l2.l_partkey",
                                "l2.l_suppkey",
                                "l2.l_linenumber",
                                "l2.l_quantity",
                                "l2.l_extendedprice",
                                "l2.l_discount",
                                "l2.l_tax",
                                "l2.l_returnflag",
                                "l2.l_linestatus",
                                "l2.l_shipdate",
                                "l2.l_commitdate",
                                "l2.l_receiptdate",
                                "l2.l_shipinstruct",
                                "l2.l_shipmode",
                                "l2.l_comment"
                              ],
                              "Index Cond": "(l2.l_orderkey = l1.l_orderkey)",
                              "Filter": "(l2.l_suppkey <> l1.l_suppkey)"
                            }
                          ]
                        },
                        {
                          "Node Type": "Index Scan",
                          "Parent Relationship": "Inner",
                          "Parallel Aware": false,
                          "Async Capable": false,
                          "Scan Direction": "Forward",
                          "Index Name": "orders_pkey",
                          "Relation Name": "orders",
                          "Schema": "public",
                          "Alias": "orders",
                          "Startup Cost": 0.43,
                          "Total Cost": 0.46,
                          "Plan Rows": 1,
                          "Plan Width": 4,
                          "Output": [
                            "orders.o_orderkey",
                            "orders.o_custkey",
                            "orders.o_orderstatus",
                            "orders.o_totalprice",
                            "orders.o_orderdate",
                            "orders.o_orderpriority",
                            "orders.o_clerk",
                            "orders.o_shippriority",
                            "orders.o_comment"
                          ],
                          "Index Cond": "(orders.o_orderkey = l1.l_orderkey)",
                          "Filter": "(orders.o_orderstatus = 'F'::bpchar)"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.587,
    "JIT": {
      "Functions": 44,
      "Options": {
        "Inlining": false,
        "Optimization": false,
        "Expressions": true,
        "Deforming": true
      }
    }
  }
]
```

---

## 21. Q22 - Q22_100_seed_812199069.sql

**Template:** Q22

**File:** `Q22_100_seed_812199069.sql`

### EXPLAIN JSON

```json
[
  {
    "Plan": {
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Partial Mode": "Simple",
      "Parallel Aware": false,
      "Async Capable": false,
      "Startup Cost": 48079.63,
      "Total Cost": 48175.36,
      "Plan Rows": 668,
      "Plan Width": 72,
      "Output": [
        "(SUBSTRING(customer.c_phone FROM 1 FOR 2))",
        "count(*)",
        "sum(customer.c_acctbal)"
      ],
      "Group Key": [
        "(SUBSTRING(customer.c_phone FROM 1 FOR 2))"
      ],
      "Plans": [
        {
          "Node Type": "Aggregate",
          "Strategy": "Plain",
          "Partial Mode": "Finalize",
          "Parent Relationship": "InitPlan",
          "Subplan Name": "InitPlan 1",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 6245.82,
          "Total Cost": 6245.83,
          "Plan Rows": 1,
          "Plan Width": 32,
          "Output": [
            "avg(customer_1.c_acctbal)"
          ],
          "Plans": [
            {
              "Node Type": "Gather",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 6245.6,
              "Total Cost": 6245.81,
              "Plan Rows": 2,
              "Plan Width": 32,
              "Output": [
                "(PARTIAL avg(customer_1.c_acctbal))"
              ],
              "Workers Planned": 2,
              "Single Copy": false,
              "Plans": [
                {
                  "Node Type": "Aggregate",
                  "Strategy": "Plain",
                  "Partial Mode": "Partial",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": false,
                  "Async Capable": false,
                  "Startup Cost": 5245.6,
                  "Total Cost": 5245.61,
                  "Plan Rows": 1,
                  "Plan Width": 32,
                  "Output": [
                    "PARTIAL avg(customer_1.c_acctbal)"
                  ],
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "customer",
                      "Schema": "public",
                      "Alias": "customer_1",
                      "Startup Cost": 0.0,
                      "Total Cost": 5240.62,
                      "Plan Rows": 1988,
                      "Plan Width": 6,
                      "Output": [
                        "customer_1.c_custkey",
                        "customer_1.c_name",
                        "customer_1.c_address",
                        "customer_1.c_nationkey",
                        "customer_1.c_phone",
                        "customer_1.c_acctbal",
                        "customer_1.c_mktsegment",
                        "customer_1.c_comment"
                      ],
                      "Filter": "((customer_1.c_acctbal > 0.00) AND (SUBSTRING(customer_1.c_phone FROM 1 FOR 2) = ANY ('{34,29,27,25,12,22,15}'::text[])))"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "Node Type": "Gather Merge",
          "Parent Relationship": "Outer",
          "Parallel Aware": false,
          "Async Capable": false,
          "Startup Cost": 41833.8,
          "Total Cost": 41912.83,
          "Plan Rows": 668,
          "Plan Width": 38,
          "Output": [
            "(SUBSTRING(customer.c_phone FROM 1 FOR 2))",
            "customer.c_acctbal"
          ],
          "Workers Planned": 3,
          "Plans": [
            {
              "Node Type": "Sort",
              "Parent Relationship": "Outer",
              "Parallel Aware": false,
              "Async Capable": false,
              "Startup Cost": 40833.76,
              "Total Cost": 40834.3,
              "Plan Rows": 215,
              "Plan Width": 38,
              "Output": [
                "(SUBSTRING(customer.c_phone FROM 1 FOR 2))",
                "customer.c_acctbal"
              ],
              "Sort Key": [
                "(SUBSTRING(customer.c_phone FROM 1 FOR 2))"
              ],
              "Plans": [
                {
                  "Node Type": "Hash Join",
                  "Parent Relationship": "Outer",
                  "Parallel Aware": true,
                  "Async Capable": false,
                  "Join Type": "Right Anti",
                  "Startup Cost": 5249.74,
                  "Total Cost": 40825.43,
                  "Plan Rows": 215,
                  "Plan Width": 38,
                  "Output": [
                    "SUBSTRING(customer.c_phone FROM 1 FOR 2)",
                    "customer.c_acctbal"
                  ],
                  "Inner Unique": true,
                  "Hash Cond": "(orders.o_custkey = customer.c_custkey)",
                  "Plans": [
                    {
                      "Node Type": "Seq Scan",
                      "Parent Relationship": "Outer",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Relation Name": "orders",
                      "Schema": "public",
                      "Alias": "orders",
                      "Startup Cost": 0.0,
                      "Total Cost": 30974.71,
                      "Plan Rows": 483871,
                      "Plan Width": 4,
                      "Output": [
                        "orders.o_orderkey",
                        "orders.o_custkey",
                        "orders.o_orderstatus",
                        "orders.o_totalprice",
                        "orders.o_orderdate",
                        "orders.o_orderpriority",
                        "orders.o_clerk",
                        "orders.o_shippriority",
                        "orders.o_comment"
                      ]
                    },
                    {
                      "Node Type": "Hash",
                      "Parent Relationship": "Inner",
                      "Parallel Aware": true,
                      "Async Capable": false,
                      "Startup Cost": 5240.62,
                      "Total Cost": 5240.62,
                      "Plan Rows": 729,
                      "Plan Width": 26,
                      "Output": [
                        "customer.c_phone",
                        "customer.c_acctbal",
                        "customer.c_custkey"
                      ],
                      "Plans": [
                        {
                          "Node Type": "Seq Scan",
                          "Parent Relationship": "Outer",
                          "Parallel Aware": true,
                          "Async Capable": false,
                          "Relation Name": "customer",
                          "Schema": "public",
                          "Alias": "customer",
                          "Startup Cost": 0.0,
                          "Total Cost": 5240.62,
                          "Plan Rows": 729,
                          "Plan Width": 26,
                          "Output": [
                            "customer.c_phone",
                            "customer.c_acctbal",
                            "customer.c_custkey"
                          ],
                          "Filter": "((customer.c_acctbal > (InitPlan 1).col1) AND (SUBSTRING(customer.c_phone FROM 1 FOR 2) = ANY ('{34,29,27,25,12,22,15}'::text[])))"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    "Planning Time": 0.091
  }
]
```

---

