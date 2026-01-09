import sqlite3
from datetime import datetime

def log_call(call_sid, user_text, ai_text):
    conn = sqlite3.connect("calls.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            call_sid TEXT,
            user_message TEXT,
            ai_response TEXT,
            timestamp TEXT
        )
    """)
    c.execute(
        "INSERT INTO calls (call_sid, user_message, ai_response, timestamp) VALUES (?, ?, ?, ?)",
        (call_sid, user_text, ai_text, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()
