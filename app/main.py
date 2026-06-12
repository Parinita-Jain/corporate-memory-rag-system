from fastapi import FastAPI
from pydantic import BaseModel

from rag.pipeline import ask_question

app = FastAPI()


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Advanced RAG Running"}


@app.post("/ask")
def ask(q: Query):

    return ask_question(q.question)