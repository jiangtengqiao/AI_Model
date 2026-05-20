import os
from typing import List
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
from app.core.config import get_settings

settings = get_settings()

class VectorStore:
    def __init__(self):
        os.makedirs(settings.CHROMA_PERSIST_DIR, exist_ok=True)
        self.embeddings = None
        self.vectorstore = None
        self._initialized = False
    
    def _initialize(self):
        if self._initialized:
            return
        try:
            print("正在加载嵌入模型...")
            self.embeddings = SentenceTransformerEmbeddings(
                model_name="all-MiniLM-L6-v2"
            )
            self.vectorstore = Chroma(
                persist_directory=settings.CHROMA_PERSIST_DIR,
                embedding_function=self.embeddings,
                collection_name="xianzhi_docs"
            )
            self._initialized = True
            print("向量存储初始化完成！")
        except Exception as e:
            print(f"警告：初始化向量存储失败: {e}")
            print("系统将以受限模式运行（无法使用知识库功能）")
    
    def add_documents(self, documents: List[Document]):
        self._initialize()
        if self.vectorstore:
            self.vectorstore.add_documents(documents)
            self.vectorstore.persist()
    
    def similarity_search(self, query: str, k: int = 4):
        self._initialize()
        if self.vectorstore:
            return self.vectorstore.similarity_search(query, k=k)
        return []
    
    def as_retriever(self):
        self._initialize()
        if self.vectorstore:
            return self.vectorstore.as_retriever(search_kwargs={"k": 4})
        return None

vector_store = VectorStore()
