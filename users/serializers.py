from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "nickname",
                  "phone_number", "birthday", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # SimpleJWT는 기본적으로 'username' 필드를 통해 인증하므로 phone_number로 맵핑
        attrs["username"] = attrs.get("phone_number")
        return super().validate(attrs)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["last_name", "first_name",
                  "nickname", "phone_number", "birthday"]
