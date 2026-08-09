import pymupdf

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF

    Args:
        file_path (str): Takes the file path as input

    Returns:
        str: Return the extracted text from the PDF
    """
    
    document = pymupdf.open(file_path)
    
    text = ""
    
    for page in document:
        text += page.get_text()
        
    document.close()
    
    return text