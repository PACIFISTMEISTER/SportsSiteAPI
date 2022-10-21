from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Moderator


class MyToken(TokenObtainPairSerializer):
    """кастомный токен,с зашитой инофрмацией о статусе пользователя, пока не решил зачем, но пусть будет"""
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        if Moderator.objects.filter(user=user).exists():
            token['isModerator'] = True
        else:
            token['isModerator'] = False

        return token


def GetToken(user: User):
    """генерация токена"""
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token)
