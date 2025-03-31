from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "nickname", "phone_number", "birthday", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # phone_number -> username 필드로 옮겨 SimpleJWT가 인식하게끔
        attrs["username"] = attrs.get("phone_number")
        return super().validate(attrs)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "nickname", "phone_number", "birthday")
