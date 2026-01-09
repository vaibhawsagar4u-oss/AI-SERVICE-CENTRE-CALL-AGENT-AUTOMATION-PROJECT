sessions = {}

def get_session(call_sid):
    return sessions.get(call_sid, [])

def update_session(call_sid, user, assistant):
    sessions.setdefault(call_sid, []).extend([
        {"role": "user", "content": user},
        {"role": "assistant", "content": assistant}
    ])
