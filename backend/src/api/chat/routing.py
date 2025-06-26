from fastAPI import APIRouter , Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage
from api.db import get_session


router = APIRouter()

# api/chat/
@router.get("")
def chat_health():
    return {"message": "Welcome to the Chat API"}



# /api/chat/recent/
# curl http://localhost:8000/api/chat/recent/ 
@router.get("/recent/")
def chat_list_messages(
    session: Session = Depends(get_session)
):
    query = select(ChatMessage) # sql -> query
    result = session.exec(query).fetchall()[:10]  # Fetch the last 10 messages
    return result



# HTTP post 
# curl -X POST -d '{"message": "Hello, world!"}' -H "Content-Type: application/json" http://localhost:8000/api/chat/
@router.post("/", response_model=ChatMessage)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj) # ensure id/primary key is set

    # Ready to store in the database

    return obj



