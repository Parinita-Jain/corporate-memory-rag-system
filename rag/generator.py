from langchain_community.llms import Ollama

def generate_answer(context, query):

    llm = Ollama(model="llama3")

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY from the context below.
    If answer not present, say "Not found in documents".

    Context:
    {context}

    Question:
    {query}
    """

    return llm.invoke(prompt)