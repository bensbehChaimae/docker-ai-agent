import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Befor app startup 
    init_db()
    yield 
    # After app startup 



app = FastAPI(lifespan=lifespan)
app.include_router(chat_router , prefix="/api/chat")



API_KEY = os.environ.get("API_KEY")
if API_KEY is None:
    raise NotImplementedError("API key was not set")

# Root endpoint to check if the server is running
@app.get("/")

def read_index():
    return {"message": "welcome"}

