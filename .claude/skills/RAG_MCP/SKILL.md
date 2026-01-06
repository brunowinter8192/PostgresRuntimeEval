---
name: RAG_MCP
description: Vector search over indexed documents
---

# RAG MCP Tools

## Available Tools

| Tool | Purpose |
|------|---------|
| `mcp__rag__search` | Semantic search over documents |
| `mcp__rag__search_keyword` | BM25 keyword search for exact terms |
| `mcp__rag__read_document` | Read continuous text from a position |
| `mcp__rag__list_collections` | List all indexed collections |
| `mcp__rag__list_documents` | List documents in a collection |

---

## Workflow

1. `list_collections()` → see available collections
2. `search(collection="...", query="...")` → semantic search (concepts)
3. `search_keyword(collection="...", query="...")` → keyword search (exact terms)
4. `read_document(collection, document, start_chunk)` → read more context

**Decision Guide:**

| User Intent | Tool |
|-------------|------|
| "Was ist X?" / "Erkläre X" | `search` (semantic) |
| "Wo steht X?" / "Definition von X" | `search_keyword` (BM25) |
| Technical terms, column names | `search_keyword` |
| Conceptual understanding | `search` |
| Konzeptfrage mit anderer Terminologie | HyDE Pattern (see below) |
| "Lies mehr davon" / need full section | `read_document` |

**Drill-Down Pattern:**
```
1. search("supplier relationships TPC-H")  → finds Chunk: 42
2. read_document(start_chunk=40, num_chunks=10) → read full section
3. search_keyword("l_suppkey")             → find exact definition
```

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

**Context Expansion:**
- Search results show `Chunk: X`
- Use `read_document(start_chunk=X-2, num_chunks=10)` to read surrounding context
- Useful when search result is partial/truncated

---

## Tool: `mcp__rag__search`

Semantic search over indexed documents using vector embeddings.

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query (natural language) |
| `collection` | string | Yes | Collection to search in (use list_collections first) |
| `top_k` | int | No | Number of results (1-20, default: 5) |
| `document` | string | No | Filter by document (e.g. "chapter1.md") |
| `neighbors` | int | No | Include N chunks before/after each match (0-2, default: 0) |

---

## Context Expansion (neighbors)

When `neighbors > 0`, each result includes adjacent chunks for better context:

- `neighbors=1`: [prev_chunk] + [match] + [next_chunk]
- `neighbors=2`: [prev-2] + [prev-1] + [match] + [next+1] + [next+2]

**Behavior:**
- Overlapping matches are deduplicated and merged
- Results sorted by document order (not score) when neighbors > 0
- Edge cases handled (first/last chunk)

---

## When to Use

Use RAG search when:
- User asks about content in indexed documents
- User needs specific information from the knowledge base
- Answering questions that require document context

Do NOT use when:
- Information is in codebase files (use Grep/Read instead)
- User asks about general knowledge (use your training data)
- Document hasn't been indexed yet

---

## Examples

### Basic Search
```
mcp__rag__search(query="TPC-H benchmark performance", top_k=3)
```

### Filter by Collection
```
mcp__rag__search(query="pricing requirements", collection="specification")
```

### Filter by Document
```
mcp__rag__search(query="query execution", collection="specification", document="specification.md")
```

### With Context Expansion
```
mcp__rag__search(query="mindset behavior", top_k=3, neighbors=1)
```
Returns 3 results, each with prev + match + next chunk concatenated.

---

## Output Format

```
--- Result 1 (score: 0.7421) ---
Collection: specification | Document: specification.md | Chunk: 42
[full content, overlap-deduplicated]

--- Result 2 (score: 0.6812) ---
Collection: specification | Document: specification.md | Chunk: 87
[full content, overlap-deduplicated]
```

**Note:**
- Content is automatically deduplicated - overlapping text between chunks is merged cleanly.
- Use `Chunk: X` value to call `read_document(start_chunk=X)` for more context.

---

