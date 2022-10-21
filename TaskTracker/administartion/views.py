from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.permissions import IsAdminUser

from AuthApp.Permisions import IsModerator
from Tracker.models import Command, Player, Bet, Match
from Tracker.serializer import PlayerSerialzier, CommandListSerializer, MatchesSerializer, MatchSerializer
from administartion.serializers import CommandSerializer, PlayerForPostSerializer, BetAdminSerializer


class CommandsView(generics.ListCreateAPIView):
    """вывод информации о командах и возможность добавления"""
    serializer_class = CommandListSerializer
    queryset = Command.objects.all()
    permission_classes = (IsModerator,)


class PlayersView(generics.ListCreateAPIView):
    """вывод информации о игроках и возможность добавления"""
    serializer_class = PlayerSerialzier
    queryset = Player.objects.all()
    permission_classes = (IsModerator,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PlayerForPostSerializer
        else:
            return PlayerSerialzier


class CommandView(generics.RetrieveUpdateDestroyAPIView):
    """вывод информации о команде и возможность изменения"""
    serializer_class = CommandSerializer
    queryset = Command.objects.all()
    permission_classes = (IsModerator,)


class PlayerView(generics.RetrieveUpdateDestroyAPIView):
    """вывод информации о игроке и возможность изменения"""
    serializer_class = PlayerSerialzier
    queryset = Player.objects.all()
    permission_classes = (IsModerator,)


class BetMatchView(generics.ListAPIView):
    """вывод информации о ставке """
    serializer_class = BetAdminSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return Bet.objects.filter(Match=Match.objects.get(self.lookup_url_kwarg))


class MatchListView(generics.ListCreateAPIView):
    """вывод информации о матчах и возможность добавления"""
    serializer_class = MatchesSerializer
    queryset = Match.objects.all()

class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    """вывод информации о матче и возможность изменения"""
    serializer_class = MatchSerializer
    queryset = Match.objects.all()

