from django.contrib import admin
from cryptos.models import Crypto


class CryptoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "abbreviation",
        "purchase_price",
        "sale_price",
        "update_at",
    )
    search_fields = (
        "name",
        "abbreviation",
    )

    list_filter = (
        "sale_price",
        "purchase_price",
    )


admin.site.register(Crypto, CryptoAdmin)
