import os
from dotenv import load_dotenv

from src.loader import load_pdf
from src.chunker import split_documents
from src.embedder import create_vector_store
from src.retriever import get_retriever
from src.qa_chain import answer_question

load_dotenv()


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

    print("Creating retriever...")
    retriever = get_retriever(vector_store)

    print("\nRAG system ready 🚀")

    question = input("\nEnter your question: ").strip()

    answer, sources = answer_question(retriever, question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSource chunks:\n")
    for i, doc in enumerate(sources, start=1):
        print(f"Source {i}:")
        print(doc.page_content[:300])
        print("-" * 60)


if __name__ == "__main__":
    main()