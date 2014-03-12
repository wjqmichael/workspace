def set_zeroes(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    first_row, first_col = False, False
    for i in matrix[0]:
        if i == 0:
            first_row = True
    for row in matrix:
        if row[0] == 0:
            first_col = True

    for i in xrange(1, len(matrix)):
        for j in xrange(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0], matrix[0][j] = 0, 0

    for i in xrange(1, len(matrix)):
        for j in xrange(1, len(matrix[i])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row:
        for j in xrange(len(matrix[0])):
            matrix[0][j] = 0

    if first_col:
        for i in xrange(len(matrix)):
            matrix[i][0] = 0

    return matrix

def print_matrix(matrix):
    for i in matrix:
        print i

m = [
    [1, 2, 3, 4],
    [5, 6, 7, 0],
    [0, 2, 0, 1],
    [9, 9, 9, 9]
]
print_matrix(set_zeroes(m))