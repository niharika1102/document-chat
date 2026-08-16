from app.ingestion.loader import extract_text_from_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import generate_embeddings
from app.retrieval.vector_store import add_chunks


pdf_path = "data/docs/DBMS-BOSS-SHEET.pdf"


# 1. Extract
pages = extract_text_from_pdf(pdf_path)

print("Pages:", len(pages))


# 2. Chunk
chunks = chunk_text(
    pages,
    chunk_size=500,
    overlap=50
)

print("Chunks:", len(chunks))


# 3. Embed
embeddings = generate_embeddings(chunks)

print("Embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))


# 4. Store
add_chunks(chunks, embeddings)

print("Successfully stored chunks in ChromaDB.")