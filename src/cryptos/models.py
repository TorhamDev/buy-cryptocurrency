from django.db import models
from utils.models import BaseModel


class Crypto(BaseModel):
    """
    This model store the information of cryptocurrencies.
    these cryptocurrencies are sellable
    """

    name = models.CharField("Crypto name", max_length=50)
    abbreviation = models.CharField("Crypto name abbreviation", max_length=20)
    purchase_price = models.BigIntegerField("Crypto purchase price")
    sale_price = models.BigIntegerField("Crypto sales price")
    logo = models.ImageField("Crypto logo", null=True, blank=True)

    created_at = models.DateTimeField(("date joined"), auto_now_add=True)
    update_at = models.DateTimeField(("update date"), auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.abbreviation}"
