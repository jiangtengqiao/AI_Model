#!/bin/bash

set -e  # 遇到错误立即退出

echo "=========================================="
echo "       贤智AI - 完整设置脚本"
echo "=========================================="
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 创建必要的数据目录
echo -e "${GREEN}[1/7]${NC} 创建数据目录..."
mkdir -p /workspace/backend/data/chroma
mkdir -p /workspace/backend/data
mkdir -p /workspace/crawler/data/raw
echo "   ✓ 数据目录创建完成"
echo ""

# 后端设置
echo -e "${GREEN}[2/7]${NC} 设置后端环境..."
cd /workspace/backend

if [ ! -d "venv" ]; then
    echo "   创建 Python 虚拟环境..."
    python -m venv venv
fi

echo "   激活虚拟环境..."
source venv/bin/activate

echo "   安装 Python 依赖包..."
pip install --upgrade pip
pip install -r requirements.txt
echo "   ✓ 后端依赖安装完成"
echo ""

# 前端设置
echo -e "${GREEN}[3/7]${NC} 设置前端环境..."
cd /workspace/frontend

if [ ! -d "node_modules" ]; then
    echo "   安装 Node.js 依赖包..."
    npm install
fi
echo "   ✓ 前端依赖安装完成"
echo ""

# 初始化数据库
echo -e "${GREEN}[4/7]${NC} 初始化数据库..."
cd /workspace/backend
source venv/bin/activate
python scripts/init_db.py
echo ""

# 添加示例数据
echo -e "${GREEN}[5/7]${NC} 添加示例知识库数据..."
python scripts/add_sample_data.py
echo ""

echo -e "${GREEN}[6/7]${NC} 设置完成！"
echo ""
echo -e "${YELLOW}=========================================="
echo "        接下来的操作步骤"
echo "==========================================${NC}"
echo ""
echo "1. 配置 API 密钥："
echo "   编辑文件：/workspace/backend/.env"
echo "   将 OPENAI_API_KEY 替换为您的实际 API 密钥"
echo ""
echo "2. 启动后端服务（终端 1）："
echo "   cd /workspace/backend"
echo "   source venv/bin/activate"
echo "   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "3. 启动前端服务（终端 2）："
echo "   cd /workspace/frontend"
echo "   npm run dev"
echo ""
echo "4. 访问应用："
echo "   打开浏览器访问: http://localhost:3000"
echo ""
echo -e "${GREEN}==========================================${NC}"
