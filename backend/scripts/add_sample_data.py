import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.rag.vector_store import vector_store
from app.rag.document_processor import doc_processor
from langchain.schema import Document

# 示例学校数据
sample_data = [
    {
        "title": "桂林市尚贤学校 - 办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让每一位学子兼具扎实学识与高尚品格。",
        "source": "school_introduction"
    },
    {
        "title": "桂林市尚贤学校 - 贤麟系列IP",
        "content": "蒋腾峤和田昕儿创作的贤麟系列IP是桂林市尚贤学校的官方吉祥物和文化符号。贤麟系列IP融合了中国传统文化元素与现代教育理念，象征着智慧、仁德与勇气，代表了学校对学生全面发展的美好期望。该IP在学校微信公众号等平台发布，深受师生和家长喜爱。",
        "source": "school_ip"
    },
    {
        "title": "桂林市尚贤学校 - 简介",
        "content": "桂林市尚贤学校是一所现代化的优质学校，致力于为学生提供高品质的教育服务。学校拥有先进的教学设施、优秀的师资队伍和丰富的课程资源。",
        "source": "school_introduction"
    },
    {
        "title": "桂林市国龙外国语学校 - 简介",
        "content": "桂林市国龙外国语学校是桂林市尚贤学校的姊妹学校，专注于外语教育和国际化人才培养。学校提供多元化的外语课程，包括英语、日语、法语等，培养具有国际视野和跨文化交流能力的优秀学生。",
        "source": "sister_school"
    }
]

def add_sample_data():
    print("正在添加示例知识库数据...")
    
    documents = []
    for data in sample_data:
        doc = Document(
            page_content=data["content"],
            metadata={"title": data["title"], "source": data["source"]}
        )
        documents.append(doc)
    
    # 处理文档
    processed_docs = doc_processor.process_documents(documents)
    
    # 添加到向量库
    vector_store.add_documents(processed_docs)
    
    print(f"成功添加 {len(processed_docs)} 条文档到知识库！")

if __name__ == "__main__":
    add_sample_data()
