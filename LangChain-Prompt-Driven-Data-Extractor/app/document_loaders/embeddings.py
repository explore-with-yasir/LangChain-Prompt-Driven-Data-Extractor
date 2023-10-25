from langchain.embeddings.openai import OpenAIEmbeddings

class Embeddings:
    def get_openai_embedding(self):
        return OpenAIEmbeddings()
