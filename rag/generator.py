import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()


def generate_answer(context, query):

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY from the context below.

    If answer is not present,
    say "Not found in documents".

    Context:
    {context}

    Question:
    {query}
    """

    return llm.invoke(prompt).content