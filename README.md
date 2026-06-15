# Corporate Memory RAG System

A production-style Retrieval-Augmented Generation (RAG) system that enables question answering over corporate documents using FastAPI, Groq Llama 3.1, and document retrieval techniques.

The project is maintained in two versions:

| Branch         | Purpose                                                    |
| -------------- | ---------------------------------------------------------- |
| `main`         | Lightweight cloud deployment optimized for Render Free     |
| `advanced-rag` | Full semantic RAG using ChromaDB and Sentence Transformers |

The live demo is running from the `main` branch.

---

# Live Demo

## Live Deployment

https://corporate-memory-rag-system.onrender.com

## Swagger Documentation

https://corporate-memory-rag-system.onrender.com/docs

---

## Note

The live Render deployment uses the lightweight `main` branch.

For full semantic retrieval using ChromaDB, Sentence Transformers, and vector embeddings, use the `advanced-rag` branch locally.

---

# Business Problem

Organizations store critical information across:

* Policies
* Reports
* Internal documentation
* Training material
* Knowledge bases

Traditional keyword search systems often fail to retrieve the most relevant information and frequently lack contextual understanding.

This project implements a Retrieval-Augmented Generation (RAG) workflow that:

1. Retrieves relevant document content
2. Builds contextual information
3. Uses a Large Language Model to generate grounded answers
4. Returns source references

This reduces hallucinations and improves answer reliability.

---

# Retrieval Modes

This project provides two retrieval modes through separate Git branches.

## main — Lightweight Cloud Deployment

The `main` branch is deployed on Render Free.

### Technologies

* FastAPI
* PyPDF
* Groq Llama 3.1
* Pydantic
* Python

### Features

* PDF and TXT document support
* Keyword-based retrieval
* Source attribution
* FastAPI REST API
* Cloud deployment on Render

### Workflow

```text
User Question
       ↓
Keyword Retrieval
       ↓
Relevant Document Chunks
       ↓
Groq Llama 3.1
       ↓
Answer + Sources
```

### Why This Version Exists

Render Free instances provide:

```text
512 MB RAM
0.1 CPU
```

Running:

* ChromaDB
* Sentence Transformers
* Embedding generation

can exceed memory limits.

This version avoids memory-intensive components while preserving the same RAG workflow and API interface.

---

## advanced-rag — Full Semantic RAG

The `advanced-rag` branch contains the complete semantic Retrieval-Augmented Generation implementation.

### Technologies

* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* Groq Llama 3.1
* FastAPI

### Features

* Semantic chunking
* Vector embeddings
* Persistent vector store
* ChromaDB
* Semantic similarity search
* Source attribution

### Workflow

```text
Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Semantic Retrieval
      ↓
Groq Llama 3.1
      ↓
Answer + Sources
```

### Run Full Semantic RAG Locally

```bash
git checkout advanced-rag

python -m venv venv_rag

venv_rag\Scripts\activate

pip install -r requirements.txt

python -m ingestion.ingest

uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

The command:

```bash
python -m ingestion.ingest
```

creates the local `vectorstore/` directory used by ChromaDB.

The generated vector database is intentionally excluded from GitHub through `.gitignore`.

---

# Architecture

```text
User Question
       │
       ▼
Document Retrieval
       │
       ▼
Context Construction
       │
       ▼
Groq Llama 3.1
       │
       ▼
Grounded Answer
       │
       ▼
Source Attribution
```

---

# Technology Stack

## Deployed Version (`main`)

* Python
* FastAPI
* Pydantic
* PyPDF
* Groq
* Llama 3.1
* Render

## Semantic Version (`advanced-rag`)

* Python
* FastAPI
* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* Groq
* Llama 3.1

---

# Project Structure

```text
Corporate_memory/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   └── main.py
│
├── data/
│   ├── *.pdf
│   └── *.txt
│
├── ingestion/
│   └── ingest.py
│
├── rag/
│   ├── config.py
│   ├── generator.py
│   ├── pipeline.py
│   └── retriever.py
│
├── screenshots/
│
├── tests/
│   └── test_rag.py
│
├── requirements.txt
├── render.yaml
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Parinita-Jain/corporate-memory-rag-system.git

cd corporate-memory-rag-system
```

The repository contains two branches:

| Branch | Purpose |
|----------|----------|
| `main` | Lightweight Render deployment |
| `advanced-rag` | Full semantic RAG with ChromaDB |

By default, Git clones the `main` branch.

To use the deployed lightweight version:

```bash
git checkout main
```

To use the full semantic RAG version:

```bash
git checkout advanced-rag
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```
---

# Run Locally

## Lightweight Version (main)

```bash
git checkout main

uvicorn app.main:app --reload
```

## Full Semantic RAG (advanced-rag)

```bash
git checkout advanced-rag

python -m ingestion.ingest

uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Usage

## Endpoint

```http
POST /ask
```

### Request

```json
{
  "question": "What does the Cab Booking System document discuss?"
}
```

### Response

```json
{
  "answer": "The document discusses data analysis of cab booking patterns...",
  "sources": [
    "Data Analysis of Cab Booking Systems.pdf"
  ]
}
```

---

# Health Check

## Endpoint

```http
GET /health
```

### Response

```json
{
  "status": "healthy"
}
```

---

# Deployment (Render)

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Environment Variable

```env
GROQ_API_KEY=your_groq_api_key
```

---

# CI/CD

GitHub Actions automatically runs on every push and pull request to the `main` branch.

The workflow:

* Checks out the repository
* Sets up Python 3.11
* Installs dependencies
* Performs syntax validation
* Runs automated tests

Workflow file:

```text
.github/workflows/ci.yml
```

---

# Testing

Run tests locally:

```bash
pytest -q
```

Current tests verify:

* Home endpoint (`/`)
* Health endpoint (`/health`)
* API startup validation

---

# Engineering Tradeoff

The original implementation used:

* ChromaDB
* Sentence Transformers
* Local embeddings

During deployment testing on Render Free (512 MB RAM), the service exceeded available memory and experienced container restarts.

To ensure reliable cloud deployment, the production (`main`) branch was redesigned to use lightweight retrieval while preserving the same API contract and RAG workflow.

The full semantic implementation remains available in the `advanced-rag` branch for local execution and demonstration purposes.

---

# Future Improvements

* Hybrid Search
* Retrieval Reranking
* OCR Support
* Conversational Memory
* Authentication & Authorization
* Docker Deployment
* Kubernetes Deployment
* AWS Deployment
* Managed Vector Databases
* Production Monitoring

---

# Author

**Parinita Jain**

Applied AI Engineer | Machine Learning Engineer | Data Science Trainer

GitHub:
https://github.com/Parinita-Jain/corporate-memory-rag-system

