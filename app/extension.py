import redis
from flask import current_app

class RedisClient:
    def __init__(self):
        self.client = None

    def init_app(self, app):
        self.client = redis.Redis(
            host="redis",  # nama service di docker-compose
            port=6379,
            decode_responses=True
        )

    def get_client(self):
        return self.client

redis_client = RedisClient()
