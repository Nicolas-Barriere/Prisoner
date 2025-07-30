from .engine import PrisonerGame

GAMES = {}

def create_game(game_id: str):
    GAMES[game_id] = PrisonerGame()

def get_game(game_id: str):
    return GAMES.get(game_id)
