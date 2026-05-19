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
