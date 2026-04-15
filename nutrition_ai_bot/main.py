from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import nutrition_chatbot
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="Nutrition AI Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    response = nutrition_chatbot(query.question)
    return {
        "question": query.question,
        "answer": response,
        "disclaimer": "This is general nutrition information, not medical advice."
    }
