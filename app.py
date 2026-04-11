from src.loader import load_pdf

def main():
    pdf_path = "data/sample.pdf"

    print("Loading PDF...")
    documents = load_pdf(pdf_path)

    print(f"Loaded {len(documents)} pages.")

    # print first page content
    print("\nFirst page preview:\n")
    print(documents[0].page_content[:500])


if __name__ == "__main__":
    main()