import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def generate_answer(context, query):
    groq_key = os.getenv("GROQ_API_KEY")

    print("GROQ KEY EXISTS:", bool(groq_key))
    print("GROQ KEY START:", groq_key[:4] if groq_key else "NONE")
    print("GROQ KEY LENGTH:", len(groq_key) if groq_key else 0)

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=groq_key
    )

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY from the context below.
    If answer not present, say "Not found in documents".

    Context:
    {context}

    Question:
    {query}
    """

    return llm.invoke(prompt).content