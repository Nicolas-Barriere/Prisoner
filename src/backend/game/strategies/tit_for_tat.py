from .base import BaseStrategy

class TitForTat(BaseStrategy):
    def decide(self, my_history, opponent_history):
        if not opponent_history:
            return "C"
        return opponent_history[-1]
