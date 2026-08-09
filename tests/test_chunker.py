from app.ingestion.chunker import chunk_text
from app.ingestion.loader import extract_text_from_pdf

file_path = "data/docs/DBMS-BOSS-SHEET.pdf"

pages = extract_text_from_pdf(file_path)

chunk = chunk_text(pages, chunk_size = 500, overlap = 50)

print("Total chunks: ", len(chunk))


for i, chunk in enumerate(chunk[:4]):
    print(f"\n--- Chunk {i + 1} ---")
    print("Source:", chunk["metadata"]["source"])
    print("Page:", chunk["metadata"]["page"])
    print("Text:", chunk["text"])