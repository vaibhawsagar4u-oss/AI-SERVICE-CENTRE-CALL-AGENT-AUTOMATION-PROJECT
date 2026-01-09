import os, requests

def trigger_webhook(call_sid, user, assistant):
    url = os.getenv("N8N_WEBHOOK_URL")
    if not url:
        return
    payload = {
        "call_sid": call_sid,
        "user_message": user,
        "ai_reply": assistant
    }
    requests.post(url, json=payload)
