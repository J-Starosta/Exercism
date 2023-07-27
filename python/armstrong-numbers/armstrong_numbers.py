def is_armstrong_number(number):
    number_str = str(number)
    n = len(number_str)
    sum = 0
    for digit in number_str:
        sum = sum + pow(int(digit), n)
    if sum == number:
        return True
    else:
        return False
    
