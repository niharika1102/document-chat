# Document Chatter

A simple **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions based on their content.

The application processes uploaded documents, converts their content into vector embeddings, stores them in ChromaDB, retrieves relevant information for a user's question, and uses Google's Gemini model to generate a contextual answer.

---

## Features

- Upload PDF documents through an API
- Extract text from PDF files
- Split document content into chunks
- Generate embeddings using Sentence Transformers
- Store document embeddings in ChromaDB
- Perform semantic search to retrieve relevant chunks
- Generate contextual answers using Google Gemini
- REST API built with FastAPI
- Interactive API documentation using Swagger UI

---

# How It Works

The application has two main pipelines:

1. **Document Ingestion**
2. **Question Answering**

## Document Ingestion

When a PDF is uploaded, it goes through the following pipeline:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding Generation
 ↓
ChromaDB
```

The document is processed once and its embeddings are stored in the vector database.

---

## Question Answering

When a user asks a question:

```text
User Question
 ↓
Generate Query Embedding
 ↓
Search ChromaDB
 ↓
Retrieve Relevant Chunks
 ↓
Send Context + Question to Gemini
 ↓
Generated Answer
```

The application does not send the entire document to the LLM. Instead, it retrieves only the most relevant chunks and provides them as context to the model.

---

# Architecture

```text
                        DOCUMENT INGESTION

                              PDF
                               │
                               ▼
                       POST /documents
                               │
                               ▼
                       ingestion_service
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
             Loader         Chunker        Embedder
                                                │
                                                ▼
                                            ChromaDB


                        QUESTION ANSWERING

User Question
     │
     ▼
 POST /chat
     │
     ▼
 rag_service
     │
     ├── Generate Query Embedding
     │
     ├── Retrieve Relevant Chunks
     │
     └── Generate Answer using Gemini
                    │
                    ▼
                 Answer
```

---

# Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **PyMuPDF**
- **Sentence Transformers**
- **all-MiniLM-L6-v2**
- **ChromaDB**
- **Google Gemini API**

---

# Project Structure

```text
document-chat/
│
├── app/
│   │
│   ├── generation/
│   │   ├── __init__.py
│   │   └── generator.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   └── embedder.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   └── vector_store.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ingestion_service.py
│   │   └── rag_service.py
│   │
│   └── main.py
│
├── data/
│   ├── chroma/
│   └── docs/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Setup

## 1. Clone the repository

```bash
git clone https://github.com/niharika1102/document-chat.git
cd document-chat
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

## 3. Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure environment variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Upload a Document

### `POST /documents`

Uploads and processes a PDF document.

The uploaded document goes through the following pipeline:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding Generation
 ↓
ChromaDB
```

Only PDF files are currently supported.

### Example Response

```json
{
  "message": "Document ingested successfully",
  "filename": "example.pdf",
  "chunks_added": 45
}
```

---

## Ask a Question

### `POST /chat`

Accepts a question and generates an answer based on the uploaded documents.

### Request Body

```json
{
  "question": "What is normalization?"
}
```

### Processing Flow

```text
Question
   ↓
Generate Query Embedding
   ↓
Search ChromaDB
   ↓
Retrieve Relevant Document Chunks
   ↓
Provide Context + Question to Gemini
   ↓
Generate Answer
```

### Example Response

```json
{
  "answer": "Normalization is the process of organizing database tables to reduce redundancy and prevent anomalies."
}
```

---

# How RAG Works in This Project

This project uses **Retrieval-Augmented Generation (RAG)** to generate answers based on uploaded documents.

Instead of sending an entire PDF to the LLM every time a user asks a question, the document is processed beforehand.

## Step 1: Extract Text

Text is extracted from each page of the uploaded PDF using PyMuPDF.

```text
PDF
 ↓
Page 1 → Text
Page 2 → Text
Page 3 → Text
...
```

Metadata such as the source document and page number is preserved.

---

## Step 2: Chunk the Text

The extracted text is split into smaller chunks.

```text
Document Text
       ↓
┌────────┐
│ Chunk 1│
├────────┤
│ Chunk 2│
├────────┤
│ Chunk 3│
└────────┘
```

Chunking allows the system to retrieve smaller, relevant pieces of information instead of searching through an entire document.

---

## Step 3: Generate Embeddings

Each text chunk is converted into a numerical representation called an embedding.

The project uses:

```text
all-MiniLM-L6-v2
```

from Sentence Transformers.

Conceptually:

```text
"Normalization reduces redundancy"
              ↓
        Embedding Model
              ↓
[0.12, -0.45, 0.83, ...]
```

Embeddings allow the application to compare the semantic meaning of text.

---

## Step 4: Store Embeddings

The embeddings, document chunks, and metadata are stored in ChromaDB.

```text
Chunk
  +
Embedding
  +
Metadata
  ↓
ChromaDB
```

---

## Step 5: Retrieve Relevant Information

When a user asks a question, the question is also converted into an embedding.

```text
"What is normalization?"
          ↓
   Embedding Model
          ↓
   Query Embedding
```

ChromaDB compares the query embedding with the stored document embeddings and retrieves the most semantically relevant chunks.

---

## Step 6: Generate the Answer

The retrieved chunks are combined into a context and sent to Gemini along with the user's question.

```text
Relevant Chunks
       +
User Question
       ↓
     Gemini
       ↓
Generated Answer
```

---

# Complete RAG Flow

```text
                        DOCUMENT PROCESSING

PDF
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
Embedding Generation
 │
 ▼
Vector Database
 │
 │
 │
 └──────────────────────────────┐
                                │
                                ▼
                          User Question
                                │
                                ▼
                         Query Embedding
                                │
                                ▼
                         Similarity Search
                                │
                                ▼
                        Relevant Chunks
                                │
                                ▼
                    Context + User Question
                                │
                                ▼
                              Gemini
                                │
                                ▼
                              Answer
```

---

# Key Learning Outcomes

This project was built as a hands-on exercise to understand the core components of a RAG system.

Through this project, I learned how to:

- Build a document ingestion pipeline
- Extract text from PDF documents
- Chunk documents for retrieval
- Generate embeddings
- Understand the difference between document embeddings and query embeddings
- Store embeddings in a vector database
- Perform semantic search
- Retrieve relevant context for a user query
- Connect a vector retrieval pipeline to an LLM
- Build a complete RAG pipeline
- Expose the pipeline through a FastAPI backend
- Handle PDF uploads through an API

---

# Future Improvements

This project was intentionally kept simple as a learning project.

Possible future improvements include:

- Returning source documents and page numbers with generated answers
- Preventing duplicate document ingestion
- Supporting additional file formats
- Adding conversation history
- Adding authentication
- Adding a frontend interface
- Streaming LLM responses
- Supporting document deletion and management

---

# License

This project is intended for learning and experimentation.
