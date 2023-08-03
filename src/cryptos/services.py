from utils.redis_db import get_redis_connection
from accounts.models import User


def create_buy_record(
    user: User, crypto_id: int, crypto_amount: int, price_to_buy: int
) -> bool | None:
    redis_db = get_redis_connection()
    buy_record = {
        "crypto_id": crypto_id,
        "crypto_amount": crypto_amount,
        "price_to_buy": price_to_buy,
    }

    return redis_db.set(user.pk, str(buy_record))
