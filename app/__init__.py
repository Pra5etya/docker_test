from flask import Flask
from flask_session import Session
from app.extension import redis_client
from app.routes import main

def create_app():
    app = Flask(__name__)

    # Secret key wajib untuk session
    app.config["SECRET_KEY"] = "super-secret-key"

    # Konfigurasi Flask-Session dengan Redis
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_REDIS"] = redis_client.get_client()
    app.config["SESSION_PERMANENT"] = False

    # Init Redis client
    redis_client.init_app(app)

    # Init Session
    Session(app)

    # Register blueprint
    app.register_blueprint(main)

    return app
