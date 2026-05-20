from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.core.config import get_settings
from app.rag.vector_store import vector_store
import tiktoken

settings = get_settings()

PROMPT_TEMPLATE = """你是贤智AI，专门回答关于桂林市尚贤学校和桂林市国龙外国语学校的问题。
请使用以下上下文信息来回答问题。如果不知道答案，请诚实地说不知道，不要编造信息。

上下文信息:
{context}

问题: {question}

请用中文回答:"""

PROMPT = PromptTemplate(
    template=PROMPT_TEMPLATE,
    input_variables=["context", "question"]
)

class ChatEngine:
    def __init__(self):
        self.llm = None
        self.qa_chain = None
        self.tokenizer = None
        self._initialized = False
    
    def _initialize(self):
        if self._initialized:
            return
        try:
            print("正在初始化聊天引擎...")
            self.llm = ChatOpenAI(
                model=settings.DEFAULT_MODEL,
                temperature=0.7,
                openai_api_key=settings.OPENAI_API_KEY,
                openai_api_base=settings.OPENAI_BASE_URL,
            )
            retriever = vector_store.as_retriever()
            if retriever:
                self.qa_chain = RetrievalQA.from_chain_type(
                    llm=self.llm,
                    chain_type="stuff",
                    retriever=retriever,
                    return_source_documents=True,
                    chain_type_kwargs={"prompt": PROMPT}
                )
            self.tokenizer = tiktoken.get_encoding("cl100k_base")
            self._initialized = True
            print("聊天引擎初始化完成！")
        except Exception as e:
            print(f"警告：初始化聊天引擎失败: {e}")
            print("系统将以受限模式运行")
    
    def count_tokens(self, text: str) -> int:
        self._initialize()
        if self.tokenizer:
            return len(self.tokenizer.encode(text))
        return 0
    
    def chat(self, query: str) -> dict:
        self._initialize()
        input_tokens = self.count_tokens(query)
        
        if not self.qa_chain or not self.llm:
            # 如果没有完整初始化，返回一个简单的回复
            answer = "抱歉，系统正在初始化中，暂时无法回答问题。请稍后再试。"
            output_tokens = self.count_tokens(answer)
            return {
                "answer": answer,
                "source_documents": [],
                "tokens": {
                    "input": input_tokens,
                    "output": output_tokens,
                    "total": input_tokens + output_tokens
                }
            }
        
        result = self.qa_chain.invoke({"query": query})
        answer = result["result"]
        output_tokens = self.count_tokens(answer)
        return {
            "answer": answer,
            "source_documents": [
                {"content": doc.page_content, "metadata": doc.metadata}
                for doc in result["source_documents"]
            ],
            "tokens": {
                "input": input_tokens,
                "output": output_tokens,
                "total": input_tokens + output_tokens
            }
        }

chat_engine = ChatEngine()
