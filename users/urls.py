from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from .views import (
    SignupView,
    UserDetailView,
    SameNameRecipientListView,
    simple_signup_view,
    custom_login_view,
)

urlpatterns = [
    # REST API
    path("signup/", SignupView.as_view(), name="signup"),
    path("me/", UserDetailView.as_view(), name="me"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),

    # HTML Views
    path("login/", custom_login_view, name="login"),
    path("simple-signup/", simple_signup_view, name="simple-signup"),
    path("recommend/", SameNameRecipientListView.as_view(),
         name="same-name-recipients"),
]
