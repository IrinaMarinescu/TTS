class Strategy:
    def execute(self, text):
        raise NotImplementedError("Subclasses must implement execute()")


class ByCharacter(Strategy):
    def execute(self, input_text: str):
        return list(input_text)


class ByWord(Strategy):
    def execute(self, input_text: str):
        return input_text.split()


class Tokenization:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, input_text: str):
        return self.strategy.execute(input_text)

