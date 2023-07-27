def valid_triangle(func):
    def inner(sides):
        return sum(sides) > 2 * max(sides) and func(sides)
    return inner

@valid_triangle      
def equilateral(sides):
    return len(set(sides)) == 1

@valid_triangle
def isosceles(sides):
    return len(set(sides)) < 3

@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3


