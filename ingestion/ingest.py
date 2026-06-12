from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from rag.config import DATA_DIR, VECTOR_DB_PATH


def load_documents():
    """Load all supported documents."""

    documents = []

    data_path = Path(DATA_DIR)

    # PDFs
    for pdf_file in data_path.glob("*.pdf"):

        loader = PyPDFLoader(str(pdf_file))

        documents.extend(loader.load())

    # TXT files
    for txt_file in data_path.glob("*.txt"):

        loader = TextLoader(
            str(txt_file),
            encoding="utf-8"
        )

        documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents/pages")

    return documents


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    print("Vector database created successfully")


def run_ingestion():

    documents = load_documents()

    chunks = create_chunks(documents)

    create_vector_store(chunks)

    print("Ingestion completed successfully")


if __name__ == "__main__":
    run_ingestion()