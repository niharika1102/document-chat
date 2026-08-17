from app.services.rag_service import ask_question

query = "What is normalization?"

answer = ask_question(query)

print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)