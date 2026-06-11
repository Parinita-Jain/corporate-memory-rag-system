"""
from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
import os
import traceback

from rag.pipeline import ask_question
from ingestion.ingest import run_ingestion
from rag.config import VECTOR_DB_PATH

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Server starting...")

    try:
        print("Skipping ingestion on Render startup")
    except Exception as e:
        print("Startup Error:")
        print(traceback.format_exc())

    yield

    print("Server shutting down...")

app = FastAPI(lifespan=lifespan)


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Corporate Memory RAG API is running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ask")
async def ask(q: Query):
    try:
        print(f"Question Received: {q.question}")

        result = ask_question(q.question)

        print("Response Generated Successfully")

        return result

    except Exception as e:
        print("Error in /ask endpoint:")
        print(traceback.format_exc())

        return {
            "error": str(e),
            "type": type(e).__name__
        }
"""
from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
import traceback

from rag.pipeline import ask_question


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server starting...")
    print("Skipping ingestion on Render startup")

    yield

    print("Server shutting down...")


app = FastAPI(lifespan=lifespan)


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Corporate Memory RAG API is running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ask")
async def ask(q: Query):
    try:
        print(f"Question Received: {q.question}")

        result = ask_question(q.question)

        print("Response Generated Successfully")

        return result

    except Exception as e:
        print("Error in /ask endpoint:")
        print(traceback.format_exc())

        return {
            "error": str(e),
            "type": type(e).__name__
        }