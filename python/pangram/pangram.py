import string

ALPHABET = list(string.ascii_lowercase)


def is_pangram(sentence):
    sentence = ''.join(filter(str.isalpha, sentence))
    sentence = sorted(set(sentence.lower()))
    if sentence == ALPHABET:
        return True
    return False
