import string
ALPHABET = string.ascii_letters
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
MIN_LOWER = ord('a') # 97
MAX_LOWER = ord("z") # 122
MIN_UPPER = ord("A") # 65
MAX_UPPER = ord("Z") # 90


def rotate(text, key):
    text = list(text)
    result = []
    for letter in text:
        if letter in ALPHABET:
            ascii_value = ord(letter) + key
            if letter in LOWERCASE:
                if ascii_value > MAX_LOWER:
                    letter = MIN_LOWER + (ascii_value - MAX_LOWER) - 1
                else:
                    letter = ascii_value
            elif letter in UPPERCASE: 
                if ascii_value > MAX_UPPER:
                    letter = MIN_UPPER + (ascii_value - MAX_UPPER) - 1
                else:
                    letter = ascii_value
            result.append(chr(letter))
        else:
            result.append(letter)
    return "".join(result)
