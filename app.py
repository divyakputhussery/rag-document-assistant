import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from src.loader import load_pdf
from src.chunker import split_documents
from src.embedder import create_vector_store
from src.retriever import get_retriever
from src.qa_chain import answer_question

load_dotenv()

st.set_page_config(page_title="RAG Document Assistant", layout="wide")

st.title("RAG Document Assistant")
st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_pdf_path = tmp_file.name

    try:
        with st.spinner("Processing PDF and building vector store..."):
            documents = load_pdf(temp_pdf_path)
            chunks = split_documents(documents)
            vector_store = create_vector_store(chunks)
            retriever = get_retriever(vector_store)

        st.success("PDF processed successfully.")

        question = st.text_input("Enter your question")

        if question.strip():
            with st.spinner("Finding answer..."):
                answer, sources = answer_question(retriever, question)

            st.subheader("Answer")
            st.write(answer)

            st.subheader("Source Chunks")
            for i, doc in enumerate(sources, start=1):
                with st.expander(f"Source {i}"):
                    st.write(doc.page_content)

    finally:
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)