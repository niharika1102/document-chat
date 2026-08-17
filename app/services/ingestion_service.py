from app.ingestion.loader import extract_text_from_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import generate_embeddings
from app.retrieval.vector_store import add_chunks

def ingest_document(file_path: str) -> int:
    # 1. Extract text from pdf
    pages = extract_text_from_pdf(file_path)
    
    #2. Split text into chunks
    chunks = chunk_text(pages)
    
    #3. Create embeddings
    embeddings = generate_embeddings(chunks)
    
    #4. Store embeddings to chroma
    add_chunks(chunks=chunks, embeddings=embeddings)
    
    return len(chunks)