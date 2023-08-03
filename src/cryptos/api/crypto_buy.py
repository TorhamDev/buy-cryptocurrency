from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from utils.exceotions import InsufficientWalletBalance
from cryptos.selectors import calcualte_crypto_price, is_user_balance_enough
from cryptos.services import create_buy_record


class BuyCryptoAPI(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        crypto_id = serializers.IntegerField()
        amount = serializers.IntegerField()

    @extend_schema(request=InputSerializer)
    def post(self, request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        crypto_id = serializer.validated_data.get("crypto_id")
        amount = serializer.validated_data.get("amount")

        price_to_buy = calcualte_crypto_price(
            crypto_id=crypto_id,
            amount=amount,
        )

        if is_user_balance_enough(self.request.user, price_to_buy):
            create_buy_record(
                user=self.request.user,
                crypto_id=crypto_id,
                crypto_amount=amount,
                price_to_buy=price_to_buy,
            )
            return Response({"data": price_to_buy})

        raise InsufficientWalletBalance
