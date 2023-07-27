# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    points = 0
    if category == YACHT:
        if len(set(dice)) == 1:
            points = 50
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        points = dice.count(category) * category
    if category == FULL_HOUSE:
        max_occ = max(dice, key=dice.count)
        min_occ = min(dice, key=dice.count)
        if (len(set(dice)) == 2) and (dice.count(max_occ) == 3) and (dice.count(min_occ) == 2):
            points = sum(dice)
    if category == FOUR_OF_A_KIND:
        occ = max(dice, key=dice.count)
        if dice.count(occ) >= 4:
            points = occ * 4
    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1,2,3,4,5]:
            points = 30
    if category == BIG_STRAIGHT:
        if sorted(dice) == [2,3,4,5,6]:
            points = 30
    if category == CHOICE:
        points = sum(dice)
    return points