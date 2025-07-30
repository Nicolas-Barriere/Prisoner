from .base import BaseStrategy

class AlwaysDefect(BaseStrategy):
    def decide(self, my_history, opponent_history):
        return "D"
