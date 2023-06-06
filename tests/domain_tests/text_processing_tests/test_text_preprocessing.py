from unittest import TestCase

from app.domain.text_processing.text_preprocessing import Tokenization, ByWord, ByCharacter


class TestTextPreprocessing(TestCase):

    def test_ByWord(self):
        context: Tokenization = Tokenization(strategy=ByWord())
        sample_text = "Hahaha Funny App"
        result = context.execute_strategy(sample_text)
        self.assertEqual(result, ['Hahaha', 'Funny', 'App'])

    def test_ByCharacter(self):
        context: Tokenization = Tokenization(strategy=ByCharacter())
        sample_text = "Hahaha Funny App"
        result = context.execute_strategy(sample_text)
        self.assertEqual(result, ['H', 'a', 'h', 'a', 'h', 'a', ' ', 'F', 'u', 'n', 'n', 'y', ' ', 'A', 'p', 'p'])
