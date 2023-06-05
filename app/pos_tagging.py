import nltk

import app.tokenization
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')


def pos_tagging(text):
    context: app.tokenization.Tokenization = app.tokenization.Tokenization(
        strategy=app.tokenization.ByWord())
    tokens = context.execute_strategy(text)
    tagged_tokens = pos_tag(tokens, tagset='universal')
    return tagged_tokens
