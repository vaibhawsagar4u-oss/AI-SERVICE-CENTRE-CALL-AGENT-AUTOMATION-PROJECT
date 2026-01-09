from flask import Flask, request, Response, jsonify
from twilio.twiml.voice_response import VoiceResponse
from services.ai_engine import ai_reply
from services.call_state import get_session, update_session
from services.logger import log_call
from services.webhook import trigger_webhook

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    call_sid = request.values.get("CallSid")
    speech = request.values.get("SpeechResult", "")

    session = get_session(call_sid)
    resp = VoiceResponse()

    if not speech:
        gather = resp.gather(input="speech", action="/voice", timeout=5)
        gather.say("Welcome to our automated service centre. How may I assist you today?")
        return Response(str(resp), mimetype="text/xml")

    reply = ai_reply(speech, session)
    update_session(call_sid, speech, reply)
    log_call(call_sid, speech, reply)
    trigger_webhook(call_sid, speech, reply)

    resp.say(reply)
    resp.redirect("/voice")

    return Response(str(resp), mimetype="text/xml")

@app.route("/health")
def health():
    return jsonify({"status": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
