from rag.retriever import get_documents
from rag.generator import generate_answer


def ask_question(query):

    docs = get_documents(query)

    if not docs:

        return {
            "answer": "No documents found",
            "sources": []
        }

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    answer = generate_answer(
        context,
        query
    )

    sources = list(
        set(
            [
                doc.metadata.get(
                    "source",
                    "unknown"
                )
                for doc in docs
            ]
        )
    )

    return {
        "answer": answer,
        "sources": sources
    }