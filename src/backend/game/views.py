from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .engine import run_match

class PrisonerMatch(APIView):
    def post(self, request):
        return Response(run_match())
