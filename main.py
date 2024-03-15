from flask import Flask, render_template, request, session, redirect
import os, json

app = Flask(__name__)  # Initialize Flask app
app.secret_key = os.urandom(8).hex()  # Set secret key for session management


def check_login():
    try:
        return session["username"]  # Check if user is logged in
    except KeyError:
        return False  # If not logged in, return False


@app.route("/")
def index():
    username = check_login()  # Check login status
    return render_template(
        "index.html", logged_in=username
    )  # Render index.html with login status


@app.route("/tic-tac-toe")
def tic_tac_toe():
    username = check_login()  # Check login status
    if username:
        return render_template(
            "tic-tac-toe.html", logged_in=username
        )  # Render tic-tac-toe.html if logged in
    return redirect("/login")  # Redirect to login page if not logged in


@app.route("/quiz")
def quiz():
    username = check_login()  # Check login status
    if username:
        return render_template(
            "quiz.html", logged_in=username
        )  # Render quiz.html if logged in
    return redirect("/login")  # Redirect to login page if not logged in


@app.route("/practise")
def practise():
    username = check_login()  # Check login status
    if username:
        return render_template(
            "practise.html", logged_in=username
        )  # Render practise.html if logged in
    return redirect("/login")  # Redirect to login page if not logged in


@app.route("/login", methods=["GET", "POST"])
def login():
    error = False
    logged_in = check_login()  # Check login status
    if logged_in:
        return redirect("/")  # Redirect to homepage if already logged in
    if request.method == "POST":
        username = request.form["username"]
        if not os.path.exists(f"users/{username}.json"):  # Check if user exists
            error = True
        else:
            password = request.form["password"]
            with open(f"users/{username}.json", "rb") as file:
                user = json.loads(file.read())  # Load user data
            if password == user["password"]:  # Check password
                session["username"] = username  # Start session
                return redirect("/")  # Redirect to homepage if login successful
            else:
                error = True  # Set error flag if password is incorrect
    return render_template(
        "login.html", login_page=True, error=error
    )  # Render login page with error flag


@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = False
    logged_in = check_login()  # Check login status
    if logged_in:
        return redirect("/")  # Redirect to homepage if already logged in
    if request.method == "POST":
        username = request.form["username"]
        if os.path.exists(f"users/{username}.json"):  # Check if user already exists
            error = True
        else:
            password = request.form["password"]
            user = json.dumps(
                {"username": username, "password": password}
            )  # Create user data
            with open(f"users/{username}.json", "wb") as file:
                file.write(user.encode())  # Write user data to file
                session["username"] = username  # Start session
                return redirect("/")  # Redirect to homepage after successful signup
    return render_template(
        "signup.html", login_page=True, error=error
    )  # Render signup page with error flag


@app.route("/account")
def account():
    user = check_login()  # Check login status
    if user:
        return render_template("account.html")  # Render account page if logged in
    return redirect("/login")  # Redirect to login page if not logged in


@app.route("/help")
def help():
    return render_template("help.html")  # Render help page


@app.route("/logout")
def logout():
    username = check_login()  # Check login status
    if username:
        session.pop("username")  # End session if logged in
    return redirect("/")  # Redirect to homepage after logout


if __name__ == "__main__":
    if not os.path.exists("users"):
        os.mkdir("users")  # Create 'users' directory if it doesn't exist
    app.run(host="127.0.0.1", port=8080, debug=True)  # Run the Flask app
