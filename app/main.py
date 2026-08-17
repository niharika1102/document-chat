from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
from pydantic import BaseModel

from app.services.rag_service import ask_question
from app.services.ingestion_service import ingest_document

app = FastAPI()

class ChatRequest(BaseModel):
    question: str
    
@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_question(request.question)

    return {
        "answer": answer
    }
    
@app.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    # Verfiy that file is PDF
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
        
    # Create the documents directory if it doesn't exist
    upload_dir = Path("data/docs")
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Save the uploaded file
    file_path = upload_dir / file.filename

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # Run the ingestion pipeline
    chunks_added = ingest_document(str(file_path))

    return {
        "message": "Document ingested successfully",
        "filename": file.filename,
        "chunks_added": chunks_added
    }
    