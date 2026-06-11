"""
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from rag.config import VECTOR_DB_PATH
#-------- for render---------
os.makedirs("vectorstore", exist_ok=True)
#----------------------------
# FIXED PATH (important)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data")
DB_PATH = VECTOR_DB_PATH

documents = []

for file in os.listdir(DATA_PATH):
    path = os.path.join(DATA_PATH, file)

    if file.endswith(".pdf"):
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    elif file.endswith(".txt"):
        loader = TextLoader(path, encoding="utf-8")
        documents.extend(loader.load())

print(f"Loaded docs: {len(documents)}")

# Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)
print(f"Chunks created: {len(chunks)}")

# Embeddings (FIXED)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

#db.persist()

print(" Ingestion completed successfully")

"""
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# import shared path
from rag.config import VECTOR_DB_PATH


def run_ingestion():

    DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data")

    documents = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            documents.extend(loader.load())

    print(f"Loaded docs: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    print(f"Chunks created: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    print(" Ingestion completed successfully")