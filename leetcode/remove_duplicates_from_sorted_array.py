def removeDuplicates(sorted):
    end = 1
    for i in xrange(1, len(sorted)):
        if sorted[i] != sorted[i - 1]:
            sorted[end] = sorted[i]
            end += 1
    return sorted[:end]

assert removeDuplicates([1,1,2,3,3,4,4,5]) == [1,2,3,4,5]
assert removeDuplicates([1,2,3]) == [1,2,3]
assert removeDuplicates([]) == []
assert removeDuplicates([1]) == [1]