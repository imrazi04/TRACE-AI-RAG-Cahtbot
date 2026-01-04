from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



VECTOR_DIR = Path("vectorstore/faiss_index")

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(str(VECTOR_DIR))

    print("✅ FAISS vectorstore saved successfully")
