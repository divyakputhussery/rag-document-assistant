def get_retriever(vector_store, k: int = 4):
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever