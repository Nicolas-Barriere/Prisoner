class BaseStrategy:
    def __init__(self, name):
        self.name = name

    def decide(self, my_history, opponent_history):
        raise NotImplementedError
