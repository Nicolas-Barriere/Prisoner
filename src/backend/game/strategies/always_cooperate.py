from .base import BaseStrategy

class AlwaysCooperate(BaseStrategy):
    def decide(self, my_history, opponent_history):
        return "C"
