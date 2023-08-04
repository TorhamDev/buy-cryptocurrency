import os
import redis


# redis configs
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_DB = os.environ.get("REDIS_DB", 0)


def get_redis_connection():
    """redis database connection"""

    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
