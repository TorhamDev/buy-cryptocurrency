from json import loads as json_loads

from cryptos.models import Crypto
from utils.exceptions import InvalidCryptoID
from accounts.models import User


def calcualte_crypto_price(crypto_name: int, amount: int) -> int | float:
    """
    calculating how much user must pay for this cryptos.

    param : crypto_name : name of cryptos user wants to buy
    param : amount : number of how musch user want buy from this crypto

    retrun : calcualted price
    """
    crypto: Crypto = Crypto.objects.filter(name=crypto_name).first()

    if crypto:
        return crypto.purchase_price * amount

    raise InvalidCryptoID


def calcualte_buy_records_to_exchange(buy_records: list[bytes]) -> dict[int, int]:
    """
    calcualte all users buy event for sending to exchanger.

    exmaple:
        *if every crypto price is 2 USD
        input:
            {"tether":2, "tether":1, "ABAN":5}
        retrun :
            {"tether":3, "ABAN":5, "all_prices":16}
    """
    records = {"all_prices": 0}
    for record in buy_records:
        record = json_loads(record.decode("utf-8").replace("'", '"'))
        crypto = record["crypto_name"]
        crypto_buy_amount = record["crypto_amount"]
        if crypto not in records:
            records[crypto] = crypto_buy_amount
        else:
            records[crypto] += crypto_buy_amount
        records["all_prices"] += record["price_to_buy"]

    return records


def is_user_balance_enough(user: User, amount_to_buy: int | float) -> bool:
    """user have enough money?!"""
    return user.wallet.amount >= amount_to_buy
