from unittest import TestCase

from app.domain.text_processing.text_normalization import removing_punctuation, case_normalization, removing_stopwords, \
    lemmatize, stemming


class Test(TestCase):

    def test_removing_punctuation_basic(self):
        text = "Hello, World!"
        expected_output = "Hello World"
        assert removing_punctuation(text) == expected_output, "Test failed"

    def test_removing_punctuation_empty(self):
        text = ""
        expected_output = ""
        assert removing_punctuation(text) == expected_output, "Test failed"

    def test_case_normalization_basic(self):
        text = "Hello, World!"
        expected_output = "hello, world!"
        assert case_normalization(text) == expected_output, "Test failed"

    def test_case_normalization_empty(self):
        text = ""
        expected_output = ""
        assert case_normalization(text) == expected_output, "Test failed"

    def test_removing_stopwords_basic(self):
        text = "This is a sample sentence with some stopwords."
        expected_output = ["sample", "sentence", "stopwords", "."]
        assert removing_stopwords(text) == expected_output, "Test failed"

    def test_removing_stopwords_empty(self):
        text = ""
        expected_output = []
        assert removing_stopwords(text) == expected_output, "Test failed"

    def test_lemmatize_basic(self):
        text = "He was running and eating at the same time. He has bad habit of swimming after playing long hours in " \
               "the Sun. "
        expected_output = ["He", "wa", "running", "and", "eating", "at", "the", "same", "time", ".", "He", "ha", "bad",
                           "habit", "of", "swimming", "after", "playing", "long", "hour", "in", "the", "Sun", "."]
        assert lemmatize(text) == expected_output, "Test failed"

    def test_lemmatize_empty(self):
        text = ""
        expected_output = []
        assert lemmatize(text) == expected_output, "Test failed"

    def test_stemming_basic(self):
        text = "I am running and eating at the same time. I have a bad habit of swimming after playing for long hours " \
               "in the Sun. "
        expected_output = ["i", "am", "run", "and", "eat", "at", "the", "same", "time", ".", "i", "have", "a", "bad",
                           "habit", "of", "swim", "after", "play", "for", "long", "hour", "in", "the", "sun", "."]
        assert stemming(text) == expected_output, "Test failed"

    def test_stemming_empty(self):
        text = ""
        expected_output = []
        assert stemming(text) == expected_output, "Test failed"



