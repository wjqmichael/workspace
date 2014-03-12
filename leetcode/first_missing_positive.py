def first_missing_positive(a):
    for i in xrange(len(a)):
        while 1 <= a[i] <= len(a) and a[i] != i + 1:
            val = a[i]
            replace = a[val - 1]
            a[i], a[val - 1] = replace, val
    for i in xrange(len(a)):
        if a[i] != i + 1:
            return i + 1
    return len(a)

assert(first_missing_positive([1,2,0]) == 3)
assert(first_missing_positive([3,4,-1,1]) == 2)