from app.ingestion.chunker import chunk_text
from app.ingestion.loader import extract_text_from_pdf

file_path = "data/docs/DBMS-BOSS-SHEET.pdf"

text = extract_text_from_pdf(file_path)

chunk = chunk_text(text, chunk_size = 500, overlap = 50)

for i, chunk in enumerate(chunk):
    print(f"Chunk {i + 1}: {chunk} \n")