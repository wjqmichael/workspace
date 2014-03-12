def getPermutation(n, k):
    digits = [str(i + 1) for i in xrange(n)]
    k -= 1
    factorials = [1]
    for i in xrange(2, n):
        factorials.append(factorials[-1] * i)

    rt = ''
    for fact in reversed(factorials):
        ind = k / fact
        rt += digits[ind]
        digits.remove(digits[ind])
        k %= fact
    rt += digits[0]
    return rt

for i in xrange(1, 7):
    print getPermutation(3, i)

for i in xrange(1, 25):
    print getPermutation(4, i)