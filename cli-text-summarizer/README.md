# CLI Text Summarizer

A command-line tool that summarizes text or `.txt` files into short bullet points using the Groq API (`openai/gpt-oss-120b`). Automatically chunks large documents that exceed the model's context window and produces a final combined summary.

## Features

- Summarize raw text or a text file, entered interactively via the terminal
- Automatic token counting with `tiktoken`
- Automatic chunking for large documents (splits text into token-limited chunks, summarizes each, then summarizes the summaries)
- Retry logic with exponential backoff for rate limits.
- Clear error messages for missing files, empty input, bad encoding, and API failures

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Orchestrates the flow: takes input, decides whether to chunk, calls the summarizer |
| `input_handler.py` | Collects and validates input (raw text or file path) |
| `Text_summarizer.py` | Calls the Groq API and handles all API-related errors/retries |
| `huge_doc_summarizer.py` | Token counting and chunking logic for large documents |

## Requirements

- Python 3.9+
- A Groq API key ([console.groq.com](https://console.groq.com))

## Installation

```bash
pip install groq tiktoken python-dotenv
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

## Usage

```bash
python main.py
```

You'll be prompted to either:
- Press `t` and paste/type text directly, or
- Press `f` and provide a path to a `.txt` file

The summary will be printed to the terminal.

## ⚠️ Note on large documents

If your input is large enough to require chunking (roughly 8,000+ tokens), summarization can take **several minutes**, since each chunk is sent to the API as a separate request. On Groq's free tier this is also where you're most likely to hit rate limits — if that happens, the tool will automatically wait and retry.

## Known Limitations

- Groq's free tier has fairly low per-minute and per-day token limits, so summarizing many large documents in a short time window may trigger rate-limit waits
- Chunking splits on token count only, not on sentence/paragraph boundaries, so a chunk may occasionally cut off mid-sentence