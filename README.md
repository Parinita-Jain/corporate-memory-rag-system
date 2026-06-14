# Corporate Memory RAG System

A production-style Retrieval-Augmented Generation (RAG) system that enables question answering over corporate documents using FastAPI, Groq Llama 3.1, and document retrieval techniques.

The project is maintained in two versions:

| Branch         | Purpose                                                    |
| -------------- | ---------------------------------------------------------- |
| `main`         | Lightweight cloud deployment optimized for Render Free     |
| `advanced-rag` | Full semantic RAG using ChromaDB and Sentence Transformers |

---

# Live Demo

## Live Deployment

https://corporate-memory-rag-system.onrender.com

## Swagger Documentation

https://corporate-memory-rag-system.onrender.com/docs

## Ask Endpoint

https://corporate-memory-rag-system.onrender.com/docs#/default/ask_ask_post

---

# Business Problem

Organizations store critical information across:

* Policies
* Reports
* Internal documentation
* Training material
* Knowledge bases

Traditional keyword search often fails to retrieve the most relevant information.

This project provides a Retrieval-Augmented Generation (RAG) workflow that:

1. Retrieves relevant document content
2. Builds contextual information
3. Uses a Large Language Model to generate answers
4. Returns source references

This reduces hallucinations and improves answer reliability.

---

# Branch Strategy

## Main Branch (Render Deployment)

Optimized for Render Free Tier (512 MB RAM).

### Features

* FastAPI API
* PDF and TXT document support
* Lightweight retrieval
* Groq Llama 3.1 generation
* Source attribution
* Cloud deployment

### Why a Lightweight Version?

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

The lightweight version avoids those components to remain deployable on free infrastructure.

---

## Advanced-RAG Branch

Full semantic Retrieval-Augmented Generation implementation.

### Features

* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* Vector Database
* Semantic Search
* Persistent Vector Store
* Groq Llama 3.1

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
Groq LLM
    ↓
Answer + Sources
```

Recommended for:

* Local development
* Demonstrations
* Interviews
* Production environments with sufficient memory

---

# Technology Stack

## Deployed Version (main)

* Python
* FastAPI
* Pydantic
* PyPDF
* Groq
* Llama 3.1
* Render

## Advanced Version (advanced-rag)

* Python
* FastAPI
* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* Groq
* Llama 3.1

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

# Project Structure

```text
Corporate_memory/

├── .github/
│   └── workflows/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── data/
│   ├── Data Analysis of Cab Booking Systems.pdf
│   ├── Modulewise Exam Structure - 2025-26 v2.pdf
│   └── *.txt
│
├── ingestion/
│   ├── __init__.py
│   └── ingest.py
│
├── rag/
│   ├── __init__.py
│   ├── config.py
│   ├── generator.py
│   ├── pipeline.py
│   └── retriever.py
│
├── screenshots/
│   ├── RenderDeployment.png
│   ├── RenderOutput.png
│   └── SuccessfullyDeployedOnRender.png
│
├── tests/
│   ├── __init__.py
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

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

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

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

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

Endpoint:

```http
GET /health
```

Response:

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

Create a `.env` file locally:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Screenshots

Include screenshots inside:

```text
screenshots/
```

Examples:

* Render deployment success
* Swagger UI
* API response example
* Successful Render deployment

---

# Future Improvements

* Hybrid Search
* Reranking
* Conversational Memory
* Authentication
* OCR Support
* Docker Deployment
* Kubernetes Deployment
* AWS Deployment
* Advanced Semantic Search
* External Vector Databases

---

# Author

**Parinita Jain**

Applied AI Engineer | Machine Learning Engineer | Data Science Trainer

GitHub:
https://github.com/Parinita-Jain/corporate-memory-rag-system
