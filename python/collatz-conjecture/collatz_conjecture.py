def steps(number):
    if number > 0:
        counter = 0
        while number > 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1
            counter = counter + 1
    else:
        raise ValueError("Only positive integers are allowed")
        
    return counter
