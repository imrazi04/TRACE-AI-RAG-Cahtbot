# TRACE-AI RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot project built with Python, LangChain (new modular packages), HuggingFace embeddings, and FAISS.  
This repository follows a **three-pipeline architecture** and is being developed step by step.

---

## Project Architecture (High Level)

The complete system is divided into **three pipelines**:

1. **Data Ingestion Pipeline** ✅ (Member A – Mostly Completed)
2. **Query & Retrieval Pipeline** ⏳ (Pending)
3. **LLM Response Generation Pipeline** ⏳ (Pending)

---

## 1. Data Ingestion Pipeline (Member A)

### ✅ Status: COMPLETED

This pipeline is responsible for converting raw documents into searchable vector embeddings and storing them in a vector database.

### What has been implemented:

#### 1. PDF Loading
- Curated PDF documents are loaded from disk
- Each PDF is converted into page-level documents

**Output:**
- `120` total PDF pages loaded

---

#### 2. Text Chunking
- Pages are split into smaller overlapping text chunks
- Uses `RecursiveCharacterTextSplitter`

**Output:**
- `918` clean text chunks generated

---

#### 3. Embedding Generation
- Each text chunk is converted into a dense vector embedding
- Model used:
sentence-transformers/all-MiniLM-L6-v2

yaml
Copy code

---

#### 4. Vector Store Creation
- FAISS is used as the vector database
- All embeddings are stored locally for fast similarity search

**Output:**
- FAISS vector index successfully saved to disk

---

### Confirmation of Completion

✔ Embeddings have been **successfully generated**  
✔ Embeddings have been **stored in FAISS**  
✔ Data ingestion pipeline is **fully functional and verified**

---

## Current Progress Summary

| Pipeline | Description | Status |
|--------|------------|--------|
| Pipeline 1 | Data Ingestion (PDF → Chunks → Embeddings → FAISS) | ✅ Completed |
| Pipeline 2 | Query Processing + Retriever (Cosine Similarity) | ❌ Not Started |
| Pipeline 3 | Context Injection + LLM Response Generation | ❌ Not Started |

---

## Project Structure (Current)

TRACE-AI-RAG-Chatbot/
│
├── ingestion/
│ ├── init.py
│ ├── run_ingestion.py
│ ├── pdf_loader.py
│ ├── text_splitter.py
│ └── embed_store.py
│
├── vectorstore/
│ └── faiss_index/
│
├── data/
│ └── curated_pdfs/
│
├── venv/
│
└── README.md

yaml
Copy code

---

## How Ingestion Was Run

```bash
python -m ingestion.run_ingestion
Successful execution confirms:

PDFs loaded

Text chunks created

Embeddings generated

FAISS vector store saved

Next Steps (Remaining Work)
Pipeline 2: Query & Retrieval
Load FAISS vector store

Embed user query

Apply cosine similarity search

Retrieve top-k relevant chunks

Pipeline 3: LLM Generation
Inject retrieved context into prompt

Pass prompt to LLM

Generate final grounded response

Notes
LangChain deprecated imports have been fixed

Project now uses updated modular packages

The system is stable up to the ingestion stage

Conclusion
Member A’s responsibility (Data Ingestion) is almost 100% complete.
The system is now ready to move into retrieval and LLM integration.