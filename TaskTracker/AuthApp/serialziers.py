from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Moderator
from .token import GetToken


class CreateUser(serializers.Serializer):
    """сериализация нового пользоателя/возвращение токена"""
    username = serializers.CharField()
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise ValidationError("passwords must be same")
        return attrs

    def create(self, validated_data):
        password=make_password(validated_data['password'])
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )
        user.save()
        self.token, self.refresh_token = GetToken(user)
        return user

    def to_representation(self, instance):
        rep = super(CreateUser, self).to_representation(instance)

        rep['token'] = self.token
        rep['refresh_token'] = self.refresh_token

        return rep


class UserSerializer(serializers.ModelSerializer):
    """возвращение информации о пользователе"""
    class Meta:
        model = User
        fields=('username','email')
