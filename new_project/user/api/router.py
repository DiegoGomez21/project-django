from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter, SimpleRouter


urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]

# Forma dos, No se pudo
# router_user = DefaultRouter()
# router_user.register(prefix='auth/login', basename='token_obtain_pair', viewset=TokenObtainPairView)
# router_user.register(prefix='auth/token/refresh', basename='token_refresh', viewset=TokenRefreshView)