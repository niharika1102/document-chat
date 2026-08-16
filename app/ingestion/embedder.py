from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks: list[dict]) -> list[list[float]]:
    """Generate embeddings for a list of text chunks
    
    Args:
        chunks (list[dict]): Takes a list of text chunks as input
    
    Returns:
        list[list[float]]: a list of embeddings for each chunk
    """
    
    texts = [
        chunk["text"]
        for chunk in chunks
    ]
    
    embeddings = model.encode(texts)
    
    return embeddings.tolist()