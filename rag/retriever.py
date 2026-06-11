"""
from langchain_chroma import Chroma
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from rag.config import VECTOR_DB_PATH
def get_documents(query):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    return retriever.invoke(query)
'''
retriever.py → fetch relevant documents
generator.py → call LLM
pipeline.py → connect both
'''
"""
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from rag.config import VECTOR_DB_PATH
import os

_embeddings = None
_db = None


def get_vector_db():
    global _embeddings, _db

    print("CURRENT DIRECTORY:", os.getcwd())
    print("VECTOR DB PATH:", VECTOR_DB_PATH)
    print("VECTORSTORE EXISTS:", os.path.exists(VECTOR_DB_PATH))

    if _embeddings is None:
        print("Loading embedding model...")
        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Embedding model loaded")

    if _db is None:
        print("Loading Chroma DB...")
        _db = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=_embeddings
        )
        print("Chroma DB loaded")

    return _db


def get_documents(query):
    db = get_vector_db()
    retriever = db.as_retriever(search_kwargs={"k": 2})
    return retriever.invoke(query)