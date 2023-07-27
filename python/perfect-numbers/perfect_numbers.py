def isprime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    else:
        return True


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    divisors = []
    if number > 0:
        for n in range(1, number):
            if number % n == 0:
                divisors.append(n)
        s = sum(divisors)
        if s == number:
            return "perfect"
        elif s > number:
            return "abundant"
        elif isprime(s):
            return "deficient"
    else:
        raise ValueError("Classification is only possible for positive integers.")