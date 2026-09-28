# Hybrid Search Retriever (BM25 + Dense) with LangChain

A hands-on RAG retrieval project that combines **keyword search (BM25)** and **semantic search (dense embeddings)** into a single **hybrid retriever**, tested on a real-world document: Tesla's FY2023 Form 10-K annual report.

## Overview

Pure semantic search can miss exact terms (names, codes, figures), while pure keyword search cannot understand paraphrased queries. This project runs both retrievers on the same chunks and merges their results with LangChain's `EnsembleRetriever`, so you can compare **BM25 only**, **Dense only**, and **Hybrid** results side by side for any query.

## How It Works

```
PDF (Tesla 10-K)
      |
      v
Load selected pages  ->  Clean whitespace  ->  Chunk (Recursive splitter)
                                                   |
                          +------------------------+------------------------+
                          v                                                 v
                 BM25Retriever (keyword)                     Chroma + MiniLM embeddings
                          |                                     (dense / semantic)
                          +------------------------+------------------------+
                                                   v
                                          EnsembleRetriever
                                       (weighted rank fusion)
                                                   |
                                                   v
                                             Ranked results
```

1. **Load**: `PyPDFLoader` reads the PDF. Only pages with index 4 to 28 (Item 1 Business and Item 1A Risk Factors) are used, because the later financial-statement pages are table-heavy and plain text extraction breaks tables.
2. **Clean**: PDF text extraction leaves extra whitespace (justified text), so multiple spaces are collapsed with a regex before chunking.
3. **Chunk**: `RecursiveCharacterTextSplitter` with `chunk_size=500` and `chunk_overlap=50`.
4. **Dense retriever**: `all-MiniLM-L6-v2` embeddings stored in a Chroma vector store.
5. **BM25 retriever**: `BM25Retriever` built on the same chunks.
6. **Hybrid retriever**: `EnsembleRetriever` combines both using configurable weights.

## Tech Stack

- Python 3.10+
- LangChain (`langchain`, `langchain-community`, `langchain-classic`, `langchain-text-splitters`, `langchain-huggingface`)
- `rank_bm25` for the BM25 algorithm
- ChromaDB as the vector store
- `sentence-transformers` (`all-MiniLM-L6-v2`) for embeddings
- `pypdf` for PDF loading

## Setup

```bash
# 1. Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt
```

### Get the PDF

Download Tesla's FY2023 Form 10-K and save it in the project folder as `tesla_10k.pdf`:

https://ir.tesla.com/_flysystem/s3/sec/000162828024002390/tsla-20231231-gen.pdf

## Usage

```bash
python main.py
```

Enter a query when prompted. The script prints the top results from:

1. BM25 only
2. Dense only
3. Hybrid (Ensemble)



## Configuration

| Setting | Where | Default | Notes |
|---|---|---|---|
| Page range | `pages[4:29]` | Business + Risk Factors | Change if you use a different document |
| Chunk size / overlap | `RecursiveCharacterTextSplitter` | 500 / 50 | Tune per document type |
| Top-k per retriever | `search_kwargs={"k": 5}` and `bm25_retriever.k` | 5 | Larger k means better recall, more noise |
| Fusion weights | `EnsembleRetriever(weights=[bm25, dense])` | `[0.5, 0.5]` | Weights should sum to 1.0 |

## Suggested Test Queries

**Exact-keyword style (BM25 tends to help):**
- `Gigafactory Berlin-Brandenburg`
- `Supercharger network`
- `cybersecurity incident response plan`

**Paraphrased / semantic style (dense tends to help):**
- `What dangers does Tesla face from other car companies?`
- `How does the company make sure customer data stays safe?`
- `What could go wrong with getting raw materials for batteries?`

## Observations From Testing

- With more weight on **dense** search, paraphrased queries (for example the battery raw materials query) returned consistently relevant chunks.
- With more weight on **BM25**, keyword overlap sometimes pulled in loosely related chunks (for example, a query about competition surfaced the CEO-dependency paragraph).
- Lower-ranked results (around 4th to 6th) often drifted off-topic, which shows that a single fixed weight setting does not suit every query type.
- Risk-factor headings in a 10-K appear twice in the source PDF (bold heading followed by the same sentence in the paragraph), so some chunks contain a repeated sentence. This comes from the document itself, not from a chunking bug.

## Known Limitations

- Table-heavy pages (financial statements) are intentionally excluded, since table parsing is not implemented here.
- Weights are set manually; there is no query classification or reranking step yet.
- BM25 uses simple whitespace tokenization with no stemming or stopword removal.

## Possible Next Steps

- Reciprocal Rank Fusion implemented from scratch
- Query classification and query rewriting
- Reranking with a cross-encoder
- Table-aware PDF ingestion

## License

For learning and portfolio purposes. The Tesla 10-K is a public SEC filing.