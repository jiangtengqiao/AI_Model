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
