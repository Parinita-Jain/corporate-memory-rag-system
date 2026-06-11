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
"""
import os
import re
from dataclasses import dataclass
from pypdf import PdfReader
from rag.config import DATA_DIR


@dataclass
class SimpleDocument:
    page_content: str
    metadata: dict


_documents_cache = None


def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


def chunk_text(text, source, chunk_size=1200, overlap=200):
    chunks = []
    text = clean_text(text)

    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(
                SimpleDocument(
                    page_content=chunk,
                    metadata={"source": source}
                )
            )

        start += chunk_size - overlap

    return chunks


def load_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""
        text += "\n"

    return text


def load_documents():
    global _documents_cache

    if _documents_cache is not None:
        return _documents_cache

    print("Loading documents from:", DATA_DIR)

    docs = []

    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)

        if filename.lower().endswith(".pdf"):
            text = load_pdf(path)
            docs.extend(chunk_text(text, filename))

        elif filename.lower().endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            docs.extend(chunk_text(text, filename))

    print("Loaded chunks:", len(docs))

    _documents_cache = docs
    return docs


def score_document(query, doc):
    query_words = set(re.findall(r"\w+", query.lower()))
    doc_words = set(re.findall(r"\w+", doc.page_content.lower()))

    if not query_words:
        return 0

    return len(query_words.intersection(doc_words))


def get_documents(query):
    docs = load_documents()

    ranked_docs = sorted(
        docs,
        key=lambda doc: score_document(query, doc),
        reverse=True
    )

    top_docs = [
        doc for doc in ranked_docs
        if score_document(query, doc) > 0
    ]

    return top_docs[:3]