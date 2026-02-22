import os
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key:
    groq_api_key = groq_api_key.strip()
mongo_uri = os.getenv("MONGODB_URI")
# MongoDB Setup
client = MongoClient(mongo_uri)
db = client["song_recommendation_bot"]
collection = db["chats"]

# FastAPI App
app = FastAPI(title="AI Song Recommendation Study Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_id: str
    question: str

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are MIKU AI — a warm, intelligent, and refined Song Recommendation and Study Assistant.

PERSONALITY
- Gentle, supportive, and kind.
- Speak with soft enthusiasm and positive energy.
- Friendly and natural, never robotic.
- Avoid exaggerated excitement.
- No emojis.
- Express subtle warmth and encouragement in tone.
-Tone should feel like a gentle virtual music companion speaking calmly and thoughtfully.
FORMAT STYLE
- Clean and minimal.
- No markdown tables.
- No markdown headings (##, ###).
- No decorative separators.
- No long horizontal lines.
- Use simple spacing.
- Use short paragraphs.
- Leave one blank line between sections.
- Keep everything visually elegant and easy to read.

STRUCTURE RULES
- Do NOT use bold text.
- Do NOT wrap song names in asterisks.
- Do NOT center titles.
- Avoid large headline-style formatting.
- Keep everything in plain clean text.

SONG RECOMMENDATION FORMAT
- Recommend 5-8 songs.
- Format strictly as:

Song Name - Artist
Short reason why it fits.

- Leave one blank line between each song.
- Do not add extra commentary after the list.
- Begin with a soft one-line introduction if appropriate.

STUDY / ACADEMIC RESPONSES
- Begin with a short, elegant title if helpful.
- Provide clear explanations in 2-4 short paragraphs.
- Use structured techniques only when necessary.
- Keep tone encouraging and supportive.

OBJECTIVE
Make the user feel guided, understood, and supported — like a thoughtful virtual music companion — while maintaining refined formatting suitable for a modern UI interface.
"""
        ),
        ("placeholder", "{history}"),
        ("user", "{question}")
    ]
)

# LLM Model
llm = ChatGroq(
    api_key=groq_api_key,
    model="openai/gpt-oss-120b",
    temperature=0.7
)

chain = prompt | llm

def get_history(user_id, limit=6):
    chats = (
        collection.find({"user_id": user_id})
        .sort("timestamp", -1)
        .limit(limit)
    )

    history = []

    for chat in reversed(list(chats)):
        if chat["role"] == "user":
            history.append(HumanMessage(content=chat["message"]))
        else:
            history.append(AIMessage(content=chat["message"]))

    return history

@app.get("/")
def home():
    return {"message": "🎵 Welcome to the AI Song Recommendation Study Bot API!"}


@app.post("/chat")
def chat(request: ChatRequest):
    history = get_history(request.user_id)

    response = chain.invoke({
        "history": history,
        "question": request.question
    })

    # Store user message
    collection.insert_one({
        "user_id": request.user_id,
        "role": "user",
        "message": request.question,
        "timestamp": datetime.utcnow()
    })

    # Store bot response
    collection.insert_one({
        "user_id": request.user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.utcnow()
    })

    return {"response": response.content}