import os
from dotenv import load_dotenv

from src.loader import load_pdf
from src.chunker import split_documents
from src.embedder import create_vector_store

load_dotenv()  # 🔥 THIS WAS MISSING


def main():
    pdf_path = "data/sample.pdf"

    print("Loading PDF...")
    documents = load_pdf(pdf_path)
    print(f"Loaded {len(documents)} pages.")

    print("\nSplitting document into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("\nCreating vector store...")
    vector_store = create_vector_store(chunks)

    print("Vector store created successfully!")


if __name__ == "__main__":
    main()