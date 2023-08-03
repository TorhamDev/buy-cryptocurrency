from cryptos.models import Crypto
from utils.exceotions import InvalidCryptoID


def calcualte_crypto_price(crypto_id: int, amount: int) -> int | float:
    crypto: Crypto = Crypto.objects.filter(id=crypto_id).first()

    if crypto:
        return crypto.purchase_price * amount

    raise InvalidCryptoID
