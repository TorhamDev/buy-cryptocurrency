from django.urls import path
from accounts.api.register import UserRegisterAPI

urlpatterns = [
    path("register/", UserRegisterAPI.as_view(), name="user-register"),
]
