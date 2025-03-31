from django.contrib import admin
from .models import Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birthday", "address", "phone_number")
    search_fields = ("name", "address")
    list_filter = ("birthday",)
