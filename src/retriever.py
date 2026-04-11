def get_retriever(vector_store, k: int = 3):
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever