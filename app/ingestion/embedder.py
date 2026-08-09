from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    """Generate embeddings for a list of text chunks
    
    Args:
        chunks (list[str]): Takes a list of text chunks as input
    
    Returns:
        list[list[float]]: a list of embeddings for each chunk
    """
    
    embeddings = model.encode(chunks)
    
    return embeddings.tolist()