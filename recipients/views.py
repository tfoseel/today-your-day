from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .models import Recipient, RollingPaper
from .serializers import (
    RecipientSerializer,
    RollingPaperSerializer,
    RecipientDetailSerializer,
)

# -----------------------------
# 🔹 REST API Views
# -----------------------------


class RecipientCreateView(CreateAPIView):
    """수신자 등록 API"""
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RollingPaperCreateView(CreateAPIView):
    """롤링페이퍼 등록 API (비회원도 가능)"""
    queryset = RollingPaper.objects.all()
    serializer_class = RollingPaperSerializer
    permission_classes = [AllowAny]


class RecipientDetailByUUIDView(RetrieveAPIView):
    """특정 수신자의 롤링페이퍼 포함 상세 조회 API"""
    queryset = Recipient.objects.all()
    serializer_class = RecipientDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "uuid"

# -----------------------------
# 🔹 HTML Template Views
# -----------------------------


def recipient_invite_view(request, uuid):
    """초대장 랜딩 페이지"""
    recipient = get_object_or_404(Recipient, uuid=uuid)
    return render(request, 'recipients/recipient_invite.html', {
        'recipient': recipient
    })


def write_rollingpaper_view(request, uuid):
    """롤링페이퍼 작성 페이지 (비회원)"""
    recipient = get_object_or_404(Recipient, uuid=uuid)

    if request.method == "POST":
        message = request.POST.get("message", "")
        image = request.FILES.get("image")

        if len(message) > 100:
            return render(request, "recipients/write_rollingpaper.html", {
                "recipient": recipient,
                "error": "메시지는 100자 이하로 작성해주세요."
            })

        RollingPaper.objects.create(
            recipient=recipient,
            message=message,
            image=image
        )
        return redirect("recipient-invite", uuid=recipient.uuid)

    return render(request, "recipients/write_rollingpaper.html", {
        "recipient": recipient
    })


def recipient_rollingpapers_view(request, uuid):
    """수신자가 받은 롤링페이퍼 목록 HTML"""
    recipient = get_object_or_404(Recipient, uuid=uuid)
    rollingpapers = recipient.rollingpapers.all().order_by('-created_at')

    return render(request, "recipients/recipient_rollingpapers_display.html", {
        "recipient": recipient,
        "rollingpapers": rollingpapers
    })
