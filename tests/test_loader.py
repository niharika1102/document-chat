from app.ingestion.loader import extract_text_from_pdf

pdf_path = "data/docs/DBMS-BOSS-SHEET.pdf"

page = extract_text_from_pdf(pdf_path)

print(page)