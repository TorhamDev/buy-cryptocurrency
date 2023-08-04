import redis
from django.conf import settings


def get_redis_connection():
    """redis database connection"""

    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
    )
