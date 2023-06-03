import nltk
from nltk.tokenize import word_tokenize


class Tokenization:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, text):
        self.strategy.execute(text)


class Strategy:
    def execute(self, text):
        raise NotImplementedError("Subclasses must implement execute()")


class ByCharacter(Strategy):
    def execute(self, text):
        return list(text)


class ByWord(Strategy):
    def execute(self, text):
        return word_tokenize(text)
