from fastapi import FastAPI
from pydantic import BaseModel
from rag.pipeline import ask_question

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask(q: Query):
    result = ask_question(q.question)
    return result