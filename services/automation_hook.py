import os
import requests

def trigger_workflow(call_sid, user_text, ai_text):
    url = os.getenv("N8N_WEBHOOK_URL")
    if not url:
        return

    payload = {
        "call_id": call_sid,
        "user_message": user_text,
        "ai_response": ai_text
    }

    try:
        requests.post(url, json=payload, timeout=2)
    except Exception:
        pass
