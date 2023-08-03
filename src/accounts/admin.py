from django.contrib import admin
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "date_joined", "is_active", "is_staff", "update_at")
    search_fields = ("phone_number",)

    list_filter = (
        "is_active",
        "is_staff",
    )


admin.site.register(User, UserAdmin)
