from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,    # 로그인
    TokenBlacklistView      # 로그아웃 (refresh 블랙리스트)
)

from .views import SignupView, UserDetailView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),  # 로그아웃
    path("me/", UserDetailView.as_view(), name="me"),  # GET, DELETE
]
