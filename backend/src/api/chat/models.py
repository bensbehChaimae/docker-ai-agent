from sqlmodel import SQLModel, Field


class ChatMessagePayload(SQLModel):
    # validation : [pydantic model]
    message: str

class ChatMessage(SQLmodel , table=True) :
    # saving , updating , getting , deleting : [database table]
    # primary key :
    id: int | None = Field(default=None, primary_key=True)
    
    message: str



    
