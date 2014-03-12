def subsets(S):
    # Using recursion
    if len(S) == 0:
        return [[]]
    rt = subsets(S[:-1])
    for i in xrange(len(rt) - 1, -1, -1):
        rt.append(rt[i][:] + [S[-1]]) # Make a copy is important!
    return rt

def subsets2(S):
    # without using recursion
    print 'subset2'
    if len(S) == 0:
        return [[]]
    rt = [[]]
    for i in S:
        j = len(rt) - 1
        while j >= 0:
            rt.append(rt[j][:] + [i])
            j -= 1
    return rt


subsets = subsets2
print subsets([])
print subsets([1])
print subsets([1, 2, 3])