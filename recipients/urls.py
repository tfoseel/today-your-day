from django.urls import path
from .views import (
    RecipientCreateView,
    RollingPaperCreateView,
    RecipientDetailByUUIDView,
    recipient_invite_view,
    write_rollingpaper_view,
    recipient_rollingpapers_view,
)

urlpatterns = [
    path("", RecipientCreateView.as_view(), name="recipient-create"),
    path("rollingpapers/", RollingPaperCreateView.as_view(),
         name="rollingpaper-create"),

    path("<uuid:uuid>/", RecipientDetailByUUIDView.as_view(),
         name="recipient-detail-by-uuid"),
    path("<uuid:uuid>/invite/", recipient_invite_view, name="recipient-invite"),
    path("<uuid:uuid>/write/", write_rollingpaper_view, name="write-rollingpaper"),
    path("<uuid:uuid>/papers/", recipient_rollingpapers_view,
         name="recipient-rollingpapers"),
]
