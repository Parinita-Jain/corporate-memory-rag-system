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