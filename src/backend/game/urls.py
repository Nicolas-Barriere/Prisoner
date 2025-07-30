from django.urls import path
from .views import PrisonerMatch

urlpatterns = [
    path("play/", PrisonerMatch.as_view()),
]
