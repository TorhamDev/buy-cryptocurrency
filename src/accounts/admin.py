from django.contrib import admin
from accounts.models import User, Wallet


class WalletInline(admin.TabularInline):
    """wallet inline for user admin"""

    model = Wallet


class UserAdmin(admin.ModelAdmin):
    """User admin class for user model in admin panel"""

    list_display = (
        "id",
        "phone_number",
        "date_joined",
        "is_active",
        "is_staff",
        "update_at",
    )
    search_fields = ("phone_number",)

    list_filter = (
        "is_active",
        "is_staff",
    )
    inlines = [
        WalletInline,
    ]


class WalletAdmin(admin.ModelAdmin):
    """Wallet admin for wallet model in admin panel for showing more data"""

    list_display = (
        "id",
        "user",
        "amount",
        "created_at",
        "update_at",
    )

    search_fields = ("user",)


admin.site.register(User, UserAdmin)
admin.site.register(Wallet, WalletAdmin)
