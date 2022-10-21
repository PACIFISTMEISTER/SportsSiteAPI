from django.urls import path, include
from .views import CommandsView, CommandView, MatchView, MatchesView, PostBet,PlayerList,PlayerDetail

urlpatterns = [
    path('commands',CommandsView.as_view()),
    path('players',PlayerList.as_view()),
    path('player/<int:pk>',PlayerDetail.as_view()),
    path('command/<int:pk>',CommandView.as_view()),
    path('match/<int:pk>',MatchView.as_view()),
    path('match/<int:pk>/bet',PostBet.as_view()),
    path('matches',MatchesView.as_view()),
    path('admin/',include('administartion.urls'))
]

