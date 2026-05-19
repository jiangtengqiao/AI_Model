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
        self.llm = ChatOpenAI(
            model=settings.DEFAULT_MODEL,
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY,
            openai_api_base=settings.OPENAI_BASE_URL,
        )
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
    
    def count_tokens(self, text: str) -> int:
        return len(self.tokenizer.encode(text))
    
    def chat(self, query: str) -> dict:
        input_tokens = self.count_tokens(query)
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
