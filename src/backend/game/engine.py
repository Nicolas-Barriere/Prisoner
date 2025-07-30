class PrisonerGame:
    def __init__(self, players=["GPT", "Mistral"], max_rounds=50):
        self.players = players
        self.max_rounds = max_rounds
        self.round = 0
        self.history = []  # liste de dicts avec p1, p2, s1, s2
        self.scores = {p: 0 for p in players}

    def is_finished(self):
        return self.round >= self.max_rounds

    def add_round(self, p1_move, p2_move):
        s1, s2 = get_score(p1_move, p2_move)
        print(s1, s2)
        self.history.append({
            "p1": p1_move,
            "p2": p2_move,
            "s1": s1,
            "s2": s2
        })
        self.scores[self.players[0]] += s1
        self.scores[self.players[1]] += s2
        self.round += 1

def get_score(p1, p2):
    if p1 == "C" and p2 == "C":
        return 3, 3
    elif p1 == "C" and p2 == "D":
        return 0, 5
    elif p1 == "D" and p2 == "C":
        return 5, 0
    else:
        return 1, 1
