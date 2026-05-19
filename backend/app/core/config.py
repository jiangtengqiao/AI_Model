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