## Tool: `mcp__rag__search_keyword`

BM25 keyword search for exact term matches. Complements semantic `search`.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Keywords to search (space = AND) |
| `collection` | string | Yes | Collection to search in |
| `top_k` | int | No | Number of results (1-20, default: 5) |
| `document` | string | No | Filter by document |

### When to Use

- Finding **exact terms**: "l_suppkey", "TPC-H", "MIN_ERROR_THRESHOLD"
- Finding **definitions**: "Definition: ..."
- **Technical terms**, column names, function names
- When semantic search returns conceptually related but not exact matches

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

## Score Interpretation

| Score | Meaning |
|-------|---------|
| > 0.7 | High relevance |
| 0.5 - 0.7 | Moderate relevance |
| < 0.5 | Low relevance |

---

## Data Structure

```
data/documents/
  {collection}/           <- Filter with collection="..."
    raw/
      {document}.md       <- Original from MinerU
    {document}.md         <- Cleaned version (indexed)
    {document}.json       <- Chunked for indexing
```

**Multi-Document Collections:**
- Ein Ordner kann mehrere MD-Files enthalten → 1 Collection mit N Documents
- Beispiel: `Thesis/` mit `1.Einleitung.md`, `2.Grundlagen.md`, `A_Setup.md`
- `list_documents(collection="Thesis")` zeigt alle Documents
- `search(collection="Thesis", document="A_Setup.md")` filtert auf ein Document

---

## Indexed Collections

Use `mcp__rag__list_collections` to see available collections.

---

## Thesis-Specific Collections

| Collection | Content | Use Case | Document Filter |
|------------|---------|----------|-----------------|
| `Thesis` | Existing thesis chapters | Consistency checking, terminology | `document="3.Plan_Level_Fließ.md"` etc. |
| `Learning-based_Query_Performance_Modeling_and_Pred` | Base paper (Akdere et al.) | Method definitions, citations | — |
| `postgresql-17-US` | PostgreSQL 17 Documentation | Technical definitions, EXPLAIN output | — |
| `specification` | TPC-H Benchmark Specification | Query definitions, schema details | — |

### Search Examples

```
# Check term usage in existing thesis chapter
mcp__rag__search(query="Optimizer Baseline", collection="Thesis", document="3.Plan_Level_Fließ.md")

# Find paper definition
mcp__rag__search(query="operator-level prediction", collection="Learning-based_Query_Performance_Modeling_and_Pred")

# PostgreSQL technical details
mcp__rag__search(query="actual_total_time EXPLAIN", collection="postgresql-17-US")

# TPC-H schema
mcp__rag__search(query="LINEITEM table", collection="specification")
```

---

## Tool: `mcp__rag__list_collections`

List all indexed collections with chunk counts.

**Parameters:** None

**Example:**
```
mcp__rag__list_collections()
```

**Output:**
```
Indexed Collections:

  specification (402 chunks)
```

---

## Tool: `mcp__rag__list_documents`

List all documents in a collection with chunk counts.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `collection` | string | Yes | Collection name |

**Example:**
```
mcp__rag__list_documents(collection="specification")
```

**Output:**
```
Documents:

  specification.md (402 chunks)
```

---

## Tool: `mcp__rag__read_document`

Read continuous text from a document starting at a specific chunk index.

**Use Case:** After `search` finds a relevant chunk, use `read_document` to read more context forward.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `collection` | string | Yes | Collection name |
| `document` | string | Yes | Document name (e.g. "chunks.md") |
| `start_chunk` | int | Yes | Chunk index to start reading from |
| `num_chunks` | int | No | Number of chunks to read (1-20, default: 5) |

**Example Workflow:**
```
1. search("mindset change", neighbors=1) → finds chunk 50
2. read_document("The Outward Mindset", "chunks.md", 50, 10) → reads chunks 50-59
```

**Output:**
```
Document: chunks.md | Chunks 50-59

[continuous text, overlap-deduplicated]
```
