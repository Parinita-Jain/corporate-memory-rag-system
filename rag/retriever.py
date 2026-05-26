from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_documents(query):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    return retriever.invoke(query)
'''
retriever.py → fetch relevant documents
generator.py → call LLM
pipeline.py → connect both
'''