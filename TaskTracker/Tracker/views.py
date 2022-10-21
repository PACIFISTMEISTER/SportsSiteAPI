from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Command, Match, Bet, Player
from .serializer import (CommandListSerializer, CommandSerialzer,
                         MatchSerializer, MatchesSerializer,
                         CreateBet, BetSerializer, PlayerSerialzier)


class CommandsView(generics.ListAPIView):
    """информация о командах"""
    queryset = Command.objects.all()
    serializer_class = CommandListSerializer


class CommandView(generics.RetrieveAPIView):
    """инофрмация о команде"""
    queryset = Command.objects.all()
    serializer_class = CommandSerialzer


class MatchView(generics.RetrieveAPIView):
    """информация о матче"""
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchesView(generics.ListAPIView):
    """информация о матчах"""
    queryset = Match.objects.all()
    serializer_class = MatchesSerializer




class PostBet(CreateAPIView):
    """ставка"""
    serializer_class = BetSerializer
    queryset = Bet.objects.all()
    permission_classes = (IsAuthenticated,)

    # serializer_class = CreateBet
    # queryset = Bet.objects.all()
    #
    # def perform_create(self, serializer):
    #     return serializer.save()
    #
    # def create(self, request, *args, **kwargs):
    #     self.perform_create(self.serializer_class)
    #     return Response(status=201)


class PlayerList(generics.ListAPIView):
    """информация о игроках"""
    serializer_class = PlayerSerialzier
    queryset = Player.objects.all()


class PlayerDetail(generics.RetrieveAPIView):
    """инофрмация о игроке"""
    serializer_class = PlayerSerialzier
    queryset = Player.objects.all()
