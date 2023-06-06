import string
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from autocorrect import Speller

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')


def case_normalization(text: str):
    return text.lower()


def removing_punctuation(text: str):
    normalized_text = text.translate(str.maketrans("", "", string.punctuation))
    return normalized_text


def removing_stopwords(text: str):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    normalized_text = [word for word in word_tokens if word.casefold() not in stop_words]
    return normalized_text


def lemmatize(text: str):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    normalized_text = [lemmatizer.lemmatize(word) for word in word_tokens]
    return normalized_text


def stemming(text: str):
    stemmer = PorterStemmer()
    word_tokens = word_tokenize(text)
    normalized_text = [stemmer.stem(word) for word in word_tokens]
    return normalized_text


def numerals_dates(text: str):
    text = re.sub(r'\d+', 'NUMERAL', text)
    normalized_text = re.sub(r'\d{4}-\d{2}-\d{2}', 'DATE', text)
    return normalized_text


def spell_checker(text: str):
    spell = Speller()
    corrected_text = spell(text)
    return corrected_text
