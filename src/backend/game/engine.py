from .strategies.always_cooperate import AlwaysCooperate
from .strategies.tit_for_tat import TitForTat

SCORES = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1)
}

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.history = []
        self.score = 0

    def play(self, opponent_history):
        action = self.strategy.decide(self.history, opponent_history)
        self.history.append(action)
        return action

def run_match(rounds=50):
    p1 = Player(AlwaysCooperate("GPT"))
    p2 = Player(TitForTat("Claude"))

    round_results = []
    for _ in range(rounds):
        a1 = p1.play(p2.history)
        a2 = p2.play(p1.history)
        s1, s2 = SCORES[(a1, a2)]
        p1.score += s1
        p2.score += s2
        round_results.append({"p1": a1, "p2": a2, "s1": s1, "s2": s2})

    return {
        "players": [p1.strategy.name, p2.strategy.name],
        "rounds": round_results,
        "score": {
            p1.strategy.name: p1.score,
            p2.strategy.name: p2.score,
        }
    }
