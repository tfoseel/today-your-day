from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nickname",
                    "birthday", "phone_number")
    search_fields = ("name", "nickname", "phone_number")
    readonly_fields = ()
