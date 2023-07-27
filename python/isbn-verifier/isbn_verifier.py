MULTIPLIERS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def is_valid(isbn):
    isbn = "".join(filter(str.isalnum, isbn))
    isbn = list(isbn)
    result = 0
    if len(isbn) != 10:
        return False
    first = isbn[:9]
    if not all(ele.isdigit() for ele in first):
        return False
    for index, ele in enumerate(first):
        result = result + MULTIPLIERS[index] * int(ele)
    check_digit = isbn[9]
    if check_digit == "X":
        result = result + MULTIPLIERS[9] * 10
    elif check_digit in "0123456789":
        result = result + MULTIPLIERS[9] * int(check_digit)
    else:
        return False
    
    return result % 11 == 0
        