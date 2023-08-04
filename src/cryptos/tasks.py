from celery import shared_task
from utils.redis_db import get_redis_connection

from cryptos.services import buy_from_exchange, remove_exchanged_buy_records
from cryptos.selectors import calcualte_buy_records_to_exchange

redis_db = get_redis_connection()


@shared_task
def call_exchange():
    """
    Exchanger task. this task is runin every 30s.
    and receives all the events from the Redis database and sends them to the buy_from_exchange
    after success exchange events are removed from Redis.

    check core/celery.py
    """
    buy_records = redis_db.lrange("purchases", 0, -1)
    records_to_exchabge = calcualte_buy_records_to_exchange(buy_records)
    exchange = buy_from_exchange(**records_to_exchabge)
    if exchange:
        remove_exchanged_buy_records(buy_records)
