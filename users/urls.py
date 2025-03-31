from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView

from .views import SignupView, UserDetailView, SameNameRecipientListView, simple_signup_view, custom_login_view


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", custom_login_view, name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),  # 로그아웃
    path("me/", UserDetailView.as_view(), name="me"),  # GET, DELETE
    path('simple-signup/', simple_signup_view, name='simple-signup'),
    path("recommend/", SameNameRecipientListView.as_view(),
         name="same-name-recipients"),
]
