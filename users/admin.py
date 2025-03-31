from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nickname",
                    "phone_number", "birthday", "is_active")
    search_fields = ("name", "nickname", "phone_number")
    list_filter = ("is_active",)
