from django.contrib import admin
from accounts.models import User, Wallet


class WalletInline(admin.TabularInline):
    model = Wallet


class UserAdmin(admin.ModelAdmin):
    list_display = (
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
    list_display = (
        "user",
        "amount",
        "created_at",
        "update_at",
    )

    search_fields = ("user",)


admin.site.register(User, UserAdmin)
admin.site.register(Wallet, WalletAdmin)
