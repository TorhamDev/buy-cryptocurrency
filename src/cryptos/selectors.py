from cryptos.models import Crypto
from utils.exceotions import InvalidCryptoID
from accounts.models import User


def calcualte_crypto_price(crypto_id: int, amount: int) -> int | float:
    crypto: Crypto = Crypto.objects.filter(id=crypto_id).first()

    if crypto:
        return crypto.purchase_price * amount

    raise InvalidCryptoID


def is_user_balance_enough(user: User, amount_to_buy: int) -> bool:
    return user.wallet.amount >= amount_to_buy
