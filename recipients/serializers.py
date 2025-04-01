from rest_framework import serializers
from .models import Recipient, RollingPaper


class RecipientSerializer(serializers.ModelSerializer):
    """Recipient 생성 및 기본 조회용 Serializer"""
    class Meta:
        model = Recipient
        fields = ['id', 'name', 'birthday', 'address', 'phone_number', 'uuid']
        read_only_fields = ['id', 'uuid']


class RollingPaperSerializer(serializers.ModelSerializer):
    """롤링페이퍼 생성 및 상세 조회용 Serializer"""
    class Meta:
        model = RollingPaper
        fields = ['id', 'recipient', 'message', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']


class RollingPaperSimpleSerializer(serializers.ModelSerializer):
    """Recipient 상세 조회 시 포함되는 간단한 롤링페이퍼 정보"""
    class Meta:
        model = RollingPaper
        fields = ['message', 'image', 'created_at']


class RecipientDetailSerializer(serializers.ModelSerializer):
    """Recipient + 연결된 롤링페이퍼 간단 요약"""
    rollingpapers = RollingPaperSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Recipient
        fields = ['name', 'birthday', 'rollingpapers']
