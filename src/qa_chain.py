from langchain_openai import ChatOpenAI


def answer_question(retriever, question: str):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    relevant_docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in relevant_docs)

    prompt = f"""
You are answering questions using the provided document context.

Rules:
1. Use only the context below.
2. If the answer is clearly present, answer directly.
3. If the question asks for a summary, summarize the document using the retrieved context.
4. If the context is incomplete but still gives enough meaning, provide the best possible answer.
5. Only say "I could not find a clear answer in the document." if the context is truly unrelated.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content, relevant_docs