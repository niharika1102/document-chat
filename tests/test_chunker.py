from app.ingestion.chunker import chunk_text

text = """
Python is a high-level programming language.
It is widely used for web development, automation,
data analysis, artificial intelligence, and machine learning.
FastAPI is a modern web framework for building APIs with Python.
"""

chunk = chunk_text(text, chunk_size=10, overlap=2)

for i, chunk in enumerate(chunk):
    print(f"Chunk {i + 1}: {chunk}")