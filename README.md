# Corporate Memory — Production-Grade RAG System

An enterprise-grade Retrieval-Augmented Generation (RAG) system designed to enable semantic search and grounded AI responses across internal corporate documents using LangChain, ChromaDB, Ollama, and Llama 3.

## Business Problem

Organizations store critical knowledge across PDFs, reports, policies, and internal documents.

Traditional keyword search systems fail to provide contextual understanding.

This project implements a production-style RAG architecture enabling semantic retrieval and AI-powered question answering with source attribution to reduce hallucinations.

## Features

- Multi-document ingestion
- PDF and text processing
- Semantic chunking
- Vector database storage
- Retrieval-Augmented Generation (RAG)
- Source attribution
- FastAPI serving
- Local LLM execution via Ollama
- Modular production architecture

## Tech Stack

- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Ollama
- Llama 3
- FastAPI
- Uvicorn

## Architecture

User Query
→ Semantic Retrieval
→ ChromaDB Vector Search
→ Context Injection
→ Llama 3 Generation
→ Grounded AI Response

## Installation

```bash
git clone <repo_url>

cd Corporate_memory

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

```bash
git clone https://github.com/parinitajain/corporate-memory-rag-system

cd Corporate_memory

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run Ollama

```bash
ollama run llama3
```

Keep this terminal open while running the FastAPI server.

---

## Run Document Ingestion

```bash
python ingestion/ingest.py
```

This will:
- load documents,
- create embeddings,
- store vectors in ChromaDB.

---

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Example Query

```json
{
  "query": "What does the Cab Booking System document discuss?"
}
```

---

## Example Response

```json
{
  "answer": "The document discusses data analysis of cab booking patterns...",
  "sources": [
    "Data Analysis of Cab Booking System.pdf"
  ]
}
```

---

## Note

The vector database is generated dynamically during ingestion and is excluded from version control.

## Future Improvements

- Docker deployment
- Kubernetes orchestration
- Hybrid search
- OCR support
- Authentication
- AWS deployment
- Conversational memory


