from rest_framework import serializers

from AuthApp.serialziers import UserSerializer
from Tracker.models import Command, Player, Bet
from Tracker.serializer import MatchesSerializer


class CommandSerializer(serializers.ModelSerializer):
    """сериализация информации о команде"""
    class Meta:
        model = Command
        exclude = ('id', 'Wins',)


class CommandName(serializers.ModelSerializer):
    """сериализация имени команды"""
    class Meta:
        model = Command
        fields = ('Name',)


class PlayerForPostSerializer(serializers.ModelSerializer):
    """добавление игрока"""
    class Meta:
        model = Player
        exclude = ('id', 'Earingngs', 'MatchesPlayed')


class BetAdminSerializer(serializers.ModelSerializer):
    """просмотр инофрмации о ставке"""
    user = UserSerializer
    Command = CommandName
    Match = MatchesSerializer

    class Meta:
        model = Bet
        exclude = ('id')


