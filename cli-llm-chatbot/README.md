# CLI LLM Chatbot

A command-line chatbot built using the Groq LLM API, with conversation history and error handling.

## What this demonstrates

- Integrating with an LLM provider's API (Groq — OpenAI-compatible syntax)
- Managing multi-turn conversation history/context across requests
- Secure API key management using environment variables
- Handling real-world API failure modes: rate limits and connection errors

## Tech stack

Python · Groq API · `python-dotenv`

## Setup

```bash
cd cli-llm-chatbot
pip install -r requirements.txt
cp .env.example .env   # then add your own Groq API key
python llm.py
```

## Example usage

```
You: What's a good way to start learning Python?
Bot: Start with the basics — variables, control flow, and functions — then build small projects...
You: exit
```

## Notes

Groq was chosen specifically for its OpenAI-compatible API syntax, since that same interaction pattern carries over directly into LangChain and other LLM tooling used in RAG and agentic AI development.