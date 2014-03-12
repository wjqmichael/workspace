def combine(n, k):
    rt = []
    if n < k: return rt

    if k == 1:
        for i in xrange(1, n + 1):
            rt.append([i])
        return rt

    for i in xrange(n, k - 1, -1): 
        for item in combine(i - 1, k - 1):
            item.append(i)
            rt.append(item[:])
    return rt

print combine(4, 1)
print combine(4, 2)