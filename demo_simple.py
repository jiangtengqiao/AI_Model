#!/usr/bin/env python3#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id":#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让每一位学子兼具扎实学识与高尚品格。"
    },
    {
        "#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让每一位学子兼具扎实学识与高尚品格。"
    },
    {
        "id": 2,
        "title": "贤麟系列IP",
        "content#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让每一位学子兼具扎实学识与高尚品格。"
    },
    {
        "id": 2,
        "title": "贤麟系列IP",
        "content": "蒋腾峤和田昕儿创作的贤麟系列IP是桂林市尚贤学校的#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让每一位学子兼具扎实学识与高尚品格。"
    },
    {
        "id": 2,
        "title": "贤麟系列IP",
        "content": "蒋腾峤和田昕儿创作的贤麟系列IP是桂林市尚贤学校的官方吉祥物和文化符号。贤麟系列IP融合了中国传统文化元素与现代教育理念，#!/usr/bin/env python3
"""
贤智AI - 简化演示版本
一个简单的命令行聊天机器人，演示RAG问答功能
"""

import sys
import os
from typing import List, Dict

# 示例知识库 - 桂林市尚贤学校相关信息
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "办学理念",
        "content": "桂林市尚贤学校深植教育沃土，以“尚贤立校，尚贤树人”为办学理念，秉承“尚真立贤，厚德致远”的校训精神，致力于构建全人教育体系。在办学实践中，学校既注重夯实学生知识根基，培养思辨创新能力，又强调品德修养与社会责任的塑造，让每一位学子兼具扎实学识与高尚品格。"
    },
    {
        "id": 2,
        "title": "贤麟系列IP",
        "content": "蒋腾峤和田昕儿创作的贤麟系列IP是桂林市尚贤学校的官方吉祥物和文化符号。贤麟系列IP融合了中国传统文化元素与现代教育理念，象征着智慧、仁德与勇气，代表了学校对学生全面发展的美好期望。该