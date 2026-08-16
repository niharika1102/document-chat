from app.ingestion.embedder import generate_query_embedding
from app.retrieval.vector_store import retrieve_chunks

query = "What is normalization?"

# 1. Convert the question into an embedding
query_embedding = generate_query_embedding(query)

# 2. Search ChromaDB
results = retrieve_chunks(
    query_embedding=query_embedding,
    top_k=3
)

print("\nQuestion:")
print(query)

print("\nRetrieved chunks:")

for i, document in enumerate(results["documents"][0]):
    metadata = results["metadatas"][0][i]

    print(f"\n--- Result {i + 1} ---")
    print("Source:", metadata["source"])
    print("Page:", metadata["page"])
    print("\nText:")
    print(document)