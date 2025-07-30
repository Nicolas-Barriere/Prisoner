from django.urls import path
from .views import NewGame, NextRound

urlpatterns = [
    path("new_game/", NewGame.as_view()),
    path("next_round/", NextRound.as_view()),
]