---
name: RAG_MCP
description: Vector search over indexed documents
---

# Meta Rules

## Activation Rule

**CRITICAL:** Use RAG MCP tools ONLY when user writes exactly `rag` in their prompt.

**Triggers RAG:**
- "rag schau was das Paper sagt"
- "rag wie haben wir das gemacht"
- "check mal rag"

**Does NOT trigger RAG:**
- "raggie", "ragms", "raggg" (keine Varianten)
- Prompts ohne das Wort "rag"

**Rule:** Exact match only. No RAG = no RAG tools.

---

## Honesty & Precision (CRITICAL)

**MANDATORY:** For every RAG response:

1. **Provide short quotes** - Quote relevant text directly. Keep quotes brief for verification. Full context not needed in quote.
2. **Flag figures/graphics** - If data is only in a figure you cannot read, IMMEDIATELY say: "The values are in Figure X, I can only read the text"
3. **Communicate uncertainty immediately** - If you cannot find a value in the text, DO NOT guess. Say: "This value is not stated in the text"
4. **No summaries as facts** - "7-114%" is WRONG if you only have "7.30% average" and "114% single example"
5. **State context and scope** - Distinguish between general statements and specific examples

**Example WRONG:**
> "The paper achieved 7-114% MRE (Section 5)"

**Example RIGHT:**
> "The paper states: 'the average error is 7.30%'. The 114% is from a specific example. Per-template values are in Figure 6(d), which I cannot read."

**CRITICAL:** User is writing scientific documents. Incorrect citations = scientific misconduct.

---

## HyDE Pattern (Hypothetical Document Embeddings)

**Problem:** Semantic search fails when user's question uses different words than the document.
- Query: "Wie funktioniert CBO?"
- Document says: "The query planner estimates path costs..."
- → No match despite same concept

**Solution:** Generate a hypothetical answer first, then search with that.

**When to use:**
- Conceptual questions ("How does X work?", "Why does Y happen?")
- User's terminology differs from document terminology
- Direct search returns low-relevance results

**Process:**
1. User asks: "Wie funktioniert CBO?"
2. Generate hypothetical answer (1-2 sentences):
   "Cost-based optimization estimates the cost of different query execution plans by analyzing statistics about table sizes and join selectivity."
3. Search with hypothetical answer as query:
   `search(query="Cost-based optimization estimates the cost of different query execution plans...", collection="...")`
4. Return results

**Do NOT use when:**
- Looking for exact terms (use `search_keyword`)
- User already describes the concept well
- Technical definitions or column names

---

# Tool Framework

## Tool Overview

| Tool | Purpose |
|------|---------|
| `mcp__rag__search` | Semantic search over documents |
| `mcp__rag__search_keyword` | BM25 keyword search for exact terms |
| `mcp__rag__read_document` | Read continuous text from a position |
| `mcp__rag__list_collections` | List all indexed collections |
| `mcp__rag__list_documents` | List documents in a collection |

---

## Cross Tool Usage Example

1. `list_collections()` → see available collections
2. `search(collection="...", query="...")` → semantic search (concepts)
3. `search_keyword(collection="...", query="...")` → keyword search (exact terms)
4. `read_document(collection, document, start_chunk, num_chunks=5)` → read more context

**Drill-Down Pattern:**
```
1. search("supplier relationships TPC-H")  → finds Chunk: 42
2. read_document(start_chunk=40, num_chunks=10) → read full section
3. search_keyword("l_suppkey")             → find exact definition
```

**Workflow Hierarchy:**

`read_document` is a follow-up tool - always use after search/search_keyword.

```
search / search_keyword
         ↓
    Chunk clear? → done
         ↓ no
    read_document(start_chunk from result)
```

**Rule of thumb:** If chunk content is not fully clear → `read_document` for context.

**Complex queries:** For complex user questions, first `search` with `neighbors=1-2`, then `read_document` if needed.

---

## mcp__rag__search

