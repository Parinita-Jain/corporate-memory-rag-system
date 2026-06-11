#from rag.retriever import get_documents
#from rag.generator import generate_answer
"""
def ask_question(query):

    docs = get_documents(query)

    if not docs:
        return {
            "answer": "No relevant documents found",
            "sources": []
        }

    context = "\n\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, query)

    #sources = [doc.metadata.get("source", "unknown") for doc in docs]
    sources = list(set([doc.metadata.get("source", "unknown") for doc in docs]))
    for doc in docs:
        print("\n--- DOC ---")
        print(doc.page_content[:200])
        print("SOURCE:", doc.metadata.get("source"))
    return {
        "answer": answer,
        "sources": sources
    }
"""
"""
def ask_question(query):

    print("STEP 1")

    docs = get_documents(query)

    print("STEP 2")

    context = "\n\n".join([doc.page_content for doc in docs])

    print("STEP 3")

    answer = generate_answer(context, query)

    print("STEP 4")

    return {
        "answer": answer,
        "sources": list(set([doc.metadata.get("source", "unknown") for doc in docs]))
    }
"""
"""
from rag.retriever import get_documents
from rag.generator import generate_answer


def ask_question(query):
    print("STEP 1: Starting retrieval")

    docs = get_documents(query)

    print("STEP 2: Documents retrieved")

    if not docs:
        return {
            "answer": "No relevant documents found",
            "sources": []
        }

    context = "\n\n".join([doc.page_content[:1500] for doc in docs])

    print("STEP 3: Context prepared")

    answer = generate_answer(context, query)

    print("STEP 4: Answer generated")

    return {
        "answer": answer,
        "sources": list(set([doc.metadata.get("source", "unknown") for doc in docs]))
    }
"""
from rag.retriever import get_documents
from rag.generator import generate_answer


def ask_question(query):
    print("STEP 1: Starting retrieval")

    docs = get_documents(query)

    print("STEP 2: Documents retrieved")

    if not docs:
        return {
            "answer": "No relevant documents found",
            "sources": []
        }

    context = "\n\n".join([doc.page_content for doc in docs])

    print("STEP 3: Context prepared")

    answer = generate_answer(context, query)

    print("STEP 4: Answer generated")

    return {
        "answer": answer,
        "sources": list(set([doc.metadata.get("source", "unknown") for doc in docs]))
    }