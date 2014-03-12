def rotate(matrix):
    n = len(matrix)
    for i in xrange(n/2):
        for j in xrange(i, n - 1 - i):
             tmp = matrix[i][j]
             matrix[i][j] = matrix[n - 1 - j][i]
             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
             matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
             matrix[j][n - 1 - i] = tmp
    return matrix

m1 = [
    [1]
]

m2 = [
    [1,2],
    [3,4]
]

m3 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]



print rotate(m1)
print rotate(m2)
print rotate(m3)