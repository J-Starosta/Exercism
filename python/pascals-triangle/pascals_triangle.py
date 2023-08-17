def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    else:
        triangle = []
        for row in range(1, row_count + 1):
            triangle.append(triangle_row(row))
        return triangle

def triangle_row(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle_row(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row
