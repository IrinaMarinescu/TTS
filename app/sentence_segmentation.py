from nltk.tokenize import sent_tokenize


class Sentence_Segmentation_Strategy:
    def splitting(self, text: str) -> list:
        return NotImplemented


class Sentence_Segmentation_Library(Sentence_Segmentation_Strategy):
    def splitting(self, text: str) -> list:
        return sent_tokenize(text=text)
    