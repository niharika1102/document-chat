def chunk_text(pages: list[dict], chunk_size: int = 500, overlap: int = 50) -> list[dict]:
    """Generate chunks from a text
    
    Args:
        pages (list[dict]): Takes a list of page dictionaries as input
        chunk_size (int, optional): The size of each chunk. Defaults to 500.
        overlap (int, optional): The number of overlapping words between chunks. Defaults to 50.

    Returns:
        list[dict]: a list of chunk dictionaries
    """
    
    chunks = []
    
    for page in pages:
        words = page["text"].split()
        start = 0
        
        while start < len(words):
            end = start + chunk_size
            
            chunk = words[start:end]
            chunks.append({
                "text": chunk,
                "metadata": {
                    "source": page["metadata"]["source"],
                    "page": page["metadata"]["page"]
                }
            })
            
            start += chunk_size - overlap
        
    return chunks