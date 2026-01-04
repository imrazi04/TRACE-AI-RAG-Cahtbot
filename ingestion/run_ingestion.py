from ingestion.pdf_loader import load_pdfs
from ingestion.text_splitter import split_documents
from ingestion.embed_store import create_vectorstore

def main():
    print("🚀 Starting ingestion pipeline...")

    documents = load_pdfs()
    if not documents:
        print("❌ No documents loaded")
        return

    chunks = split_documents(documents)
    create_vectorstore(chunks)

    print("🎉 Ingestion pipeline completed successfully")

if __name__ == "__main__":
    main()
