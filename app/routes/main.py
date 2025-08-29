from flask import render_template, request, session, redirect, url_for
from app.routes import main
from app.extension import redis_client

# Dummy user (contoh, sebaiknya dari DB)
USER_DATA = {"username": "admin", "password": "123"}

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USER_DATA["username"] and password == USER_DATA["password"]:
            session["user"] = username
            return redirect(url_for("main.index"))
        else:
            return "Login gagal!", 401

    return """
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    """

@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))

@main.route("/", methods=["GET", "POST"])
def index():
    r = redis_client.get_client()

    if "user" not in session:
        return redirect(url_for("main.login"))

    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            r.lpush("messages", f"{session['user']}: {msg}")

    messages = r.lrange("messages", 0, 4)
    return render_template("index.html", messages=messages, user=session["user"])
