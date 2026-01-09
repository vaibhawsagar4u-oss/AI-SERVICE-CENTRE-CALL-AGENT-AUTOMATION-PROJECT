# AI Service Centre Call Agent (Production-Grade)

A complete AI-powered service centre call agent that automatically answers phone calls,
understands customer speech, generates intelligent responses, and speaks back like a real call-centre agent.

This project is **production-structured**, **GitHub-ready**, and **automation-compatible**.

---

## 🔥 Core Capabilities
- Automatically picks up incoming calls
- Speech-to-Text (STT)
- AI-based intent understanding
- Text-to-Speech (TTS)
- Multi-turn conversations
- Call session tracking
- Call logging & transcripts
- Webhook support for n8n / CRM
- Dockerized deployment

---

## 🧠 Architecture

Caller → Twilio Voice  
→ STT → AI Engine → TTS  
→ Caller  
→ Logs + Webhooks

---

## 🛠 Tech Stack
- Python
- Flask
- Twilio Voice (TwiML)
- OpenAI API
- REST APIs
- JSON
- Docker

---

## ▶ Quick Start

```bash
pip install -r requirements.txt
python app.py
```

Expose with:
```bash
ngrok http 5000
```

Paste the public URL in Twilio Voice Webhook:
```
https://xxxx.ngrok.io/voice
```

---

## 📡 API Endpoints
- POST /voice  → Twilio Voice Webhook
- POST /webhook/n8n → Automation trigger
- GET /health → Status check

---

## 📜 License
MIT
