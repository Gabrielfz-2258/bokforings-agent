from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import chat
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

class Message(BaseModel):
    message:str

@app.post("/chat")
def chat_endpoint(body: Message):
    svar = chat(body.message)
    return {"svar": svar}

@app.get("/")
def index():
    return FileResponse("src/static/index.html")