"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
PIP = ['2','3','4','5','6','7','8','9','10']
FIGURES = ['J','Q','K']
MAX_VALUE = 21

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in FIGURES:
        return 10
    if card in PIP:
        return int(card)
    if card == "A":
        return 1


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    sum = 0
    
    value_1 = 11 if card_one == "A" else value_of_card(card_one)
    value_2 = 11 if card_two == "A" else value_of_card(card_two)
    total = value_1 + value_2 + 11
    return 1 if total > 21 else 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    value_1 = 11 if card_one == "A" else value_of_card(card_one)
    value_2 = 11 if card_two == "A" else value_of_card(card_two)
    total = value_1 + value_2
    return True if total == 21 else False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if (card_one in FIGURES) and (card_two in FIGURES):
        return True
    elif card_one == card_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    value_1 = 1 if card_one == "A" else value_of_card(card_one)
    value_2 = 1 if card_two == "A" else value_of_card(card_two)
    total = value_1 + value_2
    return True if 9 <= total <=11 else False
