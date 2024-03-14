from flask import Flask, render_template, request, session, redirect
import os, json

app = Flask(__name__)
app.secret_key = os.urandom(8).hex()


def check_login():
    try:
        return session["username"]
    except KeyError:
        return False


@app.route("/")
def index():
    username = check_login()
    return render_template("index.html", logged_in=username)


@app.route("/tic-tac-toe")
def tic_tac_toe():
    username = check_login()
    if username:
        return render_template("tic-tac-toe.html", logged_in=username)
    return redirect("/login")


@app.route("/quiz")
def quiz():
    username = check_login()
    if username:
        return render_template("quiz.html", logged_in=username)
    return redirect("/login")


@app.route("/practise")
def practise():
    username = check_login()
    if username:
        return render_template("practise.html", logged_in=username)
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = False
    logged_in = check_login()
    if logged_in:
        return redirect("/")
    if request.method == "POST":
        username = request.form["username"]
        if not os.path.exists(f"users/{username}.json"):
            error = True
        else:
            password = request.form["password"]
            with open(f"users/{username}.json", "rb") as file:
                user = json.loads(file.read())
            print(user["password"])
            if password == user["password"]:
                session["username"] = username
                return redirect("/")
            else:
                error = True
    return render_template("login.html", login_page=True, error=error)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = False
    logged_in = check_login()
    if logged_in:
        return redirect("/")
    if request.method == "POST":
        username = request.form["username"]
        if os.path.exists(f"users/{username}.json"):
            error = True
        else:
            password = request.form["password"]
            user = json.dumps({"username": username, "password": password})
            with open(f"users/{username}.json", "wb") as file:
                file.write(user.encode())
                session["username"] = username
                return redirect("/")
    return render_template("signup.html", login_page=True, error=error)


@app.route("/account")
def account():
    user = check_login()
    if user:
        return render_template("account.html")
    return redirect("/login")


@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/logout")
def logout():
    username = check_login()
    if username:
        session.pop("username")
    return redirect("/")


if __name__ == "__main__":
    if not os.path.exists("users"):
        os.mkdir("users")
    app.run(host="127.0.0.1", port=8080, debug=True)
