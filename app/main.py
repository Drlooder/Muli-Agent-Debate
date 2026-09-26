from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main.html")


if "__main__" == __name__:
    app.run(debug=True)