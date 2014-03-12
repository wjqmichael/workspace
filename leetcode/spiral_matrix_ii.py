def generateMatrix(n):
    rt = [[0] * n for i in xrange(n)]
    count = 1
    start = 0
    end = n - 1
    while start < end:
        for j in xrange(start, end):
            rt[start][j] = count
            count += 1
        for i in xrange(start, end):
            rt[i][end] = count
            count += 1
        for j in xrange(end, start, -1):
            rt[end][j] = count
            count += 1
        for i in xrange(end, start, -1):
            rt[i][start] = count
            count += 1
        start += 1
        end -= 1
    if start == end:
        rt[start][start] = count
    return rt

print generateMatrix(2)
print generateMatrix(3)
print generateMatrix(4)