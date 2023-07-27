def square_of_sum(number):
    sum = 0
    for n in range(1, number + 1):
        sum = sum + n
    return pow(sum, 2)


def sum_of_squares(number):
    sum = 0
    for n in range(1, number + 1):
        sum = sum + pow(n, 2)
    return sum


def difference_of_squares(number):
    return abs(square_of_sum(number) - sum_of_squares(number))
