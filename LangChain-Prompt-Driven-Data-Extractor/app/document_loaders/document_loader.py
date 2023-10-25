from langchain.document_loaders import PyPDFLoader

from app.document_loaders import embeddings
from app.services.google_drive_loader import GoogleDriveLoader
from .vector_store import VectorStore
from app.config import Config

import json

class DocumentLoader:
    vectorStore = VectorStore()
    def load_pdfs(self, pdf_paths, embedding, persist_directory):
        loaders = [PyPDFLoader(pdf_path) for pdf_path in pdf_paths]
        docs = [loader.load() for loader in loaders]
        # Process the documents and create the vector store
        # ...

    def load_gdrive(self, username, embedding, persist_directory):
        docs = GoogleDriveLoader.load(username)
        # Process the documents and create the vector store
        # ...
        embedding = embeddings.get_openai_embedding()

        vectordb = self.vectorStore.load_and_create_vector_store(embedding, Config.PERSIST_DIRECTORY, documents=docs)
