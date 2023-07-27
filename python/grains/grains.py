NUMBER_OF_SQUARES = 64

def square(number):
    if 1 <= number <= 64:
        power = number - 1
        return pow(2, power)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    grains_sum = 0
    for i in range(1,65):
        grains_sum = grains_sum + square(i)
    return grains_sum
