def is_paired(input_string):
    opened = "[{("
    closed = "]})"
    stack = []
    for index, element in enumerate(input_string):
        if element in opened:
            stack.append(element)
        elif element in closed:
            if not stack or (opened[closed.index(element)] != stack.pop()):
                return False
    return not stack
