from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# Load embeddings
embedding = HuggingFaceEmbeddings()

# Load vector DB
db = Chroma(persist_directory="../chroma_db", embedding_function=embedding)

# Retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# LLM (local)
llm = Ollama(model="llama3")


def ask_question(query):

    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question using only the context below.
    
    Context:
    {context}
    
    Question:
    {query}
    
    Also mention which document the answer came from.
    """

    answer = llm.invoke(prompt)

    sources = [doc.metadata.get("source", "unknown") for doc in docs]

    return {
        "answer": answer,
        "sources": sources
    }