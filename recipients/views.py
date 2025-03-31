from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .models import Recipient, RollingPaper
from .serializers import RecipientSerializer, RollingPaperSerializer, RecipientDetailSerializer


class RecipientCreateView(CreateAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RollingPaperCreateView(CreateAPIView):
    queryset = RollingPaper.objects.all()
    serializer_class = RollingPaperSerializer
    permission_classes = [AllowAny]


class RecipientDetailByUUIDView(RetrieveAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "uuid"
