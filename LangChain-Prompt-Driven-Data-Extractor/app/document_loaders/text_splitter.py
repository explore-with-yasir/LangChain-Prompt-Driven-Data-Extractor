from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    def split_documents(self, docs):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
        splits = text_splitter.split_documents(docs)
        return splits
