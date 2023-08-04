from utils.redis_db import get_redis_connection
from accounts.models import User

redis_db = get_redis_connection()


def buy_crypto_for_user(*, user: User, c_name: int, c_amount: int, price: int) -> bool:

    user.wallet.decreasing_wallet(price)

    buy_record = {
        "user": user.pk,
        "crypto_name": c_name,
        "crypto_amount": c_amount,
        "price_to_buy": price,
    }
    create_buy_record(buy_record)


def create_buy_record(buy_record: dict) -> bool:
    return redis_db.rpush("purchases", str(buy_record))


def remove_exchanged_buy_records(buy_records: list[bytes]):
    for record_index in range(len(buy_records)):
        redis_db.ltrim("purchases", record_index, record_index)


def buy_from_exchange(**kwargs):
    # sending request to exchanger ....

    return True
