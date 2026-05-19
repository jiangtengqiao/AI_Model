# 贤智AI - 完整实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一个完整的AI大模型问答系统，专注于桂林市尚贤学校和国龙外国语学校的知识问答，包含用户系统、计费支付功能和Web界面。

**Architecture:** 采用前后端分离架构，后端使用FastAPI提供RESTful API，前端使用React构建现代化聊天界面，通过RAG技术实现基于知识库的智能问答。

**Tech Stack:** Python 3.11+, FastAPI, React 18, LangChain, ChromaDB, PostgreSQL, Redis, Scrapy

---

## 项目目录结构

```
/workspace/
├── backend/                 # 后端服务
│   ├── app/
│   │   ├── api/            # API路由
│   │   ├── core/           # 核心配置
│   │   ├── models/         # 数据模型
│   │   ├── services/       # 业务逻辑
│   │   └── rag/            # RAG引擎
│   ├── tests/
│   └── requirements.txt
├── frontend/               # 前端应用
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── lib/
│   └── package.json
├── crawler/                # 爬虫系统
│   ├── spiders/
│   └── scrapy.cfg
├── docs/                   # 文档
└── scripts/                # 工具脚本
```

---

## 第一阶段：核心功能开发

### Task 1: 后端项目初始化

**Files:**
- Create: `/workspace/backend/requirements.txt`
- Create: `/workspace/backend/app/main.py`
- Create: `/workspace/backend/app/core/config.py`
- Create: `/workspace/backend/.env.example`

**Steps:**

- [ ] **Step 1: 创建后端依赖文件**

```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
alembic==1.13.1
redis==5.0.1
celery==5.3.6
langchain==0.1.8
langchain-openai==0.0.6
langchain-community==0.0.21
chromadb==0.4.22
sentence-transformers==2.3.1
tiktoken==0.5.2
pydantic==2.6.1
pydantic-settings==2.1.0
python-dotenv==1.0.1
httpx==0.26.0
```

- [ ] **Step 2: 创建配置文件**

```python
# backend/app/core/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "贤智AI"
    DEBUG: bool = True
    
    # 数据库
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/xianzhi_ai"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    # AI
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    DEFAULT_MODEL: str = "gpt-3.5-turbo"
    
    # 向量数据库
    CHROMA_PERSIST_DIR: str = "./data/chroma"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
```

- [ ] **Step 3: 创建主应用文件**

```python
# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "欢迎使用贤智AI", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

- [ ] **Step 4: 创建环境变量示例文件**

```env
# .env.example
APP_NAME=贤智AI
DEBUG=True

DATABASE_URL=postgresql://xianzhi:password@localhost:5432/xianzhi_ai
REDIS_URL=redis://localhost:6379/0

SECRET_KEY=your-super-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

OPENAI_API_KEY=sk-your-openai-api-key
OPENAI_BASE_URL=https://api.openai.com/v1
DEFAULT_MODEL=gpt-3.5-turbo

CHROMA_PERSIST_DIR=./data/chroma
```

---

### Task 2: 数据模型与数据库

**Files:**
- Create: `/workspace/backend/app/models/__init__.py`
- Create: `/workspace/backend/app/models/base.py`
- Create: `/workspace/backend/app/models/user.py`
- Create: `/workspace/backend/app/models/order.py`
- Create: `/workspace/backend/app/core/database.py`

**Steps:**

- [ ] **Step 1: 创建基础模型**

```python
# backend/app/models/base.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, func

Base = declarative_base()

class TimestampMixin:
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
```

- [ ] **Step 2: 创建用户模型**

```python
# backend/app/models/user.py
from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from app.models.base import Base, TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), nullable=True)
    hashed_password = Column(String(255), nullable=True)
    avatar = Column(String(500), nullable=True)
    balance = Column(Float, default=0.0, nullable=False)
    total_tokens_used = Column(Integer, default=0, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    wechat_openid = Column(String(100), unique=True, nullable=True)
```

- [ ] **Step 3: 创建订单模型**

```python
# backend/app/models/order.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
import enum
from app.models.base import Base, TimestampMixin

class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class Order(Base, TimestampMixin):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    order_no = Column(String(64), unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), default=OrderStatus.PENDING, nullable=False)
    payment_method = Column(String(20), nullable=True)
    description = Column(Text, nullable=True)
    
    user = relationship("User", backref="orders")

