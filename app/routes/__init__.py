from flask import Blueprint

main = Blueprint("main", __name__)

from app.routes import main  # import route dari main.py
