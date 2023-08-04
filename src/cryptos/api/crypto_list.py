from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from cryptos.models import Crypto


class CryptosListAPI(APIView):
    class CryptosListOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Crypto
            fields = "__all__"

    @extend_schema(responses=CryptosListOutputSerializer)
    def get(self, request):
        cryptos = Crypto.objects.all()
        serializer = self.CryptosListOutputSerializer(
            instance=cryptos,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
