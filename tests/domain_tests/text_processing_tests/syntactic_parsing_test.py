from app.domain.text_processing.syntactic_parsing import Syntactic_Parsing
from app.domain.text_processing.text_preprocessing import Tokenization, ByWord


def test_one_simple_sentence():
    tokenization_strategy: Tokenization = Tokenization(ByWord())
    parser: Syntactic_Parsing = Syntactic_Parsing(tokenization_strategy)

    input_text = "This is an example."

    expected_syntax: list = ['DT', 'VBZ', 'DT', 'NN']

    assert parser.process_syntactic_sentence(input_text).get_syntax_list() == expected_syntax


def test_one_complex_sentence():
    tokenization_strategy: Tokenization = Tokenization(ByWord())
    parser: Syntactic_Parsing = Syntactic_Parsing(tokenization_strategy)

    input_text = "This is a complex sentence, which provides more insight on the structure and evolution of the normal, " \
                 "simple sentence."

    expected_syntax: list = ['DT', 'VBZ', 'DT', 'JJ', 'NN', 'WDT', 'VBZ', 'JJR', 'NN', 'IN', 'DT', 'NN', 'CC',
                             'NN', 'IN', 'DT', 'JJ', 'NN', 'NN']

    assert parser.process_syntactic_sentence(input_text).get_syntax_list() == expected_syntax
