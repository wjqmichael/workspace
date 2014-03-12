def removeDuplicates(A):
    if len(A) < 3: return len(A)
    ct = 2
    for i in xrange(2, len(A)):
        if A[i] != A[i - 2]:
            ct += 1
    return ct

print removeDuplicates([])
print removeDuplicates([1,1,1,1,1,1])
print removeDuplicates([1,1,1,2,2,3])