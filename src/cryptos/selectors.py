from cryptos.models import Crypto
from utils.exceotions import InvalidCryptoID
from accounts.models import User
import json


def calcualte_crypto_price(crypto_name: int, amount: int) -> int | float:
    crypto: Crypto = Crypto.objects.filter(name=crypto_name).first()

    if crypto:
        return crypto.purchase_price * amount

    raise InvalidCryptoID


def calcualte_buy_records_to_exchange(buy_records: list[bytes]) -> dict[int, int]:
    records = dict()
    for record in buy_records:
        record = json.loads(record.decode("utf-8").replace("'", '"'))
        crypto = record["crypto_name"]
        crypto_buy_amount = record["crypto_amount"]
        if crypto not in records:
            records[crypto] = crypto_buy_amount
        else:
            records[crypto] += crypto_buy_amount

    return records


def is_user_balance_enough(user: User, amount_to_buy: int) -> bool:
    return user.wallet.amount >= amount_to_buy
