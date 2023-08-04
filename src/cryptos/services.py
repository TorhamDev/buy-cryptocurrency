from utils.redis_db import get_redis_connection
from accounts.models import User

redis_db = get_redis_connection()


def create_buy_record(
    user: User, crypto_name: int, crypto_amount: int, price_to_buy: int
) -> bool | None:
    redis_db = get_redis_connection()
    buy_record = {
        "user": user.pk,
        "crypto_name": crypto_name,
        "crypto_amount": crypto_amount,
        "price_to_buy": price_to_buy,
    }

    return redis_db.rpush("purchases", str(buy_record))


def remove_exchanged_buy_records(buy_records: list[bytes]):
    for record_index in range(len(buy_records)):
        print(redis_db.ltrim("purchases", record_index, record_index))


def buy_from_exchange(**kwargs):
    # sending request to exchanger ....

    return True
