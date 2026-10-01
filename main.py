from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot import get_ai_response

app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI Chatbot Backend Running",
        "status": "success"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_ai_response(request.message)

    return {
        "reply": reply
    }
