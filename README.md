# 贤智AI - 桂林市尚贤学校AI问答系统

一个功能完整的AI大模型问答系统，专注于回答关于桂林市尚贤学校和国龙外国语学校的问题。

## 功能特性

- 🤖 RAG知识库问答系统
- 👤 用户认证系统（邮箱/微信扫码）
- 💳 Token计费与支付系统
- 🕷️ 数据爬虫系统
- 💬 美观的聊天界面
- 📱 响应式设计

## 技术栈

### 后端
- Python 3.11+
- FastAPI
- LangChain
- ChromaDB (向量数据库)
- PostgreSQL (关系数据库)
- Redis (缓存)

### 前端
- React 18
- TypeScript
- Tailwind CSS
- Vite

### 爬虫
- Scrapy
- BeautifulSoup4

## 项目结构

```
/workspace/
├── backend/              # 后端服务
│   ├── app/
│   │   ├── api/         # API路由
│   │   ├── core/        # 核心配置
│   │   ├── models/      # 数据模型
│   │   ├── services/    # 业务逻辑
│   │   └── rag/         # RAG引擎
│   └── requirements.txt
├── frontend/            # 前端应用
│   ├── src/
│   │   ├── components/
│   │   └── pages/
│   └── package.json
├── crawler/            # 爬虫系统
│   ├── spiders/
│   └── scrapy.cfg
└── docs/               # 文档
```

## 快速开始

### 前置要求

- Python 3.11+
- Node.js 18+
- PostgreSQL
- Redis

### 1. 后端设置

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 复制环境变量配置
cp .env.example .env
# 编辑 .env 文件，填入您的配置
```

### 2. 前端设置

```bash
cd frontend
npm install
npm run dev
```

### 3. 数据库设置

```bash
# 创建数据库
createdb xianzhi_ai

# 后端会自动创建表结构
```

### 4. 启动服务

```bash
# 启动后端
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 启动前端 (新终端)
cd frontend
npm run dev
```

访问 http://localhost:3000 即可使用！

## 使用说明

1. **注册账号** - 使用邮箱注册新账号
2. **配置API** - 在 `.env` 文件中配置 OpenAI API Key
3. **爬取数据** - 运行爬虫采集学校信息
4. **构建知识库** - 将采集的数据添加到向量数据库
5. **开始问答** - 在聊天界面提问

## 详细文档

完整的实施计划请参见 [docs/superpowers/plans/2026-05-19-xianzhi-ai-implementation-plan.md](docs/superpowers/plans/2026-05-19-xianzhi-ai-implementation-plan.md)

## Token计费

系统采用按Token计费模式，默认费率：
- 0.00001 元 / Token

可在代码中自定义费率。

## License

MIT