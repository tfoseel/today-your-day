from rest_framework import serializers
from .models import Recipient, RollingPaper


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['id', 'name', 'birthday', 'address', 'phone_number']
        read_only_fields = ['id']


class RollingPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollingPaper
        fields = ['id', 'recipient', 'message', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']


class RollingPaperSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollingPaper
        fields = ['message', 'image', 'created_at']


class RecipientDetailSerializer(serializers.ModelSerializer):
    rollingpapers = RollingPaperSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Recipient
        fields = ['name', 'birthday', 'rollingpapers']
