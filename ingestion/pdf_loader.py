import json
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


CURATED_DIR = Path("data/curated_pdfs")
METADATA_PATH = Path("data/metadata/metadata.json")

def load_metadata():
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_pdfs():
    metadata_list = load_metadata()
    documents = []

    for meta in metadata_list:
        pdf_path = CURATED_DIR / meta["filename"]

        if not pdf_path.exists():
            print(f"❌ Missing file: {pdf_path}")
            continue

        loader = PyPDFLoader(str(pdf_path))
        pages = loader.load()

        for page in pages:
            page.metadata.update(meta)
            documents.append(page)

    print(f"✅ Loaded {len(documents)} pages from curated PDFs")
    return documents
