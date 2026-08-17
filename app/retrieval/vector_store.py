import chromadb
import os

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(name="documents")

def add_chunks(chunks: list[dict], embeddings: list[list[float]]):
    ids = [
        f"{os.path.basename(chunk['metadata']['source'])}_chunk_{i}"
        for i, chunk in enumerate(chunks)
    ]
    
    documents = [
        chunk["text"]
        for chunk in chunks
    ]
    
    metadatas = [
        chunk["metadata"]
        for chunk in chunks
    ]
    
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )
    
def retrieve_chunks(query_embedding: list[float], top_k: int = 3): 
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )
    
    return results