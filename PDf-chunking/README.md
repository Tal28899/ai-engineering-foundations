# RAG Chunking & Retrieval Experiment

A Retrieval-Augmented Generation (RAG) project that explores how different **text chunking strategies** affect semantic retrieval and LLM-generated answers.

The project implements three chunking approaches — **fixed-size, sentence-based, and recursive chunking** — stores the resulting chunks in **ChromaDB**, retrieves relevant chunks for a user query, and uses a Groq-hosted LLM to generate an answer grounded in the retrieved context.

---

## Overview

A RAG system does not need to send an entire document to an LLM.

Instead, it:

```text
                 DOCUMENT
                     │
                     ▼
              TEXT EXTRACTION
                     │
                     ▼
                CHUNKING
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Fixed       Sentence     Recursive
     Chunking     Chunking      Chunking
        │            │            │
        └────────────┼────────────┘
                     ▼
               VECTOR STORAGE
                  ChromaDB
                     │
                     ▼
                USER QUERY
                     │
                     ▼
              SEMANTIC SEARCH
                     │
                     ▼
             RELEVANT CHUNKS
                     │
                     ▼
                  LLM
                     │
                     ▼
              GROUNDED ANSWER
```

The main goal of this project is not simply to build a chatbot, but to understand an important RAG engineering question:

> **How does the way we chunk documents affect the quality of retrieved context?**

---

## Key Features

- PDF text extraction
- Multiple chunking strategies
- Fixed-size chunking
- Sentence-based chunking
- Recursive chunking
- 🔎 Semantic retrieval using ChromaDB
- 🧠 Vector database persistence
- LLM-powered answer generation
- 🔐 Environment-variable based API key management
- 🔄 API retry handling with exponential backoff
- ⚠️ Handling for authentication, rate-limit, timeout, connection, and API errors
- 🧩 Modular project structure
-  Designed for comparing different chunking strategies

---


## Error Handling

The LLM integration includes handling for several API failure scenarios:

- Invalid or missing API key
- Rate limiting
- API connection failures
- Request timeouts
- API status errors
- Unexpected exceptions

Rate-limit handling also supports retrying requests using exponential backoff when an explicit retry interval is not provided.

Example retry behavior:

```text
Attempt 1
   ↓
wait
   ↓
Attempt 2
   ↓
longer wait
   ↓
Attempt 3
```

This makes the application more resilient to temporary API failures.

---

## Project Structure

```text
rag-project/
│
├── main.py
├── chunking.py
├── embeddings.py
├── input.py
├── llm.py
├── text_extracter.py
│
├── .env
├── .gitignore
├── requirements.txt
│
└── my_chunks_vector/
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Coordinates the complete RAG pipeline |
| `chunking.py` | Implements the three chunking strategies |
| `embeddings.py` | Handles ChromaDB collections and semantic retrieval |
| `input.py` | Validates user queries |
| `llm.py` | Handles LLM API calls and error handling |
| `text_extracter.py` | Extracts text from the source document |
| `.env` | Stores local environment variables |
| `requirements.txt` | Project dependencies |
| `my_chunks_vector/` | Persistent ChromaDB storage |

---

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/Tal28899/ai-engineering-foundations>
cd <PDf-chunking>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your real API key to GitHub.

---

## Configuration

Update the document path used by the application:

```python
data = extract_text("path/to/your/document.pdf")
```
Using a relative project path is recommended instead of a machine-specific absolute path.

---

## Running the Project

After activating your virtual environment and configuring your API key:

```bash
python main.py
```

The application will:

1. Load the source document
2. Extract its text
3. Generate chunks using the implemented strategies
4. Store the chunks in ChromaDB
5. Accept a user query
6. Retrieve relevant chunks
7. Send the retrieved context to the LLM
8. Generate the final response

---

## Why Multiple Chunking Strategies?

Chunking is one of the most important design decisions in a RAG system.

If chunks are too small:

```text
Too little context
       ↓
Poor retrieval context
       ↓
Incomplete answers
```

If chunks are too large:

```text
Too much irrelevant information
       ↓
Noisy context
       ↓
Less precise retrieval
```

The ideal chunking strategy depends on the type and structure of the data.

This project therefore treats chunking as an **engineering variable to experiment with**, rather than assuming that one strategy works for every document.

---

## What I Learned From This Project

This project focuses on understanding the components behind a basic RAG pipeline:

- Why documents need to be chunked
- How different chunking strategies affect retrieved context
- How vector databases can store and retrieve document chunks
- How semantic search connects user queries with relevant text
- How retrieved context is passed to an LLM
- Why API error handling matters in real applications
- Why retry strategies are important for unreliable network/API conditions
- How to structure a RAG application into separate modules

---
---

## Project Goal

The goal of this project is to move beyond simply calling an LLM API and understand what happens **before the LLM receives a prompt**.

The project focuses on the retrieval side of AI systems:

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retrieval
   ↓
Context
   ↓
LLM
   ↓
Answer
```

This provides a foundation for building more advanced RAG systems in the future.

---

## Tech Stack

- **Python**
- **spaCy** — sentence segmentation
- **ChromaDB** — vector storage and semantic retrieval
- **Groq API** — LLM inference
- **python-dotenv** — environment variable management

---

## Disclaimer

This project is an experimental learning implementation focused on understanding RAG fundamentals and comparing chunking approaches. It is not intended to represent a production-ready RAG architecture.

---
