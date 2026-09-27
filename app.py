from dotenv import load_dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from ciphers.caesar import caesar

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

if __name__ == "__main__": # for testing, if it's not running this specific file (__main__, app.py), then it wont handler.start() or else it's never gonna give you up, no i mean, it's going to hang there and not stop
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

