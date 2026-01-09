import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_reply(text, session):
    messages = session + [
        {"role": "user", "content": text}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a polite and professional service centre call agent."}
        ] + messages,
        temperature=0.3
    )
    return response.choices[0].message.content
