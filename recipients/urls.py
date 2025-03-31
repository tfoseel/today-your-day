from django.urls import path
from .views import RecipientCreateView, RollingPaperCreateView, RecipientDetailByUUIDView

urlpatterns = [
    path("", RecipientCreateView.as_view(), name="recipient-create"),
    path("rollingpapers/", RollingPaperCreateView.as_view(),
         name="rollingpaper-create"),
    path("<uuid:uuid>/", RecipientDetailByUUIDView.as_view(),
         name="recipient-detail-by-uuid"),
]
