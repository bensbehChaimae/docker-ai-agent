import os
from fastapi import FastAPI


pyapp = FastAPI()

API_KEY = os.environ.get("API_KEY")
if API_KEY is None:
    raise NotImplementedError("API key was not set")

# Root endpoint to check if the server is running
@pyapp.get("/")

def read_index():
    return {"message": "welcome"}

