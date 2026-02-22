# 🎵 MIKU AI STUDIO  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen.svg)
![LangChain](https://img.shields.io/badge/LangChain-LLM_Framework-purple.svg)
![Groq](https://img.shields.io/badge/Groq-LLM_API-black.svg)

---

## ✨ Overview

**MIKU AI STUDIO** is a lightweight AI-powered song recommendation and study assistant built using FastAPI, LangChain, Groq LLM, and MongoDB.

This project demonstrates how modern AI systems:

- Integrate Large Language Models (LLMs)
- Maintain conversational memory using databases
- Provide context-aware responses
- Deploy as scalable REST APIs

The system includes a futuristic static frontend powered by Three.js and a backend capable of persistent contextual conversations.

---

## 🚀 Features

- 🎶 Song recommendation & study assistant persona  
- 🧠 Context-aware responses using MongoDB-backed memory  
- 🔗 LangChain + ChatGroq LLM integration  
- 💾 Persistent chat storage  
- 🌐 Simple REST API for chat  
- 🎨 Futuristic static frontend (Three.js powered)

---

## 🏗 System Architecture

User → Frontend → FastAPI Backend → MongoDB (Memory) → Groq LLM → Response → Store → Return to User

### 🧠 Memory Logic Explained

1. User sends a message via frontend.
2. Backend receives the message through `/chat`.
3. System retrieves recent conversation history from MongoDB using `user_id`.
4. The history + new question are passed to the Groq LLM via LangChain.
5. LLM generates a context-aware response.
6. Both user message and assistant response are saved in MongoDB.
7. Response is returned to the frontend.

This ensures:
- Context continuity  
- Personalized conversations  
- Persistent memory across sessions  

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- LangChain (ChatGroq)
- MongoDB (PyMongo)

### Frontend
- HTML
- CSS
- JavaScript
- Three.js

---

## 📂 Project Structure

```
Miku-AI-Studio/
│
├── app.py
├── index.html
├── requirement.txt
├── .env
```

---

## 📦 Requirements

Install Python 3.10+ and dependencies listed in `requirement.txt`:

- numpy  
- langchain  
- langchain_groq  
- langchain_core  
- langchain_community  
- pymongo  
- fastapi  
- uvicorn  
- python-multipart  
- python-dotenv  

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
MONGODB_URI=your_mongodb_connection_string
```

Example:

```
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxx
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/song_recommendation_bot?retryWrites=true&w=majority
```

⚠️ Never commit `.env` or secrets to GitHub.

---

## ▶ Run Locally (Windows)

1. Open PowerShell in project directory  

2. Create & activate virtual environment:

```powershell
python -m venv .\env
.\env\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r .\requirement.txt
```

4. Start API:

```powershell
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

5. Open `index.html` in browser.

---

## 🌐 API Endpoints

### GET /

Health check endpoint.

Response:

```json
{
  "message": "🎵 Welcome to the AI Song Recommendation Study Bot API!"
}
```

---

### POST /chat

Request:

```json
{
  "user_id": "string",
  "question": "string"
}
```

Response:

```json
{
  "response": "assistant reply text"
}
```

---

## 💾 Data Storage

- Database: `song_recommendation_bot`
- Collection: `chats`

Document structure:

- `user_id`
- `role` ("user" | "assistant")
- `message`
- `timestamp`

This enables persistent contextual memory.

---

## 🚢 Deployment (High-Level)

1. Deploy backend (Render / AWS / Azure / etc.)
2. Set environment variables:
   - `GROQ_API_KEY`
   - `MONGODB_URI`
3. Run production server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

4. Host frontend via:
   - Netlify
   - Vercel
   - Or same backend server

Add your deployment link:

Live URL: https://miku-ai-studio.onrender.com

---

## 🔒 Security & Operational Notes

- Do not commit `.env`
- Restrict MongoDB IP access
- Add authentication before public deployment
- Monitor Groq API usage
- Implement rate limiting in production

---

## 🧪 Testing

```powershell
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d "{\"user_id\":\"test\",\"question\":\"Recommend study songs\"}"
```

---

# 📜 License

This project is licensed under the MIT License.

---

## MIT License

```
MIT License

Copyright (c) 2026 N. Sai Vikas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Thank You

Thank you for reviewing **MIKU AI STUDIO**.

This project demonstrates real-world AI assistant architecture by combining:

- Large Language Models  
- Persistent database memory  
- REST API backend development  
- Cloud deployment readiness  

Your time and evaluation are sincerely appreciated.
