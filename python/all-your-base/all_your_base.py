def to_base_10(input_base, digits):
    n = len(digits)
    result = 0
    for i, digit in enumerate(reversed(digits)):
        result = result + (digit * pow(input_base, i))
    return result


def to_new_base(base_10, output_base):
    result = []
    dividor = base_10
    division = 1
    while division != 0:
        division = dividor // output_base
        remaining = dividor % output_base
        dividor = division
        result.append(remaining)
    result.reverse()
    return result


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    for digit in digits:
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
    base_10 = to_base_10(input_base, digits)
    result = to_new_base(base_10, output_base)
    return result