class Transaction(Base, TimestampMixin):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(20), nullable=False)
    amount = Column(Float, nullable=False)
    balance_before = Column(Float, nullable=False)
    balance_after = Column(Float, nullable=False)
    tokens = Column(Integer, default=0, nullable=False)
    model = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    
    user = relationship("User", backref="transactions")
```

- [ ] **Step 4: 创建数据库连接配置**

```python
# backend/app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

### Task 3: RAG 知识库系统

**Files:**
- Create: `/workspace/backend/app/rag/__init__.py`
- Create: `/workspace/backend/app/rag/vector_store.py`
- Create: `/workspace/backend/app/rag/document_processor.py`
- Create: `/workspace/backend/app/rag/chat_engine.py`

**Steps:**

- [ ] **Step 1: 创建向量存储模块**

```python
# backend/app/rag/vector_store.py
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
        self.embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        self.vectorstore = Chroma(
            persist_directory=settings.CHROMA_PERSIST_DIR,
            embedding_function=self.embeddings,
            collection_name="xianzhi_docs"
        )
    
    def add_documents(self, documents: List[Document]):
        self.vectorstore.add_documents(documents)
        self.vectorstore.persist()
    
    def similarity_search(self, query: str, k: int = 4):
        return self.vectorstore.similarity_search(query, k=k)
    
    def as_retriever(self):
        return self.vectorstore.as_retriever(search_kwargs={"k": 4})

vector_store = VectorStore()
```

- [ ] **Step 2: 创建文档处理模块**

```python
# backend/app/rag/document_processor.py
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
```

- [ ] **Step 3: 创建聊天引擎**

```python
# backend/app/rag/chat_engine.py
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
```

---

### Task 4: 爬虫系统

**Files:**
- Create: `/workspace/crawler/requirements.txt`
- Create: `/workspace/crawler/scrapy.cfg`
- Create: `/workspace/crawler/shangxian/spiders/__init__.py`
- Create: `/workspace/crawler/shangxian/spiders/school_spider.py`
- Create: `/workspace/crawler/shangxian/settings.py`

**Steps:**

- [ ] **Step 1: 创建爬虫依赖文件**

```txt
scrapy==2.11.0
beautifulsoup4==4.12.3
requests==2.31.0
```

- [ ] **Step 2: 创建 Scrapy 配置**

```ini
# crawler/scrapy.cfg
[settings]
default = shangxian.settings

[deploy]
project = shangxian
```

- [ ] **Step 3: 创建爬虫设置**

```python
# crawler/shangxian/settings.py
BOT_NAME = "shangxian"
SPIDER_MODULES = ["shangxian.spiders"]
NEWSPIDER_MODULE = "shangxian.spiders"
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
FEED_EXPORT_ENCODING = "utf-8"
```

- [ ] **Step 4: 创建学校爬虫**

```python
# crawler/shangxian/spiders/school_spider.py
import scrapy
from bs4 import BeautifulSoup
import json
import os

class SchoolSpider(scrapy.Spider):
    name = "school"
    start_urls = [
        # 待添加学校官网URL
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_dir = "./data/raw"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else ""
        content = soup.get_text(separator="\n", strip=True)
        
        data = {
            "url": response.url,
            "title": title,
            "content": content,
            "source": "school_website"
        }
        
        filename = f"{self.output_dir}/{hash(response.url)}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        yield data
        
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)
```

---

### Task 5: API 路由与认证

