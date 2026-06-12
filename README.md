# Corporate Memory — Production-Grade RAG System

An enterprise-grade Retrieval-Augmented Generation (RAG) system designed to enable semantic search and grounded AI responses across internal corporate documents using LangChain, Groq Llama 3.1, FastAPI, and PDF-based document retrieval..

## Business Problem

Organizations store critical knowledge across PDFs, reports, policies, and internal documents.

Traditional keyword search systems fail to provide contextual understanding.

This project implements a production-style RAG architecture enabling semantic retrieval and AI-powered question answering with source attribution to reduce hallucinations.

## Features

- Multi-document PDF retrieval
- Context-aware question answering
- Source attribution
- FastAPI REST API
- Groq Llama 3.1 integration
- Modular RAG architecture
- Cloud deployment on Render

## Tech Stack

- Python
- FastAPI
- LangChain
- Groq
- Llama 3.1
- PyPDF
- Render

## Architecture

User Query
        ↓
Document Retrieval
        ↓
Context Creation
        ↓
Groq Llama 3.1
        ↓
Grounded Response
        ↓
Source Attribution

## Project Structure

Corporate_memory/
│
├── app/
├── rag/
├── data/
├── tests/
├── requirements.txt
└── README.md

## Installation

```bash
git clone https://github.com/parinitajain/corporate-memory-rag-system

cd Corporate_memory

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```
Create `.env`

```bash
touch .env
```

Add:

```text
GROQ_API_KEY=your_key
```

Run:

```bash
uvicorn app.main:app --reload
```

## Swagger UI

```text
http://127.0.0.1:8000/docs

---

6. **Live Deployment**

```markdown
## Live Deployment

https://corporate-memory-rag-system.onrender.com

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


## Future Improvements

- Docker deployment
- Kubernetes orchestration
- OCR support
- Authentication
- AWS deployment
- Conversational memory


