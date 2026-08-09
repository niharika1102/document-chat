def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Generate chunks from a text
    
    Args:
        text (str): Takes the text as input
        chunk_size (int, optional): The size of each chunk. Defaults to 500.
        overlap (int, optional): The number of overlapping words between chunks. Defaults to 50.

    Returns:
        list[str]: a list of text chunks
    """
    
    words = text.split()
    chunks = []
    start = 0
    
    while start < len(words):
        end = start + chunk_size
        
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        
        start += chunk_size - overlap
        
    return chunks