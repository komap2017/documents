import nltk
import os
import string


def _get_marker_words():
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, '_trust')
    words = []
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            words.append(line.strip())
    return set(words)


_MARKER = _get_marker_words()


def _search_over(word):
    return word in _MARKER


def get_names(text):
    stopwords = set(nltk.corpus.stopwords.words('russian'))
    tokens = nltk.word_tokenize(text.lower())
    all_stops = stopwords | set(string.punctuation)
    cleared = [el for el in tokens if el not in all_stops]
    i = 0
    for i, word in enumerate(cleared):
        if _search_over(word):
            i += 1
            break
    after = cleared[i:i + 3]
    after = [el.capitalize() for el in after]
    return after