Semantic search over indexed documents using vector embeddings.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query (natural language) |
| `collection` | string | Yes | Collection to search in (use list_collections first) |
| `top_k` | int | No | Number of results (1-20, default: 5) |
| `document` | string | No | Filter by document (e.g. "chapter1.md") |
| `neighbors` | int | No | Include N chunks before/after each match (0-2, default: 0) |

### Context Expansion (neighbors)

When `neighbors > 0`, each result includes adjacent chunks for better context:

- `neighbors=1`: [prev_chunk] + [match] + [next_chunk]
- `neighbors=2`: [prev-2] + [prev-1] + [match] + [next+1] + [next+2]

**Behavior:**
- Overlapping matches are deduplicated and merged
- Results sorted by document order (not score) when neighbors > 0
- Edge cases handled (first/last chunk)

### Examples

```
mcp__rag__search(query="TPC-H benchmark performance", top_k=3)
mcp__rag__search(query="pricing requirements", collection="specification")
mcp__rag__search(query="query execution", collection="specification", document="specification.md")
mcp__rag__search(query="mindset behavior", top_k=3, neighbors=1)
```

**Note:**
- Content is automatically deduplicated - overlapping text between chunks is merged cleanly.
- Use `Chunk: X` value to call `read_document(start_chunk=X)` for more context.

---

## mcp__rag__search_keyword

BM25 keyword search for exact term matches. Complements semantic `search`.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Keywords to search (space = AND) |
| `collection` | string | Yes | Collection to search in |
| `top_k` | int | No | Number of results (1-20, default: 5) |
| `document` | string | No | Filter by document |

### Examples

```
mcp__rag__search_keyword(query="l_suppkey", collection="specification")
mcp__rag__search_keyword(query="TPC-H benchmark", collection="specification", top_k=10)
```

### Query Syntax

- Multiple words are ANDed: `"TPC-H benchmark"` → matches chunks with BOTH words
- Case insensitive
- Stems words: "running" matches "run"

---

## mcp__rag__list_collections

List all indexed collections with chunk counts.

### Parameters

None

### Examples

```
mcp__rag__list_collections()
```

**Output:**
```
Indexed Collections:

  specification (402 chunks)
```

---

## mcp__rag__list_documents

List all documents in a collection with chunk counts.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `collection` | string | Yes | Collection name |

### Examples

```
mcp__rag__list_documents(collection="specification")
```

**Output:**
```
Documents:

  specification.md (402 chunks)
```

---

## mcp__rag__read_document

Read continuous text from a document starting at a specific chunk index.

**Use Case:** After `search` finds a relevant chunk, use `read_document` to read more context forward.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `collection` | string | Yes | Collection name |
| `document` | string | Yes | Document name (e.g. "chunks.md") |
| `start_chunk` | int | Yes | Chunk index to start reading from |
| `num_chunks` | int | No | Number of chunks to read (1-20, default: 5) |

### Examples

```
1. search("mindset change", neighbors=1) → finds chunk 50
2. read_document("The Outward Mindset", "chunks.md", 50, 10) → reads chunks 50-59
```

```
mcp__rag__read_document(collection="specification", document="specification.md", start_chunk=40, num_chunks=10)
mcp__rag__read_document(collection="Thesis", document="3.Plan_Level_Fließ.md", start_chunk=15, num_chunks=5)
mcp__rag__read_document(collection="postgresql-17-US", document="postgresql-17-US.md", start_chunk=100)
```

---

# Thesis Specifics

Swap this section for different projects.

## Relevant Collections

| Collection | Content |
|------------|---------|
| `Thesis` | Existing thesis chapters (multi-document) |
| `Learning-based_Query_Performance_Modeling_and_Pred` | Base paper (Akdere et al.) |
| `postgresql-17-US` | PostgreSQL 17 Documentation |
| `specification` | TPC-H Benchmark Specification |
| `Richtlinien wiss. Arbeiten_01.09.2025` | Formatting and citation guidelines |

**Note:** Collection `Thesis` contains multiple documents. Use `list_documents(collection="Thesis")` to see all, or filter with `document="3.Plan_Level_Fließ.md"`.
