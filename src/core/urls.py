from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)



document_urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema")),
]

token_urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

api_urlpatterns = [
    path("accounts/", include("accounts.api.urls")),
    path("cryptos/", include("cryptos.api.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", include(token_urlpatterns)),
    path("api/", include(api_urlpatterns)),
]


if settings.DEBUG:
    urlpatterns += document_urlpatterns
