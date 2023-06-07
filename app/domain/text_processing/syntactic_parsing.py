import nltk

from app.domain.text_processing.text_preprocessing import Tokenization
from nltk import pos_tag, word_tokenize, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


class Sentence_Processed_Tagged:
    def __init__(self, text_tagged: list):
        self._word_list: list = []
        self._syntax_list: list = []

        for tuple_word in text_tagged:
            self._word_list.append(tuple_word[0])
            self._syntax_list.append(tuple_word[1])

    def get_word_list(self) -> list:
        return self._word_list

    def get_syntax_list(self) -> list:
        return self._syntax_list


class Syntactic_Parsing:
    def __init__(self, tokenization_strategy: Tokenization):
        self.tokenization_strategy = tokenization_strategy

    def process_syntactic_sentence(self, input_text: str) -> Sentence_Processed_Tagged:
        tokens = self.tokenization_strategy.execute_strategy(input_text)

        text_tagged = pos_tag(tokens)

        return Sentence_Processed_Tagged(text_tagged)
