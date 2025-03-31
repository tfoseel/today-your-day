from recipients.models import Recipient
from datetime import date
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from datetime import datetime
from .models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    SignupSerializer,
    UserDetailSerializer,
)


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer


# class LoginView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        request.user.delete()
        return Response({"message": "계정이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


def simple_signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        nickname = request.POST.get("nickname")
        birthday = request.POST.get("birthday")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        # 필수값 확인
        if not all([name, nickname, birthday, password]):
            return render(request, "users/simple_signup.html", {"error": "필수 항목을 모두 입력해 주세요."})

        user = User.objects.create_user(
            name=name,
            nickname=nickname,
            birthday=birthday,
            phone_number=phone_number or None,
            password=password
        )

        return render(request, "users/signup_complete.html", {"user": user})

    return render(request, "users/simple_signup.html")


@method_decorator(login_required, name='dispatch')
class SameNameRecipientListView(TemplateView):
    template_name = "users/same_name_recipients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        user_name = self.request.user.name

        # 이름이 같은 Recipient들 중 생일이 가까운 순 정렬
        same_name_recipients = Recipient.objects.filter(name=user_name)

        sorted_recipients = sorted(
            same_name_recipients,
            key=lambda r: (
                (r.birthday.replace(year=today.year) - today).days
                if r.birthday.replace(year=today.year) >= today
                else (r.birthday.replace(year=today.year + 1) - today).days
            )
        )

        context["recipients"] = sorted_recipients[:3]
        return context


def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("same-name-recipients")
        else:
            return redirect("/api/users/login/?error=true")  # 👈 여기!
    return render(request, "users/login.html")
