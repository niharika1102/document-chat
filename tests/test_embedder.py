from app.ingestion.embedder import generate_embeddings

chunks = [
    "Normalization reduces data redundancy in databases.",
    "Normalization organizes tables and improves data integrity.",
    "TCP is a transport layer protocol."
]

embeddings = generate_embeddings(chunks)

print("Number of embeddings generated: ", len(embeddings))
print("Dimension of each embedding: ", len(embeddings[0]))
print("First embedding: ", embeddings[0])