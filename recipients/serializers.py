from rest_framework import serializers
from .models import Recipient, RollingPaper


class RollingPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollingPaper
        fields = ['id', 'recipient', 'message', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']


class RollingPaperSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollingPaper
        fields = ['message', 'image', 'created_at']


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['id', 'last_name', 'first_name', 'birthday',
                  'address', 'phone_number', 'uuid', 'music']
        read_only_fields = ['id', 'uuid']


class RecipientDetailSerializer(serializers.ModelSerializer):
    rollingpapers = RollingPaperSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Recipient
        fields = ['last_name', 'first_name',
                  'birthday', 'music', 'rollingpapers']
