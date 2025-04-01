from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from .views import (
    signup_view,
    login_view,
    UserDetailView,
    HomeView,
)

urlpatterns = [
    # REST API
    path("me/", UserDetailView.as_view(), name="me"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),

    # HTML Views
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("home/", HomeView.as_view(),
         name="home"),
]