**Files:**
- Create: `/workspace/backend/app/api/__init__.py`
- Create: `/workspace/backend/app/api/auth.py`
- Create: `/workspace/backend/app/api/chat.py`
- Create: `/workspace/backend/app/services/user_service.py`
- Create: `/workspace/backend/app/core/security.py`

**Steps:**

- [ ] **Step 1: 创建安全模块**

```python
# backend/app/core/security.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.config import get_settings
from app.core.database import get_db
from app.models.user import User

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭证",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user
```

- [ ] **Step 2: 创建用户服务**

```python
# backend/app/services/user_service.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash, verify_password
from typing import Optional

class UserService:
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create_user(db: Session, email: str, password: str, username: str = None) -> User:
        hashed_password = get_password_hash(password)
        user = User(email=email, hashed_password=hashed_password, username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        user = UserService.get_user_by_email(db, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    @staticmethod
    def update_balance(db: Session, user_id: int, amount: float):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.balance += amount
            db.commit()
            return user
        return None

user_service = UserService()
```

- [ ] **Step 3: 创建认证 API**

```python
# backend/app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.database import get_db
from app.core.config import get_settings
from app.core.security import create_access_token, get_current_user
from app.services.user_service import user_service
from app.models.user import User
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["认证"])
settings = get_settings()

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    username: str | None = None

class UserResponse(BaseModel):
    id: int
    email: str
    username: str | None
    balance: float
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    existing_user = user_service.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="邮箱已被注册")
    user = user_service.create_user(db, user_data.email, user_data.password, user_data.username)
    return user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="邮箱或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserResponse.model_validate(user)
    }

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
```

- [ ] **Step 4: 创建聊天 API**

```python
# backend/app/api/chat.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.rag.chat_engine import chat_engine
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["聊天"])

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    tokens: dict

@router.post("/send", response_model=ChatResponse)
async def send_message(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.balance <= 0:
        raise HTTPException(status_code=402, detail="余额不足，请充值")
    
    try:
        result = chat_engine.chat(request.message)
        
        tokens_used = result["tokens"]["total"]
        cost = tokens_used * 0.00001
        
        current_user.balance -= cost
        current_user.total_tokens_used += tokens_used
        db.commit()
        
        return ChatResponse(
            answer=result["answer"],
            tokens=result["tokens"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

- [ ] **Step 5: 更新主应用**

```python
# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api import auth, chat

settings = get_settings()

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "欢迎使用贤智AI", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

---

### Task 6: 前端项目初始化

**Files:**
- Create: `/workspace/frontend/package.json`
- Create: `/workspace/frontend/vite.config.ts`
- Create: `/workspace/frontend/tsconfig.json`
- Create: `/workspace/frontend/tailwind.config.js`
- Create: `/workspace/frontend/src/main.tsx`
- Create: `/workspace/frontend/src/App.tsx`

**Steps:**

- [ ] **Step 1: 创建 package.json**

```json
{
  "name": "xianzhi-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.0",
    "axios": "^1.6.7",
    "lucide-react": "^0.330.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.55",
    "@types/react-dom": "^18.2.19",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.3.3",
    "vite": "^5.1.0",
    "tailwindcss": "^3.4.1",
    "postcss": "^8.4.35",
    "autoprefixer": "^10.4.17"
  }
}
```

- [ ] **Step 2: 创建 Vite 配置**

```typescript
// frontend/vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
```

- [ ] **Step 3: 创建 TypeScript 配置**

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

- [ ] **Step 4: 创建 Tailwind 配置**

```javascript
// frontend/tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

- [ ] **Step 5: 创建主入口文件**

```tsx
// frontend/src/main.tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

- [ ] **Step 6: 创建主应用组件**

```tsx
// frontend/src/App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Chat from './pages/Chat'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Chat />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
```

---

## 第二阶段：完善与扩展

（包括支付集成、用户中心、管理后台等）

---

## 第三阶段：测试与部署

（包括测试用例、Docker配置、部署脚本等）

---

**Plan complete.** 以上是第一阶段核心功能的详细实施计划。准备好后我们可以开始执行！
