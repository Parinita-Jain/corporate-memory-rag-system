from rag.pipeline import ask_question

query = "What is this document about?"

result = ask_question(query)

print("\nANSWER:\n", result["answer"])
print("\nSOURCES:\n", result["sources"])