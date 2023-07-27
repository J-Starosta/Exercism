import math

def score(x, y):
    z = math.sqrt(pow(x,2) + pow(y,2))
    if z > 10:
        return 0
    if z <= 1:
        return 10
    if z <= 5:
        return 5
    else:
        return 1
        