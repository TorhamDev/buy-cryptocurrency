from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from utils.exceotions import InsufficientWalletBalance
from cryptos.selectors import calcualte_crypto_price, is_user_balance_enough
from cryptos.services import buy_crypto_for_user


class BuyCryptoAPI(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        crypto_name = serializers.CharField()
        amount = serializers.IntegerField()

    @extend_schema(request=InputSerializer)
    def post(self, request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        crypto_name = serializer.validated_data.get("crypto_name")
        amount = serializer.validated_data.get("amount")

        price_to_buy = calcualte_crypto_price(
            crypto_name=crypto_name,
            amount=amount,
        )

        if is_user_balance_enough(self.request.user, price_to_buy):
            buy_crypto_for_user(
                user=self.request.user,
                crypto_name=crypto_name,
                crypto_amount=amount,
                price_to_buy=price_to_buy,
            )
            return Response({"data": price_to_buy})

        raise InsufficientWalletBalance
