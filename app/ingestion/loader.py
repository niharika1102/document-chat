import pymupdf

def extract_text_from_pdf(file_path: str) -> list[dict]:
    """Extracts text from a PDF

    Args:
        file_path (str): Takes the file path as input

    Returns:
        str: Return the extracted text from the PDF
    """
    
    document = pymupdf.open(file_path)
    
    pages = []
    
    for page_num, page in enumerate(document):
        pages.append({
            "text": page.get_text(),
            "metadata": {
                "source": file_path,
                "page": page_num + 1
            }
        })
        
    document.close()
    
    return pages