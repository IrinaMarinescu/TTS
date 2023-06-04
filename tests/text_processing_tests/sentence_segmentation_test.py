from app.sentence_segmentation import Sentence_Segmentation_Strategy, Sentence_Segmentation_Library


def _assert_strategy(input_text, expected_result):
    strategy: Sentence_Segmentation_Strategy = Sentence_Segmentation_Library()

    assert strategy.splitting(input_text) == expected_result


def test_one_sentence():
    input_text: str = "This is a text."
    expected_result: list = ["This is a text."]

    _assert_strategy(input_text, expected_result)


def test_multiple_sentences():
    input_text: str = "This is a text. This is another text, that contains some more words. At the end, " \
                      "we have multiple sentences. "
    expected_result: list = ["This is a text.", "This is another text, that contains some more words.",
                             "At the end, we have multiple sentences."]

    _assert_strategy(input_text, expected_result)


def test_multiple_delimiters():
    input_text: str = "This is an interesting text! Care to read it? At the end, this text (the one showed before), " \
                      "is a text. We accentuate the idea of *text*, because, in its sense, it is a \"text\". "
    expected_result: list = ["This is an interesting text!", "Care to read it?",
                             "At the end, this text (the one showed before), is a text.",
                             "We accentuate the idea of *text*, because, in its sense, it is a \"text\"."]

    _assert_strategy(input_text, expected_result)
