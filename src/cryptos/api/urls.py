from django.urls import path
from cryptos.api.crypto_list import CryptosListAPI
from cryptos.api.crypto_buy import BuyCryptoAPI

urlpatterns = [
    path("", CryptosListAPI.as_view(), name="cryptos-list"),
    path("buy/", BuyCryptoAPI.as_view(), name="crypto-buy"),
]
