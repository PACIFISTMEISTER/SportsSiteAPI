from django.urls import path

from administartion.views import (CommandsView,PlayersView,CommandView,PlayerView,BetMatchView,
                                  MatchListView,MatchDetailView)

urlpatterns = [
 path('commands',CommandsView.as_view()),
 path('command/<int:pk>',CommandView.as_view()),
 path('matches',MatchListView.as_view()),
 path('match/<int:pk>',MatchDetailView.as_view()),
 path('match/<int:pk>/bets',BetMatchView.as_view()),
 path('players',PlayersView.as_view()),
 path('player/<int:pk>',PlayerView.as_view()),
]
