#!/bin/bash

echo "=========================================="
echo "       贤智AI - 快速启动脚本"
echo "=========================================="

# 检查Python版本
echo "检查Python版本..."
python --version

echo ""
echo "正在创建数据目录..."
mkdir -p backend/data/chroma
mkdir -p crawler/data/raw

echo ""
echo "=========================================="
echo "后端设置"
echo "=========================================="
cd backend

if [ ! -d "venv" ]; then
    echo "创建Python虚拟环境..."
    python -m venv venv
fi

echo "激活虚拟环境..."
source venv/bin/activate

echo "安装Python依赖..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "前端设置"
echo "=========================================="
cd ../frontend

if [ ! -d "node_modules" ]; then
    echo "安装Node.js依赖..."
    npm install
fi

echo ""
echo "=========================================="
echo "设置完成！"
echo "=========================================="
echo ""
echo "接下来的步骤："
echo "1. 配置后端环境变量：编辑 backend/.env"
echo "2. 启动PostgreSQL和Redis"
echo "3. 初始化数据库：cd backend && python scripts/init_db.py"
echo "4. 添加示例数据：cd backend && python scripts/add_sample_data.py"
echo "5. 启动后端：cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo "6. 启动前端：cd frontend && npm run dev"
echo ""
echo "访问 http://localhost:3000 即可使用！"
