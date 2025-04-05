from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def redirect_to_login(request):
    return redirect('login')  # 'login'이라는 name의 URL로 이동


urlpatterns = [
    path('', redirect_to_login),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("recipients/", include("recipients.urls"))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
