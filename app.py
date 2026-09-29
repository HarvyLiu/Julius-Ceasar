from dotenv import load_dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from ciphers.caesar import caesar
from ciphers.b64 import b64_encode, b64_decode


load_dotenv()
app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/caesar")
def handle_caesar(ack, respond, command):
    ack()
    text = command.get("text", "").strip()
    if not text: # "" == false, "text here" == true
        respond("Use: /caesar <shift> <message>  e.g. /caesar 3 hello")
        return
    parts = text.split(" ", 1) #rsplit for from right side
    if len(parts) < 2:
        respond("Use: /caesar <shift> <message>  e.g. /caesar 3 hello")
        return
    try:
        shift = int(parts[0]) # <shift>
    except ValueError:
        respond(f"Shift must be a number, got '{parts[0]}'. Try /caesar 3 hello")
        return

    message = parts[1]
    result = caesar(shift, message)
    respond(result)

@app.command("/rot13")
def handle_rot13(ack, respond, command):
    ack()
    text = command.get("text", "").strip()
    if not text: # "" == false, "text here" == true
        respond("Use: /rot13 <message>  e.g. /rot13 hello")
        return
    result = caesar(13, text)
    respond(result)

@app.command("/base64")
def handle_base64(ack, respond, command):
    ack()
    text = command.get("text", "").strip()
    if not text:
        respond("Use: /base64 <encode/decode> <message> e.g. /base64 encode hello")
        return
    parts = text.split(" ", 1)
    if len(parts) < 2:
        respond("Use: /base64 <encode|decode> <message> e.g. /base64 encode hello")
        return

    action, message = parts[0].lower(), parts[1]
    
    if action == "encode":
        respond(b64_encode(message))
    elif action == "decode":
        try:
            respond(b64_decode(message))
        except Exception:
            respond("Invalid base64. Try /base64 decode aGVsbG8=")
    else:
        respond("Use: /base64 <encode|decode> <message> e.g. /base64 encode hello")


if __name__ == "__main__": # for testing, if it's not running this specific file (__main__, app.py), then it wont handler.start() or else it's never gonna give you up, no i mean, it's going to hang there and not stop
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

