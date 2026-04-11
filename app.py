from src.loader import load_pdf
from src.chunker import split_documents


def main():
    pdf_path = "data/sample.pdf"

    print("Loading PDF...")
    documents = load_pdf(pdf_path)
    print(f"Loaded {len(documents)} pages.")

    print("\nSplitting document into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("\nFirst chunk preview:\n")
    print(chunks[0].page_content[:500])


if __name__ == "__main__":
    main()