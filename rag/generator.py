#from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv("GROQ_API_KEY"))
from langchain_groq import ChatGroq

def generate_answer(context, query):

   
    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
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

    #return llm.invoke(prompt)
    return llm.invoke(prompt).content