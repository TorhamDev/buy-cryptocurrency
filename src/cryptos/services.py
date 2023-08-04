from uuid import uuid4

from utils.redis_db import get_redis_connection
from accounts.models import User

redis_db = get_redis_connection()


def buy_crypto_for_user(
    *, user: User, c_name: int, c_amount: int, price: int | float
) -> None:
    """
    decreasing user wallet amount and then create a buy record.
    buy record with be handle with cryptos.tasks.call_exchange task every 30s.
    """
    user.wallet.decreasing_wallet(price)

    buy_record = {
        "record_id": str(uuid4()),
        "user": user.pk,
        "crypto_name": c_name,
        "crypto_amount": c_amount,
        "price_to_buy": price,
    }
    create_buy_record(buy_record)


def create_buy_record(buy_record: dict) -> bool:
    """saving buy record to Redis events list"""
    return redis_db.rpush("purchases", str(buy_record))


def remove_exchanged_buy_records(buy_records: list[bytes]):
    """removeing exchanged events from Redis events list"""
    for record_index in buy_records:
        redis_db.lrem("purchases", 1, record_index)


def buy_from_exchange(**kwargs):
    """Exchanging cryptos..."""

    if kwargs["all_price"] >= 10:
        # sending request to exchanger ....
        return True

    return False
