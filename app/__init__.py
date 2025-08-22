from flask import Flask
from .extension import redis_client

def create_app():
    app = Flask(__name__)

    # init redis client
    redis_client.init_app(app)

    # register blueprints
    from .routes.main import main
    app.register_blueprint(main)

    return app
