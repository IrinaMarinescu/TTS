from app.text_preprocessing import Tokenization, ByWord, ByCharacter


def main():
    # Create the context object and set the initial strategy

    context: Tokenization = Tokenization(strategy=ByWord())

    sample_text = "Hahaha Funny App"
    # Execute the strategy
    tokens1 = context.execute_strategy(sample_text)
    print(tokens1)

    # Change the strategy dynamically
    context.strategy = ByCharacter()
    tokens2 = context.execute_strategy(sample_text)
    print(tokens2)


if __name__ == '__main__':
    main()
