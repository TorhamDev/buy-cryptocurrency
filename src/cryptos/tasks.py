from celery import shared_task
from utils.redis_db import get_redis_connection
from random import randint

redis_db = get_redis_connection()


@shared_task
def sleepy():
    redis_db.set("random", randint(1, 50))
    redis_db.expire("random", 20)
