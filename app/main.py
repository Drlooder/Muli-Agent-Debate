from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from LLM.ai import generate_response
import Services.saving as _SAVE

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret!"
socketIo = SocketIO(app)

_CACHE_ID = 0

@app.route("/", methods=["GET"])
def main_route():
    return render_template("main.html")

@socketIo.on("send_prompt")
def handle_prompt(data):
    global _CACHE_ID
    prompt = data.get("prompt")

    response = generate_response(prompt)

    if _CACHE_ID > 0:
        _SAVE.add_message_to_cache(_CACHE_ID, response)
    else:
        id = _SAVE.save_cache(response)
        _CACHE_ID = id

    emit("prompt_response", {
        "status": "success",
        "submitted_prompt": prompt,
        "generated_response": response
    })

@socketIo.on("new_session")
def handle_sessions(data):
    _CACHE_ID = 0

    emit("new_session_response", {
        "status": "success",
    })

if "__main__" == __name__:
    socketIo.run(app, debug=True)