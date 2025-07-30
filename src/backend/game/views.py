from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .engine import get_score
from .game_store import create_game, get_game
from .ai import gpt_decision, mistral_decision
import uuid
import asyncio

class NewGame(APIView):
    def post(self, request):
        game_id = str(uuid.uuid4())
        create_game(game_id)
        return Response({"game_id": game_id})

class NextRound(APIView):
    def post(self, request):
        game_id = request.data.get("game_id")
        game = get_game(game_id)

        if not game:
            return Response({"error": "Invalid game_id"}, status=status.HTTP_404_NOT_FOUND)
        if game.is_finished():
            return Response({"error": "Game finished"}, status=status.HTTP_400_BAD_REQUEST)

        history = [r["p1"] for r in game.history]

        p1_move = gpt_decision(history)
        p2_move = mistral_decision(history)

        game.add_round(p1_move, p2_move)

        return Response({
            "round": game.round,
            "p1": p1_move,
            "p2": p2_move,
            "scores": game.scores,
            "history": game.history,
            "finished": game.is_finished()
        })
