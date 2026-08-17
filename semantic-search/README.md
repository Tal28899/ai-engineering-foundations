# Semantic Search with Sentence Transformers

A simple semantic search project that retrieves the most relevant sentences from a small dataset using **Sentence Transformers** and **cosine similarity**.

Instead of matching exact keywords, the system converts both the stored sentences and the user's query into numerical embeddings and ranks the sentences according to their semantic similarity.

## How It Works

The application follows this pipeline:

```text
User Query
    ↓
Input Validation
    ↓
Generate Query Embedding
    ↓
Generate Dataset Embeddings
    ↓
Calculate Cosine Similarity
    ↓
Sort by Similarity Score
    ↓
Return Top 3 Results
```

The project uses the `all-MiniLM-L6-v2` Sentence Transformer model to generate embeddings.

## Features

* Semantic search using sentence embeddings
* Uses `all-MiniLM-L6-v2` for text representation
* Cosine similarity for comparing embeddings
* Returns the top 3 most similar sentences
* Basic input validation
* Lightweight in-memory dataset
* Simple implementation suitable for understanding the fundamentals of retrieval

## Tech Stack

* **Python**
* **NumPy**
* **Sentence Transformers**
* **Cosine Similarity**


## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd semantic-search
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

A minimal `requirements.txt`:

```text
numpy
sentence-transformers
```


## Current Limitations

This implementation is intentionally simple and is designed to demonstrate the core concept of semantic retrieval.

* The dataset is hard-coded in the Python file.
* Dataset embeddings are regenerated every time the program runs.
* There is no vector database or persistent embedding index.
* Retrieval is performed with a linear scan over the dataset.
* There is no chunking or document ingestion pipeline.
* Results are printed directly to the terminal.
* The project does not generate an LLM response from the retrieved context.

For a small dataset, this approach is perfectly suitable for learning and experimentation. Larger retrieval systems typically introduce persistent vector indexes or vector databases to make retrieval more scalable.

## Learning Goals

This project demonstrates several fundamental concepts used in modern **RAG (Retrieval-Augmented Generation)** systems:

* Text embeddings
* Semantic similarity
* Cosine similarity
* Query encoding
* Document encoding
* Similarity-based ranking
* Top-K retrieval

It serves as a foundational step toward building more advanced retrieval pipelines.

## License

This project is intended for educational and experimentation purposes.
