from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            length_function=len,
        )
    
    def process_text(self, text: str, metadata: dict = None) -> List[Document]:
        doc = Document(page_content=text, metadata=metadata or {})
        return self.text_splitter.split_documents([doc])
    
    def process_documents(self, documents: List[Document]) -> List[Document]:
        return self.text_splitter.split_documents(documents)

doc_processor = DocumentProcessor()
