from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from app.Services.ai import generate_response
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

if "__main__" == __name__:
    socketio.run(app, debug=True)