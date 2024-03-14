from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route("/")
def index():
    return 200


@app.route("/tic-tac-toe")
def tic_tac_toe():
    return 200


@app.route("/quiz")
def quiz():
    return 200


@app.route("/practice")
def practice():
    return 200


@app.route("/login")
def login():
    return 200


@app.route("/signup")
def signup():
    return 200


@app.route("/logout")
def logout():
    return 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
