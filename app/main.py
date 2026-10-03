from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from Services.ai import generate_response, get_random_topic
import Services.saving as _SAVE
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY_FALSK")
socketio = SocketIO(app)

_CACHE_ID = 0

@app.route("/", methods=["GET"])
def main_route():
    return render_template("index.html")

@socketio.on("start_debate")
def start_debate(data: dict):
    topic = data.get('topic')

    response = generate_response(topic, "1")
    emit("agent_response", {
        'agent': "agent_1",
        'chunk': response
    })

    response_2 = generate_response(response, "2")
    emit("agent_response", {
        "agent": "agent_2",
        "chunk": response_2
    })

    to_send = str({
        "topic": topic,
        "agent_pro": response,
        "agent_con": response_2,
    })

    response_3 = generate_response(to_send, "3")

    emit("agent_response", {
        "agent": "moderator",
        "chunk": response_3
    })

@socketio.on("generate_random_topic")
def handle_topic_generation():
    emit("generated_topic", {'topic': get_random_topic()})
    
if "__main__" == __name__:
    socketio.run(app, debug=True)