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
