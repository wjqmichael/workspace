import itertools

def my_permutatins(iterable):
    def on_index(iterable, index):
        return tuple(iterable[i] for i in index)

    index = range(len(iterable))
    yield on_index(iterable, index)
    while True:
        i = len(index) - 2
        while i >= 0 and index[i] > index[i + 1]:
            i -= 1
        if i < 0:
            break
        j = len(index) - 1
        while index[j] < index[i]:
            j -= 1
        index[i], index[j] = index[j], index[i]
        index[i + 1:] = reversed(index[i + 1:])
        yield on_index(iterable, index)

test_data = [[1,2,3], [], ['a','b','c','d'], [1]]
for data in test_data:
    print 'data=%s' % data
    print list(itertools.permutations(data))
    print list(my_permutatins(data))