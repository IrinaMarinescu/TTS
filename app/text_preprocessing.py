from app.tokenization import Strategy


def preprocess(text: str, strategy: Strategy):
    # split the string into sentences
    # for each sentence apply pos_tagging(it calls tokenization by default)