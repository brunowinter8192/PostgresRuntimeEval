---
name: RAG_MCP
description: Vector search over indexed documents
---

# RAG MCP Tools

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

1. **Provide exact section references** - Not "Section 5", but "Section 5.3.2"
2. **Flag figures/graphics** - If data is only in a figure you cannot read, IMMEDIATELY say: "The values are in Figure X, I can only read the text"
3. **Communicate uncertainty immediately** - If you cannot find a value in the text, DO NOT guess. Say: "This value is not stated in the text"
4. **No summaries as facts** - "7-114%" is WRONG if you only have "7.30% average" and "114% single example"

**Example WRONG:**
> "The paper achieved 7-114% MRE (Section 5)"

**Example RIGHT:**
> "The text states 7.30% average for 11 templates (Section 5.3.2). The 114% comes from a single example in Section 3.4. The per-template values are only in Figure 6(d), which I cannot read."

5. **State context and scope** - Distinguish between general statements and specific examples

**Example WRONG:**
> "The paper identifies the Materialize operator as the main cause for prediction errors (Section 3.4)"

**Example RIGHT:**
> "Using Template-13 as example, the paper identifies the Materialize operator as the main cause for prediction errors (Section 3.4). This is a specific example to motivate the hybrid approach, not a general statement about all templates."

**Rationale:** User is writing a thesis. Incorrect citations = scientific misconduct.

---

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
4. `read_document(collection, document, start_chunk, num_chunks=5)` → read more context

**Decision Guide:**

| User Intent | Tool |
|-------------|------|
| User writes "rag" + question | Use RAG tools |
| "What is X?" / "Explain X" | `search` (semantic) |
| "Where is X?" / "Definition of X" | `search_keyword` (BM25) |
| Technical terms, column names | `search_keyword` |
| Conceptual understanding | `search` |
| Conceptual question with different terminology | HyDE Pattern (see below) |
| "Read more of this" / need full section | `read_document` |

**Drill-Down Pattern:**
```
1. search("supplier relationships TPC-H")  → finds Chunk: 42
2. read_document(start_chunk=40, num_chunks=10) → read full section
3. search_keyword("l_suppkey")             → find exact definition
```

**Workflow-Hierarchie:**

`read_document` ist ein Follow-up Tool - immer nach search/search_keyword verwenden.

```
search / search_keyword
         ↓
    Chunk klar? → fertig
         ↓ nein
    read_document(start_chunk aus Result)
```

**Faustregel:** Wenn der Chunk-Inhalt nicht vollständig klar ist → `read_document` für Context.

**Komplexe Queries:** Bei komplexen User-Fragen zuerst `search` mit `neighbors=1-2`, dann bei Bedarf `read_document`.

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

- User asks about content in indexed documents
- User needs specific information from the knowledge base
- Answering questions that require document context

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

## Indexed Collections

Use `mcp__rag__list_collections` to see available collections.

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

**Examples:**
```
# Nach search: Chunk 42 gefunden, mehr Context holen
mcp__rag__read_document(collection="specification", document="specification.md", start_chunk=40, num_chunks=10)

# Nach search_keyword: Definition gefunden, Umgebung lesen
mcp__rag__read_document(collection="Thesis", document="3.Plan_Level_Fließ.md", start_chunk=15, num_chunks=5)

# Default: 5 chunks ab Position 100
mcp__rag__read_document(collection="postgresql-17-US", document="postgresql-17-US.md", start_chunk=100)
```
