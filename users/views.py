from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserDetailSerializer
from recipients.models import Recipient


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        request.user.delete()
        return Response({"message": "계정이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


def signup_view(request):
    if request.method == "POST":
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        nickname = request.POST.get("nickname")
        birthday = request.POST.get("birthday")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        # 하이픈 제거
        clean_phone = phone_number.replace("-", "") if phone_number else None

        if not all([last_name, first_name, nickname, birthday, password]):
            return render(request, "users/signup.html", {
                "error": "필수 항목을 모두 입력해 주세요."
            })

        user = User.objects.create_user(
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            birthday=birthday,
            phone_number=clean_phone,
            password=password
        )

        login(request, user)
        messages.success(request, f"{user.nickname}님, 가입을 축하합니다!")
        return redirect("home")

    return render(request, "users/signup.html")


def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("username")
        password = request.POST.get("password")

        # 하이픈 제거
        clean_phone = phone.replace("-", "") if phone else ""

        user = authenticate(request, username=clean_phone, password=password)

        if user:
            login(request, user)
            return redirect("home")

        # ⛔ 로그인 실패 시 에러 메시지 포함
        return render(request, "users/login.html", {
            "error": "전화번호 또는 비밀번호가 올바르지 않습니다."
        })

    return render(request, "users/login.html")


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "users/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()

        same_name_recipients = Recipient.objects.filter(
            first_name=self.request.user.first_name)
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
