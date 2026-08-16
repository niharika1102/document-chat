import chromadb

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(name="documents")

def add_chunks(chunks: list[dict], embeddings: list[list[float]]):
    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
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