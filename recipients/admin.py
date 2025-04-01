from django.contrib import admin
from django.utils.html import format_html
from .models import Recipient, RollingPaper


class RollingPaperInline(admin.TabularInline):
    model = RollingPaper
    extra = 0
    readonly_fields = ("message", "image_preview", "created_at")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;" />',
                obj.image.url
            )
        return "(No Image)"
    image_preview.short_description = "Image Preview"


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "birthday",
                    "address", "phone_number", "uuid", "music")
    search_fields = ("first_name", "last_name",
                     "first_name", "address", "phone_number")
    readonly_fields = ("uuid",)
    inlines = [RollingPaperInline]


@admin.register(RollingPaper)
class RollingPaperAdmin(admin.ModelAdmin):
    list_display = ("id", "recipient", "message_preview",
                    "created_at", "thumbnail")
    search_fields = ("recipient__last_name",
                     "recipient__first_name", "message")
    list_filter = ("created_at",)

    def message_preview(self, obj):
        return obj.message[:20]
    message_preview.short_description = "Message"

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;" />',
                obj.image.url
            )
        return "(No Image)"
    thumbnail.short_description = "Image"
