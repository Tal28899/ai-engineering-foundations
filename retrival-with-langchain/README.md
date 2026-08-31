# PDF Q&A Bot (LangChain Edition)

A command-line RAG (Retrieval-Augmented Generation) app that answers questions about a PDF using only the content of that document — now rebuilt with LangChain and smarter persistence.

## How It Works

1. **Load** – Reads the PDF via `PyPDFLoader`.
2. **Split** – Breaks the document into overlapping chunks with `RecursiveCharacterTextSplitter`.
3. **Embed & Store** – Converts chunks into embeddings using `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`) and stores them in a local `Chroma` vector database — one dedicated database folder per PDF (e.g. `chroma_db_resume`, `chroma_db_tesla_10k`), so no PDF's data ever overwrites another's.
4. **Reuse** – If a PDF's database already exists on disk, it's loaded directly — no re-processing needed.
5. **Retrieve** – Fetches the top matching chunks from the vector store for each question.
6. **Answer** – Passes the retrieved context to a Groq-hosted LLM, which answers strictly from that context — and says "I don't know" if the answer isn't found.

## Tech Stack

- LangChain (community, text-splitters, huggingface, chroma, groq)
- ChromaDB (local, per-document vector stores)
- HuggingFace sentence-transformers (embeddings)
- Groq API (LLM inference)

## Setup

1. Install dependencies:
   ```bash
   pip install langchain-community langchain-text-splitters langchain-huggingface langchain-chroma langchain-groq python-dotenv pypdf
   ```
2. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```

## Usage

```bash
python main.py
```

Enter the path to your PDF when prompted, then ask questions. Type `quit` to exit.

## Known Limitation

Retrieval here is semantic-only (dense embeddings). Dense search can miss answers that depend on exact keyword matches — common in domain-heavy documents like financial filings. This gap is what motivated moving on to hybrid (keyword + semantic) search in the next stage of this project.

## Notes

Rebuild of an earlier raw-Python PDF chatbot, now using LangChain's abstractions and a per-PDF persistence structure so multiple documents can be indexed without overwriting each other.