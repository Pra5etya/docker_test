from flask import Blueprint, render_template, request
from ..extension import redis_client

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    r = redis_client.get_client()

    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            r.lpush("messages", msg)

    messages = r.lrange("messages", 0, 4)
    return render_template("index.html", messages=messages)
