from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main.html")

@app.route("/start", methods=["POST"])
def start():
    prompt = request.form.get('Prompt')

    print(prompt)
    return render_template("main.html", status="Success", submitted_prompt=prompt)

if "__main__" == __name__:
    app.run(debug=True)