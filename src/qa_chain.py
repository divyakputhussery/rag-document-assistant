from langchain_openai import ChatOpenAI


def answer_question(retriever, question: str):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # get relevant chunks
    relevant_docs = retriever.invoke(question)

    # combine context
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # prompt
    prompt = f"""
You are a helpful assistant.
Answer ONLY from the context below.
If not found, say: "I could not find that in the document."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content, relevant_docs