from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", logged_in=False)


@app.route("/tic-tac-toe")
def tic_tac_toe():
    return render_template("tic-tac-toe.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/practise")
def practise():
    return render_template("practise.html")


@app.route("/login")
def login():
    return 200


@app.route("/signup")
def signup():
    return 200


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/logout")
def logout():
    return 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
