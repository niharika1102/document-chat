from app.ingestion.embedder import generate_query_embedding
from app.retrieval.vector_store import retrieve_chunks
from app.generation.generator import generate_answer

query = "What is normalization?"

# 1. Convert the question into an embedding
query_embedding = generate_query_embedding(query)

# 2. Retrieve relevant chunks from ChromaDB
results = retrieve_chunks(
    query_embedding=query_embedding,
    top_k=3
)

# 3. Extract the retrieved documents
documents = results["documents"][0]

# 4. Combine the documents into one context
context = "\n\n".join(documents)

# 5. Generate the final answer
answer = generate_answer(
    question=query,
    context=context
)

print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)