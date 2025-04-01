from django.db import models
import uuid


class Recipient(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthday = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    music = models.FileField(
        upload_to='recipient_music/', blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.birthday})"


class RollingPaper(models.Model):
    recipient = models.ForeignKey(
        Recipient, on_delete=models.CASCADE, related_name="rollingpapers")
    message = models.TextField(max_length=100)
    image = models.ImageField(
        upload_to='rollingpaper_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.recipient.first_name} - {self.message[:20]}"
