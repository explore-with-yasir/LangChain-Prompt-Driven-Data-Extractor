from langchain.vectorstores import Chroma
from app.document_loaders.text_splitter import TextSplitter

class VectorStore:
    vectordb = None
    def create_vector_store(self, documents, embedding, persist_directory):
        self.vectordb = Chroma.from_documents(documents=documents, embedding=embedding, persist_directory=persist_directory)
        return self.vectordb

    def load_and_create_vector_store(self, embedding, persist_directory, loaders=None, documents=None):
        docs = []

        if loaders is not None:
            for loader in loaders:
                docs.extend(loader.load())

        if documents is not None:
            docs.extend(documents)

        splits = TextSplitter.split_documents(docs)

        return self.create_vector_store(documents=splits, embedding=embedding, persist_directory=persist_directory)


    def get_vector_db_ref(self, embedding, persist_directory):
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
        return vectordb.get()